
# portion_down_payment = 0  # Cost needed for down payment
# current_savings = 0  # Amount I have saved
# investment = (current_savings*.04) / 12  # Investment return


# monthly_salary = annual_salary / 12


class PS1:
    def __init__(self, annual_salary, portion_saved, total_cost, semi_annual_salary):
        self.annual_salary = annual_salary
        self.portion_saved = portion_saved
        self.total_cost = total_cost  # Total cost of home
        self.semi_annual_salary = semi_annual_salary
        self.r = .04

    def p(self):
        print(portion_saved)

    def months_to_buy_dream_home(self):
        downpay = total_cost * .25
        current_saving = 0
        months = 0
        while current_saving < downpay:
            if months > 0 and months % 6 == 0:
                self.annual_salary = (
                    self.annual_salary * self.semi_annual_salary) + self.annual_salary
            annual = self.annual_salary
            monthly_salary = self.annual_salary / 12
            monthly_payment = monthly_salary * self.portion_saved
            ret = current_saving * self.r / 12
            current_saving += ret + monthly_payment
            months += 1
        print(f"Months to make downpayment is: {months}")


annual_salary = float((input("What is your annual salary?\n")))
portion_saved = float((
    input("What percentage do you want saved? Enter as decimal, ie. 10% = .1\n")))
total_cost = float((input("What is the total cost of your dream home?\n")))
semi_annual_salary = float((input("What is your semi-annual salary raise?\n")))
p1 = PS1(annual_salary, portion_saved, total_cost, semi_annual_salary)

p1.months_to_buy_dream_home()
