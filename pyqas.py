def Remove_Duplicates(lst) :
    lst_no_duplicates=[]
    for el in lst:
        if el not in lst_no_duplicates :
            lst_no_duplicates.append(el)
    return lst_no_duplicates
def Reverse_Lst(lst) :
    lst_reversed=[]
    for el in range(1,  len(lst)+1) :
        lst_reversed.append(lst[-el])
    return lst_reversed
def Get_Counts(list, el) :
    list_counts=[]
    for item in list:
        if item==el :
            list_counts.append(item)
    return len(list_counts)
def Order_Nums(list) :
    list_orderd=[]
    boolean_list=[]
    for num in list :
        if len(list_orderd)==1 :
            if num>=list_orderd[0] :
                list_orderd.append(num)
                list_orderd=Reverse_Lst(list_orderd)
            else :
                list_orderd.append(num)
                
        elif len(list_orderd) > 1 :
            boolean_list.clear()
            for i in range(0, len(list_orderd)) :
                if num >= list_orderd[i] :
                    boolean_list.append(True)
                else :
                    boolean_list.append(False)
            counts_False=Get_Counts(boolean_list, False)
            counts_True=Get_Counts(boolean_list, True)
            if counts_False==0 :
                list_orderd.append(num)
                for i in range(1, len(list_orderd)) :
                    list_orderd[-i]=list_orderd[-i-1]
                list_orderd[0]=num
            if counts_True==0 :
                list_orderd.append(num)
            if counts_False==len(list_orderd)-1 and counts_True==1:
                list_orderd.append(num)
                list_orderd[-1]=list_orderd[-2]
                list_orderd[-2]=num
            if counts_False!=0 and counts_True!=0 and  counts_False!=len(list_orderd)-1 and counts_True!=1:
                list_orderd.append(num)
                for i in range(1, counts_True+1) :
                    list_orderd[-i]=list_orderd[-i-1]
                list_orderd[counts_False]=num
        else :
            list_orderd.append(num)
    return list_orderd
def Max_Value(lst) :
    ordered_nums=Order_Nums(lst)
    return ordered_nums[0]
def Remove_word(text, word) :
    text_words=text.split()
    str_after="".join(f'{wrd} ' for wrd in text_words if wrd!=word)
    return str_after
def Replace_word(text, word, new_word) :
    lst= []
    text_words=text.split()
    str_after=""
    for item in text_words:
        if item==word :
            str_after="".join(new_word)
            lst.append(str_after)
        else :
            
            str_after="".join(item)
            lst.append(str_after)
    nw_str="".join(f'{i} ' for i in lst)
    return nw_str
def Paste_text() :
    import pandas as pd
    copied_data = pd.read_clipboard() 
    return(copied_data.columns[0])
    # or 
    # import clipboard
    # text = clipboard.paste()
    # print(text)
# download sound from sound cloud 
def download_sound_from_sound_cloud() :
    import time
    from pyqas import Remove_word
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.get("https://www.soundcloudme.com/")
    links_list=[]
    with open('snd_cld_lnks.txt', 'r') as line :
        line_txt=line.readlines()
        links_list=line_txt
    url=driver.find_element_by_name("url")
    form_download=driver.find_element_by_id("soundcloud_form")
    for i in range(151, len(links_list)+1) :
        url=driver.find_element_by_name("url")
        form_download=driver.find_element_by_id("soundcloud_form")
        url.clear()
        nw_lnk=Remove_word(links_list[i], '\n')
        url.send_keys(nw_lnk)
        form_download.submit()
        time.sleep(2)
        btn=driver.find_element_by_class_name('btn.single-download')
        btn.click()
        driver.get("https://www.soundcloudme.com/")
        time.sleep(5)
        print('the first link is being downloaded')
# get the links of the sounds from the sound_cloud
class Extracting_Nums_At_The_First :
    def __init__(self, string, list) :
        self.string=string
        self.list=list
    def Processing(self, string, list) :
        letters_lst=[l for l in string]
        for i in range(0, len(letters_lst)) :
            try :
                new=int(letters_lst[i])
                list.append(new)
                for s in range(1, len(letters_lst)):
                    try :
                        new1=int(letters_lst[s])
                        list.append(new1)
                    except :
                        return list
                return "end"
            except :
                pass
    def Returning(self) :
        processed_list=Extracting_Nums_At_The_First.Processing(self, self.string, self.list)
        newobj="".join(str(s) for s in processed_list)
        newobj=int(newobj)
        return newobj
def ExtractNums(string) :
    list=[]
    x=[x for x in str(string)]
    for l in x :
        try :
            new=int(l)
            list.append(str(new))
        except :
            pass
    if len(list)==0 :
        return "None"
    else:
        str1="".join(x for x in list)
        return int(str1)
def ExtractMessage(string) :
    list=[]
    x=[x for x in str(string)]
    for i in range(2, len(x)) :
        if (x[i]!="'") :
            list.append(x[i])
    new="".join(x for x in list)
    return new
