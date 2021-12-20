def possibility(y, listn):
    x = listn[0]
    while x < y:
        x += listn[x-1]
    if x == y:
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    n,t=map(int, input().split())
    a = map(int, input().split(" "))
    if possibility(t, list(a)) == True:
        print('Yes')
    else:
        print('No')
