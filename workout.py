def generate_workout_plan(goal, days_available):
    if goal == "strength":
        exercises = ["Push-ups", "Squats", "Deadlifts", "Bench Press", "Pull-ups"]
    elif goal == "cardio":
        exercises = ["Jogging", "Cycling", "Jump Rope", "HIIT"]
    else:
        exercises = ["Walking", "Yoga", "Stretching"]

    plan = {}
    for day in range(1, days_available + 1):
        plan[f"Day {day}"] = exercises[day % len(exercises)]

    return plan