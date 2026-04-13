# Live Execution + Real-world Learning

from core.meta_ai import meta_decision
from core.resource_feedback import update_feedback


def execute_live(domain, execution_func):
    # Select or generate best model
    model = meta_decision(domain)

    print(f"[LIVE] Using model: {model}")

    # Execute real-world function (e.g., trade, scan, analyze)
    result = execution_func(model)

    # Expect result to contain 'reward'
    reward = result.get("reward", 0)

    # Update feedback loop
    update_feedback(model, reward)

    print(f"[LIVE RESULT] reward={reward}")

    return result
