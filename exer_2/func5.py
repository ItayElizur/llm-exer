def mystery_function(lst):
    new_lst = []
    for item in lst:
        flag = True
        for i in range(2, int(item**0.5) + 1):
            if item % i == 0:
                flag = False
                break
        if flag and item > 1:
            new_lst.append(item)
    return new_lst

def process_file(filename):
    data = open(filename, 'r').read()
    lines = data.split('\n')
    result = ""
    for line in lines:
        result += line.upper() + "\n"
    return result
