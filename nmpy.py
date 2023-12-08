import numpy as np

# Array creation and manipulation
arr = np.array([1, 2, 3])
print("Array:", arr)

arr = np.zeros((3, 3))
print("Array of zeros:", arr)

arr = np.ones((2, 2))
print("Array of ones:", arr)

arr = np.empty((4, 4))
print("Empty array:", arr)

arr = np.arange(1, 10, 2)
print("Array with evenly spaced numbers:", arr)

arr = np.linspace(0, 1, 100)
print("Array with evenly spaced numbers with specified number of elements:", arr)

arr = arr.reshape((2, -1))
print("Reshaped array:", arr)

# Mathematical operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.add(arr1, arr2)
print("Addition:", arr)

arr = np.subtract(arr1, arr2)
print("Subtraction:", arr)

arr = np.multiply(arr1, arr2)
print("Multiplication:", arr)

arr = np.divide(arr1, arr2)
print("Division:", arr)

arr = np.sqrt(arr)
print("Square root:", arr)

arr = np.power(arr, 2)
print("Element-wise power:", arr)

arr = np.exp(arr)
print("Exponential:", arr)

# Statistical functions
arr = np.random.rand(3, 3)

mean_value = np.mean(arr)
print("Mean:", mean_value)

median_value = np.median(arr)
print("Median:", median_value)

std_value = np.std(arr)
print("Standard deviation:", std_value)

variance_value = np.var(arr)
print("Variance:", variance_value)

# Other useful functions
arr = np.random.rand(3, 3)

result = np.dot(arr, arr.T)
print("Dot product:", result)

arr = np.array([1, 2, 3])
arr = np.append(arr, 4)
print("Append element:", arr)

arr = np.delete(arr, 2)
print("Delete element:", arr)

arr = np.sort(arr)
print("Sorted array:", arr)

print("Unique elements:", np.unique(arr))