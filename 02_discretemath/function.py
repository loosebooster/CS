# Function Discriminator

## A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
## B = Input-data
## Determining the relationship between A & B
## f1 = {(1, 1), (2, 1), (3, 1), (3, 4), (6, 5), (6, 6), (7, 1), (7, 2), (9, 9), (10, 10)}
## f2 = {(1, 3), (2, 4), (3, 1), (4, 2), (5, 6), (6, 7), (7, 4), (8, 3), (9, 1), (10, 9)}


A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

f1 = {(1, 1), (2, 1), (3, 1), (3, 4), (6, 5), (6, 6), (7, 1), (7, 2), (9, 9), (10, 10)}
f2 = {(1, 3), (2, 4), (3, 1), (4, 2), (5, 6), (6, 7), (7, 4), (8, 3), (9, 1), (10, 9)}

''''''

def func(A, input):
    s = set()
    t = set()
    l = list(input)
    for i in range(len(l)):
        s.add(l[i][0])
        t.add(l[i][1])
    if A == s and A.issuperset(t):
        print("correct")
    else:
        print("wrong")

''''''

func(A, f1)   # >>> wrong
func(A, f2)   # >>> correct