alph = { 'A' : '.-',
         'B' : '-...',
         'C' : '-.-.',
         'D' : '-..',
         'E' : '.',
         'F' : '..-.',
         'G' : '--.',
         'H' : '....',
         'I' : '..',
         'J' : '.---',
         'K' : '-.-',
         'L' : '.-..',
         'M' : '--',
         'N' : '-.',
         'O' : '---',
         'P' : '.--.',
         'Q' : '--.-',
         'R' : '.-.',
         'S' : '...',
         'T' : '-',
         'U' : '..-',
         'V' : '...-',
         'W' : '.--',
         'X' : '-..-',
         'Y' : '-.--',
         'Z' : '--..' 
       }


def morse(strg, alphabet):
  inpstrg = strg.upper()
  morsestrg = ''
  for i in inpstrg:
    newsymb = alphabet.get(i)
    morsestrg = morsestrg[::] + newsymb + ' '
  return(morsestrg)


if __name__ == '__main__':
  _inpstrg = input()
  _morsestrg = morse(_inpstrg, alph)
  print(_morsestrg)
