def generate_diet_plan(goal, preference, meals_per_day):
    # Basic mock meal sets
    meal_options = {
        "veg": ["Oats with fruits", "Paneer salad", "Mixed vegetable curry", "Daal + rice", "Boiled eggs + toast"],
        "non-veg": ["Boiled eggs", "Chicken breast + rice", "Fish curry", "Greek yogurt + fruits", "Omelette"],
        "vegan": ["Tofu stir-fry", "Chickpea salad", "Oats with almond milk", "Lentil soup", "Smoothie bowl"]
    }

    selected_meals = meal_options.get(preference.lower(), meal_options["veg"])
    plan = {}

    for meal_num in range(1, meals_per_day + 1):
        plan[f"Meal {meal_num}"] = selected_meals[meal_num % len(selected_meals)]

    return plan
