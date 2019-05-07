import PySimpleGUI as sg
import selectaggregation as sag
import deleteaggregation as dag

window = sg.Window('TL;DR')

layout = [[sg.Text('Please select the article you would like summarized')],
          [sg.InputCombo(['Why Turkey’s Election Results Test Erdogan’s Grip on Power', 
                          'The High Stakes Battle Between Donald Trump and the Federal Reserve',
                          'Kirstjen Nielsen’s Inevitable Resignation from the Department of Homeland Security', 'How Trump Betrayed the General Who Defeated ISIS', 'Netanyahu, Gantz, and Five Scenarios for the Israeli Election'
                         ], key = 'article', change_submits = False, readonly = True)],
          [sg.Text('Summarize using:')], [sg.InputCombo(['selection', 'deletion'], key = 'type', change_submits = False, readonly = True)],
    [sg.Text('Please select how summarized you would like your article to be')],
 [sg.Text('Values range from 0% to 100%')],
 [sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=50, key='sliderval')],
 [sg.Submit(), sg.Cancel()]]      
    
event, values = window.Layout(layout).Read()     

def summary(article, agreement):
    if(values['type'] == 'deletion'):
        return dag.summarize(article, agreement, "data/delete_qc_output.csv", "data/delete_sentence_dict.csv")
    else:
        return sag.summarize(article, agreement, "data/select_qc_output.csv", "data/select_sentence_dict.csv")
    
if(values['article'] == 'Netanyahu, Gantz, and Five Scenarios for the Israeli Election'):
    sg.PopupScrolled(summary(3, values['sliderval']), title = "Summary")
elif(values['article'] == 'How Trump Betrayed the General Who Defeated ISIS'):
    sg.PopupScrolled(summary(5, values['sliderval']), title = "Summary")
elif(values['article'] == 'Kirstjen Nielsen’s Inevitable Resignation from the Department of Homeland Security'):
    sg.PopupScrolled(summary(4, values['sliderval']), title = "Summary")
elif(values['article'] == 'The High Stakes Battle Between Donald Trump and the Federal Reserve'):
    sg.PopupScrolled(summary(2, values['sliderval']), title = "Summary")
else:
    sg.PopupScrolled(summary(1, values['sliderval']), title = "Summary")
