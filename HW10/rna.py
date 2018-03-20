from heapq import heapify, heappop, heappush, nsmallest
from collections import defaultdict
from time import time


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






def kbest(n, k):

    i, j = 0, len(n)
    d = {'': [[0, '']], 'A': [[0, '.']], 'U': [[0, '.']], 'C': [[0, '.']], 'G': [[0, '.']]}   # format: sum, possibilities, paths(a lot)
    # dict_best = defaultdict(-1)
    rna = {'AU', 'GC', 'GU', 'UA', 'CG', 'UG'}

    def find(i, j):

        # if (i,j) in dict_best:
        #     return dict_best[(i,j)]

        if n[i:j] in d:
            return d[n[i:j]]

        matrix = []
        check_set = set()
        a, b = [], []
        for l in range(i+1, j):
            matched = []
            if (n[i] + n[l]) in rna:  # if they make a pair
                a = find(i+1, l)    # find between i and l
                b = find(l+1, j)    # find from l+1 to j

            if a or b: matched = [a,b,len(matrix)]

            if matched: matrix.append(matched)

        nex = find(i+1, j)
        heap = [[matrix[i][0][0][0] + matrix[i][1][0][0] - 1,'('+ matrix[i][0][0][1] + ')'+ matrix[i][1][0][1], matrix[i][2], 0, 0] for i, a in enumerate(matrix)]
        last = len(matrix)
        heap.append([nex[0][0], '.' + nex[0][1], last, 0])

        heapify(heap)
        temp = []


        while heap :

            if len(temp) >= k: break

            popped = heappop(heap)


            if len(popped) == 5: #from matched

                summ, path, m_id, a, b = popped

                if (m_id, a, b) not in check_set:
                    temp.append([summ, path])
                    # check_set.add((m_id, a, b))


                    curr = matrix[m_id]

                    if a + 1 < len(curr[0]) and (m_id, a+1, b) not in check_set:
                        heappush(heap, [matrix[m_id][0][a+1][0] + matrix[m_id][1][b][0] - 1 ,'('+ matrix[m_id][0][a+1][1] + ')'+ matrix[m_id][1][b][1], matrix[m_id][2], a+1, b])
                        check_set.add((m_id, a+1, b))
                    if b + 1 < len(curr[1]) and (m_id, a, b+1) not in check_set:
                        heappush(heap, [matrix[m_id][0][a][0] + matrix[m_id][1][b+1][0] - 1,'(' + matrix[m_id][0][a][1] + ')' + matrix[m_id][1][b+1][1], matrix[m_id][2], a, b+1])
                        check_set.add((m_id, a, b+1))
            else: #from nex

                summ, path, m_id, idx = popped

                if (m_id, idx) not in check_set:
                    temp.append([summ, path])
                    # check_set.add((m_id, idx))


                    if idx < len(nex) and (m_id, idx) not in check_set:

                        heappush(heap, [nex[idx][0], '.' + nex[idx][1], m_id, idx+1])
                        check_set.add((m_id, idx))

            print("C SET: ",check_set)

        d[n[i:j]] = temp
        # print(temp)
        return temp

    f = find(i, j)

    f = [ [i*-1, _] for i, _ in f ]
    # print(d)

    return f

# print(kbest('AGGCAUCAAACCCUGCAUGGGAGCG',10))


def performance_test():
    t = time()
    print(kbest('AGGCAUCAAACCCUGCAUGGGAGCG',10))
    print("TestTime:",time() - t)

performance_test()