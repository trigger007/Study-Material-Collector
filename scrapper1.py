import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
print("1.software engineer")
print("2.operating systems")
c=int(input("enter your option:"))

software=["-classical-waterfall-model/","-iterative-waterfall-model/","-information-system-life-cycle/","-software-maintenance/","-requirements-engineering-process/",
          "-classification-of-software-requirements/","-seven-principles-of-software-testing/","-black-box-testing/","-black-box-testing/","-white-box-testing/",
          "-integration-testing/","-user-interface-design/","-coupling-and-cohesion/","-spiral-model/","-agile-development-models/","-sdlc-v-model/",
          "-incremental-process-model/","-extreme-programming-xp/","-rapid-application-development-model-rad/","-iterative-waterfall-model/","-classical-waterfall-model/"
          ,"-classical-waterfall-model/","all the notes"]
software1= ["classical waterfall model "," iterative waterfall model "," information system life cycle/"," software maintenance "," requirements engineering process",
          " classification of software requirements "," seven principles of software testing "," black box testing "," black box testing","white box testing",
          " integration testing "," user interface design "," coupling and cohesion "," spiral model "," agile development models"," sdlc v model ",
          " incremental process model "," extreme programming xp "," rapid application development model rad"," iterative waterfall model ","classical waterfall model"
          ," classical waterfall model", "all the notes"]

os=["introduction-of-operating-system-set-1","types-of-operating-systems/","functions-of-operating-system/",
    "difference-between-multitasking-multithreading-and-multiprocessing/","process-table-and-process-control-block-pcb/",
    "cpu-scheduling-in-operating-systems/","preemptive-and-non-preemptive-scheduling/","program-for-fcfs-cpu-scheduling-set-1/",
    "program-for-shortest-job-first-or-sjf-cpu-scheduling-set-1-non-preemptive/","program-shortest-job-first-scheduling-set-2srtf-make-changesdoneplease-review/",
    "program-shortest-job-first-scheduling-set-2srtf-make-changesdoneplease-review/","round-robin-scheduling-with-different-arrival-times/","program-for-priority-cpu-scheduling-set-1/",
    "multilevel-queue-mlq-cpu-scheduling/","multiple-processor-scheduling-in-operating-system/","introduction-of-process-synchronization/",
    "g-fact-70/","inter-process-communication-ipc/","petersons-algorithm-in-process-synchronization/","dekkers-algorithm-in-process-synchronization/",
    "bakery-algorithm-in-process-synchronization/","producer-consumer-problem-using-semaphores-set-1/","dining-philosopher-problem-using-semaphores/",
    "readers-writers-problem-set-1-introduction-and-readers-preference-solution/","sleeping-barber-problem-in-process-synchronization/","sleeping-barber-problem-in-process-synchronization/",
    "methods-in-interprocess-communication/","all the notes"]

       

          

def file(txt,k):
    nfile = open(k+'.txt','w') 
    nfile.write(txt)
    nfile.close() 

def scrapper(url,k):
    src=requests.get(url,headers)
    source=src.text
    soup=BeautifulSoup(source,"html.parser")
    txt=''
    for data in soup('div',{'class':'entry-content'}):
        t=data.text+"\n"
        txt=txt+t
    for data1 in soup('p'):
        t1=data1.text+"\n"
        txt=txt+t1
        file(txt,k)

if c==1:
    for i in range(len(software1)):
        print(i,".",software1[i])
    d=int(input("enter the topic you want notes for:"))
    url="https://www.geeksforgeeks.org/software-engineering"
    k=software[d]
    url=url+k
    scrapper(url,k)
elif c==2:
    for i in range(len(os)):
        print(i,".",os[i])
    d=int(input("enter the topic you want notes for:"))
    url="https://www.geeksforgeeks.org/"
    k=os[d]
    url=url+k
    scrapper(url,k) 


