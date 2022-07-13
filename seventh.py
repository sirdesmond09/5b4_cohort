# data = {"name":"Grace",
#         "course":"Backend",
#         "scores":[10,7,9,5,8],
#         "address":{"str_num":40,
#                    "str_name":"montgomery road",
#                    "city":"yaba"},
#         (1,"john"):"This is is the tuple"
#     }


# # print(data[(1,"john")])


# data['new_name'] = data.pop('name')
# print(data)


#Write a program to sort this dictionary using the value.
data = {"5":8,
 "3":10,
 "4":2,
 "9":3,
 "2":7,
 "0":5}


# sorted_x = sorted(data.items(), key=lambda x: x[1], reverse=True)

# print(dict(sorted_x))

# list1 = [2,3,5,6,7,8]
# list2 = ["abc", "def", "ghi", "jkl", "mno", "pqr"]

# a = dict(zip(list1, list2))
# print(a)

# data = {"V":"S001","VI": "S002","VII": "S001","VIII": "S005", "VIV":"S005", "VV":"S009","VVI":"S007"}


# print(set(data.values()))


# while True:
#     data = int(input("> "))
#     print(data)
#     if data == 5:
#         break
    

    
a = 100
count = 0
while a > 0:
    print(a)
    a-=1
    count += 1
    if count ==  3:
        break