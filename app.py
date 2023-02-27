from flask import Flask, render_template
import random

app = Flask(__name__)

# Define a list of breakfast, lunch, and dinner options
breakfast_options = ['Oatmeal', 'Greek yogurt', 'Eggs', 'Smoothie', 'Avocado toast']
lunch_options = ['Salad', 'Grilled chicken', 'Tuna sandwich', 'Veggie burger', 'Chicken wrap']
dinner_options = ['Salmon', 'Grilled vegetables', 'Quinoa bowl', 'Stir-fry', 'Baked chicken']

# Define a function to generate a random meal plan for the day
def generate_meal_plan():
    breakfast = random.choice(breakfast_options)
    lunch = random.choice(lunch_options)
    dinner = random.choice(dinner_options)
    meal_plan = {'Breakfast': breakfast, 'Lunch': lunch, 'Dinner': dinner}
    return meal_plan

# Define a route to render the meal plan page
@app.route('/')
def meal_plan():
    meal_plans = []
    for i in range(7):
        meal_plan = generate_meal_plan()
        meal_plans.append(meal_plan)
    return render_template('meal_plan.html', meal_plans=meal_plans)
