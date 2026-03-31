import numpy as np

##array creation
np.random.seed(1)
# age, salary, experience
age = np.random.randint(20, 45, 50)
salary = np.random.randint(20000, 60000, 50)
experience = np.random.randint(1, 15, 50)
data = np.column_stack((age, salary, experience))
print(data)
print(type(data))

##indexing
print("Age of first person",data[0,0])
print("Salary of seventh person",data[6,1])
print("experience of 3rd person",data[2, 2])

## Slicing
print("Get first 5 rows",data[:5])
print("Get only salary of everyone",data[:,1])
print("Get rows 10 to 20",data[10:20])
print("Get Age and salary of everyone",data[:,0:2])

## Mathematical,axis-wise,statistical operations
print("Sum:", np.sum(data, axis=0))
updated_salary = data[:,1] * 1.10
print(updated_salary)

bonus_salary = data[:,1] + 5000
print(bonus_salary)

print("Min:", np.min(data, axis=0))
print("Max:", np.max(data, axis=0))
print("Average age, salary, experience:", np.mean(data, axis=0))
print("Row mean:", np.mean(data, axis=1))
print("Row sum:", np.sum(data, axis=1))

print("Average salary:", np.mean(data[:,1]))
print("Max experience:", np.max(data[:,2]))
print("Salary Std Dev:", np.std(data[:,1]))

##reshaping and broadcasting
print(data.shape)
reshaped = data.reshape(25, 6)
print("Reshaped Data:\n", reshaped)

flat = data.reshape(-1)
print(flat)

new_salary = data[:,1] + 5000
print(new_salary)

updated = data + [1, 1000, 1]
print("Broadcasted Data:\n", updated)

# Save array
np.save("data_array", data)

# Load array
loaded_data = np.load("data_array.npy")
print("Loaded Data:\n", loaded_data)

