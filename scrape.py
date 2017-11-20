import time
import urllib3
from bs4 import BeautifulSoup as soup
import requests
from datetime import datetime
while True:
    time.sleep(3599)
    d = {"username":"IMT2017522","password":"rAth2014#",'next':'/'}
    url = 'https://lms.iiitb.ac.in/moodle/login/index.php'
    urllib3.disable_warnings()
    with requests.session() as url1:
        url1.get(url,verify=False)
        url1.post(url,data=d)
        a = url1.get('https://lms.iiitb.ac.in/moodle/my')
        html = soup(a.text,'html.parser')
        data1 = []
        g = html.findAll('div',{'class':'date'})
        for i in g:
            data1.append([i.a.string,i.get_text()])
        file1 = open("/Users/rathinbhargava/IIITB/Update.txt",'a+')
        file2 = open("/Users/rathinbhargava/IIITB/Updatechecker.txt","r+")
        check1 = []
        check1 = file2.readlines()
        date = datetime.now().time()
        s1,s2,s3 = str(date.hour),str(date.minute),str(date.second)
        if len(s1)==1: s1 = "0"+s1
        if len(s2)==1: s2 = "0"+s2
        if len(s3)==1: s3 = "0"+s3
        #file1.write(str(s1)+":"+str(s2)+":"+str(s3)+"\n")
        file2.close()
        file2 = open("/Users/rathinbhargava/IIITB/Updatechecker.txt","w+")
        #file2.write(str(s1)+":"+str(s2)+"\n")
        data2 = html.findAll('div',{'class':'event'})
        for i in range(len(data2)):
            file2.write(data1[i][0]+" "+data1[i][1]+" "+data2[i].a.string+" "+data2[i].div.a.string+"\n")
        check2 = []
        #print g.read()
        file2.close()
        file2 = open("/Users/rathinbhargava/IIITB/Updatechecker.txt","r+")
        check2 = file2.readlines()
        print check1,check2
        if check1!=check2:
            file1.write(str(s1)+":"+str(s2)+":"+str(s3)+"\n")
            for i in range(len(data2)):
                file1.write(data1[i][0]+" "+data1[i][1]+" "+data2[i].a.string+" "+data2[i].div.a.string+"\n") 
        else:
            file1.write("NO UPDATE\n")

