# d = {"a":1, "b":4, "c":9}
#
# # for key in d.keys():
# #         print(key, end=' ')
# #
#
# # for key in d.keys():
# #     d[key] **= 2
# # print(d)
# #tuple deconstruction
#
# for key, value in d.items():
#     print(f"Key: {key}, Value: {value}")
#
# if 4 in d.values():
#     print('4 is a value in my dictionary')
#

# data_to_list = [item for item in input().split()]
# stocks = {data_to_list[i]: int(data_to_list[i+1]) for i in range(0, len(data_to_list), 2)}
# products = input().split()
#
# for i in products:
#     if i in stocks.keys():
#         print(f"We have {stocks[i]} of {i} left")
#     else:
#         print(f"Sorry, we don't have {i}")


def get_stock(raw_data):
    data = raw_data.split(' ')
    return {data[i]: int(data[i + 1]) for i in range(0,len(data), 2)}

def check_availability(stock: dict, search_products: list) -> str:
    res = ''
    for product in search_products:
        if not stock.get(product):
            res += f"Sorry, we don't have {product}\n"
        else:
            res += f"We have {stock[product]} of {product} left\n"
    return res




stock = get_stock(input())
print(check_availability(stock, input().split(' ')))


def get_stock(raw_data):
    data = raw_data.split(' ')
    return {data[i]: int(data[i + 1]) for i in range(0,len(data), 2)}

def check_availability(stock: dict, search_products: list):
    return '\n'.join([f"Sorry, we don't have {product}" if not stock.get(product)
            else f"We have {stock[product]} of {product} left"
            for product in search_products
    ])

stock = get_stock(input())
print(check_availability(stock, input().split(' ')))

