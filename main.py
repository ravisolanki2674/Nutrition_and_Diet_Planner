from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load food database
with open('food_database.json') as f:
    food_db = json.load(f)

# Sample goals (would be stored in a DB in a real-world app)
user_goals = {
    "calories": 2000,
    "protein": 150,
    "fats": 70,
    "carbs": 250
}

# Store meals logged by the user
user_meals = []

# Diet recommendation data
diet_data = [
    {"calories": 1500, "protein": 100, "fats": 50, "carbs": 150, "goal": "Weight Loss",
     "recommendation": "Reduce carbs and increase vegetables."},
    {"calories": 2000, "protein": 150, "fats": 70, "carbs": 250, "goal": "Muscle Gain",
     "recommendation": "Increase protein intake and consume healthy fats."},
    {"calories": 1800, "protein": 120, "fats": 60, "carbs": 200, "goal": "Maintenance",
     "recommendation": "Balanced diet with all macronutrients."},
    {"calories": 1600, "protein": 80, "fats": 40, "carbs": 180, "goal": "Weight Loss",
     "recommendation": "Focus on low-calorie foods and lean proteins."},
    {"calories": 2200, "protein": 180, "fats": 90, "carbs": 300, "goal": "Muscle Gain",
     "recommendation": "Consume protein-rich meals and healthy snacks."}
]


def get_recommendation(goals):
    """Get dietary recommendation based on user's goals."""
    closest_diff = float('inf')
    closest_recommendation = None

    for data in diet_data:
        diff = (
                abs(data["calories"] - goals["calories"]) +
                abs(data["protein"] - goals["protein"]) +
                abs(data["fats"] - goals["fats"]) +
                abs(data["carbs"] - goals["carbs"])
        )
        if diff < closest_diff:
            closest_diff = diff
            closest_recommendation = data["recommendation"]

    return closest_recommendation


@app.route('/')
def index():
    return render_template('index.html', food_db=food_db, meals=user_meals)


@app.route('/log-meal', methods=['POST'])
def log_meal():
    food_item = request.form.get('food_item')
    custom_calories = request.form.get('custom_calories')

    # Find the selected food in the database or take the custom entry
    if custom_calories:
        meal = {
            "name": food_item,
            "calories": float(custom_calories),
            # You can add custom nutrients here
        }
    else:
        meal = next(item for item in food_db if item["name"] == food_item)

    user_meals.append(meal)

    return redirect(url_for('index'))


@app.route('/set-goals', methods=['GET', 'POST'])
def set_goals():
    if request.method == 'POST':
        # Update user goals here
        user_goals["calories"] = int(request.form.get('calories'))
        user_goals["protein"] = int(request.form.get('protein'))
        user_goals["fats"] = int(request.form.get('fats'))
        user_goals["carbs"] = int(request.form.get('carbs'))
        return redirect(url_for('index'))

    return render_template('index.html', goals=user_goals)


@app.route('/insights')
def insights():
    # Calculate nutrient intake summary
    total_calories = sum(meal['calories'] for meal in user_meals)

    # Get dietary recommendation based on the user's goals
    recommendation = get_recommendation(user_goals)

    return render_template('index.html', total_calories=total_calories, goals=user_goals, recommendation=recommendation)


if __name__ == '__main__':
    app.run(debug=True)