def ExtractingCh(string, lst) :
    x=[x for x in string]
    for l in x :
        try :
            new=int(l)
        except:
            lst.append(l)
    NewString="".join(x for x in lst)
    return NewString

from moviepy.editor import *


def filter_command(command) :
    try:
        path = command.split("-p=")[1].split(" -f=")[0]
        files = command.split("-f=")[-1]
        # filtering the path
        lst_end = []
        lst_start = []
        txt = "mohamed\q"
        for i in range(-(len(path)-1), 1) :
            if (path[-i] != " "):
                lst_end.append(-i)
        new_path = "".join(path[x] for x in range(0, lst_end[0]+1))
        for i in range(0, len(new_path)) :
            if new_path[i] != " " :
                lst_start.append(i)
        new_path = "".join(new_path[x] for x in range(lst_start[0], len(new_path)))
        if new_path[-1] != "/" or new_path[-1] != txt[-2] :
            if '/' in new_path :
                new_path = new_path+"/"
            elif txt[-2] in new_path :
                new_path = new_path+txt[-2]
        # end of the filtering the path
        # filtering the files
        lst_files_end = []
        lst_files_start = []
        lst_files_main = []
        if "*" not in files :
            files = files.split(",")
            for file in files :
                lst_files_end = []
                for i in range(-(len(file)-1), 1) :
                    if (file[-i] != " "):
                        lst_files_end.append(-i)
                new_file = "".join(file[x] for x in range(0, lst_files_end[0]+1))
                lst_files_start = []
                for i in range(0, len(new_file)) :
                    if new_file[i] != " " :
                        lst_files_start.append(i)
                new_file = "".join(new_file[x] for x in range(lst_files_start[0], len(new_file)))
                lst_files_main.append(new_file)
                data = {
                    "path" :new_path,
                    "files" :lst_files_main,
                } 
                return data
        else :
            files = files.split(",")
            for i in range(-(len(files[0])-1), 1) :
                if (files[0][-i] != " "):
                    lst_files_end.append(-i)
            new_file = "".join(files[0][x] for x in range(0, lst_files_end[0]+1))
            for i in range(0, len(new_file)) :
                    if files[0][i] != " " :
                        lst_files_start.append(i)
            new_file = "".join(new_file[x] for x in range(lst_files_start[0], len(new_file)))
            data = {
                "path" :new_path,
                "files" :new_file,
            } 
            return data
        # end of the filtering files
    except :
        return "Please enter a valid command "



def downloadFromYoutube() :
    import time
    import youtube_dl
    with open("youtube_links.txt", "r") as file :
        links = file.readlines()
        for link in links :
            lnk = link.split()[0]
            print(lnk)
            with youtube_dl.YoutubeDL() as ydl :
                ydl.download([lnk])

    print("Downloaded")

def convertMp4ToMp3(path_of_mp4, path_to_put_mp3) :
    txt = "mohamed\q"
    if path_of_mp4[-1] != "/"  :
        if "/" in path_of_mp4 :
            path_of_mp4 = path_of_mp4+"/"
        else :
            path_of_mp4 = path_of_mp4+txt[-2]
    if path_to_put_mp3[-1] != "/"  :
        if "/" in path_to_put_mp3 :
            path_to_put_mp3 = path_to_put_mp3+"/"
        else :
            path_to_put_mp3 = path_to_put_mp3+txt[-2]
    import time
    import os
    videos = os.listdir(path_of_mp4)
    for video in videos :
        if os.path.isfile(path_of_mp4+video) :
            if ".mp4" in video :

                print(f"Coverting {video}")

                clip = VideoFileClip(path_of_mp4+video)

                audio = clip.audio
                audio.write_audiofile(path_to_put_mp3+video.split('.')[0]+'.mp3')

                clip.close()
                audio.close()
                print("Converted ..")
                time.sleep(2)
            else :
                print("The file isnot video file ")
        else :
            print("That's not file ")

def getIpAddress() :
    # finding the ip of the device

    import os

    lst_ips = []


    ip_res = os.popen("ipconfig").read()

    # first we will create a text file to put it the res

    with open("ip.txt", "w") as file :
        file.write(ip_res)
    # second we will read that file

    with open("ip.txt", "r") as file :
        lines=file.readlines()
        for line in lines:
            if "IPv4 Address. . . . . " in line :
                lst_ips.append(line.split()[-1])
        os.popen("del ip.txt")
        return lst_ips[-1]
    




def extract_dir_name(path) :
    print(len(path))
    lst = []
    txt = "mohamed\q"
    for i in range(-(len(path)-1), 1) :
        if path[-1] == '/' or path[-1] == txt[-2] :
            if path[-i] == '/' or path[-i] == txt[-2]:
                if -i != len(path)-1 :
                    lst.append(-i)
        else :
            if path[-i] == '/' or path[-i] == txt[-2] :
                lst.append(-i)
    new_str = "".join(path[i] for i in range(lst[0]+1, len(path)) if path[i] != "/" and path[i] != txt[-2])
    return new_str



