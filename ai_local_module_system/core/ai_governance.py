# AI Governance + Hierarchy System
# Leader / Roles / Authority Control

class AgentRole:
    ANALYZER = "analysis"
    EXECUTOR = "execution"
    RISK = "risk"
    LEADER = "leader"


class GovernedAgent:
    def __init__(self, name, role, weight=1):
        self.name = name
        self.role = role
        self.weight = weight

    def decide(self, context):
        # simple decision logic
        return {
            "agent": self.name,
            "role": self.role,
            "action": "hold",
            "confidence": 0.5
        }


class GovernanceSystem:
    def __init__(self):
        self.agents = []
        self.leader = None

    def add_agent(self, agent):
        if agent.role == AgentRole.LEADER:
            self.leader = agent
        self.agents.append(agent)

    def decide(self, context):
        decisions = []

        for agent in self.agents:
            d = agent.decide(context)
            decisions.append(d)

        # Leader override logic
        if self.leader:
            leader_decision = self.leader.decide(context)
            print(f"[LEADER OVERRIDE] {leader_decision}")
            return leader_decision

        # Weighted voting
        score = {}

        for d in decisions:
            action = d["action"]
            weight = 1

            score[action] = score.get(action, 0) + weight

        final = max(score, key=score.get)

        return {
            "action": final,
            "decisions": decisions
        }
