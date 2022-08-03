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
    

    
# a = 100
# count = 0
# while a > 0:
#     print(a)
#     a-=1
#     count += 1
#     if count ==  3:
#         break
    
1,2,2,3,3,4,5,5,6
    
    
## Correction
array = [3,2,5,6,3,5,2,1,4]

def mean(arr):
    """Calculates the mean of a given array

    Args:
        arr (list): The array to calculate the mean

    Returns:
        average: The mean value
    """
    return sum(arr)/len(arr)


# def median(arr):
#     """Generate the median of a given array"""
    
#     arr.sort()
    
#     mid_point = len(arr)//2

    
#     if len(arr)%2==0:
#         return (arr[mid_point] + arr[mid_point-1])/2
    
#     else:
#         return arr[mid_point]

def median(list_of_numbers):
    list_of_numbers.sort()
    if len(list_of_numbers) % 2 == 1:
        middle_num = int((len(list_of_numbers) -1) / 2)
        return list_of_numbers[middle_num] 
    elif len(list_of_numbers) % 2 == 0:
        middle_num1 = int(len(list_of_numbers) / 2)
        middle_num2 = int(len(list_of_numbers) / 2) -1
        mean_of_median = mean([list_of_numbers[middle_num1],list_of_numbers[middle_num2]])
        return mean_of_median
    

# print(mean(array))
print(median(array))