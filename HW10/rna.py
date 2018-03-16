
def best1(n):
    d = {'': [0, ''], 'A': [0, '.'], 'U': [0, '.'], 'C': [0, '.'], 'G': [0, '.'], 'AU': [1, '()'], 'GC': [1, '()'],
         'GU': [1, '()'], 'UA': [1, '()'], 'CG': [1, '()'], 'UG': [1, '()'], 'AC': [0, '..'], 'CA': [0, '..'],
         'UC': [0, '..'], 'CU': [0, '..'], 'AG': [0, '..'], 'GA': [0, '..'], 'AA': [0, '..'], 'GG': [0, '..']}

    def pair(a):
        rna = set(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])
        return a in rna

    def find(n, i, j):
        print(i,j,n[i:j])
        if n[i:j] in d:
            return d[n[i:j]]
        else:
            if pair(n[i] + n[j-1]): # if they make a pair

                sum, path = find(n,i+1,j-1)
                print(n,n[i] + n[j-1], sum, path)
                d[n[i:j]] = [sum + 1, '(' + path + ')']
                return d[n[i:j]]
            else:
                temp = []
                for k in range(i+1,j):
                    print(n[i+1:j],k)
                    if n[i:k] not in d:
                        d[n[i:k]] = find(n,i,k)
                    if n[k:j] not in d:
                        d[n[k:j]] = find(n,k,j)

                    temp.append([d[n[i:k]][0]+d[n[k:j]][0], d[n[i:k]][1]+d[n[k:j]][1]])

                return max(temp, key= lambda x: x[0])
    return tuple(find(n,0,len(n)))


def best(n):

    i, j = 0, len(n)


    d = {'': [0, ''], 'A': [0, '.'], 'U': [0, '.'], 'C': [0, '.'], 'G': [0, '.']}


    def pair(a):
        rna = set(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])
        return a in rna

    def find(n,i,j):

        print(n[i:j])
        if n[i:j] in d:
            return d[n[i:j]]

        matched = []
        for k in range(i+1, j):
            print(n[i] + n[k])
            if pair(n[i] + n[k]):  # if they make a pair
                print(k, i, j)
                sum, path = find(n, i+1, k-1)
                # d[n[i:k]] = [sum + 1, '(' + path + ')']
                sum1, path1 = find(n, k+1, j)
                # d[n[k:j]] = [sum1, path1]
                print(sum, path, sum1, path1)
                matched.append([sum+sum1,path+path1])
            print("MATCHED:",matched)

        # d[n[i:j]] = max(find(n,i,j),find(n,i+1,j), key= lambda x: x[0])

        return d[n[i:j]]
    # find(n,i,j)


    return find(n,i,j), d


def total():
    return 0

def kbest():
    return 0

print(best('GCACG'))