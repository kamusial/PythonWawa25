orders_list = [
    ['komputer', 'patelnia'],
    ['hak', 'ketchup', 'sluchawki'],
    ['pierogi'],
    ['Python', 'lampka', 'gitara', 'flet']
]
# pogrupowac zamowienia, osobno max 2 produkty
# osobno wieksze

# print(orders_list[2])    # jedno zamowienie
# print(orders_list[2][1])  # konretny element
small_orders = []
big_orders = []

# for i in range(len(orders_list)):
#     if len(orders_list[i]) > 2:
#         big_orders.append(orders_list[i])
#     else:
#         small_orders.append(orders_list[i])
# print(small_orders)

for order in orders_list:
    if len(order) <= 2:
        small_orders.append(order)
    else:
        big_orders.append(order)
print(big_orders)
