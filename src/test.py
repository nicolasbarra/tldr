import PySimpleGUI as sg

layout = [[sg.Text('Fuckme')],      
          [sg.Input(), sg.FileBrowse()],      
          [sg.OK(), sg.Cancel()]]

event, (number,) = sg.Window('Get filename example').Layout(layout).Read()

sg.Popup(event, number)
