# this is code for longest palindrome
def isPalindrome(element):

    temp = element
    rev_num = 0

    while element > 0:
        remainder = element % 10
        rev_num = rev_num * 10 + remainder
        element = element//10

    if temp == rev_num:
        return True
    else:
        return False


def isLargest(size_array, arr):

    arr.sort()
    for i in range(size_array-1, -1, -1):

        # if number is palindrome
        if(isPalindrome(arr[i])):
            return arr[i]

    return -1


if __name__ == "__main__":

    size_array = int(input("enter the size of array:"))
    arr = []
    for i in range(size_array):
        arr.append(int(input()))

    # print required answer
    print(f" Longest Palindrome in Array is {isLargest(size_array, arr)}")
