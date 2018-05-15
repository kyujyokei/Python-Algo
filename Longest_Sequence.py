import sys
import re

class Node(object):
    def __init__(self, data):
        self.data = data
        self.path = []
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def longest_subsequence(n, grid):
    """
    Take a rectangular grid of numbers and find the length
    of the longest sequence.
    Return the length as an integer.
    """
    adj = dict() # adjacency list
    d = dict() # the dictionary to prevent repeat calculations
    res = 0

    def make_tree(node):

        for n in adj[node.data]:
            if n not in node.path:
                new = Node(n)
                node.add_child(new)
                new.path = node.path + [n]
                new.data = n
                if adj[n]: make_tree(new)
    def print_tree(node):
        arr = []
        for c in node.children:
            arr.append(len(c.path))
            arr.append(print_tree(c))
        return max(arr) if arr else 0


    def map(n, grid):
        for i, arr in enumerate(grid):
            for j, x in enumerate(arr):

                if j > 0 and abs(grid[i][j-1] - x) > 3 : adj.setdefault((x,i,j),[]).append((grid[i][j-1],i,j-1)) # item at left
                if j+1 < n and abs(grid[i][j+1] - x) > 3 : adj.setdefault((x,i,j),[]).append((grid[i][j+1],i,j+1)) # item at right
                if i > 0 and abs(grid[i-1][j] - x) > 3 : adj.setdefault((x,i,j),[]).append((grid[i-1][j],i-1,j)) # top
                if i+1 < n and abs(grid[i+1][j] - x) > 3 : adj.setdefault((x,i,j),[]).append((grid[i+1][j],i+1,j)) # bottom
                if i > 0 and j > 0 and abs(grid[i-1][j-1] - x) > 3: adj.setdefault((x,i,j),[]).append((grid[i-1][j-1],i-1,j-1)) # top left
                if i > 0 and j+1 < n and abs(grid[i-1][j+1] - x) > 3: adj.setdefault((x,i,j),[]).append((grid[i-1][j+1],i-1,j+1)) # top right
                if j > 0 and i+1 < n and abs(grid[i+1][j-1] - x) > 3: adj.setdefault((x,i,j),[]).append((grid[i+1][j-1],i+1,j-1)) # bottom left
                if i+1 < n and j+1 < n and abs(grid[i+1][j+1] - x) > 3: adj.setdefault((x,i,j),[]).append((grid[i+1][j+1],i+1,j+1)) # bottom right

    map(n,grid)

    for x in adj:

        root = Node(x)
        root.path = [x]
        root.data = x
        make_tree(root)
        curr_longest = print_tree(root)
        if curr_longest > res: res = curr_longest

    return res

def main():
    # dims = [int(i) for i in sys.stdin.readline().split()]
    # num_rows, num_cols = 3, 3
    n = 3
    # grid = [[int(i) for i in sys.stdin.readline().split()] for _ in range(num_rows)]
    grid = [[8, 2, 4], [0, 6, 1], [3, 7, 9]]
    grid2 = [[4, 2, 4],[0, 3, 1],[3, 7, 9]]
    grid3 = [[1, 6, 2],[8, 3, 7],[4, 9, 5]]
    grid4 = [[1, 5, 1], [1, 1, 1], [1, 1, 1]]
    res = longest_subsequence(n, grid4)
    print(str(res) + "\n")

if __name__ == "__main__":
    main()