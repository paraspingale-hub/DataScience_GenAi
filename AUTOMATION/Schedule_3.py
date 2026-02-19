import time
import datetime
import schedule
def fun():
    print("inside sun at" , datetime.datetime.now())
def main ():
    print("inside main at" , datetime.datetime.now())
    print("::marvellous_automation_script::")
    schedule.every(20).seconds.do(fun)
    while (True):
        schdule.run_pending()                                       #search for pending work and do it 
        time.sleep(1)                                               #sleep for 1 sec 
main()