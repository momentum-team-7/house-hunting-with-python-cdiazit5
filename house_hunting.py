# Write your code here

# portion_down_payment = int(total_cost) * .25
# r = 0.04 
# current_savings = 0 
# annual_salary = int(input("What is your annual salary? "))
# total_costs = int(input("What is the price of your dream home? "))
# months = 0 
# portion_saved = 0.1


def months_needed():
    portion_down_payment = 0.25
    r = float(0.04)
    current_savings = 0 
    annual_salary = float(input("What is your annual salary? "))
    total_costs = float(input("What is the price of your dream home? "))
    months = 0 
    portion_saved = float(input("What percent of your salary can you save? (As a decimal) "))
    down_payment = total_costs*portion_down_payment

    while current_savings < down_payment:
        current_savings += (annual_salary/12*portion_saved) + (current_savings * (r/12))
        months += 1 
    print("It would require ", months,"months to purchase your home.")

months_needed()