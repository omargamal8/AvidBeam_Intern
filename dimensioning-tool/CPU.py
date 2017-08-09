#!/usr/bin/python
import psutil
import time
import os
import matplotlib.pyplot as plt
import numpy as np
import pymongo
import json
from itertools import chain
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import webbrowser

#File_Name = '/home/avidbeam/CPUTEST/Slave2.txt'

#File_Name = 'sftp://192.168.1.222/home/avidbeam/leena/test.txt'
#now = time.time()
#future = now + 30

"""
This method is used to calculate CPU usage. It is called when user clicks on
generatee hardware configuration or calculate hardware estimate. It does a 
30 sec scanning and gets the average.
"""
def scanning(pids):
    summ=0
    now = time.time()
    future = now + 30
    File_Name = '/home/avidbeam/leena/test.txt'
    File_Name = './output.txt'
    Output_File = open(File_Name, 'w')
    Output_File.close()
    File_OS = os.stat(File_Name)
    Creation_Time = File_OS.st_mtime
    Delete_Time = 600000
    Time = []
    CPU_Plot = []
    sums=[]
    sumofavg=0
    CPUSum= []
    totalRam=[]
    cpusump=[]
    global actualCPUSumP
    actualCPUSumP=[]
    global actualCores
    actualCores=[]
    thrdsofallprocesses=[]
    avgcpu1=[]
    sum_cpu_percent_list=[]
    #print(psutil.pids())
    for ids in pids:
        p=psutil.Process(ids)
        #print('nameeeeeeeeeee: ',p.name())
        c=0
        CPUSum2=[]
        cpu_percent_list=[]
        now = time.time()
        future = now + 30

        while True:
            c+=1
        #for i in range(10):
            if time.time() > future:
                break 
        
            File_OS = os.stat(File_Name)
            Current_Time = File_OS.st_mtime
            if ((Current_Time-Creation_Time) > Delete_Time):
                Output_File = open(File_Name, 'w')
                File_OS = os.stat(File_Name)
                Creation_Time = File_OS.st_mtime
            else:
                Output_File = open(File_Name, 'a')
            S = ''
            Time_Stamp = time.time()
            #print Time_Stamp
            S = S + repr(Time_Stamp) + ' '
            #cpu_no kam cpu running
            #cpu percent kol cpu wakhed ad eh
            global CPU_No 
            CPU_No = psutil.cpu_count()
            global avgCPUPer
            CPU_Percent = psutil.cpu_percent(interval=0.1, percpu=True)
            cpu_percent=p.cpu_percent(interval=0.1) 
            cpu_percent_list.append(cpu_percent)   ###list of cpu%s in a process

            for i in range(CPU_No):
                S = S + repr(CPU_Percent[i]) + ' '

            global Ram_Memory
            Ram_Memory = psutil.virtual_memory()

            global ramProcess
            memoryInfo = p.memory_info()
            ramProcess= memoryInfo.rss

            global Ram_available
            Ram_available= Ram_Memory.available

            Swap_Memory = psutil.swap_memory()

            global Ram_Percent
            Ram_Percent = Ram_Memory.percent
            Swap_Percent = Swap_Memory.percent

            S = S + repr(Ram_Percent) + ' '
            S = S + repr(Swap_Percent) + ' '

            S = S + ' \n'
            Output_File.write(S)
            Output_File.close()
            SUM = 0

            for l in range(CPU_No):
                SUM += CPU_Percent[l]

            Time.append(Current_Time-Creation_Time)
            CPU_Plot.append(float(SUM)/CPU_No) #################### list of avg cpu1+2+3../40, ...
            CPUSum.append(SUM) ######################## list of sum of cpu usags f 40 nat cpu1+cpu2..., cpu1+cpu2..

        sum_cpu_percent=0
        for i in cpu_percent_list:
            sum_cpu_percent+=i

        sum_cpu_percent_list.append(sum_cpu_percent/len(cpu_percent_list))  ## list of avg cpu%s for all processes
         

        global threads
        thrdsofallprocesses.append(p.num_threads())
      
        totalRam.append(ramProcess)
        #print('list ram length: ',len(totalRam))
    
    sumCores=0
    for i in sum_cpu_percent_list:
        sumCores+=i

    global finalCores
    finalCores=sumCores/100

    global sumThreads
    sumThreads=0
    for thrd in thrdsofallprocesses:
        sumThreads += thrd

    global sumRam
    sumRam=0

    for ram in totalRam:
        sumRam+=ram 
            

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

