#system
import time
import webbrowser
import json
import os
import datetime

#built
import pager
import version

#external
import zroya

dir_path = os.path.dirname(os.path.realpath(__file__))

txts = {
    "A1":f"{dir_path}/../res/a1.txt",
    "A2":"",
    "B1":"",
    "B2":"",
    "C1":"",
    "C2":""
    
}


       
    
status = zroya.init(
    app_name="Dascal",
    company_name="Dascal",
    product_name="Dascal",
    sub_product="Dascal",
    version=version.version
)


# Template 
notification_template = zroya.Template(zroya.TemplateType.ImageAndText4)
notification_template.setImage("../res/icon.ico")



def send_notification(first,level,html_url):
    notification_template.setFirstLine(first)
    notification_template.setSecondLine(f"New Word {level}")
    # notification_template.setThirdLine()
    notification_template.addAction("Read More")
    zroya.show(notification_template, webbrowser.open(html_url, new=1))


# # prepare handler
# def onAction(nid, action_id):
#     if action_id == 0:
        
#     if action_id == 1:
#         zroya.hide()
#         # zroya.show(ok_template)
#     # else:
#         # zroya.show(fine_template)


# integrate notifier.py with res/data.json and res/b1.txt
# autorun notifier.py in background
# auto schedule according to time

def fetch_schedules():
    # loading data
    global loaded_data
    with open(f'{dir_path}\\..\\res\\data.json', 'r') as file:
        loaded_data = json.load(file)
        
    # serializing data
    global serialized_data
    serialized_data={}
    for i in loaded_data:
        serialized_data[i] = loaded_data[i]['time']
    serialized_data = dict(sorted(serialized_data.items(), key=lambda item: item[1]))

def choose_word(level):
    src = txts[level]
    
    with open(src,'r') as file:
        words = file.readlines()
    word = words[0].split(" ")[0].replace("!","")
    del words[0]
    with open(src, "w") as file:
        file.write(''.join(words))
    return word.replace("\n",'')

def main():
    while True:
        fetch_schedules()
        e = datetime.datetime.now()
        current_time = e.strftime("%I:%M %p")
        
        for i in serialized_data:
            if current_time == loaded_data[i]['time']:
                
                level = loaded_data[i]['level']
                word = choose_word(level)
                tup = pager.page(loaded_data[i]['lang'],word)
                
                send_notification(tup[0],level,tup[1])

                time.sleep(40)
        
        time.sleep(20)

fetch_schedules()
main()
