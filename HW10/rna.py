
def best(n):

    d = {'':[0,''],'A':[0,'.'], 'U':[0,'.'], 'C':[0,'.'], 'G':[0,'.'], 'AU':[1,'()'], 'GC':[1,'()'], 'GU':[1,'()'], 'UA':[1,'()'], 'CG':[1,'()'], 'UG':[1,'()'], 'AC':[0,'..'], 'CA':[0,'..'], 'UC':[0,'..'], 'CU':[0,'..'], 'AG':[0,'..'], 'GA':[0,'..']}

    def pair(a):
        rna = set(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])
        return a in rna

    def find(n):

        i, j = 0, len(n)
        if n in d:
            return d[n]
        else:
            if pair(n[i] + n[j-1]): # if they make a pair
                # print(n[i] + n[j-1])
                sum, path = find(n[i+1:j-1])
                d[n] = [sum + 1, '(' + path + ')']
                return d[n]
            else:
                temp = []
                for k in range(1,j):
                    if n[0:k] not in d:
                        d[n[0:k]] = find(n[0:k])
                    if n[k:j] not in d:
                        d[n[k:j]] = find(n[k:j])
                    print("D:",d[n[0:k]], d[n[k:j]])
                    temp.append([d[n[0:k]][0]+d[n[k:j]][0], d[n[0:k]][1]+d[n[k:j]][1]])
                # print(temp)
                return max(temp, key= lambda x: x[0])


    return find(n)

def total():
    return 0

def kbest():
    return 0


print(best('AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA'))