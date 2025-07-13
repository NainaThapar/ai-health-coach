from workout import generate_workout_plan
from diet import generate_diet_plan

if __name__ == "__main__":
    goal = input("Enter your fitness goal (strength/cardio/flexibility): ")
    days = int(input("How many days do you want to workout this week? "))
    preference = input("What's your diet preference? (veg/non-veg/vegan): ")
    meals = int(input("How many meals per day do you prefer? (e.g., 3 or 5): "))

    workout_plan = generate_workout_plan(goal, days)
    diet_plan = generate_diet_plan(goal, preference, meals)

    print("\n🏋️ Your Workout Plan:")
    for day, exercise in workout_plan.items():
        print(f"{day}: {exercise}")

    print("\n🍽️ Your Diet Plan:")
    for meal, item in diet_plan.items():
        print(f"{meal}: {item}")
