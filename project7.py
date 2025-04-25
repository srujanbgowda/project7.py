import random

moods = {
    "Sunny": "You are feeling bright and full of energy today!",
    "Rainy": "A little emotional — maybe a good day for music and coffee.",
    "Cloudy": "Chilled and calm, just like a soft breeze.",
    "Stormy": "Lots going on in your head — take deep breaths.",
    "Rainbow": "Colorful vibes everywhere! You are glowing today!"
}

mood = random.choice(list(moods.keys()))
print(f"Today's Mood Forecast: {mood}")
print(moods[mood])