def extract_the_added_dir() :
    txt = "mohamed/q"
    dirs = os.listdir(os.getcwd())
    lst =[]
    for dir in dirs :
        time =os.path.getmtime(os.getcwd()+txt[-2]+dir)
        lst.append(float(time))
    ordered_dirs = Order_Nums(lst)
    for dir in dirs :
        time =os.path.getmtime(os.getcwd()+txt[-2]+dir)
        if float(time) == ordered_dirs[0] :
            return dir




def Calc_Time_With_Seconds(time1, time2) :
    oneHour = 60 * 60
    oneMinute = 60
    day_dif = int(time2['day']-time1['day'])
    hours_dif = int(time1['hours']) - int(time2['hours'])
    minutes_dif = int(time2['minutes']) - int(time1['minutes'])
    seconds_dif = int(time2['seconds']) - int(time1['seconds'])
    print(seconds_dif)
    if abs(day_dif) == 0 :
        if hours_dif == 0 :
            return int(oneMinute * abs(minutes_dif) + seconds_dif)
        else :
            if seconds_dif == 0 :
                if minutes_dif == 0 :
                    return int(oneHour * abs(hours_dif))
                elif minutes_dif > 0 :
                    return int(oneHour * abs(hours_dif) + oneMinute * abs(minutes_dif))
                else :
                    if abs(hours_dif) == 1 :
                        return int(oneMinute * (60 - time1['minutes'] + time2['minutes']))
                    else :
                        return int(oneHour * hours_dif + oneMinute * minutes_dif)
            elif  seconds_dif > 0:
                if minutes_dif == 0 :
                    return int(oneHour * abs(hours_dif) + abs(seconds_dif))
                elif minutes_dif > 0 :
                    return int(oneHour * abs(hours_dif) + oneMinute * abs(minutes_dif) + abs(seconds_dif))
                else :
                    if abs(hours_dif) == 1 :
                        return int(oneMinute * (60 - time1['minutes'] + time2['minutes']) + abs(seconds_dif))
                    else :
                        return int(oneHour * hours_dif + oneMinute * minutes_dif + abs(seconds_dif))
            else :
                if minutes_dif == 0 :
                    return int(oneHour * abs(hours_dif) + seconds_dif)
                elif minutes_dif > 0 :
                    return int(oneHour * abs(hours_dif) + oneMinute * abs(minutes_dif) + seconds_dif)
                else :
                    if abs(hours_dif) == 1 :
                        return int(oneMinute * (60-time1['minutes'] + time2['minutes']) + seconds_dif)
                    else :
                        return int(oneHour * hours_dif + oneMinute * minutes_dif + seconds_dif)
    else :
        hours_dif = 24 - time1['hours'] + time2['hours']
        if hours_dif == 0 :
            return int(oneMinute * abs(minutes_dif) + abs(seconds_dif))
        else :
            if seconds_dif == 0 :
                if minutes_dif == 0 :
                    return int(oneHour * abs(hours_dif))
                elif minutes_dif > 0 :
                    return int(oneHour * abs(hours_dif) + oneMinute * abs(minutes_dif))
                else :
                    if abs(hours_dif) == 1 :
                        return int(oneMinute * (60-time1['minutes'] + time2['minutes']))
                    else :
                        return int(oneHour * hours_dif + oneMinute * (60-time1['minutes'] + time2['minutes']))
            elif  seconds_dif > 0:
                if minutes_dif == 0 :
                    return int(oneHour * abs(hours_dif) + abs(seconds_dif))
                elif minutes_dif > 0 :
                    return int(oneHour * abs(hours_dif) + oneMinute * abs(minutes_dif) + abs(seconds_dif))
                else :
                    if abs(hours_dif) == 1 :
                        return int(oneMinute * (60-time1['minutes'] + time2['minutes']) + abs(seconds_dif))
                    else :
                        return int(oneHour * hours_dif + oneMinute * (60-time1['minutes'] + time2['minutes']) + abs(seconds_dif))
            else :
                if minutes_dif == 0 :
                    return int(oneHour * abs(hours_dif) + 60 - time1['seconds'] + time2['seconds'])
                elif minutes_dif > 0 :
                    return int(oneHour * abs(hours_dif) + oneMinute * abs(minutes_dif) + 60 - time1['seconds'] + time2['seconds'])
                else :
                    if abs(hours_dif) == 1 :
                        return int(oneMinute * (60-time1['minutes'] + time2['minutes']) + abs(seconds_dif))
                    else :
                        return int(oneHour * hours_dif + oneMinute * (60-time1['minutes'] + time2['minutes']) + abs(seconds_dif))
