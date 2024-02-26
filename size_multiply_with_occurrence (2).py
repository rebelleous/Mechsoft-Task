'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t,z):
    max_flag = 0 #Flag for counting the max value.
    t_length = len(t)

    for x in range(t_length):

        for y in range(x + 1, t_length + 1): #Finding the substrings

            substrings = t[x:y]
            count = z.count(substrings) #Counting the substrings that occurs.
            max_flag = max(max_flag, len(substrings) * count) #Update the max value.

    return max_flag


if __name__ == '__main__':
    find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    result = find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa") #Checking the result if it works.
    print(result)
    