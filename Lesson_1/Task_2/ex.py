def main(strg):
    if strg == strg[::-1]:
       print('This is palindrome.')
    else:
      print('This is not palindrome.')

if __name__ == '__main__':
    input_string=input()
    main(input_string)
