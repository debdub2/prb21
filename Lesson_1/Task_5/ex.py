def replacestrg(strg):
    x = 0
    while x < n-2:
        if strg[x] == B and s[x+1] == G:
            strg=strg.replace(s[x], 'B')
            strg=strg.replace(s[x+1], 'G')
            x +=1
        x += 1
    return(strg)
    
if __name__ == '__main__':
    n=int(input())
    t=int(input())
    s=input()
    for i in range(t-1):
        s=s.replace(s, replacestrg(s))
    print(s)
