#https://codeforces.com/problemset/problem/4/A

def check(_weight):
  if _weight % 2 == 0 and _weight != 2:
    return 'Yes'
  else:
    return 'No'
 

if __name__ == '__main__':
  w = int(input())
  print(check(w))
