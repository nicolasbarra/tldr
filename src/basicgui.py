import PySimpleGUI as sg
import aggregation as ag

window = sg.Window('Test GUI')

layout = [[sg.Text('Please select how summarized you would like your article to be')],
 [sg.Text('Values range from 0% to 100%')],
 [sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=50, key='sliderval')],
 [sg.Submit(), sg.Cancel()]]      
    
event, values = window.Layout(layout).Read()      
sg.PopupScrolled(ag.summarize('trdl', values['sliderval'],"data/test_output.csv", "data/dict.csv" ), title = "Summary")