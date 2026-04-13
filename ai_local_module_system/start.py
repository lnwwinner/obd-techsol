from core.ai_boot import AIBoot

# REAL EXECUTION PLACEHOLDER (replace with IQ Option API)
def execute(model):
    print(f"[REAL EXEC] using {model}")
    return {"reward": 1}

boot = AIBoot(domain="trading", execution_func=execute, interval=10)
boot.start()

# keep alive
import time
while True:
    time.sleep(1)
