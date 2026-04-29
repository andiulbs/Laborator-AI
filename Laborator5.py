import numpy as np

# Cu liste

a = np.array([1, 2, 3])
print(a)    # => [1 2 3]
print(type(a))  # type of object a => <class 'numpy.ndarray'>
print(a.dtype)  # type of elements in a => int32
print(a.shape)  # tuple containing length of a on each dimension => (3,)
print(a[0])     # access element at index 0 => 1

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)  # => (2, 3)
print(b[0][2])  # => 3
print(b[0, 2])  # => 3

c = np.asarray([[1, 2], [3, 4]])
print(type(c))  # => <class 'numpy.ndarray'>
print(c.shape)  # => (2, 2)

# Cu functii

zero_array = np.zeros((3, 2))  # creates an array containing only 0s
print(zero_array)    # => [[0. 0.]]
                     #     [0. 0.]]
                     #     [0. 0.]]

ones_array = np.ones((2, 2))  # creates an array containing only 1s
print(ones_array)    # => [[1. 1.]]
                     #     [1. 1.]]

constant_array = np.full((2, 2), 8)  # creates a constant array
print(constant_array)    # => [[8 8]]
                         #     [8 8]]

identity_matrix = np.eye(3)  # creates a 3x3 identity matrix
print(identity_matrix)    # => [[1. 0. 0.]]
                          #     [0. 1. 0.]]
                          #     [0. 0. 1.]]

random_array = np.random.rand(1, 2)  # creates an array with random values
# uniform distribution in [0, 1)

print(random_array)  # => ex: [[0.00672748 0.12277961]]

mu, sigma = 0, 0.1
gaussian_random = np.random.normal(mu, sigma, (3, 6))  # creates an array with random
    # values from a Gaussian distribution
    # with mean mu and standard deviation sigma

first_5 = np.arange(5)  # creates an array containing the first 5 natural numbers
print(first_5)    # => [0 1 2 3 4]

# Slicing

first_5 = np.arange(5)  # creates an array containing the first 5 natural numbers
print(first_5)    # => [0 1 2 3 4]

array_to_slice = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
slice = array_to_slice[:, :]    # take all rows and columns 0, 1, 2
print(slice)    # => [[ 1 2 3]
                #     [ 5 6 7]
                #     [ 9 10 11]]

# ! modifying the slice automatically modifies array_to_slice
print(array_to_slice[0][0])  # => 1
slice[0][0] = 100
print(array_to_slice[0][0])  # => 100

# to avoid this, the subset can be copied
slice_copy = np.copy(array_to_slice[:, :])  # corrected line
print(slice_copy[0][0])    # => 100
print(array_to_slice[0][0])  # => 1 (after reset or redefinition)


### Mathematical functions

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Element-wise sum => [[ 6.0 8.0]
#                     [ 10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Element-wise difference => [[ -4.0 -4.0]
#                            [ -4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Element-wise product => [[ 5.0 12.0]
#                         [ 21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Element-wise division => [[ 0.2 0.33333333]
#                          [ 0.42857143 0.5]]
print(x / y)
print(np.divide(x, y))

# Element-wise square root => [[ 1. 1.41421356]
#                             [ 1.73205081 2. ]]
print(np.sqrt(x))

# Exponentiation
my_array = np.arange(5)
powered = np.power(my_array, 3)
print(powered)  # => [ 0 1 8 27 64]

# dot product

x = np.array([[1, 2],[3, 4]])
y = np.array([[5, 6],[7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

# vector x vector => 219
print(v.dot(w))
print(np.dot(v, w))

# matrix x vector => [29 67]
print(np.matmul(x, v))

# matrix x matrix => [[19 22]
#                     [43 50]]
print(np.matmul(x, y))

# operations on matrices

# transpose of a matrix
my_array = np.array([[1, 2, 3], [4, 5, 6]]) # [[1, 2, 3],
                                              #  [4, 5, 6]]
print(my_array.T) # => [[1, 4],
                  #     [2, 5],
                  #     [3, 6]]

# inverse of a matrix
my_array = np.array([[1., 2.], [3., 4.]])
print(np.linalg.inv(my_array)) # => [[-2.,  1. ],
                               #     [ 1.5, -0.5]]

# functions that perform operations along a specific dimension

x = np.array([[1, 2],[3, 4]])

# sum along a specific dimension
print(np.sum(x))          # Sum of all elements => 10
print(np.sum(x, axis=0))  # Sum along columns => [4 6]
print(np.sum(x, axis=1))  # Sum along rows => [3 7]

# we can also specify multiple axes on which to perform the operation:
print(np.sum(x, axis=(0, 1)))  # Sum of all elements => 10

# mean along a specific dimension
y = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
              [[1, 2, 3, 4], [5, 6, 7, 8]],
              [[1, 2, 3, 4], [5, 6, 7, 8]]])  # corrected
print(y.shape) # => (3, 2, 4)
print(y) # => [[[1 2 3 4]
         #     [5 6 7 8]]
         #    [[1 2 3 4]
         #     [5 6 7 8]]
         #    [[1 2 3 4]
         #     [5 6 7 8]]]

print(np.mean(y, axis=0)) # => [[1. 2. 3. 4.]
                           #     [5. 6. 7. 8.]]

print(np.mean(y, axis=1)) # => [[3. 4. 5. 6.]
                           #     [3. 4. 5. 6.]
                           #     [3. 4. 5. 6.]]

# index of the maximum element on each row
z = np.array([[10, 12, 5], [17, 11, 19]])
print(np.argmax(z, axis=1)) # => [1 2]


# MATPLOTLIB

import matplotlib.pyplot as plt

# Calculate the (x, y) coordinates of points on a sine curve
# x - values from 0 to 3 * np.pi, in steps of 0.1
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot the points
plt.plot(x, y)

# Add labels for each axis
plt.xlabel('x axis label')
plt.ylabel('y axis label')

# Add title
plt.title('Sine')

# Add legend
plt.legend(['Sine'])

# Display the figure
plt.show()

# Calculate the (x, y) coordinates of points on a sine curve and a cosine curve
# x - values from 0 to 3 * np.pi, in steps of 0.1
x = np.arange(0, 3 * np.pi, 0.1)
y_1 = np.sin(x)
y_2 = np.cos(x)

# Plot the points on the same figure
plt.plot(x, y_1)
plt.plot(x, y_2)

# Add title
plt.title('Sine and Cosine')

# Add legend
plt.legend(['Sine', 'Cosine'])

plt.show()


#
# Calculate the (x, y) coordinates of points on a sine curve and a cosine curve
# x - values from 0 to 3 * np.pi, in steps of 0.1
x = np.arange(0, 3 * np.pi, 0.1)
y_1 = np.sin(x)
y_2 = np.cos(x)

# define the first plot in figure 1
first_plot = plt.figure(1)
plt.plot(x, y_1)
plt.title('Sine')
plt.legend(['Sine'])

# define the second plot in figure 2
second_plot = plt.figure(2)
plt.plot(x, y_2)
plt.title('Cosine')
plt.legend(['Cosine'])

# display the figures
plt.show()

# Calculate the (x, y) coordinates of points on a sine curve and a cosine curve
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create a grid with height 2 and width 1
# and set the first subplot as active
plt.subplot(2, 1, 1)
# Plot the first values
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active
# and plot the second dataset
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Display the figure
plt.show()