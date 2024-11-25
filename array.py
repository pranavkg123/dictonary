def sum_dict(d1):
    sum = 0
    for i in d1.values(): 
      sum = sum+i
    return sum
d1 = {'a': 5, 'b':10 , 'c': 15}
result = sum_dict(d1)
print("Sum", result)
