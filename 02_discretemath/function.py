# Function Discriminator

## A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
## B = Input-data
## Determining the relationship between A & B
## f1 = {(1, 1), (2, 1), (3, 1), (3, 4), (6, 5), (6, 6), (7, 1), (7, 2), (9, 9), (10, 10)}
## f2 = {(1, 3), (2, 4), (3, 1), (4, 2), (5, 6), (6, 7), (7, 4), (8, 3), (9, 1), (10, 9)}


A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

f1 = {(1, 1), (2, 1), (3, 1), (3, 4), (6, 5), (6, 6), (7, 1), (7, 2), (9, 9), (10, 10)}
f2 = {(1, 3), (2, 4), (3, 1), (4, 2), (5, 6), (6, 7), (7, 4), (8, 3), (9, 1), (10, 9)}
'''
def func(A, input):
    li = list(input)
    A = list(A)
    domain = []
    codomain = []
    for i in range(len(li)):
        domain.append(li[i][0])
        codomain.append(li[i][1])
    for j in range(len(A)):
        if A[i] in domain:
            for k in range(len(codomain)):
                if codomain[k] in A:
                    print("correct")
        else:
            print("wrong")
'''