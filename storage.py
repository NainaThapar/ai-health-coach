import json
import os
from datetime import datetime

def save_plan_to_file(workout_plan, diet_plan, filename="plans.json"):
    plan_data = {
        "timestamp": datetime.now().isoformat(),
        "workout_plan": workout_plan,
        "diet_plan": diet_plan
    }

    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    existing.append(plan_data)

    with open(filename, "w") as f:
        json.dump(existing, f, indent=2)

    print(f"\n💾 Your plan was saved to {filename}")
