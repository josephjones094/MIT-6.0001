
# portion_down_payment = 0  # Cost needed for down payment
# current_savings = 0  # Amount I have saved
# investment = (current_savings*.04) / 12  # Investment return


# monthly_salary = annual_salary / 12


class PS1:
    def __init__(self, annual_salary, portion_saved, total_cost):
        self.total_cost = annual_salary  # Total cost of home
        self.portion_saved = portion_saved
        self.annual_salary = total_cost

    def p(self):
        print(portion_saved)

    def months_to_buy_dream_home(self):
        monthly_salary = annual_salary / 12
        monthly_payment = monthly_salary * portion_saved
        downpay = total_cost * .25
        current_saving = 0
        months = 0
        while current_saving < downpay:

            ret = current_saving * .04 / 12
            current_saving += ret + monthly_payment
            months += 1

        print(months)


annual_salary = float((input("What is your annual salary?\n")))
portion_saved = float((
    input("What percentage do you want saved? Enter as decimal, ie. 10% = .1\n")))
total_cost = float((input("What is the total cost of your dream home?\n")))
p1 = PS1(annual_salary, portion_saved, total_cost)

p1.months_to_buy_dream_home()
