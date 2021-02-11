import os
import time
import datetime
import pyautogui
import VarsForZoom 

times_arr =[]
subjects_arr=[]

def GetDateNumber(): ###Working.
    now = datetime.datetime.now()
    dayName = now.strftime("%A")
    arr = VarsForZoom.days
    for i in range(len(arr)):
        day = VarsForZoom.days[i]
        if(dayName == day):
            return i

def GetDaysubjectsAndtimesByNum(num):
    time_arr =[]
    subject_arr=[]
    if(num == 1):
        time_arr = VarsForZoom.Sunday_Times
        subject_arr = VarsForZoom.Sunday_Subjects
    if(num == 2):
        time_arr = VarsForZoom.Monday_Times
        subject_arr = VarsForZoom.Monday_Subjects
    if(num == 3):
        time_arr = VarsForZoom.Tuesday_Times
        subject_arr = VarsForZoom.Tuesday_Subjects
    if(num == 4):
        time_arr = VarsForZoom.Wednesday_Times
        subject_arr = VarsForZoom.Wednesday_Subjects
    if(num == 5):
        time_arr = VarsForZoom.Thursday_Times
        subject_arr = VarsForZoom.Thursday_Subjects
    if(num == 6):
        time_arr = VarsForZoom.Friday_Times
        subject_arr = VarsForZoom.Friday_Subjects
    return time_arr,subject_arr

def GetTime():
    now = datetime.datetime.now() # Get Time
    current_time = now.strftime("%H:%M") # Set a var
    return str(current_time)
#######################################
def Join(link):
    os.popen('start Chrome.exe')
    time.sleep(1.5)
    pyautogui.write(link)
    pyautogui.press('Enter')
    print('Joined!!!!')
    return True

def GetLinkByName(name):
    subjects = VarsForZoom.subjects
    links = VarsForZoom.links
    for i in range(len(subjects)):
        sub = subjects[i]
        if(name == sub):
            link = links[i]
            return link   
        
def GetClassNameByTime(Ctime):
    for i in range(len(times_arr)):
        t = times_arr[i]
        if(Ctime == t):
            sub = subjects_arr[i]
            return sub   

HasJoined = False
while HasJoined == False:
    x = GetDateNumber()+1
    times_arr,subjects_arr = GetDaysubjectsAndtimesByNum(x)
    Ctime = GetTime()
    for time1 in times_arr:
        if(Ctime == time1):
            className = GetClassNameByTime(Ctime)
            link = GetLinkByName(className)
            print('Class Found its: '+className +', Joining by this link: '+str(link))
            HasJoined = Join(str(link))
            break
        else:
            print('No class to join right now...')
    time.sleep(60)
