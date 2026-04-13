# AI Boot System
# Auto start kernel loop + scheduling

import time
from threading import Thread
from core.ai_core_kernel import AICoreKernel


class AIBoot:
    def __init__(self, domain, execution_func, interval=60):
        self.domain = domain
        self.execution_func = execution_func
        self.interval = interval
        self.kernel = AICoreKernel(domain)
        self.running = False

    def loop(self):
        print("[BOOT] AI system starting...")
        while self.running:
            try:
                self.kernel.run(self.execution_func)
            except Exception as e:
                print(f"[BOOT ERROR] {e}")
            time.sleep(self.interval)

    def start(self):
        if self.running:
            return
        self.running = True
        t = Thread(target=self.loop, daemon=True)
        t.start()
        print("[BOOT] Started")

    def stop(self):
        self.running = False
        print("[BOOT] Stopped")


# Example usage
if __name__ == "__main__":
    def dummy_exec(model):
        print(f"[EXEC] using {model}")
        return {"reward": 1}

    boot = AIBoot(domain="trading", execution_func=dummy_exec, interval=5)
    boot.start()

    time.sleep(20)
    boot.stop()