"""
Writes hardware estimate calculations in a pdf and opens it automatically.
"""       
def hardwareEstimate(cores, RamM,pids):
    print('dkhal method')
    from reportlab.pdfgen import canvas
    import subprocess
    for ids in pids:
        p = psutil.Process(ids)
        p.terminate()  
    ramper= Ram_Percent/100
    ram = Ram_available * ramper
    ramF= bytes2human(ram)

    #ramProcess2 = bytes2human(ramProcess)
    sumRam2= bytes2human(sumRam)

    #finalAvgRam2 = bytes2human(finalAvgRam)
#    total= float(avgcpuf) * logCores
    doc = SimpleDocTemplate("hwEstimate.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []
     
    data = [
    ["","Module parameters","Actual calculations"],
    ["Cores: ","%s" %cores, "%s" %finalCores],
    ["Ram:"," %s" %RamM, "%s" %sumRam2],
    ]
     
    #TODO: Get this line right instead of just copying it from the docs
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                           ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                           ('VALIGN',(0,0),(0,-1),'TOP'),
                           ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                           ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                           ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                           ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])
     
    #Configure style and word wrap
    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    data2 = [[Paragraph(cell, s) for cell in row] for row in data]
    t=Table(data2)
    t.setStyle(style)
     
    #Send the data and build the file
    elements.append(t)
    doc.build(elements)
    original_path = 'r/home/avidbeam/leena/hwEstimate.pdf'
    modified_path = './hwEstimate.pdf'
    webbrowser.open_new(modified_path)



"""
Writes hardware configuration calculations in a pdf and opens it automatically.
"""
def hwConfiguration(cores,ram_req,threadsM,pids):
    c=2
    print('dkhal method')
    for ids in pids:
        p = psutil.Process(ids)
        p.terminate() 
    from reportlab.pdfgen import canvas
    import subprocess
    print('cpuno')
    print(CPU_No)
    print('ram av')
    print(Ram_available)
    #cpuCores = CPU_No/cores
#    total= avgcpuf * CPU_No

    ramRam=Ram_available*Ram_Percent/100
    #finalAvgRam2 = bytes2human(finalAvgRam)
    sumRam2= bytes2human(sumRam)
    doc = SimpleDocTemplate("hwConfiguration.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []
     
    data = [
    ["","Module parameters", "Actual parameters"],
    ["Cores:", "%s" %cores, "%s" %finalCores],
    ["Ram:"," %s" %ram_req, "%s" %sumRam2],
    ["Threads: ","%s" %threadsM, "%s" %sumThreads],
    ]
     
    #TODO: Get this line right instead of just copying it from the docs
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                           ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                           ('VALIGN',(0,0),(0,-1),'TOP'),
                           ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                           ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                           ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                           ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])
     
    #Configure style and word wrap
    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    data2 = [[Paragraph(cell, s) for cell in row] for row in data]
    t=Table(data2)
    t.setStyle(style)
     
    #Send the data and build the file
    elements.append(t)
    doc.build(elements)
    old_path = r'/home/avidbeam/leena/hwConfiguration.pdf'
    new_path = r'./hwConfiguration.pdf'
    webbrowser.open_new(new_path)

        


from pymongo import MongoClient
client = MongoClient()
db = client['Algo_conf']
modules = db.modules

"""
Inserts a computing module added by user to a database.
""" 
def add_computing_module(algo_name, ram_req, threads, cores, pcores_count, max_inp_res, max_fr, fps, algo_ver, plugin_path, plugin_context):
    #print('geh hena')
    module_data = {
    'algo_name': algo_name,
    'ram_req':ram_req,
    'threads': threads,
    'cores': cores,
    'pcores_count': pcores_count,
    'max_inp_res': max_inp_res,
    'max_fr':max_fr,
    'fps':fps,
    'algo_ver':algo_ver,
    'plugin_path': plugin_path,
    'plugin_context':plugin_context
    }
    modules.insert(module_data)
"""
Removes a computing module from database using the algorthim name.
"""
def remove_computing_module(algo_name):
    modules.remove({"algo_name": algo_name})

"""
Edits a certain computing module's parameters using algorithm name (updates database).
"""
def edit_computing_module(algo_name, ram_req, threads, cores, pcores_count, max_inp_res, max_fr, fps, algo_ver, plugin_path,plugin_context):
    modules.update({
    "algo_name": algo_name
    },{
    '$set': {
        'ram_req':ram_req,
        'threads': threads,
        'cores': cores,
        'pcores_count': pcores_count,
        'max_inp_res': max_inp_res,
        'max_fr':max_fr,
        'fps':fps,
        'algo_ver':algo_ver,
        'plugin_path': plugin_path,
        'plugin_context':plugin_context
        }
    }, upsert=False, multi=False)


deployments = db.deployments

