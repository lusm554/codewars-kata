# https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python

def data_reverse(data):
    b = []
    for i in range(0, len(data), 8): b.append(data[i:i+8])
    return [item for sublist in reversed(b) for item in sublist]
    
data = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
print(data_reverse(data))

# [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
