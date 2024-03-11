# Meal Tracker

def run_program_again():
    while True:
        print("")
        answer = input("Do you want to run the program again? (y/n): ")
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")

def main():
    print("This is a program to keep track of your meals every week")
    print("")

    while True:
        try:
            total_meals = int(input("How many meals do you have in your meal plan for the week: "))
            meals_used = 0

            answer = input("Do you know how many meals you have used so far? (y/n): ")
            if answer.lower() == 'y':
                meals_used = int(input("How many meals have you had so far this week: "))
                meals_remaining = total_meals - meals_used
                print("Total meals used:", meals_used)
                print("Meals remaining:", meals_remaining)
            else:
                Monday = int(input("How many meals did you have on Monday: "))
                Tuesday = int(input("How many meals did you have on Tuesday: "))
                Wednesday = int(input("How many meals did you have on Wednesday: "))
                Thursday = int(input("How many meals did you have on Thursday: "))
                Friday = int(input("How many meals did you have on Friday: "))
                Saturday = int(input("How many meals did you have on Saturday: "))
                Sunday = int(input("How many meals did you have on Sunday: "))

                meals_used = Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday
                meals_remaining = total_meals - meals_used
                if meals_remaining < 0:
                    print("You cannot use more meals than your meal plan")
                else:
                    with open('meal_tracker.txt', 'w') as file:
                        file.write("Monday meals: " + str(Monday) + "\n")
                        file.write("Tuesday meals: " + str(Tuesday) + "\n")
                        file.write("Wednesday meals: " + str(Wednesday) + "\n")
                        file.write("Thursday meals: " + str(Thursday) + "\n")
                        file.write("Friday meals: " + str(Friday) + "\n")
                        file.write("Saturday meals: " + str(Saturday) + "\n")
                        file.write("Sunday meals: " + str(Sunday) + "\n")
                        file.write("\nTotal meals used: " + str(meals_used) + "\n")
                        file.write("Meals remaining: " + str(meals_remaining))

                    print("")
                    print("Monday meals:", Monday)
                    print("Tuesday meals:", Tuesday)
                    print("Wednesday meals:", Wednesday)
                    print("Thursday meals:", Thursday)
                    print("Friday meals:", Friday)
                    print("Saturday meals:", Saturday)
                    print("Sunday meals:", Sunday)
                    print("")
                    print("Total meals used:", meals_used)
                    print("Meals remaining:", meals_remaining)

                    if meals_remaining == 0:
                        print("You have used all your meals for the week")
                    else:
                        pass

            if not run_program_again():
                break  # Exit the program if the user doesn't want to run it again

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
