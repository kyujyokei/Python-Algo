from heapq import heapify, heappop, heappush

def _mbest(n, matrix):
    heap = [(a[0][0], i, 0, 0) for i, a in enumerate(matrix)]
    heapify(heap)
    for _ in range(0,n-1):
        value, a, i, j = heappop(heap)
        yield value
        print(i)
        curr = matrix[a]
        if i + 1 < len(curr):
            if (matrix[a][i+1][j],a,i+1,j) not in heap: heappush(heap,((matrix[a][i+1][j]),a,i+1,j))
        if j + 1 < len(curr[a]):
            if (matrix[a][i][j+1],a,i,j+1) not in heap: heappush(heap,((matrix[a][i][j+1]),a,i,j+1))

mbest = lambda n, matrix: list(_mbest(n, matrix))

matrix = [[[1,2,4,5,6],[2,3,5,6,7],[4,5,6,7,8],[5,6,7,8,9],[6,7,8,9,10]],[[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10]],[[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10]],[[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10]],[[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10]]]

print(mbest(15,matrix))