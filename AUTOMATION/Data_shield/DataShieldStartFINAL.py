import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile

def Make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")

    zip_name = folder +"_"+timestamp+".zip"

    #open the zip file
    zobj = zipfile.ZipFile(zip_name,"w",zipfile.ZIP_DEFLATED)                   # zipfile.ZIP_DEFLATED this compress the file 

    for root,dir,files in os.walk(folder):
        for file in file:
            full_path = os.path.join(root,file)
            relative = os.path.join(root,files)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path , relative)
    zobj.close()
    return zip_name




def Calculate_hash(path):
    hobj = hashlib.md5
    fobj =open(path , "rb")
    while True:
        data = fobj.read(1024)

        if not data:
            break
        else:
            hobj.update(data)
    fobj.close()
    return hobj.hexdigets




def BackupFiles(Source , Destination):
    Copied_files = []
    print("Creating the backup folder for backup process")

    os.makedirs(Destination , exist_ok=True)                                                                #checks for the same name of the file and if a file already exits then it does not give nay error                                                                                            #create multiple folders 

    for root,dirs,files,in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)                                                              #relative  path acess kartoy 
            relative = os.path.relpath(src_path ,Source)                                                    #gives the relative path
            dest_path = os.path.join(Destination , relative)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            #copy the files if they are updated
            if(not (os.path.exists(dest_path) or ((Calculate_hash(src_path)) != (Calculate_hash(dest_path))))):                                                            #jar file navin asel tar copy honar nahi tar nahi 
                shutil.copy2(src_path ,dest_path)                                                               #copy from source to destination 
                Copied_files.append(relative)

           
                                                                   #copied file append to the list 

    return Copied_files

def MarvellousDatasheildStart(Source = "Data"):                                                             #entry point of the project 

    backupName = "MarvellousBackup"
    print("Backup process started successfully at ",time.ctime())
    files = BackupFiles(Source , backupName)
    Border = "-" * 50                                                                                      
    print(Border)
    zip_file = Make_zip(backupName)                                                     #will go to marvellousbakcup
    print("backup completed successfully")
    print("no of files copied",len(files))
    print("sip file gets created :" , zip_file)
    Border = "-" * 50                                                                                      
    print(Border)

def main():
    Border = "-" * 50                                                                                      
    print(Border)
    print("----------Marvellous Data Shield System----------")
    print(Border)

    if (len(sys.argv) == 2):

        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This scirpt is used to : ")
            print("1: Takes AutoBackup at given time")
            print("2: backup only new and updated files")
            print("3: Create and arhive of the backup periodically")

        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation Script as")
            print("Scriptname.py TimeInterval DireectoryName")
            print("TimeInterval is : The time in minutes for periodic sceduleing")
            print("Directory : name of Directory to create a auto logs")

        else:
            print("Unable tomproceed as ther is not suct options")
            print("Please use --h or --u for more details")

    # python Demo.py 5 Marvellous

    elif (len(sys.argv)== 3):
        #print("Inside Projects Logic")
        print("TimeInternval : ", sys.argv[1])
        print("DirectoryName :", sys.argv[2])
        # Apply the Scheduler

        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDatasheildStart, sys.argv[2])

        print("Data shield Started Successfully")
        print("Time Interval in Minutes :", sys.argv[1])
        print("Press Ctrl + C to stop the command")

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of command line arguments")
        print("Unable tomproceed as ther is not such options")
        print("Please use --h or --u for more details")
    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)
if __name__ == "__main__":

    main()