# Advanced Project Generator with Auto Injection

import os

BASE_IMPORT = "from core.system_config import init_system\n"

AI_TEMPLATE = """
# AI Ready
from core.resource_intelligence import select_best
from core.resource_feedback import update_feedback


def run_ai(domain):
    best = select_best(domain, \"models\", {})
    print(f\"[AI] Selected: {best}\")
    return best
"""

RL_TEMPLATE = """
# RL Hook
from core.rl_agent import RLAgent

agent = RLAgent()
"""

MAIN_TEMPLATE = """
{base_import}

{ai_block}

{rl_block}


def main():
    init_system()
    print(\"[PROJECT STARTED]\")

    model = run_ai(\"{domain}\")

    # simulate result
    reward = 10
    update_feedback(model[0], reward)


if __name__ == \"__main__\":
    main()
"""


def create_advanced_project(project_name, domain="general"):
    base_path = os.path.join("projects", project_name)

    os.makedirs(base_path, exist_ok=True)

    for folder in ["src", "configs", "logs", "notebooks"]:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    main_code = MAIN_TEMPLATE.format(
        base_import=BASE_IMPORT,
        ai_block=AI_TEMPLATE,
        rl_block=RL_TEMPLATE,
        domain=domain
    )

    with open(os.path.join(base_path, "main.py"), "w") as f:
        f.write(main_code)

    print(f"[ADVANCED PROJECT CREATED] {project_name}")
