# In this Kata, you will be given an array of numbers
# in which two numbers occur once and the rest occur only twice.
# Your task will be to return the sum of the numbers that occur
# only once.
#
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.
#



def repeats1(arr):
    mydict = {}
    for i in range(len(arr)):
        if arr[i] in mydict:
            mydict[arr[i]] += 1
        else:
            mydict[arr[i]] = 1

    res = 0
    for key, value in mydict.items():
        if value == 1:
            res += key

    return res


def repeats(arr):
    res = sum([x for x in arr if arr.count(x) == 1])

    return res


if __name__ == '__main__':
    print(repeats([4, 5, 7, 5, 4, 8]))
