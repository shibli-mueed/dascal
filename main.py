import os
import uuid
import json

#to get current file path
dir_path = os.path.dirname(os.path.realpath(__file__))



#initial
def initialize():
    global loaded_data
    #it only take input when you run the code first time
    try:
        with open(f'{dir_path}\\res\\data.json', 'r') as file:
            loaded_data = json.load(file)
    except:
        os.mkdir(f'{dir_path}\\htmls')
        import subprocess as sp
        cmds=["python -m pip install --upgrade pip","pip install -r requirements.txt"]
        for i in cmds:
            sp.call(i)
            
        initial_param = {
                        }
        with open(f'{dir_path}\\res\\data.json','w') as file:
            file.write(json.dumps(initial_param, indent=4))
            loaded_data = initial_param



initialize()

#gui dependencies
import PySimpleGUI as sg

#global lists
lang_support = ["English","Deutsch","Русский"]

mins = ['60', '59', '58', '57', '56', '55', '54', '53', '52', '51', '50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01', '00']

hours = ['01', '02', '03', '04', '05', '06', '07', '08', '09','10','11','12']

time_12hr = ["AM","PM"]

levels = ['A1','A2','B1','B2','C1','C2']

#add notification data
def add_notif(param,time):
    # time = f'{param["hour"]}:{param["min"]} {param["time"]}'
    uid = str(uuid.uuid4())
    notif = {
            "uid":uid,
            "name":param["name"],
            "lang":param["lang"],
            "time":time,
            "level":param["level"]
        }
    
    with open(f'res\\data.json', 'r+') as file:
        #data = json.load(file)
        file_data = json.load(file)
        file_data[uid]=notif
        file.seek(0)
        json.dump(file_data, file, indent = 4)
    return notif
        
#delete notofication data
def del_notif(param):
   
    with open(f'res\\data.json', 'r') as file:
        #data = json.load(file)
        file_data = json.load(file)
        del file_data[param]
        #file.seek(0)
    with open(f'res\\data.json', 'w') as file:
        json.dump(file_data, file, indent = 4)

def crunch(param):
    uid  =  param["uid"]
    name =  param["name"]
    lang =  param["lang"]
    time =  param["time"]
    level = param["level"]
    window.extend_layout(container=window['CONTAINER_COL'],
                                    rows=[[sg.Column(layout=[[
                                        sg.Column(layout=[[sg.Text(f'{name}'.capitalize())]]),
                                                            sg.Column(layout=[[sg.Text(f'{lang} -> {level} German | At: {time}'),   
      sg.Button(button_text='Delete',
              key=f'{uid}_REMOVE')
      ]]
                                                            )
                                                            ]],
                                                    key=f'{uid}'
                                                    )
                                           ]])
    window['CONTAINER_COL'].contents_changed()

#Theme and layout
sg.theme('Default')
sg.set_options(font='Calibri 13')
layout = [
    [sg.Text("Title "),sg.Input(key='name'),
     sg.Push(),sg.Text('ʕっ•ᴥ•ʔっ')],
    
    [sg.Text("Your Nativ Language "),sg.Combo(lang_support,
                              key='lang',
                              expand_x=True,
                              default_value='English'
                              )],
    
    [sg.Text("Time "),sg.Combo(hours,
                              key='hour',
                              expand_x=True,
                              default_value="06"
                              ),
                    sg.Combo(mins,
                              key='min',
                              expand_x=True,
                              default_value="00"
                              ),
                    sg.Combo(time_12hr,
                              key='time',
                              expand_x=True,
                              default_value='PM'
                              )],
    
    [sg.Text("Choose Level "),sg.Combo(levels,
                              key='level',
                              expand_x=True,
                              default_value='B1'
                              )],
    
    [sg.Button("Add Notification",key='SUBMIT',expand_x=True),
    sg.Button("Load All Notification",key='VIEW',expand_x=True)],
    [sg.Column(layout=[[]],size=(600, 200),
                                      key='CONTAINER_COL',
                                      scrollable=True,
                                      expand_x=True,
                                      vertical_scroll_only=True)],

]


window = sg.Window("Dascal",
                   layout,
                   no_titlebar=False)



#GUI code      
while True:
    
    event, value = window.read()
    
    if event == "VIEW":
        initialize()
        for i in list(loaded_data.keys()):
            crunch(loaded_data[i])
            window["VIEW"].update(visible=False)
    
    if event == 'SUBMIT':
        time = f'{value["hour"]}:{value["min"]} {value["time"]}'
        
        if value["lang"] in lang_support and value["hour"] in hours and value["min"] in mins and value["time"] in time_12hr and value["level"] in levels:
    
            x = True
            for i in list(loaded_data.keys()):
                if loaded_data[i]['time']==time:
                    x = False
                    
                    
            if x:
                #print(add_notif(value))
                crunch(add_notif(value,time))
                #add_notif(value)
                initialize()
            
    elif event.endswith('_REMOVE'):
        item_column_key = event.replace('_REMOVE', '')
        window[item_column_key].update(visible=False)
        del_notif(item_column_key)
        

        
        if event in ('Close', sg.WIN_CLOSED):
            break

 
window.close()