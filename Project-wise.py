puzzle = 1
def num(n,r,c,m):
    no = 1
    for i in range(r):
        for j in range(c):
            if m[i][j]  != '*':
                if j == 0 or m[i][j-1] == '*':
                    n[i][j] = no
                    no += 1
                elif i == 0 or m[i-1][j] == '*':
                        n[i][j] = no
                        no += 1
    return n


def across(n,m,r,c):
    acno = 0
    s = ""
    print('Across')
    flag =0
    for i in range(0,r):
        for j in range(0,c):
            if(m[i][j] != '*'):
                if flag == 0:
                    acno = n[i][j]
                    flag =1
                s += m[i][j]
            if m[i][j] != '*' and (j == c-1 or m[i][j+1] == '*'):
                print(str(acno)+'.'+str(s))
                flag =0
                s = ""

def down(m,n,r,c):
    print('Down')
    acno = 0
    flag = 0
    dici= dict()
    s =""
    for j in range(c):
        for i in range(r):
            if(m[i][j] != '*'):
                if flag == 0:
                    acno = n[i][j]
                    flag = 1
                s =  s + m[i][j]
            if  (i == r-1 or m[i+1][j] == '*') and m[i][j] != '*':
                flag = 0
                dici[acno] = s
                s = ""
    for i,j in sorted(dici.items()):
        print(str(i)+'.'+j)

while(True):
    p = input()
    if p == '0':
        break
    else:
        p = p.split()
        r = int(p[0])
        c = int(p[1])
        m = []
        for i in range(0,r):
            s = input()
            l = list(s)
            m.append(l)
        print('puzzle #',puzzle,':')
        n = [[0 for i in range(c)] for j in range(r)]
        n = num(n,r,c,m)
        puzzle+=1
        across(n,m,r,c)
        down(m,n,r,c)