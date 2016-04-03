#!/usr/bin/python

def determinant(l):
    n = len(l)
    if (n > 2):
        i = 1
        t = 0
        total = 0
        while t <= n - 1:
            d = {}
            t1 = 1
            while t1 <= n - 1:
                m = 0
                d[t1] = []
                while m <= n - 1:
                    if (m == t):
                        u = 0
                    else:
                        d[t1].append(l[t1][m])
                    m += 1
                t1 += 1
            l1 = [d[x] for x in d]
            total = total + i * (l[0][t]) * (determinant(l1))
            i = i * (-1)
            t += 1
        return total
    else:
        return (l[0][0] * l[1][1] - l[0][1] * l[1][0])



num = input("Enter N: ")
m = [[None] * int(num) for i in range(int(num))] # build N x N matrix
for i in range(int(num)):
    m[i] = [int(x) for x in input("Row " + str(i+1) + ": ").split(' ')]

det = determinant(m)
print("\n*** The Determinate: " + str(det))


