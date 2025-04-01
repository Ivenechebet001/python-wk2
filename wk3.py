def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))


final_price = calculate_discount(price, discount_percent)

t
if discount_percent >= 20:
    print(f"The final price after applying the {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {final_price}")


    