def main(strg):
    return(strg == strg[::-1])

if __name__ == '__main__':
    input_string=input()
    if main(input_string) == 1:
      print('This is palindrome.')
    else:
      print('This is not palindrome.')
