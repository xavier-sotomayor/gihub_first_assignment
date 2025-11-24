#Python print test
print("Welcome to my python program")
#sales prompt
sales = input("How many sales did you make today?")
#Integer conversion
sales = float(sales)
#initial calculation
#Invalid number contingency
weekly_sales = sales * 7
try:
    sales = float(sales)
except ValueError:
    print("Enter a valid numer.")
    exit()
#print statement
print(f"At this rate, you are likely to make {weekly_sales} sales this week.")

