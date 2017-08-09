import psutil
import os
import sys
#import matplotlib.pyplot as plt
#import numpy as np
#1.TimeStamp 2.CPU1 3.CPU2 4.CPU3 5.CPU4 6.RAM 7.SWAP 8.Sent 9.Rec
Option = int(sys.argv[1]) #1:ALL 2:Last
print Option
NoOfSlaves = 1
NoOfCores = psutil.cpu_count()
#TxtFileName = "Slave"
TxtFileName = "test"
#SlavePath = "/home/avidbeam/Desktop/" + TxtFileName
#MasterPath = "/home/avidbeam/CPUTEST"
MasterPath = "/home/avidbeam/leena/"
FileType = ".txt"
CPU = []
RAM = []
SWAP = []
Sent = []
Rec = []
CPU_Plot = []
Time = []
#for i in range(NoOfSlaves):
#    Command = "sshpass -p avidbeam scp avidbeam@avidbeamPC" + repr(i+1) + ":" + SlavePath + repr(2) + FileType + " " + MasterPath
    #print Command
#    os.system(Command)
if (Option==1):
    for i in range(NoOfSlaves):
        FileName = MasterPath + "/" + TxtFileName + repr(2) + FileType
        with open(FileName) as FF:
            FileContent = FF.read().splitlines()
        FileContentSplited = []
        for j in range(len(FileContent)):
            Words = FileContent[j].split()
            FileContentSplited.append(Words)
        CPU_PER = 0
        RAM_PER = 0
        SWAP_PER = 0
        Sent_PER = 0
        Rec_PER = 0
        for j in range(len(FileContentSplited)):
            SUM = 0
            for l in range(NoOfCores):
                SUM += float(FileContentSplited[j][l+1])#/100
            CPU_PER += float(SUM)/NoOfCores
            RAM_PER += float(FileContentSplited[j][NoOfCores+1])
            SWAP_PER += float(FileContentSplited[j][NoOfCores+2])
            #Sent_PER += float(FileContentSplited[j][NoOfCores+3])
            #Rec_PER += float(FileContentSplited[j][NoOfCores+4])
#    	    CPU_Plot.append(float(SUM)/NoOfCores)
#	    Time.append(FileContentSplited[j][0])
        CPU.append(float(CPU_PER)/len(FileContentSplited))
        RAM.append(float(RAM_PER)/len(FileContentSplited))
        SWAP.append(float(SWAP_PER)/len(FileContentSplited))
        #Sent.append(float(Sent_PER)/len(FileContentSplited))
        #Rec.append(float(Rec_PER)/len(FileContentSplited))
#	plt.plot(np.array(Time), np.array(CPU_Plot))
#	plt.ylabel('Total CPU %')
#	plt.xlabel('Time')
#	plt.show()
elif (Option==2):
    for i in range(NoOfSlaves):
        FileName = MasterPath + "/" + TxtFileName + repr(2) + FileType
        with open(FileName) as FF:
            FileContent = FF.read().splitlines()
        FileContentSplited = []
        Words = FileContent[len(FileContent)-1].split()
        FileContentSplited.append(Words)
        SUM = 0
        for l in range(NoOfCores):
            SUM += float(FileContentSplited[0][l+1])#/100
        CPU.append(SUM/NoOfCores)
        RAM.append(float(FileContentSplited[0][NoOfCores+1]))
        SWAP.append(float(FileContentSplited[0][NoOfCores+2]))
        #Sent.append(float(FileContentSplited[0][NoOfCores+3]))
        #Rec.append(float(FileContentSplited[0][NoOfCores+4]))
print CPU
print RAM
print SWAP
#print Sent
#print Rec
