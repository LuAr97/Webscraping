import PySimpleGUI as psg
import webscrap as ws
menu_def = [['File', ['New', 'Open', 'Save', 'Exit', ]], ['Edit', ['Cut', 'Copy', 'Paste', 'Undo'], ],  ['Help', 'About...'], ]
companies, positions, results = ws.job_seek()
filter_1 = ['Menu', companies]
filter_2 = ['Menu', positions]
company = ''
position = ''
column_layout = [[psg.ButtonMenu('not used', filter_1), psg.ButtonMenu('not used', filter_2)]]
layout = [
   [psg.Menu(menu_def)],
   [psg.ButtonMenu('By company', filter_1), psg.ButtonMenu('By positions', filter_2)],
   [psg.Text(text=len(results),
   font=('Arial Bold', 20),
   size=20,
   expand_x=True,
   justification='center')],
]
print(company, position)
window = psg.Window('SeekingJobs', layout, size=(715,250))
while True:
   event, values = window.read()
   print(event, values)
   if event == 1:
      company = values[event]
   if event == 2:
      position = values[event]
   if event == psg.WIN_CLOSED or event == 'Exit':
      break
window.close()