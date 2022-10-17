from flask import Flask
import random
app = Flask(__name__)

allMeals = [
    {
        'name': 'Chicken tikka',
        'price': '$50',
    },
    {
        'name': 'Lamb tikka',
        'price': '$60',
    },
    {
        'name': 'Paneer tikka',
        'price': '$20',
    },
    {
        'name': 'Green curry',
        'price': '$50',
    },
    {
        'name': 'Red curry',
        'price': '$20',
    },
    {
        'name': 'Yellow curry',
        'price': '$30',
    },
    {
        'name': 'Kung Pao chicken',
        'price': '$40',
    },
    {
        'name': 'Kung Pao Tofu',
        'price': '$40',
    },
    {
        'name': 'Mapo tofu',
        'price': '$30',
    },
    {
        'name': 'Drunken noodles',
        'price': '$10',
    },
    {
        'name': 'Drunken fried rice',
        'price': '$50',
    },
    {
        'name': 'White rice',
        'price': '$60',
    },
    {
        'name': 'Steamed broccoli',
        'price': '$30',
    },
    {
        'name': 'Lamb kebab',
        'price': '$40',
    },
    {
        'name': 'Chicken kebab',
        'price': '$20',
    },
]


@app.route('/get_meal')
def get_meal():
    random_meal = random.randint(0, len(allMeals)-1)
    return allMeals[random_meal]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
