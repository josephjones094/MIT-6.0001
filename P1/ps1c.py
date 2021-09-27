
# portion_down_payment = 0  # Cost needed for down payment
# current_savings = 0  # Amount I have saved
# investment = (current_savings*.04) / 12  # Investment return


# monthly_salary = annual_salary / 12


class PS1:
    def __init__(self, annual_salary, total_cost, semi_annual_salary, annual_investment_return):
        self.annual_salary = annual_salary
        self.total_cost = total_cost  # Total cost of home
        self.semi_annual_salary = semi_annual_salary
        self.annual_investment_return = .04
        self.down_payment = .25

    def months_to_buy_dream_home(self):

        low = 0
        high = 10000
        arr = [i for i in range(1, 10001)]
        counter = 0
        while low <= high:

            mid = (high + low) // 2

            months = 0
            salary = self.annual_salary
            current_saving = 0

            downpay = self.total_cost * self.down_payment
            while months < 36:
                if months > 0 and months % 6 == 0:
                    salary = (salary * self.semi_annual_salary) + salary
                monthly_salary = salary / 12
                monthly_payment = monthly_salary * (arr[mid] * .0001)
                ret = current_saving * .04 / 12
                current_saving += ret + monthly_payment
                months += 1

            if current_saving < downpay - 100:
                low = mid + 1
            elif current_saving > downpay + 100:
                high = mid - 1

            else:
                return mid * .0001

        return -1


print("I will tell you what the best savings rate for a down payment for a home in 36 months is\n")
annual_salary = float((input("What is your annual salary?\n")))
total_cost = float((input("What is the total cost of your dream home?\n")))
annual_investment_return = float(
    input("What is your annual return of your saving investments?\n"))
semi_annual_salary = float(
    (input("What is your semi-annual salary raise?\n")))
print("\n")
p1 = PS1(annual_salary, total_cost,
         semi_annual_salary, annual_investment_return)
try:
    print(f"The best savings rate is: {p1.months_to_buy_dream_home()}")
except:
    print("Your income is too low to make the downpayment in 36 months")
