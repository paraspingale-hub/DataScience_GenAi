import time
import datetime
import schedule

def fun():    
    print("inside funn at" , datetime.datetime.now())
def gun(): 
    print("inside gun at" , datetime.datetime.now())
def main ():
    
    print("inside main at" , datetime.datetime.now())
    print("::marvellous_automation_script::")
    
    schedule.every(20).seconds.do(fun)
    schedule.every(1).minute.do(gun)

    while (True):
        schedule.run_pending()                                       #search for pending work and do it 
        time.sleep(1)                                               #sleep for 1 sec 
main()