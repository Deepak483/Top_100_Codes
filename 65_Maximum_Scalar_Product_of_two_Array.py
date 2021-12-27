# Maximum Scalar product means Scalar product of two vectors is also known as the dot product. Dot product is an algebraic expression which takes two equal sized vectors and returns a single scalar.

# Lets say we have two arrays arr1 [1,3,4,2] and arr2 [2,4,3,5] , for finding the maximum scalar product of arrays we need to multiply the minimum value of arr1 to the minimum value of arr2 and add all these multiplied value. So, here we need to sort both the array 1 and array 2 in ascending order i.e.we get arr1 [1,2,3,4] and arr2 [2,3,4,5]

# Maximum dot product =  1*2 + 2*3 + 3*4 + 4*5  =  40

def max_scalar(arr1, arr2, n):
    sum = 0
    for i in range(0, n):
        sum += arr1[i]*arr2[i]
    return sum


n = int(input("Enter the size of array: "))

print("Enter the elements in first array: ")
arr1 = list(map(int, input().split()))
print("Enter the elements in second array: ")
arr2 = list(map(int, input().split()))

arr1.sort()  # Sorting in ascending order
arr2.sort()  # Sorting in ascending order

print("Maximum Scalar Product of Two Array: ", max_scalar(arr1, arr2, n))
