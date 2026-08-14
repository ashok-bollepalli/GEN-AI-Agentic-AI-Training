import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(arr * 2)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)


arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr2.ndim)
print(arr2.shape)
print(arr2.size)
print(arr2.dtype)

arr4 = np.array([10, 20, 30, 40, 50, 60], dtype=float)
print(arr4)
print(arr4[0])
print(arr4[-1])
print(arr4[0:4])


#################################

arr = np.zeros(5)
print(arr)

arr = np.ones(4)
print(arr)

arr = np.ones((2,3))
print(arr)

arr = np.full(5, 10)
print(arr)

arr = np.full((2,3), 15)
print(arr)

arr = np.arange(1,11)
print(arr)

arr = np.arange(1,11, 2)
print(arr)

#######################################

arr = np.random.randint(1, 9, 5)
print(arr)

arr = np.random.rand(5)
print(arr)

#############################

arr = np.arange(1, 13,2)
print(arr)

arr = arr.reshape(2,3)
print(arr)

arr = arr.flatten()
print(arr)
#############################

arr = np.array([10, 20, 30])

print(arr + 5)
print(arr - 5)
print(arr * 2)
print(arr / 2)


a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)


print(a.sum())
print(a.min())
print(a.max())
print(a.mean())

arr = np.array([10, 20, 30, 40, 50])

result = arr[arr > 25]
print(result)


arr = np.array([1, 2, 3, 4, 5, 6])
even = arr[ arr % 2 == 0]
print(even)



arr1 = np.array([10, 20, 30])

#arr2 = arr1.copy()
arr2 = arr1.view()

arr2[0] = 15

print(arr1)
print(arr2)










