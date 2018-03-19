from heapq import heapify, heappop, heappush, nsmallest


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
    rna = {'AU', 'GC', 'GU', 'UA', 'CG', 'UG'}

    def find(i, j):

        if n[i:j] in d:
            return d[n[i:j]]

        matrix = []
        for l in range(i+1, j):
            matched = []
            if (n[i] + n[l]) in rna:  # if they make a pair
                res1 = find(i+1, l)    # find between i and l
                res2 = find(l+1, j)    # find from l+1 to j

                heap = [[res1[0][0] + res2[0][0] - 1, '(' + res1[0][1] + ')' + res2[0][1], 0, 0]]

                for _ in range(0,k):
                    if not heap: break
                    summ, path, a, b = heappop(heap)

                    if [summ,path] not in matched:
                        matched.append([summ,path])
                    if a+1 < len(res1):
                        if [[res1[a+1][0] + res2[b][0] - 1, '(' + res1[a+1][1] + ')' + res2[b][1]], a+1, b] not in heap:
                            heappush(heap, [res1[a+1][0] + res2[b][0] - 1, '(' + res1[a+1][1] + ')' + res2[b][1], a+1, b])
                    if b+1 < len(res2):
                        if [[res1[a][0] + res2[b+1][0] - 1, '(' + res1[a][1] + ')' + res2[b+1][1]], a, b+1] not in heap:
                            heappush(heap, [res1[a][0] + res2[b+1][0] - 1, '(' + res1[a][1] + ')' + res2[b+1][1], a, b+1])
            if len(matched) == 0 : matched = [[0,'.' * len(n[i:j])]]
            matrix.append([matched])

        nex = [find(i+1, j)]

        heap = [[matrix[i][0][0][0], matrix[i][0][0][1], i, 0, 0] for i, a in enumerate(matrix)]
        last = len(matrix)

        heap.append([nex[0][0][0],'.' + nex[0][0][1], last, 0, 0])

        heapify(heap)
        temp = []

        for _ in range(0,k):

            if not heap: break
            [summ, path, m_id, a, b] = heappop(heap)

            if [summ, path] not in temp:
                temp.append([summ, path])

            if m_id < last: # comes from matched pairs
                curr = matrix[m_id]

                if a + 1 < len(curr):
                    heappush(heap, [curr[a+1][b][0],curr[a+1][b][1], m_id, a+1, b])

                if b + 1 < len(curr[a]):
                    heappush(heap, [curr[a][b+1][0], curr[a][b+1][1], m_id, a, b+1])

            else: # comes from nex
                if a + 1 < len(nex):
                    heappush(heap, [nex[a + 1][b][0], '.' + nex[a + 1][b][1], last, a + 1, b])

                if b + 1 < len(nex[a]):
                    heappush(heap, [nex[a][b+1][0], '.' + nex[a][b+1][1], last, a, b+1])


        d[n[i:j]] = temp

        return temp

    f = find(i, j)

    f = [ [i*-1, _] for i, _ in f ]

    return f

# print(kbest('AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU',20))


