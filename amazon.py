#A retailer ships all orders of 50$ or more for free
# Otherwise, a $10 shipping fee applies

order_total = float(input("How much does your order cost? "))

if order_total >= 50:
    print(f"Shipping fees do not apply for orders over $50, so the cost of your order is only {order_total}")
else:
    print(f"Because your order is under $50, there will be a shipping fee of $10, bringint the cost of your order to {order_total + 10}")

