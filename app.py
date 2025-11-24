print("Welcome to my python program")
sales = input("How many sales did you make today?")
sales = float(sales)
weekly_sales = sales * 7
try:
    sales = float(sales)
except ValueError:
    print("Enter a valid numer.")
    exit()
print(f"At this rate, you are likely to make {weekly_sales} sales this week.")

