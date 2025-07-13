from workout import generate_workout_plan
from diet import generate_diet_plan
from storage import save_plan_to_file, clear_saved_plans
import pyfiglet

def menu():
    print("\nChoose an action:")
    print("1. Create a new plan")
    print("2. Clear saved plans")
    print("3. Exit")
    return input("👉 Enter 1 / 2 / 3: ").strip()

def get_user_inputs():
    print(pyfiglet.figlet_format("AI Health Coach"))
    print("👋 Welcome to your AI Health Coach!\n")

    while True:
        goal = input("🎯 What's your fitness goal? (strength / cardio / flexibility): ").strip().lower()
        if goal in ["strength", "cardio", "flexibility"]:
            break
        print("❌ Invalid input. Please enter 'strength', 'cardio', or 'flexibility'.")

    while True:
        try:
            days = int(input("📆 How many days per week do you want to workout? (1-7): ").strip())
            if 1 <= days <= 7:
                break
            else:
                print("❌ Please enter a number between 1 and 7.")
        except ValueError:
            print("❌ Enter a valid number.")

    while True:
        preference = input("🍽️ What's your diet preference? (veg / non-veg / vegan): ").strip().lower()
        if preference in ["veg", "non-veg", "vegan"]:
            break
        print("❌ Please enter 'veg', 'non-veg', or 'vegan'.")

    while True:
        try:
            meals = int(input("🍱 How many meals per day? (e.g., 3 or 5): ").strip())
            if 1 <= meals <= 6:
                break
            else:
                print("❌ Choose 1 to 6 meals.")
        except ValueError:
            print("❌ Enter a valid number.")

    return goal, days, preference, meals


def display_plan(title, plan):
    print(f"\n🔹 {title}")
    print("-" * (len(title) + 4))
    for key, value in plan.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1":
            goal, days, preference, meals = get_user_inputs()
            workout_plan = generate_workout_plan(goal, days)
            diet_plan = generate_diet_plan(goal, preference, meals)
            display_plan("🏋️ Workout Plan", workout_plan)
            display_plan("🍎 Diet Plan", diet_plan)
            save_plan_to_file(workout_plan, diet_plan)
        elif choice == "2":
            clear_saved_plans()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

