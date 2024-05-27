import PySimpleGUI as psg
import webscrap as ws
import webbrowser

def show(res) :
    count = 5
    pane = []
    for item in res:
        if count == 0 : break
        company_text = [psg.Text(text=item['company'],
         font=('Arial', 12),
         size=12,
         expand_x=True,
         justification='left',
         background_color='#000',
         text_color='#fff')
        ]
        position_text = [psg.Text(text=item['position'],
         font=('Arial', 12),
         size=12,
         expand_x=True,
         justification='left',
         background_color='#000',
         text_color='#fff')
        ]
        url = [psg.Button('Check it out!')]
        col1 = psg.Column([company_text], background_color='#000')
        col2 = psg.Column([position_text], background_color='#000')
        col3 = psg.Column([url], background_color='#000')
        pane = [psg.Pane([col1,col2,col3], size=(1000, 100), background_color='#000')]
        
        layout.append(pane)
        count -= 1

menu_def = [['File', ['New', 'Open', 'Save', 'Exit', ]], ['Edit', ['Cut', 'Copy', 'Paste', 'Undo'], ],  ['Help', 'About...'], ]
companies, positions, results = ws.job_seek()

layout = [
   [psg.Menu(menu_def)],
   [psg.Text(text='Most Recent 5 Job Positions',
         font=('Arial Bold', 15),
         size=12,
         expand_x=True,
         justification='center',
         background_color='#000',
         text_color='#fff')]
   
]

show(results)

psg.theme('Black')
psg.theme_button_color_background()
psg.theme_button_color_text()

window = psg.Window('SeekingJobs', layout, size=(1100,650))
while True:
   event, values = window.read()
   print(event, values)
   if 'Check it out!' in event:
       event_index = event.split('!')[1]
       if event_index == '':
           value = 0
       else:
           value = int(event_index) + 1
      
       webbrowser.open(results[value]['url'])
   if event == psg.WIN_CLOSED or event == 'Exit':
      break
window.close()