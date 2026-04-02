import random

class SimpleRLAgent:
    """
    Lightweight placeholder for Reinforcement Learning agent.
    State -> Action with simple reward memory (can upgrade to DQN later)
    """

    def __init__(self):
        self.q_table = {}  # state -> action scores

    def _get_state_key(self, state: dict):
        # simplify state
        return f"{state.get('engine_temp')}_{state.get('rpm')}_{state.get('risk_level')}"

    def choose_action(self, state: dict):
        key = self._get_state_key(state)

        if key not in self.q_table:
            self.q_table[key] = {
                "CONTINUE": 0,
                "REDUCE_SPEED": 0,
                "STOP": 0
            }

        # epsilon-greedy
        if random.random() < 0.2:
            return random.choice(list(self.q_table[key].keys()))

        return max(self.q_table[key], key=self.q_table[key].get)

    def update(self, state: dict, action: str, reward: float):
        key = self._get_state_key(state)

        if key not in self.q_table:
            self.choose_action(state)

        self.q_table[key][action] += reward

    def get_policy(self):
        return self.q_table