def add_plugin_context(compMod,plugin_context):
    algo_name= compMod['algo_name']
    modules.update({
    "algo_name": algo_name
    },{
    '$set': {
        'plugin_context':plugin_context
        }
    }, upsert=False, multi=False)  
    for a in plugin_context:  
        deployments.update({
            'depMod.algo_name': algo_name
            },{
            '$push':{
            'depMod.plugin_context':a
            }

            })

"""
Inserts a depoloyment added by user to a database.
"""
def add_deployment(dep_name, st_no, media, depMod):  
    deployments_data={
    'dep_name': dep_name,
    'st_no': st_no,
    'depMod': depMod,
    'media': [media]
    }  
    deployments.insert(deployments_data)

"""
Removes a certain deployment from database using deployment name.
"""
def remove_deployment(dep_name):
    deployments.remove({'dep_name':dep_name})

#def getComputingModules():
#    m=modules.find()
#    for c in m:
        

#add_computing_module('hoho',3,4,3,5,1,5,4,3)
#add_computing_module('lolo',3,4,36,57,10,6,7,8)
#remove_computing_module('lolo') 
#edit_computing_module('mayar',000,00,00,0,0,0,0,0)
#add_deployment(1,3,4)
#modules.remove()
#deployments.remove()

"""
Updates a media source configuration parameters using media name (user cannot change media source name).
-updates the media source database with the new parameters
-updates the deployment scenarios containing that media source with the new parameters 
""" 
mediaSS= db.mediaSS  
def media_source_config(depScen,frame_rate, resol, x, y, width, height, media_path, media_name):
    mediaSS.update({
        'media_name' : media_name
            },{
        '$set': {
        'frame_rate': frame_rate,
        'resol':resol,
        'x':x,
        'y':y,
        'width':width,
        'height':height,
        'media_path' : media_path    
        }
    })
    print('media name', media_name)
    #print('media', media_path)
    dep_name= depScen['dep_name']
    media = depScen['media']
    deployments.update({
        'media.media_name':media_name
        },{
        '$set':{
        'media.frame_rate':frame_rate,
        'media.resol':resol,
        'media.x':x,
        'media.y':y,
        'media.width': width,
        'media.height': height,
        'media.media_path': media_path 
        }
        })

    """
    for k in media:
        if k['media_name'] == media_name:
            print('heeeeeeeeeeeeellloooooooooooooooooooooooooooooo')
            deployments.update({
              'dep_name' : dep_name
                 },{
              '$pull': {
              'media':{
              'media_name':media_name    
              }
              }
           })
            deployments.update({
              'dep_name' : dep_name
                 },{
              '$push': {
              'media':{
              'frame_rate':frame_rate,
              'resol':resol,
              'x':x,
              'y':y,
              'width': width,
              'height': height,
              'media_path': media_path,
              'media_name':media_name,
              'media_context':[]  
              }
              }
           })
    """        
    
"""
Inserts a media source to media sources database.
"""
def add_media_source(frame_rate,resol,x, y, width, height,media_path, media_name,media_context):
    media_source_data={
        'frame_rate':frame_rate,
        'resol':resol,
        'x':x,
        'y':y,
        'width':width,
        'height':height,
        'media_path':media_path,
        'media_name':media_name,
        'media_context': media_context
        
    } 
    mediaSS.insert(media_source_data)

"""
Updates the media source in the database to insert the plugin context
"""
def add_media_context(media,mediaContexts):
    media_name= media['media_name']
    mediaSS.update({
    "media_name": media_name
    },{
    '$set': {
        'media_context':mediaContexts
        }
    }, upsert=False, multi=False)    


"""
Removes a media source from media sources and deployments databases.
"""
def remove_media_source(depScen,frame_rate, resol, x, y, width, height,media_path, media_name,media_context):
    mediaSS.remove({'frame_rate':frame_rate,'resol':resol,'x':x,'y':y,'width':width,'height':height,'media_path':media_path,'media_name':media_name,'media_context':media_context})
    dep_name= depScen['dep_name']
    
    deployments.update({
    'media.media_name':media_name
    },{
    '$pull':{
    'media':{
    'frame_rate':frame_rate,
    'resol':resol,
    'x':x,
    'y':y,
    'width': width,
    'height': height,
    'media_path': media_path,
    'media_name':media_name,
    'media_context':media_context    
    }
    }
    })
    dep_name= depScen['dep_name'] 



#d= deployments.find()
#for dd in d:
#    print(dd)

#add_media_source('hoda',5,3,2,1,3,3)
#add_media_source('hoda',50,30,20,10,30,30)
#remove_media_source('hoda')
#f = mediaSS.find({})
#for k in f:
#   print k
#mediaSrcList('hoda')
#deployments.remove()
#mediaSS.remove()
#modules.remove()
