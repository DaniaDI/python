
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggie_size([-1, 3, 5, -5]))

#############################################################################

def count_positives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count += 1
    list[len(list)-1] = count
    return list

print(count_positives([-1, 1, 1, 1]))


def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

print(sum_total([1, 2, 3, 4]))


#############################################################################
def average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum / len(list)
print(average([1, 2, 3, 4]))
#############################################################################

def length(list):
    count=0;
    if list == []:
        return 0
    
    for i in list:

        count+=1
    return count
print(length([37,2,1,-9]))
print(length([]))

#############################################################################
def minimum(list):
    if list == []:
        return False
    
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
print(minimum([37,2,1,-9]))
#############################################################################

def maximum(list):
    if list == []:
        return False
    
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
print(maximum([37,2,1,-9]))

#############################################################################
def ultimate_analysis(list):
    if list == []:
        return False
    
    info = {
        "sumTotal": 0,
        "avg": 0,
        "min": list[0],
        "max": list[0],
        "length": 0
    }

    for i in list:
        info["sumTotal"] += i

        if i < info["min"]:
            info["min"] = i

        if i > info["max"]:
            info["max"] = i

        info["length"] += 1

    info["avg"] = info["sumTotal"] / info["length"]
    return info


print(ultimate_analysis([37,2,1,-9]))


#############################################################################

def reverse_list(list):
    reverse= []
    for i in range(len(list)-1, -1, -1):
        reverse.append(list[i])
    return reverse
print(reverse_list([37,2,1,-9]))

#############################################################################