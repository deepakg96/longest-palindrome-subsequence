'''
---------------------------------------------------------------------------
HOW TO RUN THIS FILE
---------------------------------------------------------------------------

python pa2_solved.py <input_file>
For example: python pa2_solved.py input1.txt

You can use redirection to redirect stdout to file like shown below,
python pa2_solved.py input1.txt > out1.txt
Then you can use vimdiff to see the difference in output files [or] use the palindrome checker.
'''


import sys

def longest_palindrome_sequence(ip_str):
    n = len(ip_str)

    if (n == 0):
        print("Empty string!")
        return

    del_list = [[0 for x in range(n)]for y in range(n)]
    str_list = [["" for x in range(n)]for y in range(n)]

    for i in range(n):
        del_list[i][i] = 1
        str_list[i][i] = ip_str[i]

    for x in range(2, n+1):
        for i in range(n - x + 1):
            j = i + x - 1
            if (ip_str[i] == ip_str[j] and x == 2):
                del_list[i][j] = 2
                str_list[i][j] = ip_str[i] + str_list[i][j] + ip_str[j]
            elif (ip_str[i] == ip_str[j]):
                del_list[i][j] = del_list[i + 1][j - 1] + 2
                str_list[i][j] = ip_str[i] + str_list[i + 1][j - 1] + ip_str[j]
            else:
                del_list[i][j] = max(del_list[i][j - 1], del_list[i + 1][j])
                if del_list[i][j - 1] >= del_list[i + 1][j]:
                    str_list[i][j] = str_list[i][j - 1]
                else:
                    str_list[i][j] = str_list[i + 1][j]

    print(del_list[0][n-1])
    print(str_list[0][n-1])

filename=sys.argv[1]
fp=open(filename,"r")
ip_str=fp.read()
longest_palindrome_sequence(ip_str)
fp.close()
