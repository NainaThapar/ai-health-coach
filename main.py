from workout import generate_workout_plan
from diet import generate_diet_plan

def get_user_inputs():
    print("👋 Welcome to your AI Health Coach!\n")
    goal = input("🎯 What's your fitness goal? (strength / cardio / flexibility): ").strip().lower()
    days = int(input("📆 How many days per week do you want to workout? (1-7): ").strip())
    preference = input("🍽️ What's your diet preference? (veg / non-veg / vegan): ").strip().lower()
    meals = int(input("🍱 How many meals per day? (e.g., 3 or 5): ").strip())
    return goal, days, preference, meals

def display_plan(title, plan):
    print(f"\n🔹 {title}")
    print("-" * (len(title) + 4))
    for key, value in plan.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    goal, days, preference, meals = get_user_inputs()

    workout_plan = generate_workout_plan(goal, days)
    diet_plan = generate_diet_plan(goal, preference, meals)

    display_plan("🏋️ Workout Plan", workout_plan)
    display_plan("🍎 Diet Plan", diet_plan)

    print("\n✅ You're all set! Stick to the plan and let's crush your goals!")

