import random
import string 
import PySimpleGUI as sg

sg.theme('DarkTeal12')
sg.set_options(font='Arial 15')

layout = [
  [sg.Text('No. of Uppercase: '),sg.Push(), sg.Input(size=12, key='-UP-')],
  [sg.Text('No. of Lowercase: '),sg.Push(), sg.Input(size=12, key='-LOW-')],
  [sg.Text('No. of Digits: '),sg.Push(), sg.Input(size=12, key='-DIG-')],
  [sg.Text('No. of Symbols: '),sg.Push(), sg.Input(size=12, key='-SYM-')],
  [sg.Button('Generate'), sg.Button('Cancel')],
  [sg.Text('Password'), sg.Multiline(size=20, no_scrollbar=True,disabled=True, key='-PASS-')]

]

window =sg.Window('Password Generator', layout)

while True:
    event, values =window.read()
    if event =='Cancel' or event ==sg.WIN_CLOSED:
        break
    
    if event == 'Generate':
       try:
         u_upper= int(values['-UP-'])
         upper= random.sample(string.ascii_uppercase, u_upper)

         u_lower= int(values['-LOW-'])
         lower= random.sample(string.ascii_lowercase, u_lower)

         u_digits= int(values['-DIG-'])
         digits= random.sample(string.digits, u_digits)

         u_symbols= int(values['-SYM-'])
         symbols= random.sample(string.punctuation, u_symbols)

         total= upper+lower+digits+symbols
         total=random.sample (total, len(total))
         total=''.join(total)
         print(total)  
         window['-PASS-'].update(total)

       except ValueError:
          window['-PASS-'].update("No Valid Inputs")

window.close()