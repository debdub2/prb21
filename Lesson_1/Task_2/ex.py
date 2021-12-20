def main(strg):
    x = true if strg == strg[::-1] else false

if __name__ == '__main__':
    input_string=input()
    main(input_string)
    if x == true:
      print('This is palindrome.')
    else:
      print('This is not palindrome.')
