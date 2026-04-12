 
def countdown(num):
    result = []

    for i in range(num, -1, -1):
        result.append(i)

    return result

print(countdown(5))  # [5, 4, 3, 2, 1, 0]


#secound q2#####################################3

def print_and_return(list):
    print(list[0])
    return list[1]
my_list = [10, 20]
print(print_and_return(my_list)) 


###################q3################
def first_plus_length(list):
    if(len(list) == 0):
        return "list is empty"
    return list[0] + len(list)

print(first_plus_length([1, 2, 3, 4, 5]))  # 6


#################################################q4####################3

def values_greater_than_second(list):
    if len(list) < 2:
        return False

    result = []
    second_value = list[1]

    for i in list:
        if i > second_value:
            result.append(i)

    print(len(result))
    return result


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#################################################
def length_and_value(size, value):
    result = []
    i = 0

    while i < size:
        result.append(value)
        i += 1

    return result

print(length_and_value(4, 7))  
print(length_and_value(6, 2))  
         
     
         




