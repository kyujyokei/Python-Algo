#
# def best1(n):
#     d = {'': [0, ''], 'A': [0, '.'], 'U': [0, '.'], 'C': [0, '.'], 'G': [0, '.'], 'AU': [1, '()'], 'GC': [1, '()'],
#          'GU': [1, '()'], 'UA': [1, '()'], 'CG': [1, '()'], 'UG': [1, '()'], 'AC': [0, '..'], 'CA': [0, '..'],
#          'UC': [0, '..'], 'CU': [0, '..'], 'AG': [0, '..'], 'GA': [0, '..'], 'AA': [0, '..'], 'GG': [0, '..']}
#
#     def pair(a):
#         rna = set(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])
#         return a in rna
#
#     def find(n, i, j):
#         print(i,j,n[i:j])
#         if n[i:j] in d:
#             return d[n[i:j]]
#         else:
#             if pair(n[i] + n[j-1]): # if they make a pair
#
#                 sum, path = find(n,i+1,j-1)
#                 print(n,n[i] + n[j-1], sum, path)
#                 d[n[i:j]] = [sum + 1, '(' + path + ')']
#                 return d[n[i:j]]
#             else:
#                 temp = []
#                 for k in range(i+1,j):
#                     print(n[i+1:j],k)
#                     if n[i:k] not in d:
#                         d[n[i:k]] = find(n,i,k)
#                     if n[k:j] not in d:
#                         d[n[k:j]] = find(n,k,j)
#
#                     temp.append([d[n[i:k]][0]+d[n[k:j]][0], d[n[i:k]][1]+d[n[k:j]][1]])
#
#                 return max(temp, key= lambda x: x[0])
#     return tuple(find(n,0,len(n)))


def best(n):
    i, j = 0, len(n)
    d = {'': [0, ''], 'A': [0, '.'], 'U': [0, '.'], 'C': [0, '.'], 'G': [0, '.']}

    rna = {'AU', 'GC', 'GU', 'UA', 'CG', 'UG'}

    def find(i, j):
        if n[i:j] in d:
            return d[n[i:j]]

        matched = []
        for k in range(i+1, j):
            if (n[i] + n[k]) in rna:  # if they make a pair
                sum, path = find(i+1, k)   # find between i and k
                sum1, path1 = find(k+1, j)   # find from k+1 to j
                if not matched or sum + sum1 + 1 > matched[0]:   # update the best match
                    matched = [sum + sum1 + 1, '(' + str(path) + ')' + str(path1)]

        maximum = matched if matched else [0,'.' * len(n[i:j])]   # all dots if no match

        next_sum, next_path = find(i+1, j)
        next_com = [next_sum, '.' + str(next_path)]

        d[n[i:j]] = max(maximum, next_com, key=lambda x: x[0])

        return d[n[i:j]]

    return find(i, j)


def total(n):

    i, j = 0, len(n)
    d = {'': 1, 'A': 1, 'U': 1, 'C': 1, 'G': 1}   # format: sum, possibilities, path
    rna = {'AU', 'GC', 'GU', 'UA', 'CG', 'UG'}

    def find(i, j):
        if n[i:j] in d:
            return d[n[i:j]]

        matched = 0
        for k in range(i + 1, j):
            if (n[i] + n[k]) in rna:  # if they make a pair
                sum = find(i + 1, k)  # find between i and k
                sum1 = find(k + 1, j)  # find from k+1 to j
                matched += (sum * sum1)

        next_sum = find(i + 1, j)

        d[n[i:j]] = matched + next_sum

        return d[n[i:j]]

    return find(i, j)

def kbest(n):

    i, j = 0, len(n)
    d = {'': [[0, '']], 'A': [[0, '.']], 'U': [[0, '.']], 'C': [[0, '.']], 'G': [[0, '.']]}   # format: sum, possibilities, paths(a lot)
    rna = {'AU', 'GC', 'GU', 'UA', 'CG', 'UG'}

    def find(i, j):
        if n[i:j] in d:
            return d[n[i:j]]

        matched = []
        for k in range(i+1, j):
            if (n[i] + n[k]) in rna:  # if they make a pair
                sum, path = find(i+1, k)   # find between i and k
                sum1, path1 = find(k+1, j)   # find from k+1 to j
                if not matched or sum + sum1 + 1 > matched[0]:   # update the best match
                    matched = [sum + sum1 + 1, '(' + str(path) + ')' + str(path1)]

        maximum = matched if matched else [0,'.' * len(n[i:j])]   # all dots if no match

        next_sum, next_path = find(i+1, j)
        next_com = [next_sum, '.' + str(next_path)]

        d[n[i:j]] = max(maximum, next_com, key=lambda x: x[0])

        return d[n[i:j]]

    return find(i, j)

print(kbest('ACAGU'))