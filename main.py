#Country-Capital Game in Python 
import random
# Dictionary of countries and capitals
country_capital = {
    "India": "New Delhi",
    "Pakistan": "Islamabad",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Italy": "Rome",
    "Canada": "Ottawa",
    "Australia": "Canberra",
    "Brazil": "Brasilia"
}

score = 0

print("🌍 Welcome to the Country-Capital Game!")
print("Type 'exit' to quit\n")

while True:
    country = random.choice(list(country_capital.keys()))
    answer = input(f"What is the capital of {country}? ")

    if answer.lower() == "exit":
        print("\nGame Over!")
        break

    if answer.strip().lower() == country_capital[country].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {country_capital[country]}\n")

print(f"🏆 Your Final Score: {score}")
