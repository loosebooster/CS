# make the power set of {1, 2, 3, ..., n}
# the power set (or powerset) of a set S is the set of all subsets of S, including the empty set and S itself

n = int(input("number: "))

num = []
for i in range(1,n+1):
    num.append(i)


'''
#### Not Working ####
 
arr = list(map(int, input().split()))
subsets = [[]]

for i in arr:
    L = len(subsets)
    for l in range(L):
        subsets.append(subsets[l] + [i])

print(f'subsets: {subsets}')
'''


def powerset(n):
    masks = [1 << i for i in range(len(n))]
    #print(f'masks: {masks}')
    for i in range(1 << len(n)):
        yield [s for s, mask in zip(n,masks) if mask & i]

for p in powerset(num):
    print(p)