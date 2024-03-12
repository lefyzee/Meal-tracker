def collect_meal_input(day):
    return int(input(f"How many meals did you have on {day}: "))

def save_meal_data(meals, total_meals, meals_used):
    meals_remaining = total_meals - meals_used
    if meals_remaining < 0:
        print("You cannot use more meals than your meal plan")
    else:
        with open('meal_tracker.txt', 'w') as file:
            for day, count in meals.items():
                file.write(f"{day} meals: {count}\n")
            file.write("\nTotal meals used: " + str(meals_used) + "\n")
            file.write("Meals remaining: " + str(meals_remaining))
        print("\nTotal meals used:", meals_used)
        print("Meals remaining:", meals_remaining)

def main():
    print("This is a program to keep track of your meals every week\n")

    while True:
        total_meals = int(input("How many meals do you have in your meal plan for the week: "))

        meals = {}
        answer = input("Do you know how many meals you have used so far? (y/n): ").lower()
        if answer == 'y':
            meals_used = int(input("How many meals have you had so far this week: "))
            save_meal_data(meals, total_meals, meals_used)
        elif answer == 'n':
            days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            for day in days_of_week:
                meals[day] = collect_meal_input(day)
            meals_used = sum(meals.values())
            save_meal_data(meals, total_meals, meals_used)

        if not run_program_again():
            break

def run_program_again():
    while True:
        answer = input("\nDo you want to run the program again? (y/n): ").lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")

# Start the program
main()
