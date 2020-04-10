# Complete the functions below to manipulate the given list. 
# Be sure to follow the directions carefully to be sure your results match the expected results.

def append_to_list(x): 
    # User code goes here
    x.append(123)
    return x

def insert_to_list(y):
    y.insert(2,12)
    return y

def remove_from_list(a):
    a.remove(8)
    return a

def sort_ascending(z):
    z.sort()
    return z

def check_list(d):
    if 33 in d:
        check = True
    else:
        check = False
    return check

if __name__ == '__main__':
    # Use the print statements below to check your code. Do not change starter_list or your program will not pass automated test.
    starter_list = [3, 18, 2, 75, 8, 33]
    
    print(append_to_list(starter_list))
    print(insert_to_list(starter_list))
    print(remove_from_list(starter_list))
    print(sort_ascending(starter_list))
    print(check_list(starter_list))


