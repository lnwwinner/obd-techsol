# Distributed AI System
# Multiple agents working together

from core.meta_ai import meta_decision
from core.resource_feedback import update_feedback


class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def act(self, model):
        print(f"[{self.name}] ({self.role}) using {model}")
        return {"reward": 5}


class DistributedSystem:
    def __init__(self, domain):
        self.domain = domain
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def run(self):
        model = meta_decision(self.domain)

        total_reward = 0

        for agent in self.agents:
            result = agent.act(model)
            reward = result.get("reward", 0)
            total_reward += reward

        update_feedback(model, total_reward)

        print(f"[SYSTEM] Total reward: {total_reward}")

        return total_reward
