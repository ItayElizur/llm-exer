def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i] != None:
            temp = data[i] * 2
            if temp > 10:
                result.append(temp)
            else:
                result.append(temp + 1)
    return result

def calc(x, y, z):
    if x > 0:
        if y > 0:
            if z > 0:
                return x * y * z
            else:
                return x * y
        else:
            return x
    else:
        return 0
