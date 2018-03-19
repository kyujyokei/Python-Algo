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
        # if d['G'] == []:
        #     print("STOP")
        # print("Now finding...",i,j, n[i:j])
        # print("D is now... ", d, "N[I:J] is ", n[i:j])
        # bob = n[i:j]
        if n[i:j] in d:
            return d[n[i:j]]

        matrix = []
        for l in range(i+1, j):
            matched = []
            if (n[i] + n[l]) in rna:  # if they make a pair
                res1 = find(i+1, l)    # find between i and l
                res2 = find(l+1, j)    # find from l+1 to j

                heap = [[res1[0][0] + res2[0][0] - 1, '(' + res1[0][1] + ')' + res2[0][1], 0, 0]]
                # print("Heap: ",heap, res1, res2)

                for _ in range(0,k):
                    if not heap: break
                    # print("HEAP[0]: ",heap[0])
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

            # print("Matrix: ", matrix, n[i:j])

        nex = [find(i+1, j)]

        # res = [matched[0]+[0, 0], [nex[0][0],'.' + nex[0][1],1,0]]
        # print("MATRIX: ", matrix)
        heap = [[matrix[i][0][0][0], matrix[i][0][0][1], i, 0, 0] for i, a in enumerate(matrix)]
        last = len(matrix)

        heap.append([nex[0][0][0],'.' + nex[0][0][1], last, 0, 0])

        # print("NEX:", nex, ", LAST: ", last)
        # print("HEAP:",heap)
        # print()
        heapify(heap)
        temp = []

        for _ in range(0,k):
            # print("H-POP R:", res[0], k, i, j)
            if not heap: break
            [summ, path, m_id, a, b] = heappop(heap)
            # print("Popped Now:", [summ, path, m_id, a, b])
            # print("MatrixPopped:", matrix[m_id])


            if [summ, path] not in temp:
                temp.append([summ, path])
            if m_id < last: # comes from matched pairs

                if a + 1 < len(matrix[m_id]):
                    heappush(heap, [matrix[m_id][a+1][b][0], matrix[m_id][a+1][b][1], m_id, a+1, b])
                    # print("A:",heap)
                if b + 1 < len(matrix[m_id][a]):
                    heappush(heap, [matrix[m_id][a][b+1][0], matrix[m_id][a][b+1][1], m_id, a, b+1])
                    # print("B:", [matrix[m_id][a][b+1][0], matrix[m_id][a][b+1][1], m_id, a, b+1])
            else: # comes from nex
                if a + 1 < len(nex):
                    heappush(heap, [nex[a + 1][b][0], '.' + nex[a + 1][b][1], last, a + 1, b])
                    # print("LAST A:", heap)
                if b + 1 < len(nex[a]):
                    heappush(heap, [nex[a][b+1][0], '.' + nex[a][b+1][1], last, a, b+1])
                    # print("LAST B:", [nex[a][b+1][0], '.' + nex[a][b+1][1], last, a, b+1])

            # print()

            # if len(res) >= k: break
        # next_com = [next_sum, '.' + str(next_path)]

        d[n[i:j]] = temp

        return d[n[i:j]]

    f = find(i, j)

    f = [ [i*-1, _] for i, _ in f ]

    return f

# print(kbest('CCCGGG',10))