# with open("C:/Users/BudgIT Guest/Desktop/README.txt", "a") as file:
#     # a = file.read()
    
#     # print(a)
    
#     file.write("\nI just append.")


import random
import statistics


arr = [random.choice(range(17, 30)) for i in range(20)]

mean = round(statistics.mean(arr), 3)
median = round(statistics.median(arr), 3)

try:
    mode = round(statistics.mode(arr), 3)
except statistics.StatisticsError:
    mode = None

std = round(statistics.stdev(arr), 3)
var = round(statistics.variance(arr), 3)


with open("stats.txt", "w") as file:
    file.write("================\n")
    file.write(f"The mean is {mean}.\nThe median is {median}. \nThe mode is {mode}.\nThe standard deviation is {std}.\nThe variance is {var}.")
    file.write("\n================")