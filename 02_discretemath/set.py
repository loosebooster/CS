# 03.
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


def powerset(num):
    masks = [1 << i for i in range(len(num))]
    #print(f'masks: {masks}')  ## >>> masks: [1, 2, 4, 8, 16]
    for j in range(1 << len(num)):
        yield [s for s, mask in zip(num,masks) if mask & j]    ## j = 0 ~ 2^n

for p in powerset(num):
    print(p)
