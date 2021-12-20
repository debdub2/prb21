def checkstrg(strg, x):
    a = 0
    for y in range(len(strg)):
        if x != y:
            if strg[x] == strg[y]:
                a += 1
    if a > 0:
        return(True)
    else:
        return(False)
      
if __name__ == '__main__':
    s = 0
    input_string=input()
    for i in range(len(input_string)):
        if checkstrg(input_string, i) == False:
            s += 1
    print(s)
