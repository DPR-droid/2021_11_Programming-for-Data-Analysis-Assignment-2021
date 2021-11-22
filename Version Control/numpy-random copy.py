########################################################################
# GMIT assignment for Programming for Data Analysis
# Programming-for-Data-Analysis-Assignment-2021
# Due: last commit on or before 22/11/2021
# numpy-random.py
# Author David
# The project submitted is in a Jupyter notebook
# This python script is a reference and testing 
########################################################################
# Global settings
# Importing all the modules required for the juypter Notbook
# All imports are listed in the requirments.txt
########################################################################
# Import numpy module
import numpy as np

# Import mathplotlib
import matplotlib.pyplot as plt

# Import time
import time
########################################################################
# Get user version of Numpy required for np.random.default_rng()
# This is discussed later in the assignment
########################################################################
numpyversion = np.__version__

print('######################################################################')
print('## This Jupyter notebook requires Numpy of version greater than 1.17 ##')
print('############## You are running version ' + str(numpyversion) +' #################')
print('######### This is required for features discussed #############')
print('################### in the assignment #########################')
print('###############################################################\n\n\n\n')

########################################################################
# Plot function 
########################################################################
def plotsforassignment(example, titlename, labelx, labely, binno):
    count, bins, ignored = plt.hist(example, binno, edgecolor='black', density=True)
    plt.title(titlename)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.show()



########################################################################
# Example 1
########################################################################
# Compare the speed of Python versus NumPy module in Python 
########################################################################
# If you are running this why don't you try changing increasing the size from 100000 to 50000000.
# Size of arrays and lists
size = 100000  
# size = 50000000  
# Declaring Python lists
list1 = range(size)
list2 = range(size)
   
# Declaring NumPy arrays
array1 = np.arange(size)  
array2 = np.arange(size)
   
# Capturing time before the multiplication of Python lists
PythonTime = time.time()
  
# Multiplying elements of both the lists and stored in another list
resultantList = [(a * b) for a, b in zip(list1, list2)]
   
# Calculating execution time of Python
print('######################################################################')
print("Time taken by python lists to perform multiplication:", (time.time() - PythonTime), "seconds")
   
# Capturing time before the multiplication of Numpy arrays
NumpyTime = time.time()
  
# Multiplying elements of both the Numpy arrays and stored in another Numpy array 
resultantArray = array1 * array2
   
# Calculating execution time NumPy
print("Time taken by NumPy Arrays to perform multiplication:", (time.time() - NumpyTime), "seconds")

# How fast is it?
Numpyspeed = (PythonTime/NumpyTime)
print("Numpy is in this example " + str(Numpyspeed) + " faster!")
print('###############################################################\n\n\n\n')


########################################################################
# Example 2
########################################################################
# uses the integer function to create an array of random numbers up to 
# 100, 10000 times. This returns random integers from the 
# “discrete uniform” distribution and displayed in a histogram
########################################################################
rng = np.random.default_rng()

# Create an array
randomintegers = rng.integers(100, size=10000)
# Create a plot to see the randomness
plotsforassignment(randomintegers, 'Uniform distribution', 'Array', 'Count', 10)


########################################################################
# Example 3
########################################################################
# the NumPy API Random Documentation to generate a random float. 
# This example is used to show the reader that more examples and 
# resources are available.
########################################################################
rng = np.random.default_rng()
rng.random()


########################################################################
# Example 4
########################################################################
# Random sample from a given array and the probabilities associated 
# with each entry in the array
########################################################################
rng = np.random.default_rng()
# Generates a random sample of an array
aa_milne_arr = ['Santa', 'Easter Bunny', 'Jack Frost', 'Sandman', 'Tooth Fairy']
# p value must have same size 
# 5 samples in array, 5 different p values 
#
# p value must add upto 1  
# 0.4 + 0.1 + 0.1 + 0.2 + 0.2 = 1
rng.choice(aa_milne_arr, 5, p=[0.4, 0.1, 0.1, 0.2, 0.2])


