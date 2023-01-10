try:
    # This is the function that handles the Homapage menu
    def Company_Homepage_Menu():
        print("Welcome to ABC Electrical Stores Talent page")
        print(
            """Press 1 to sign up **(Kindly note that you can only sign up after getting the verification ID from the HR department)**""")
        print("""Press 2 to log in as a regular **(This is from the entry level to the level of a supervisor)""")
        print("Press 3 to log in as an executive staff **(This only applies to the HR and the CEO )")
        homepage_input = input("")
        if homepage_input == "1":
            sign_up()
        elif homepage_input == "2":
            print("Thanks for visiting our webpage today.")
            print(
                "Kindly note that all regular employees are requested to forward their name and ID number to the HR via email. ")
            print("You can log out now. Thanks for making our company a better place")
            print("System is logging you out now......GoodBye!")
            exit(0)
        elif homepage_input == "3":
            executive_staff()
        else:
            print("Invalid input. Please try again.")
            Company_Homepage_Menu()


    # This is the function that deals with the signing up
    def sign_up():
        print("Please enter your verification ID:")
        verif_id = input()
        # This is to check if the verification ID is valid
        new_user_details_gotten_from_HR = {'hr_individual_id': '212022', 'hr_individual_id_password': "654321"}
        if verif_id == new_user_details_gotten_from_HR['hr_individual_id']:
            print("Please enter your verification ID password:")
            verif_id_password = input()
            # Check if the password is same
            print("Kindly input your password again!")
            verif_id_password_again = input()
            if verif_id_password == verif_id_password_again:
                print("Sign up successful! Please log in to continue.")
                # This will take you to take you to the executive_file()
                executive_staff()
            else:
                print("Incorrect verification ID password. Please try again.")
                sign_up()
        else:
            print("Invalid verification ID. Please try again or contact the HR department for assistance.")
            print("To enter your verification ID again, Press 1")
            print("Kindly press 0 to exit")
            decision = input()
            if decision == '1':
                sign_up()
            elif decision == '0':
                print("Kindly reach out to the HR to get the verification code. Thanks")
                exit(0)
            else:
                sign_up()


    # This is the function that deals with the executive staffs
    def executive_staff():
        print("Welcome! Distinguished Personnel")
        print("Press 1 to log in as HR Team")
        print("Press 2 to log in as the CEO")
        exec_staff_input = input("")
        if exec_staff_input == "1":
            HR_Team_Login()
        elif exec_staff_input == "2":
            print(
                "Thank you for your strong leadership and dedication to creating a positive work environment for all of us at the company.")
            print("System is logging you out now......GoodBye!")
            exit(0)
        else:
            print("Invalid input. Please try again.")
            executive_staff()


    # This is the function that deals with the login in of the HR
    def HR_Team_Login():
        hr_team_login_details = {'email': 'hrhrhr@abc.com', 'password': '123456'}
        username_and_password_incorrect = True
        while True:
            print("In case you do not remember your username. Kindly input hrhrhr@abc.com")
            print("Kindly enter your email address")
            email = input("Email ID: ")
            print("In case you do not remember your password. Kindly input 123456")
            print("Kindly enter your password")
            password = input("Password: ")
            if email == hr_team_login_details['email'] and password == hr_team_login_details['password']:
                HR_Menu()
                username_and_password_incorrect = False
            elif email != hr_team_login_details['email'] or password != hr_team_login_details['password']:
                print("Kindly check your EMAIL or password as the one you entered isn't correct")
                HR_Team_Login()
            if not username_and_password_incorrect:
                break


    # This is the function that deals with both your decision to continue
    # and also deals with the necessary info to make the code continue
    def HR_Menu():
        answer = input("Press 1 to proceed and 0 to exit: ")
        if answer == "1":
            pass
        elif answer == "0":
            exit(0)
        else:
            HR_Menu()
        ball = Calculation(
            int(input("Kindly input the general hourly wage for all employee: ")),
            input("Kindly enter the name of the employee: "),
            int(input("Kindly input hours worked by the employee in the previous month: ")),
            int(input("What is the level of the employee? ")),
            int(input("What is the rate you would like to use for employees below grade 6? ")),
            int(input("What is the rate you would like to use for employees above grade 6? ")),
            int(input("What is the long tax rate? ")),
            int(input("what is the short tax rate? ")),
            input("Is this the employee first month of joining ABC? (Enter Yes/No): "), 0.01)

        balls = ball.Salary()


    # This is the class that calculate the salary
    class Calculation(object):

        def __init__(self, hour_wage, name, hours_worked, level, rate_below_six, rate_above_six, long_tax_rate,
                     short_tax_rate, first_month, first_month_ten_percent_removal):
            self.hour_wage = hour_wage
            self.name = name
            self.hours_worked = hours_worked
            self.level = level
            self.rate_below_six = rate_below_six
            self.rate_above_six = rate_above_six
            # This is the tax that applies to employees that has worked with the company for more than a year
            self.long_tax_rate = long_tax_rate
            # This is the tax that applies to employees that joined the company less than a year ago
            self.short_tax_rate = short_tax_rate
            self.first_month = first_month
            self.first_month_ten_percent_removal = first_month_ten_percent_removal

        def Salary(self):
            if self.level <= 6 and self.first_month == "Yes":
                cad = int(self.hour_wage * self.hours_worked * self.rate_below_six -
                          self.hours_worked * self.rate_below_six *
                          self.short_tax_rate - self.hours_worked *
                          self.rate_below_six * self.first_month_ten_percent_removal)

                print(f"The salary of {self.name} is {cad} Korean Won")
                print(
                    "Kindly forward the name and amount to the Accounting department so that they can credit the employee immediately")
                dell = Again(self)
                dell.Continuation()

            elif self.level <= 6 and self.first_month == "No":
                cat = int(self.hour_wage * self.hours_worked * self.rate_below_six -
                          self.hours_worked * self.rate_below_six *
                          self.long_tax_rate)
                print(f"The salary of {self.name} is {cat} Korean Won")
                print(
                    "Kindly forward the name and amount to the Accounting department so that they can credit the employee immediately")
                dell = Again(self)
                dell.Continuation()

            elif self.level >= 6 and self.first_month == "Yes":
                caz = int(
                    self.hour_wage * self.hours_worked * self.rate_above_six - self.hours_worked * self.rate_above_six *
                    self.short_tax_rate - self.hours_worked * self.rate_above_six * self.first_month_ten_percent_removal)
                print(f"The salary of {self.name} is {caz} Korean Won")
                print(
                    "Kindly forward the name and amount to the Accounting department so that they can credit the employee immediately")
                dell = Again(self)
                dell.Continuation()

            elif self.level >= 6 and self.first_month == "No":
                cade = int(
                    self.hour_wage * self.hours_worked * self.rate_above_six - self.hours_worked * self.rate_above_six * self.long_tax_rate)
                print(f"The salary of {self.name} is {cade} Korean Won")
                print(
                    "Kindly forward the name and amount to the Accounting department so that they can credit the employee immediately")
                dell = Again(self)
                dell.Continuation()

            else:
                print("Seems you made a mistake or there is an error.")
                dell = Again(self)
                dell.boda()


    # This class is created to always take you back incase there is an error
    # or you wish to continue the task again
    class Again(object):
        def __init__(self, Calculation):
            self.Calculation = Calculation

        def boda(self):
            print("Kindly input the details again")
            HR_Menu()
            exit(0)

        # This is the function that decide if you are through with the task.
        def Continuation(self):

            decision11 = input("Do you want to continue for other staff? (Input Yes/No): ")
            if decision11 == "Yes":
                HR_Menu()
            elif decision11 == "No":
                print("Thanks........ Bye!")
            else:
                print("It seems you have entered the wrong key. Redirecting......................")
                HR_Menu()


except Exception or InterruptedError:
    print("There seems to be an Error!")