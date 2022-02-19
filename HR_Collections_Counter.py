# Comment 1
# Need import collections, which is a build-in python module that
# provides container datatype for resolving of this task

# Comment 2
# Input which takes total number of shoes in the shop (inventory).
# In our case, it will be 10 shoes.

# Comment 3
# Input, which sizes we have in the shop.
# Counter datatype is kind of smart objects, which allow to store and
# access values. Counter allows you to compute the frequency of occuring
# numbers for any iterable object, like string and lists. Counter is dict
# subclass, used to count hashable objects. It returns a dictionary
# with the elements as keys and the count (no of times the element was
# present) as values.
# It takes all size [2, 3, 4, 5, 6, 8, 7, 6, 5, 18] and links them with 10
# shoes in the store.

# Comment 4
# New variable for sales (total_revenue). Start with 0 sales.


# Comment 5
# for _ in range(int(input())) - the underscore "_" means, that we are not interested
# to return value. The input will be 6 (or 6 customers).

# Comment 6
# It maps sizes and prices. Every time if the size located in store's stock.
# It add prices and decrease the stock by 1. The loop continue 6 times, because
# we have 6 customers. This programs works only if 1 customer by only 1 pair of
# shoes.

import collections  # comment 1
store_stock = int(input())  # comment 2
sizes_in_stock = collections.Counter(map(int, input().split()))  # comment 3
revenue = 0  # comment 4

for _ in range(int(input())):  # comment 5
    size, price = map(int, input().split())  # comment 6
    if sizes_in_stock[size]:
        revenue += price
        sizes_in_stock[size] -= 1

print(revenue)
