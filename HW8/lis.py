
def lis(str):

    T = [[1,[x]] for x in str]
    if len(str) <= 1: return None

    for i in range(1,len(str)):
        j = 0
        while j < i:
            if str[i][0] > str[j][0] :
                T[i] = max([T[i][0],[str[i]]], [T[j][0]+1,T[j][1] + [str[i]]], key = lambda x: x[0])

            j += 1
            print(T)


    return max(T)




# 1. Longest (Strictly) Increasing Subsequence
#
#    input/output are lower-case strings:
#
print(lis("aebbcg"))
#    "abcg"
#
print(lis("zyx"))
#    "z"
#
#    tiebreaking: arbitrary. any optimal solution is ok.
#
#    Q: What are the time and space complexities?
#
#    filename: lis.py