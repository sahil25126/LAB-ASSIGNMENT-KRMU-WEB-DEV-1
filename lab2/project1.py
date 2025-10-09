# Name: [Your Name]
# Date: 2024-09-19
# Project Title: Daily Calorie Tracker CLI

print("--- Daily Calorie Tracker ---")
print("This program will help you track your calorie intake for the day.")

meals = []
calories = []

num_meals = int(input("How many meals to log? "))

for i in range(num_meals):
    print(f"\n--- Meal {i+1} ---")
    meal_name = input("Enter meal name: ")
    
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))
    
    meals.append(meal_name)
    calories.append(calorie_amount)

total_calories = sum(calories)
average_calories = total_calories / num_meals if num_meals > 0 else 0

daily_limit = float(input("\nEnter your daily calorie limit: "))

limit_status = ""
if total_calories > daily_limit:
    limit_status = f"You are {total_calories - daily_limit:.0f} calories OVER your limit."
else:
    limit_status = "You are WITHIN your daily limit."
    
print("\n" + limit_status)

print("\n\n--- Daily Summary ---")
print("=====================")
print(f"{'Meal':<20}{'Calories'}")
print("---------------------")
for i in range(len(meals)):
    print(f"{meals[i]:<20}{calories[i]:.0f}")
print("---------------------")
print(f"{'Total:':<20}{total_calories:.0f}")
print(f"{'Average:':<20}{average_calories:.0f}")
print("=====================")

save_option = input("\nSave this log to a file? (yes/no): ").lower()
if save_option == 'yes':
    with open("calorie_log.txt", "a") as file:
        file.write("--- New Log Entry ---\n")
        for i in range(len(meals)):
            file.write(f"- {meals[i]}: {calories[i]:.0f} calories\n")
        file.write(f"Total Calories: {total_calories:.0f}\n")
        file.write(f"Daily Limit: {daily_limit:.0f}\n")
        file.write(f"Status: {limit_status}\n\n")
    print("Log saved to calorie_log.txt")
else:
    print("Log not saved. Program finished.")