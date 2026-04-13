# AI Core Kernel
# Central brain integrating all systems

from core.live_execution import execute_live
from core.auto_evolution import evolve_strategy
from core.multi_project_intelligence import get_best_global
from core.self_rewrite import get_rule


class AICoreKernel:
    def __init__(self, domain):
        self.domain = domain

    def think(self):
        print("[KERNEL] Thinking...")
        model = evolve_strategy(self.domain)
        return model

    def act(self, execution_func):
        print("[KERNEL] Acting...")
        return execute_live(self.domain, execution_func)

    def learn(self):
        print("[KERNEL] Learning from feedback...")
        best = get_best_global(self.domain, "models")
        return best

    def adapt(self):
        print("[KERNEL] Adapting behavior...")
        risk = get_rule(self.domain, "risk_threshold", 0.5)
        print(f"[KERNEL] Current risk threshold: {risk}")
        return risk

    def run(self, execution_func):
        print("[KERNEL START]")

        self.think()
        self.adapt()
        result = self.act(execution_func)
        self.learn()

        print("[KERNEL END]")

        return result
