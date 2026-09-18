# A retailer sells widgets and offers different pricing depending on order size
# Orders of 1 to 9 widgets cost a 1.25 per widget
# Orders of 10 to 99 cost a 1.20 per widget
# Orders of 100 or more cost 1.18 per widget

n_widgets = int(input("How many widgets do you want to buy? "))

if n_widgets < 10:
    price_per_widget = 1.25
elif n_widgets < 100:
    price_per_widget = 1.20
else:
    price_per_widget = 1.18

order_cost = n_widgets * price_per_widget
print(f"{n_widgets:,d} widgets(s) will cost ${order_cost:,.2f}")