########################################################################
# Example 5
########################################################################
# How would you use Simple random data
########################################################################
# [10] Script updated for version of NumPy v1.21 Simple random data functions  
rng = np.random.default_rng()
# The number of dice to roll in each turn
numofdice = 2
# The number of turns
numofturn = 100000
# Roll the dice
dice = rng.integers(1, 7, size=(numofturn, numofdice))
# See List
print('###############################################################')
print('Example of output of dice thrown')
print(dice)
print('###############################################################\n\n')
# Sum the faces of the dice
totals = np.sum(dice, axis=1)
# Have a look
print('Example of output total when adding dice together')
print(totals)
print('###############################################################\n\n')
# Count the number of total for 2 dice.
faces, counts = np.unique(totals, return_counts=True)
faces , counts
print('Output totals to identify the highest probable outcome when throwning two dice')
print('###############################################################\n\n\n\n')
plt.xlabel('Dice')
plt.ylabel('Counts')
plt.title('Throwing 2 Dice 10000 times')
plt.bar(faces , counts)
plt.show()


########################################################################
# Example 6
########################################################################
# Permutations
########################################################################
rng = np.random.default_rng()
preshuffle = np.arange(24).reshape(3, 8)
preshuffle

shuffle = rng.permuted(preshuffle, axis=1)
shuffle


########################################################################
# Example 7
########################################################################
# Uniform Distribution
# Guessing someone's birthday
########################################################################
# Input the number of days 1 - 365
# Input the number of people 100000
rng = np.random.default_rng()
birthday = rng.uniform(1,366,100000)
# Plot Function
plotsforassignment(birthday, 'Uniform Distribution', 'Days of the year 1 - 365', 'Count', 12)


########################################################################
# Example 8
########################################################################
# Normal Distribution
# Replicate natural phenomena of IQ
########################################################################
# Input the mean 100
# Input the standard deviation of 15
# Input sample size of 1015
rng = np.random.default_rng()
IQ = np.random.default_rng().normal(100, 15, 1015)
# Plot Function
plotsforassignment(IQ, 'Normal Distribution', 'IQ Score', 'IQ Count', 18)


########################################################################
# Example 9
########################################################################
# Binomial Distribution
# Probability of SPAM
########################################################################
# Input the p (probability of success on a given trial) = 0.15
# Input the n (number of trials) = 20
# Input k (number of successes) = 1000
rng = np.random.default_rng()
spam = np.random.binomial(n=20, p=0.15, size=1000)
# Plot Function
plotsforassignment(spam, 'Binomial Distribution', 'Probability is SPAM', 'SPAM Count', 10)


########################################################################
# Example 10
########################################################################
# Poisson Distribution
# Probability of SPAM
########################################################################
# Input lam - rate or known number of occurences e.g. 2 for above problem.
# Input size - The shape of the returned array = 1000
rng = np.random.default_rng()
hungry = np.random.poisson(lam=2, size=1000)
# Plot Function
plotsforassignment(hungry, 'Poisson Distribution', 'Eating per day', 'Probability', 8)


########################################################################
# Example 11
########################################################################
# Exponential Distribution
# Probability of SPAM
########################################################################
# Input the minutes of the eruption 40
# Input sample size 1000
rng = np.random.default_rng()
geyser  = np.random.exponential(40, 1000)
# Plot Function
plotsforassignment(geyser, 'Exponential Distribution', 'Minutes', 'Probability', 20)


########################################################################
# Example 12
########################################################################
# Seeds in generating pseudorandom numbers
########################################################################
for nonseeds in range(5):
    # Any number can be used in place of '0'.
    rng = np.random.default_rng()  
    # Generated random number will be between 1 to 1000.
    print(rng.integers(1, 1000)) 


for i in range(5):  
    # Any number can be used in place of '0'.
    rng = np.random.default_rng(seed=239)  
    # Generated random number will be between 1 to 1000.
    print(rng.integers(1, 1000)) 