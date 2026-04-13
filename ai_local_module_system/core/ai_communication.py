# AI Communication Protocol
# Agents send/receive messages, simple bus + consensus

from collections import defaultdict

class MessageBus:
    def __init__(self):
        self.channels = defaultdict(list)

    def publish(self, topic, msg):
        self.channels[topic].append(msg)

    def read(self, topic):
        return self.channels.get(topic, [])


class CommunicatingAgent:
    def __init__(self, name, role, bus: MessageBus):
        self.name = name
        self.role = role
        self.bus = bus

    def send(self, topic, payload):
        self.bus.publish(topic, {"from": self.name, "role": self.role, "payload": payload})

    def receive(self, topic):
        return self.bus.read(topic)

    def decide(self, context):
        # simple stub decision
        return {"action": "hold", "confidence": 0.5, "context": context}


class Consensus:
    @staticmethod
    def majority(actions):
        count = defaultdict(int)
        for a in actions:
            count[a.get("action")] += 1
        if not count:
            return None
        return max(count, key=count.get)


class Orchestrator:
    def __init__(self, domain):
        self.domain = domain
        self.bus = MessageBus()
        self.agents = []

    def add_agent(self, agent: CommunicatingAgent):
        self.agents.append(agent)

    def run_cycle(self, market_state):
        # 1) broadcast state
        for ag in self.agents:
            ag.send("state", {"market": market_state})

        # 2) each agent decides
        decisions = []
        for ag in self.agents:
            msgs = ag.receive("state")
            d = ag.decide(msgs[-1]["payload"] if msgs else {})
            ag.send("decision", d)
            decisions.append(d)

        # 3) consensus
        final = Consensus.majority(decisions)
        self.bus.publish("final", {"action": final, "decisions": decisions})

        return {"action": final, "decisions": decisions}
