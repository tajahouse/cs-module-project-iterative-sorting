# TO-DO: Complete the selection_sort() function below
import sys
def selection_sort(array):
    # loop through n-1 elements
    for i in range(len(array)):
        cur_index = i
        for j in range(i+1, len(array)):
            if array[cur_index] > array[j]:
                cur_index = j
        array[i], array[cur_index] = array[cur_index], array[i]

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
    return array


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code 
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
