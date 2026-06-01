stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 200,
    "MICROSCOFT": 300
}

total_investment = 0

file = open("portfolio.txt", "w")
file.write("Stock Portfolio Report\n\n")

num_stocks = int(input("How many stocks do you want to enter? "))

for i in range(num_stocks):

    stock_name = input("Enter stock name: ").upper()

    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:

        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        print("Investment for", stock_name, "=", investment)

        file.write("Stock: " + stock_name + "\n")
        file.write("Quantity: " + str(quantity) + "\n")
        file.write("Investment: " + str(investment) + "\n\n")

    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total_investment)

file.write("Total Investment Value = " + str(total_investment))

file.close()

print("Result saved in portfolio.txt")