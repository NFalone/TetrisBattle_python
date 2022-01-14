array3d = [[[0 for i in range(5)] for j in range(5)] for k in range(5)]
#3d, 2d, 1d
array3d[1][2][0] = 77

# print(array3d)

array2d = [[0 for i in range(5)] for j in range(5)]
array2d[0][1] = 77

print(array2d)
array2d.append(0)
print(array2d)

def chvar(x):
    x = 10
    return x

x = 5
y = chvar(x)
print(x, y)
