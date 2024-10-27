orders_list = []
small_orders = []
big_orders = []
current_order = []

print('wprowadzasz pierwsze zamowienie')
order_decision = 'y'
while order_decision == 'y':
    decision = input('Czy chcesz wprowadzić przedmiot do zamowienia? y/n ')
    while decision == 'y':
        item = input('Wprowadz produkt:  ')
        current_order.append(item)
        decision = input('Czy chcesz wprowadzić kolejny przedmiot do zamowienia? y/n ')
    orders_list.append(current_order)
    current_order = []
    order_decision = input('Czy chcesz dodac kolejne zamowienie? y/n ')
print(orders_list)


# for order in orders_list:
#     if len(order) <= 2:
#         small_orders.append(order)
#     else:
#         big_orders.append(order)
# print(big_orders)
