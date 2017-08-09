from Tkinter import *
from CPU import *
from multiprocessing import Process
import subprocess
from itertools import chain
import tkFileDialog
import cv2


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def callback(e):
   path = tkFileDialog.askopenfilename()
   e.delete(0, END)  # Remove current text in entry
   e.insert(0, path)  # Insert the 'path'
   # print path

def browsefunc(e):
   filename =  tkFileDialog.askopenfilename()
   e.config(text=filename)

#/////////////////////////////////////////////////Computing Modules

"""
Takes computing Module parameters from user.
"""
def addCompWind():
  #global e
  filewin = Toplevel(root)
  filewin.attributes('-zoomed',True)
  filewin.wm_title("Add computing module")
  filewin.configure(background=mycolor)
  Label(filewin, text="Algorithm name:",bg=mycolor ,fg='white').grid(row=0)
  Label(filewin, text="Ram requierments:",bg=mycolor ,fg='white').grid(row=1)
  Label(filewin, text="Threads:",bg=mycolor ,fg='white').grid(row=2)
  Label(filewin, text="Cores:",bg=mycolor ,fg='white').grid(row=3)
  Label(filewin, text="Physical cores count:",bg=mycolor ,fg='white').grid(row=4)
  Label(filewin, text="Max input resolution:",bg=mycolor ,fg='white').grid(row=5)
  Label(filewin, text="Max frequency:",bg=mycolor ,fg='white').grid(row=6)
  Label(filewin, text="Algorithm processing FPS:",bg=mycolor ,fg='white').grid(row=7)
  Label(filewin, text="Algorithm version:",bg=mycolor ,fg='white').grid(row=8)
  #Label(filewin, text="Plugin path").grid(row=9)
  var = StringVar()
  e = Entry(filewin, textvariable=var).grid(row=9,column=1)
  b = Button(filewin, text="Browse",bg=mycolor,fg='white',
    command=lambda:var.set(tkFileDialog.askopenfilename())).grid(row=9,column=3)
  Label(filewin, text="Plugin Path:",bg=mycolor ,fg='white').grid(row=9)


  e1 = Entry(filewin)
  e2 = Entry(filewin)
  e3 = Entry(filewin)
  e4 = Entry(filewin)
  e5 = Entry(filewin)
  e6 = Entry(filewin)
  e7 = Entry(filewin)
  e8 = Entry(filewin)
  e9 = Entry(filewin)
  #e10 = Entry(filewin)


  e1.grid(row=0, column=1)
  e2.grid(row=1, column=1)
  e3.grid(row=2, column=1)
  e4.grid(row=3, column=1)
  e5.grid(row=4, column=1)
  e6.grid(row=5, column=1)
  e7.grid(row=6, column=1)
  e8.grid(row=7, column=1)
  e9.grid(row=8, column=1)

   # print(var.get())

  plgnContt=[]
  save = Button(filewin, text ="Add",bg=mycolor,fg='white',command= lambda: addCompEntries(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),var.get(),plgnContt ,filewin))
  save.grid(row=20, columnspan=20)

"""
When user click save button on adding computing module parameters this method is called to call
add_computing_module() method in CPU.py to add the computing module to database.
"""
def addCompEntries(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,plgnCont,filewin):
   # print(e10)
   filewin.withdraw()
   algo_name= e1
   ram_req= e2
   threads=e3
   cores=e4
   pcores_count=e5
   max_inp_res=e6
   max_fr=e7
   fps=e8
   algo_ver=e9
   plugin_path=e10
   add_computing_module(algo_name, ram_req, threads, cores, pcores_count, max_inp_res, max_fr, fps, algo_ver, plugin_path,plgnCont)
   modulesList()

"""
Shows a list of available computing modules.
"""
def modulesList():
  filewin = Toplevel(root)
  filewin.attributes('-zoomed',True)
  filewin.configure(background=mycolor)
  filewin.wm_title("Computing modules")
  Label(filewin, text="Computing Modules",font=("Times", 20, "bold"),bg=mycolor ,fg='white').grid(row=0, column=7)
  m=modules.find()
  listbox = Listbox(filewin, selectmode=SINGLE,bg=mycolor ,fg='white',selectbackground="#f0f0ed")
  for option in m:
    listbox.insert(0, option['algo_name'])
  listbox.grid()
  b = Button(filewin, command=lambda: callbackEdit(listbox,filewin), text="Edit",bg=mycolor ,fg='white')
  b.grid()
  b2 = Button(filewin, command=lambda: callbackRemove(listbox,filewin), text="Remove",bg=mycolor ,fg='white')
  b2.grid()
  b3 = Button(filewin, command=lambda: callbackShowConfig(listbox), text="Show Configuration",bg=mycolor ,fg='white')
  b3.grid()
  b4 = Button(filewin, command=lambda: callbackAddPluginContext(listbox), text="Add Plugin Context",bg=mycolor ,fg='white')
  b4.grid()

def callbackEdit(listbox,filewin):
  print (listbox.selection_get())
  m = modules.find()
  for module in m:
    if module['algo_name'] == listbox.selection_get():
    	editCompMod(module,filewin)

def callbackRemove(listbox,filewin):
  print (listbox.selection_get())
  m = modules.find()
  for module in m:
    if module['algo_name'] == listbox.selection_get():
    	confRemoveCompMod(module['algo_name'],filewin)

def callbackShowConfig(listbox):
  print (listbox.selection_get())
  m = modules.find()
  for module in m:
    if module['algo_name'] == listbox.selection_get():
    	showCompModConfig(module)

def callbackAddPluginContext(listbox):
  m = modules.find()
  for module in m:
    if module['algo_name'] == listbox.selection_get():
      addPluginContext(module)

"""
Shows computing module configuration
"""
def showCompModConfig(compMod):
	filewin = Toplevel(root)
	filewin.attributes('-zoomed',True)
	filewin.configure(background=mycolor)
	filewin.wm_title("Computing Module Configuration")
	Label(filewin, text="Algorithm: " + compMod['algo_name'],font=("Times", 15, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=False)
	Label(filewin, text="Ram requierments: " + compMod['ram_req'],font=("Times", 13, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=False)
	Label(filewin,text= "Threads: "+compMod['threads'],font=("Times", 13, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=False)
	Label(filewin, text= 'Cores: '+ compMod['cores'],font=("Times", 13, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=False)
	Label(filewin, text=  'Physical cores count: '+compMod['pcores_count'],font=("Times", 13, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=False)
	Label(filewin, text='Maximum input resolution: '+ compMod['max_inp_res'],font=("Times", 13, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=False)
	Label(filewin,text='Maximum frequency: '+compMod['max_fr'],font=("Times", 13, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=False)
	Label(filewin, text='Algorithm version: '+ compMod['algo_ver'],font=("Times", 13, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=False)
	Label(filewin, text='Plugin path: '+ compMod['plugin_path'],font=("Times", 13, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=False)

"""
Adds plugin context. Can only add one plugin context at a time; dont click on add input more than once
otherwise only the last entry will be considered.
"""
def addPluginContext(compMod):
  filewin = Toplevel(root)
  filewin.attributes('-zoomed',True)
  filewin.configure(background=mycolor)
  filewin.wm_title("Add Plugin Context")
  #global plgnCont
  plgnCont = []
  addboxButton = Button(filewin, text='Add Input',bg=mycolor ,fg="white", command=lambda:addBox(compMod,plgnCont,filewin))
  addboxButton.grid()

  #save = Button(filewin, text ="Save",bg=mycolor ,fg='white',command= lambda: addPlgnCont(compMod,filewin))
  #save.grid(row=20, columnspan=20)

"""
Adds entry fields for user input
"""
def addBox(compMod,plgnCont,filewin):
  print ("ADD")
  frame = Frame(filewin)
  frame.grid()
  Label(frame, text='Attribute').grid(row=0, column=0)
  ent1 = Entry(frame)
  ent1.grid(row=1, column=0)
  Label(frame, text='Value').grid(row=0, column=1)
  ent2 = Entry(frame)
  ent2.grid(row=1, column=1)
  Button(frame, text='Save', bg=mycolor, fg='white',command=lambda:addPlgnCont(compMod,ent1.get(),ent2.get(),plgnCont,filewin)).grid(row=1,column=2)

def savebutton(a,v,plgnCont):
  plgnCont.append((a,v))

"""
Updates computing module database to insert the plugin context
"""
def addPlgnCont(compMod,a,v,plgnCont,filewin):
  filewin.withdraw()
  print('llllllllllllllll', plgnCont)
  for a,b in plgnCont:
    print('a',a)
    print('b',b)
  plgnCont.append( (a ,v) )
  add_plugin_context(compMod,plgnCont)

"""
When user decides to edit computing module, this method is called to take new parameters from user.
"""
def editCompMod(compMod,filewin):
  filewin.withdraw()
  filewin=Toplevel(root)
  filewin.configure(background=mycolor)
  filewin.attributes('-zoomed',True)
  filewin.wm_title(compMod['algo_name'])
  Label(filewin, text="Ram requierments:",bg=mycolor ,fg='white').grid(row=0)
  Label(filewin, text="Threads:",bg=mycolor ,fg='white').grid(row=1)
  Label(filewin, text="Cores:",bg=mycolor ,fg='white').grid(row=2)
  Label(filewin, text="Physical cores count:",bg=mycolor ,fg='white').grid(row=3)
  Label(filewin, text="Max input resolution:",bg=mycolor ,fg='white').grid(row=4)
  Label(filewin, text="Max frequency:",bg=mycolor ,fg='white').grid(row=5)
  Label(filewin, text="Algorithm processing FPS:",bg=mycolor ,fg='white').grid(row=6)
  Label(filewin, text="Algorithm version:",bg=mycolor ,fg='white').grid(row=7)
  var = StringVar()
  e = Entry(filewin, textvariable=var).grid(row=9,column=1)
  b = Button(filewin, text="Browse",bg=mycolor,fg='white',
    command=lambda:var.set(tkFileDialog.askopenfilename())).grid(row=9,column=3)
  Label(filewin, text="Plugin Path:",bg=mycolor ,fg='white').grid(row=9)

  e1 = Entry(filewin)
  e2 = Entry(filewin)
  e3 = Entry(filewin)
  e4 = Entry(filewin)
  e5 = Entry(filewin)
  e6 = Entry(filewin)
  e7 = Entry(filewin)
  e8 = Entry(filewin)

  e1.grid(row=0, column=1)
  e2.grid(row=1, column=1)
  e3.grid(row=2, column=1)
  e4.grid(row=3, column=1)
  e5.grid(row=4, column=1)
  e6.grid(row=5, column=1)
  e7.grid(row=6, column=1)
  e8.grid(row=7, column=1)

  compcont=[]
  save = Button(filewin, text ="Save",bg=mycolor ,fg='white',command= lambda: editTwo(compMod['algo_name'],e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),var.get(),compcont,filewin))
  save.grid(row=20, columnspan=20)

"""
When user edits a computing module, this method calls the edit_computing_module() method in CPU.py to
update database.
"""
def editTwo(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,compcont,filewin):
   filewin.withdraw()
   print(e10)
   # print(e1, e2 , e3 ,e4 , e5 ,e6 + "------------------")
   edit_computing_module(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,compcont)
   modulesList()

"""
When user decides to remove a computing module this method is called to show a confirmation message.
"""
def confRemoveCompMod(algo_name,filewin):
   filewin.withdraw()
   filewin = Toplevel(root)
   filewin.configure(background=mycolor)
   filewin.attributes('-zoomed',True)
   filewin.wm_title("Confirm remove")
   Label(filewin, text="Are you sure you want to remove the selected module?",font=("Times", 20, "bold"),bg=mycolor ,fg='white').grid(row=0)
   Button(filewin,text="yes",bg=mycolor ,fg='white', command=lambda: removeCompMod(algo_name,filewin)).grid(row=1)
   Button(filewin,text='No',bg=mycolor ,fg='white', command=lambda: reshowModulesList(filewin)).grid(row=1,column=1)

"""
If user decides not to delete computing module this method is called to show the list of available
computing modules.
"""
def reshowModulesList(filewin):
	filewin.withdraw()
	modulesList()

"""
When user confirms the deletion of a module this method calls remove_computing_module() method in CPU.py
to remove computing module from database.
"""
def removeCompMod(algo_name,filewin):
	filewin.withdraw()
	remove_computing_module(algo_name)
	modulesList()


#//////////////////////////////////////////////////// Deployments
"""
When user decides to add a deployment scenario this method is called to show a list of available
computing modules to select from.
"""
def addDeploy():
   selectModulesList()

"""
Shows available computing modules to select from.
"""
def selectModulesList():
   # print('eh ya  hmar')
   filewin=Toplevel(root)
   filewin.configure(background=mycolor)
   filewin.attributes('-zoomed',True)
   filewin.wm_title('Select modules')
   Label(filewin, text="Please select computing module",font=("Times", 20, "bold"),bg=mycolor ,fg='white').grid()
   m=modules.find()
   listbox = Listbox(filewin, selectmode=SINGLE,bg=mycolor ,fg='white',selectbackground="#f0f0ed")
   for option in m:
   	listbox.insert(0, option['algo_name'])
   listbox.grid()
   b = Button(filewin,command= lambda: callbackselectAddMediaSource(listbox,filewin) ,text="Select",bg=mycolor ,fg='white')
   b.grid()
   Button(filewin,command=lambda:Home(filewin),text='Cancel',bg=mycolor ,fg='white').grid()


def callbackselectAddMediaSource(listbox,filewin):
	filewin.withdraw()
	c = modules.find()
	for k in c:
		if k['algo_name'] == listbox.selection_get():
			selectAddMediaSource(k)

"""
Shows a list of available media sources to select from or add a new media source option.
it is called when user creates a new deployment
"""
def selectAddMediaSource(depMod):

   filewin=Toplevel(root)
   filewin.configure(background=mycolor)
   filewin.attributes('-zoomed',True)
   filewin.wm_title('Select/Add media source')
   Label(filewin, text="Media sources",font=("Times", 20, "bold"),bg=mycolor ,fg='white').grid()
   m=mediaSS.find()
   listbox = Listbox(filewin, selectmode=SINGLE,bg=mycolor ,fg='white',selectbackground="#f0f0ed")
   for option in m:
   	listbox.insert(0, option['media_name'])
   listbox.grid()
   b = Button(filewin, command=lambda: callbackaddDeploy2(listbox,depMod,filewin), text="Select",bg=mycolor ,fg='white')
   b.grid()
   Button(filewin,command=lambda:addMediaSource(depMod,filewin),text='Add',bg=mycolor ,fg='white').grid()

def callbackaddDeploy2(listbox,depMod,filewin):
    print listbox.selection_get()
    m = mediaSS.find()
    for media in m:
    	if media['media_name'] == listbox.selection_get():
    		addDeploy2(media,depMod,filewin)


def selectMediaOption(depMod,filewin):
	filewin.withdraw()
	m=mediaSS.find()

	question = "Select Media Source"
	title = "Media Source Names"
	listOfOptions=[]

	i=0
	for c in m:
		listOfOptions.insert(i,c['media_name'])
		i=i+1

	choice = eg.choicebox(question , title, listOfOptions)

	k = mediaSS.find()
	for t in k:
		if choice == t['media_name']:
			addDeploy2(t,depMod)


"""
Shows a list of available media sources to select from and gives the option to create a new media source
It is called when a user Adds a media source to an existing deployment scenario
"""
def selectAddMediaSource2(depScen,filewin):
   filewin.withdraw()
   filewin=Toplevel(root)
   filewin.configure(background=mycolor)
   filewin.attributes('-zoomed',True)
   filewin.wm_title('Select/Add media source')
   """
   Label(filewin, text="Please select or add media source",font=("Times", 20, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=True, padx=4, pady=0)
   # print('joho')
   m=mediaSS.find()
   i=1
   for c in m:
      Button(filewin, text="media source path: "+c['media_path'],bg=mycolor ,fg='white', command= lambda c=c: addMedia(depScen,c,filewin)).pack(side="top", expand=True, padx=4, pady=i)
      i+=1
   Button(filewin, text="Add",bg=mycolor ,fg='white', command=lambda: addMediaSource2(depScen,filewin)).pack(side="top", expand=True, padx=4, pady=i)
   #depMod={}addMedia
   """
   filewin.wm_title('Select/Add media source')
   Label(filewin, text="Media sources",font=("Times", 20, "bold"),bg=mycolor ,fg='white').grid()
   m=mediaSS.find()
   listbox = Listbox(filewin, selectmode=SINGLE,bg=mycolor ,fg='white',selectbackground="#f0f0ed")
   for option in m:
   	listbox.insert(0, option['media_name'])
   listbox.grid()
   b = Button(filewin, command=lambda: callbackaddMedia(depScen,listbox,filewin), text="Select",bg=mycolor ,fg='white')
   b.grid()
   Button(filewin,command=lambda:addMediaSource2(depScen,filewin),text='Add',bg=mycolor ,fg='white').grid()

def callbackaddMedia(depScen,listbox,filewin):
	m = mediaSS.find()
	for media in m:
		if media['media_name'] == listbox.selection_get():
			addMedia(depScen,media,filewin)

"""
When user selects a media source to add to an existing deployment scenario this method is called and updates
the deployments db to insert that media source
"""
def addMedia(depScen,media,filewin):
   filewin.withdraw()
   # print('dddddddddd',depScen)
   # print('mmmmm', media)
   dep_name= depScen['dep_name']
   frame_rate= media['frame_rate']
   resol= media['resol']
   y=media['y']
   x=media['x']
   width=media['width']
   height=media['height']
   media_path=media['media_path']
   media_context=media['media_context']
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
      'media_context':media_context
      }
      }
   })
   #add_media_source(frame_rate,resol,x, y, width, height,media_path)
   print('hwa hna hmarr')
   #showMedia(depScen,filewin)


"""
When user successfully selects a media source; a window is shown to insert the deployment scenario's
parameters.
"""
def addDeploy2(media,depMod,filewin):
	filewin.withdraw()
	filewin=Toplevel(root)
	filewin.configure(background=mycolor)
	filewin.attributes('-zoomed',True)


	filewin.wm_title('New deployment')
	Label(filewin, text="Deployment name:",bg=mycolor ,fg='white').grid(row=0)
	Label(filewin, text="Number of streams:",bg=mycolor ,fg='white').grid(row=1)
	e1 = Entry(filewin)
	e2 = Entry(filewin)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	save = Button(filewin, text ="Add",bg=mycolor ,fg='white',command= lambda: addDepEntries(e1.get(),e2.get(), media, depMod,filewin))
	save.grid(row=20, columnspan=20)

"""
On adding a deployment scenario this method is called to call add_deployment() method in CPU.py to
update database.
"""
def addDepEntries(e1,e2,media,depMod,filewin):
	filewin.withdraw()
	add_deployment(e1, e2,media,depMod)
	depScenarios()

"""
Shows a list of available deployment scenarios.
"""
def depScenarios():
	filewin = Toplevel(root)
	filewin.attributes('-zoomed',True)
	filewin.configure(background=mycolor)
	filewin.wm_title("Deployment scenarios")
	Label(filewin, text="Deployment Scenarios",font=("Times", 20, "bold"),bg=mycolor ,fg='white').grid()
	d=deployments.find()
	"""
	i=1
   for k in d:
	  Button(filewin,text=k['dep_name'],bg=mycolor ,fg='white', command=lambda k=k: remDepScen(k,filewin)).pack(side="top", expand=True, padx=4, pady=i)
	  i+=1
	"""
	listbox = Listbox(filewin, selectmode=SINGLE,bg=mycolor ,fg='white',selectbackground="#f0f0ed")
	for option in d:
	    listbox.insert(0, option['dep_name'])
	listbox.grid()

	b = Button(filewin, command=lambda: callbackAddMedia(listbox,filewin), text="Add Media Source",bg=mycolor ,fg='white')
	b.grid()
	b2 = Button(filewin, command=lambda: callbackRemoveDep(listbox,filewin), text="Remove",bg=mycolor ,fg='white')
	b2.grid()
	b3 = Button(filewin, command=lambda: callbackShowMedia(listbox,filewin), text="Show Media Source",bg=mycolor ,fg='white')
	b3.grid()
	b4 = Button(filewin, command=lambda: callbackHwEst(listbox), text="Calulate HW Estimate",bg=mycolor ,fg='white')
	b4.grid()
	b5 = Button(filewin, command=lambda: callbackHwConfig(listbox), text="Generate HW Configuration Recommendation",bg=mycolor ,fg='white')
	b5.grid()


def callbackAddMedia(listbox,filewin):
	m = deployments.find()
	for dep in m:
		if dep['dep_name'] == listbox.selection_get():
			 addMediaSource2(dep,filewin)

def callbackRemoveDep(listbox,filewin):
	m = deployments.find()
	for dep in m:
		if dep['dep_name'] == listbox.selection_get():
			 confDepRem(dep['dep_name'],filewin)

def callbackShowMedia(listbox,filewin):
	m = deployments.find()
	for dep in m:
		if dep['dep_name'] == listbox.selection_get():
			 showMedia(dep,filewin)

def callbackHwEst(listbox):
	m = deployments.find()
	for dep in m:
		if dep['dep_name'] == listbox.selection_get():
			 hwEstimate(dep)

def callbackHwConfig(listbox):
	m = deployments.find()
	for dep in m:
		if dep['dep_name'] == listbox.selection_get():
			 hwConfig(dep)


"""
On clicking on a certain deployment scenario, the user is granted with multiple options to select from.
"""
def remDepScen(depScen, filewin):
   filewin.withdraw()
   filewin = Toplevel(root)
   filewin.attributes('-zoomed',True)
   filewin.configure(background=mycolor)
   filewin.wm_title("Deployment scenario settings")
   Label(filewin, text='Deployment name: '+depScen['dep_name'],font=("Times", 13, "bold"),bg=mycolor ,fg='white').pack(side="top", expand=True, padx=4, pady=0)
#	Button(filewin, text='Remove', command=lambda: confDepRem(depScen['dep_name'], filewin)).grid(row=0)
   Button(filewin, text='Remove deployment',bg=mycolor ,fg='white', command=lambda: confDepRem(depScen['dep_name'],filewin)).pack(side="top", expand=True, padx=4, pady=1)
   Button(filewin, text='Show media sources',bg=mycolor ,fg='white', command=lambda: showMedia(depScen, filewin)).pack(side="top", expand=True, padx=4, pady=2)
   Button(filewin, text='Calculate hardware estimate',bg=mycolor ,fg='white', command=lambda: hwEstimate(depScen)).pack(side="top", expand=True, padx=4, pady=3)
   Button(filewin, text='Generate HW Configuration Recommendation',bg=mycolor ,fg='white', command=lambda: hwConfig(depScen)).pack(side="top", expand=True, padx=4, pady=4)
   Button(filewin, text='Add media source',bg=mycolor ,fg='white', command=lambda:  addMediaSource2(depScen,filewin)).pack(side="top", expand=True, padx=4, pady=4)


"""
Show the media source available to a certain deployment scenario if any and gives the option of adding
a new media source if there is none
"""
def showMedia(depScen, filewin):
  filewin.withdraw()
  filewin=Toplevel(root)
  filewin.configure(background=mycolor)
  filewin.attributes('-zoomed',True)
  filewin.wm_title("Media source")
  media = depScen['media']
  i=1
  listbox = Listbox(filewin, selectmode=SINGLE,bg=mycolor ,fg='white',selectbackground="#f0f0ed")
  if media != []:
    Label(filewin, text="Media Sources",font=("Times", 20, "bold"),bg=mycolor ,fg='white').grid()
    for option in media:
      listbox.insert(0, option['media_name'])
    listbox.grid()
    Button(filewin, command=lambda: callbackShowMediaConfig(depScen,listbox,filewin), text="Show Configuration",bg=mycolor ,fg='white').grid()
    Button(filewin, command=lambda: callbackEditMediaConfig(depScen,listbox,filewin), text="Edit Configuration",bg=mycolor ,fg='white').grid()
    Button(filewin, command=lambda: callbackRemMedia(depScen,listbox,filewin), text="Remove Media Source",bg=mycolor ,fg='white').grid()
    Button(filewin, command=lambda: addMediaContext(depScen,listbox,filewin), text="Add Plugin Context",bg=mycolor ,fg='white').grid()
  else:
    Label(filewin, text="This deployment's media source has previously been removed",font=("Times", 20, "bold"),bg=mycolor ,fg='white').grid()
    Button(filewin, text='Add media source',bg=mycolor ,fg='white', command=lambda: selectAddMediaSource2(depScen,filewin)).grid()

"""
Adds media context to media source can only add one media context at atime; only click on add input once.
otherwise, only the last entry will be considered.
"""
def addMediaContext(depScen,listbox,filewin):
  filewin = Toplevel(root)
  filewin.attributes('-zoomed',True)
  filewin.configure(background=mycolor)
  filewin.wm_title("Add Media Context")
  #global mediaContexts
  mediaContexts = []
  m=mediaSS.find()
  addboxButton = Button(filewin, text='Add Input',bg=mycolor ,fg="white", command=lambda:addBoxmedia(depScen,mediaContexts,listbox,filewin))
  addboxButton.grid()
  #for k in m:
  #  if k['media_name']==listbox.selection_get():
  #    save = Button(filewin, text ="Save",bg=mycolor ,fg='white',command= lambda: addMedCont(k,filewin))
  #    save.grid(row=20, columnspan=20)

"""
entry fields for user input
"""
def addBoxmedia(depScen,mediaContexts,listbox,filewin):
  print "ADD"
  frame = Frame(filewin)
  frame.grid()
  Label(frame, text='Attribute').grid(row=0, column=0)
  ent1 = Entry(frame)
  ent1.grid(row=1, column=0)
  Label(frame, text='Value').grid(row=0, column=1)
  ent2 = Entry(frame)
  ent2.grid(row=1, column=1)
  m=mediaSS.find()
  #Button(frame, text='Add', bg=mycolor, fg='white',command=lambda:addtomedcont(ent1.get(),ent2.get())).grid(row=1,column=2)
  for k in m:
    if k['media_name']==listbox.selection_get():
      save = Button(filewin, text ="Save",bg=mycolor ,fg='white',command= lambda k=k: addMedCont(depScen,k,mediaContexts,ent1.get(),ent2.get(),filewin))
      save.grid(row=20, columnspan=20)


def addtomedcont(a,v):
  mediaContexts.append( (a ,v) )

"""
Updates databases with the media contexts
"""
def addMedCont(depScen,media,mediaContexts,a,v,filewin):
  filewin.withdraw()
  print('llllllllllllllll', mediaContexts)
  dep_name= depScen['dep_name']
  media_name = media['media_name']
  mediaContexts.append( (a ,v) )
  for a,b in mediaContexts:
    print('a',a)
    print('b',b)

  medias = depScen['media']
  """
  deployments.update({
  'dep_name' : dep_name,
  'media.media_name':media_name
     },{
  '$push': {
  'media':{
  'media_context': mediaContexts   #### mfrood media.haga tgib anhi media.media_conte
  }
  }
  })
  """
  c=0
  for m in medias:
    if m['media_name']==media_name:
      print('henaaaaa')

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
        'frame_rate':m['frame_rate'],
        'resol':m['resol'],
        'x':m['x'],
        'y':m['y'],
        'width': m['width'],
        'height': m['height'],
        'media_path': m['media_path'],
        'media_name':m['media_name'],
        'media_context': mediaContexts
        }
        }
      })

    else:
      c+=1


  add_media_context(media,mediaContexts)


def callbackShowMediaConfig(depScen,listbox,filewin):
	m=mediaSS.find()
	for k in m:
		if k['media_name']==listbox.selection_get():
			mediaSettings(depScen,k['frame_rate'],k['resol'],k['x'],k['y'],k['width'],k['height'],k['media_path'],k['media_name'],filewin)

def callbackEditMediaConfig(depScen,listbox,filewin):
	m = mediaSS.find()
	for k in m:
		if k['media_name']== listbox.selection_get():
			mediaConfig(depScen,k['media_name'],filewin)

def callbackRemMedia(depScen,listbox,filewin):
	m = mediaSS.find()
	for k in m:
		if k['media_name'] == listbox.selection_get():
			confRemMediaSrc(depScen,k['frame_rate'],k['resol'],k['x'],k['y'],k['width'],k['height'],k['media_path'],k['media_name'],k['media_context'],filewin)



"""
On clicking on calculate hardware estimate, this method is called to create json files for each media source
and runs them while scanning for calculations.
"""
def hwEstimate(depScen):
  global pids
  pids=[]
  depMod= depScen['depMod']
  media= depScen['media']
  print('scena ', depScen)
  print('depp, ', depMod)
  print("__Media:", media)
  pluginpath= depMod['plugin_path']
  plgnCont = depMod['plugin_context']
  # print('plgnn',plgnCont)
  i=1

  for m in media:
    # print('dd', m)

    med= m['media_path']
    with open("conf.json", "r") as f, open(str(i)+'.json', 'r') as to:
      json_data = json.load(f)
      json_data['plugin_path'] = pluginpath
      json_data['file_media_provider']['path'] = med

      #Clear the copied plugin context
      json_data['plugin_context'] = {}
      print("pluginCont__")
      print(plgnCont)
      print("________")
      if plgnCont != []:

        for a,v in plgnCont:
          try:
            json_data['plugin_context'][a]= int(v)
          except ValueError:
              g=v.lower()
              if g == 'true':
                json_data['plugin_context'][a]= True
              else:
                if g == 'false':
                  json_data['plugin_context'][a]= False
                else:
                  json_data['plugin_context'][a] = v

      #Clear the copied media plugin
      json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'] = {}
      m['media_context'] = [["roi_custom","false"], ["roi_width","200"], ["roi_height","200"], ["roi_rotation","4.3"], ["roi_x","100"], ["roi_y","100"]  ]
      print("___m['media_context']___")
      print(m['media_context'])
      print("_________")
      if m['media_context'] != []:
        for a,v in m['media_context']:
          try:
            json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'][a]= float(v)
          except ValueError:
            g=v.lower()
            if g == 'true':
              json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'][a]= True
            else:
              if g == 'false':
                json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'][a]= False
              else:
                json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'][a]= v

    with open(str(i)+'.json', 'w') as f:
      f.write(json.dumps(json_data,indent=2))
    run_cmd_async("./ViBEMediaBlock.a "+str(i)+".json")
    i= i+1

  scanning(pids)
  cores= depMod['cores']
  RamM= depMod['ram_req']
  RamM= int(RamM)
  cores = int(cores)
  hardwareEstimate(cores,RamM,pids)
  # print(hardwareEstimate.Ram_Percent)

"""
On clicking on generate hardware configuration, this method is called to create json files for each
media source and runs them while scanning for calculations.
"""
def hwConfig(depScen):
  global pids
  pids= []
  depMod= depScen['depMod']
  media= depScen['media']
  print('scena ', depScen)
  print('depp, ', depMod)
  pluginpath= depMod['plugin_path']
  plgnCont = depMod['plugin_context']
  i=1
  for m in media:
    # print('dd', m)
    med= m['media_path']
    with open("conf.json", "r") as f, open(str(i) + ".json", "w") as to:
      json_data = json.load(f)
      json_data['plugin_path'] = pluginpath
      json_data['file_media_provider']['path'] = med

      #Clear the copied plugin context
      json_data['plugin_context']={}
      if plgnCont != []:
        for a,v in plgnCont:
          try:
            json_data['plugin_context'][a]= int(v)
          except ValueError:
            g=v.lower()
            if g == 'true':
              json_data['plugin_context'][a]= True
            else:
              if g == 'false':
                json_data['plugin_context'][a]= False
              else:
                json_data['plugin_context'][a]= v

      # Clear the copied media plugin
      json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'] = {}
      if m['media_context'] != []:
        for a,v in m['media_context']:
          try:
            json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'][a]= int(v)
          except ValueError:
            g=v.lower()
            if g == 'true':
              json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'][a]= True
            else:
              if g == 'false':
                json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'][a]= False
              else:
                json_data['file_media_provider']['plugins'][0]['plugin_per_media_context'][a]= v

    with open(str(i)+'.json', 'w') as f:
      f.write(json.dumps(json_data,indent=2))

    run_cmd_async("./ViBEMediaBlock.a "+str(i)+".json")
    i= i+1
  scanning(pids)
   # print(depMod['cores'])
   # print(depMod['ram_req'])
  cores =depMod['cores']
  ram_req = depMod['ram_req']
  threads= depMod['threads']
  threads= int(threads)
  cores = int(cores)
  ram_req= int(ram_req)
  hwConfiguration(cores, ram_req,threads,pids)

"""
On clicking on a media source the user is granted with multiple options.
"""
def mediaSettings(depScen,frame_rate,resol,x,y,width,height,media_path,media_name,filewin):
   filewin.withdraw()
   filewin=Toplevel(root)
   filewin.attributes('-zoomed',True)
   filewin.configure(background=mycolor)
   filewin.wm_title(media_name+' Configuration')
   Label(filewin,text='Frame rate: '+frame_rate,font=("Times", 13, "bold"),bg=mycolor,fg='white').pack(side="top", expand=True, padx=4, pady=0)
   Label(filewin,text='Resolution: '+resol,font=("Times", 13, "bold"),bg=mycolor,fg='white').pack(side="top", expand=True, padx=4, pady=1)
   Label(filewin,text='x: '+x,font=("Times", 13, "bold"),bg=mycolor,fg='white').pack(side="top", expand=True, padx=4, pady=2)
   Label(filewin,text='y: '+y,font=("Times", 13, "bold"),bg=mycolor,fg='white').pack(side="top", expand=True, padx=4, pady=3)
   Label(filewin,text='Width: '+width,font=("Times", 13, "bold"),bg=mycolor,fg='white').pack(side="top", expand=True, padx=4, pady=4)
   Label(filewin,text='Height: '+height,font=("Times", 13, "bold"),bg=mycolor,fg='white').pack(side="top", expand=True, padx=4, pady=5)
   Label(filewin,text='Media path: '+media_path,font=("Times", 13, "bold"),bg=mycolor,fg='white').pack(side="top", expand=True, padx=4, pady=6)
   #Button(filewin, text='Remove media source',bg=mycolor ,fg='white', command=lambda: confRemMediaSrc(depScen,frame_rate,resol,x,y,width,height,media_path,media_name,filewin)).pack(side="top", expand=True, padx=4, pady=7)
   #Button(filewin, text='Reset configuration',bg=mycolor ,fg='white', command=lambda: mediaConfig(depScen,media_name, filewin)).pack(side="top", expand=True, padx=4, pady=8)

"""
Calls remove_deployment() in CPU.py to Remove deployment scenario from database.
"""
def confDepRem(dep_name,filewin):
	filewin.withdraw()
	remove_deployment(dep_name)

"""
Takes input from user to update media source configuration.
"""
def mediaConfig(depScen,media_name,filewin):
  filewin.withdraw()
  filewin=Toplevel(root)
  filewin.configure(background=mycolor)
  filewin.attributes('-zoomed',True)
  filewin.wm_title('Media source config')
  # Label(filewin, text="Frame rate:",bg=mycolor ,fg='white').grid(row=0)
  # Label(filewin, text="Resolution:",bg=mycolor ,fg='white').grid(row=1)
  Label(filewin, text="x:",bg=mycolor ,fg='white').grid(row=2)
  Label(filewin, text="y:",bg=mycolor ,fg='white').grid(row=3)
  Label(filewin, text="Width:",bg=mycolor ,fg='white').grid(row=4)
  Label(filewin, text="Height:",bg=mycolor ,fg='white').grid(row=5)

  var = StringVar()
  e = Entry(filewin, textvariable=var).grid(row=6,column=1)
  b = Button(filewin, text="Browse",bg=mycolor ,fg='white',
          command=lambda:var.set(tkFileDialog.askopenfilename())).grid(row=6,column=2)
  Label(filewin, text="Media path:",bg=mycolor ,fg='white').grid(row=6)

  # e1 = Entry(filewin)
  # e2 = Entry(filewin)
  e3 = Entry(filewin)
  e4 = Entry(filewin)
  e5 = Entry(filewin)
  e6 = Entry(filewin)

  # e1.grid(row=0, column=1)
  # e2.grid(row=1, column=1)
  e3.grid(row=2, column=1)
  e4.grid(row=3, column=1)
  e5.grid(row=4, column=1)
  e6.grid(row=5, column=1)

  medcont=[]
  save = Button(filewin, text ="Save",bg=mycolor ,fg='white',command= lambda: addMediaConfig(depScen,e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),var.get() ,media_name,medcont,filewin))
  save.grid(row=20)

"""
Pops a confirmation message when user clicks on remove media source.
"""
def confRemMediaSrc(depScen,frame_rate,resol,x,y,width,height,media_path,media_name,media_context,filewin):
   filewin.withdraw()
   filewin=Toplevel(root)
   filewin.attributes('-zoomed',True)
   filewin.configure(background=mycolor)
   filewin.wm_title('Confirm delete')
   Label(filewin, text="Are you sure you want to remove media source?",font=("Times", 20, "bold"),bg=mycolor ,fg='white').grid(row=0)
   Button(filewin,text="yes",bg=mycolor ,fg='white', command=lambda: remMediaSrc(depScen,frame_rate,resol,x,y,width,height,media_path,media_name,media_context,filewin)).grid(row=1)
   Button(filewin,text='No',bg=mycolor ,fg='white', command=lambda: Home(filewin)).grid(row=2)

"""
Deletion of media source from database.
"""
def remMediaSrc(depScen,frame_rate, resol, x, y, width, height,media_path,media_name,media_context,filewin):
	filewin.withdraw()
	remove_media_source(depScen,frame_rate, resol, x, y, width, height,media_path,media_name,media_context)

def Home(filewin):
	filewin.withdraw()

"""
Updates media source configuration parameters in database.
"""
def addMediaConfig(depScen,frame_rate, resol, x, y, width, height,media_path,media_name,media_context,filewin):
	filewin.withdraw()
	media_source_config(depScen,frame_rate, resol, x, y, width, height,media_path,media_name)

"""
Takes media source parameters from user.
"""
def addMediaSource(depMod,filewin):
  filewin.withdraw()
  filewin=Toplevel(root)
  filewin.configure(background=mycolor)
  filewin.attributes('-zoomed',True)
  filewin.wm_title('Add media source')
  # Label(filewin, text="Frame rate:",bg=mycolor ,fg='white').grid(row=0)
  # Label(filewin, text="Resolution:",bg=mycolor ,fg='white').grid(row=1)
  Label(filewin, text="x:",bg=mycolor ,fg='white').grid(row=2)
  Label(filewin, text="y:",bg=mycolor ,fg='white').grid(row=3)
  Label(filewin, text="Width:",bg=mycolor ,fg='white').grid(row=4)
  Label(filewin, text="Height:",bg=mycolor ,fg='white').grid(row=5)
  Label(filewin, text="Media name:",bg=mycolor ,fg='white').grid(row=6)

  var = StringVar()
  e = Entry(filewin, textvariable=var).grid(row=7,column=1)
  b = Button(filewin, text="Browse",bg=mycolor ,fg='white',
        command=lambda:var.set(tkFileDialog.askopenfilename())).grid(row=7,column=2)
  Label(filewin, text="Media path:",bg=mycolor ,fg='white').grid(row=7)

  # e1 = Entry(filewin)
  # e2 = Entry(filewin)
  e3 = Entry(filewin)
  e4 = Entry(filewin)
  e5 = Entry(filewin)
  e6 = Entry(filewin)
  e7 = Entry(filewin)

  # e1.grid(row=0, column=1)
  # e2.grid(row=1, column=1)
  e3.grid(row=2, column=1)
  e4.grid(row=3, column=1)
  e5.grid(row=4, column=1)
  e6.grid(row=5, column=1)
  e7.grid(row=6, column=1)

  medcont=[]
  def save_button_action():
    video_path = var.get()
    vid = cv2.VideoCapture(video_path)
    resolution_width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    resolution_height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = vid.get(cv2.CAP_PROP_FPS)
    # resolution_width = 123
    # resolution_height = 223
    # fps = 20
    total_resolution = str(resolution_height)+'x'+str(resolution_width)
    x = e3.get()
    y = e4.get()
    roi_width = e5.get()
    roi_height = e6.get()
    medcont=[]
    addMediaSrc(depMod,fps,total_resolution,x,y,roi_width,roi_height,var.get(),e7.get() ,medcont,filewin)

  save = Button(filewin, text ="Add",bg=mycolor ,fg='white',command= save_button_action )
  save.grid(row=20, columnspan=20)

"""
When user adds a media source to an existing deploment scenario this method is called to enable the user to
insert the media source parameters
"""
def addMediaSource2(depScen,filewin):
   print("______Function Name: addMediaSource2_______")
   filewin.withdraw()
   filewin=Toplevel(root)
   filewin.attributes('-zoomed',True)
   filewin.configure(background=mycolor)
   filewin.wm_title('Add media source')
   # Label(filewin, text="Frame rate:",bg=mycolor ,fg='white').grid(row=0)
   # Label(filewin, text="Resolution:",bg=mycolor ,fg='white').grid(row=1)
   Label(filewin, text="x:",bg=mycolor ,fg='white').grid(row=2)
   Label(filewin, text="y:",bg=mycolor ,fg='white').grid(row=3)
   Label(filewin, text="Width:",bg=mycolor ,fg='white').grid(row=4)
   Label(filewin, text="Height:",bg=mycolor ,fg='white').grid(row=5)
   Label(filewin, text="Media name:",bg=mycolor ,fg='white').grid(row=6)

   var = StringVar()
   e = Entry(filewin, textvariable=var).grid(row=7,column=1)
   b = Button(filewin, text="Browse",bg=mycolor ,fg='white',
           command=lambda:var.set(tkFileDialog.askopenfilename())).grid(row=7,column=2)
   Label(filewin, text="Media path:",bg=mycolor ,fg='white').grid(row=7)


   # e1 = Entry(filewin)
   # e2 = Entry(filewin)
   e3 = Entry(filewin)
   e4 = Entry(filewin)
   e5 = Entry(filewin)
   e6 = Entry(filewin)
   e7 = Entry(filewin)

   # e1.grid(row=0, column=1)
   # e2.grid(row=1, column=1)
   e3.grid(row=2, column=1)
   e4.grid(row=3, column=1)
   e5.grid(row=4, column=1)
   e6.grid(row=5, column=1)
   e7.grid(row=6, column=1)
   medcont=[]

   def save_button_action():
    video_path = var.get()
    vid = cv2.VideoCapture(video_path)

    resolution_width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    resolution_height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    fps = vid.get(cv2.CAP_PROP_FPS)
    # resolution_width = 123
    # resolution_height = 223
    # fps = 20
    total_resolution = str(resolution_height)+'x'+str(resolution_width)
    x = e3.get()
    y = e4.get()
    roi_width = e5.get()
    roi_height = e6.get()
    medcont=[]
    addMediaSrc2(depScen,fps,total_resolution,x,y,roi_width,roi_height,var.get(),e7.get() ,medcont,filewin)

   save = Button(filewin, text ="Add",bg=mycolor ,fg='white',command= save_button_action )
   save.grid(row=20, columnspan=20)

"""
Adds media source to database and redirects user to continue the procedure of adding a new deployment
"""
def addMediaSrc(depMod,frame_rate, resol, x, y, width, height,media_path,media_name,media_context,filewin):
   add_media_source(frame_rate,resol,x, y, width, height,media_path,media_name,media_context)
   m = mediaSS.find({'frame_rate':frame_rate,'resol':resol,'x':x,'y':y,'width':width,'height':height,'media_path':media_path,'media_name':media_name,'media_context':media_context})
   # print('hhhhhhhh ',m)
   for k in m:
      # print('shhhh',k)
      addDeploy2(k,depMod,filewin)


"""
Adds media source to deployment scenario db. its called when user adds a media source to an existing
scenario
"""
def addMediaSrc2(depScen,frame_rate, resol, x, y, width, height,media_path,media_name,media_context,filewin):
   add_media_source(frame_rate,resol,x, y, width, height,media_path,media_name,media_context)
   filewin.withdraw()
   dep_name= depScen['dep_name']
   # print('dep name', dep_name)
   # print('media pathh ', media_path)
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
      'media_context':media_context
      }
      }
   })

"""
called to run config.json in parallel when user clicks on calculate hw estimate or generate hw configuration
"""
def run_cmd_async(cmd):
    import shlex
    args = shlex.split(cmd)
    FNULL = open(os.devnull, 'w')
    pro = subprocess.Popen(args, stdout=FNULL, stderr=FNULL)
    print ("pid: " + str(pro.pid))
    pids.append(pro.pid)
    print('leng///////////', len(pids))

root = Tk()
root.wm_title("Main")
root.attributes('-zoomed',True)
mycolor= '#424949'
root.configure(background=mycolor)
menubar = Menu(root)
menubar.configure(background=mycolor, fg='white')
Computingmenu = Menu(menubar, tearoff=0)
Computingmenu.add_command(label="Add new Computing module...", command=addCompWind)
Computingmenu.add_command(label="Show computing modules", command=modulesList)
Computingmenu.configure(background=mycolor,fg='white')
#Compsubmenu = Menu(Computingmenu)
#Compsubmenu.add_command(label="Edit", command=donothing)
#Compsubmenu.add_command(label="Remove", command=donothing)
#Computingmenu.add_cascade(label='Module 1', menu=Compsubmenu, underline=0)


menubar.add_cascade(label="Computing Modules", menu=Computingmenu)
Deploymentsmenu = Menu(menubar, tearoff=0)
Deploymentsmenu.add_command(label="Add new deployment..", command=addDeploy)
Deploymentsmenu.add_command(label="Show deployments", command=depScenarios)
Deploymentsmenu.configure(bg=mycolor,fg='white')

"""
import matplotlib.pyplot as plt
plt.ion()
plt.axis([0, 60, 0, 100])
plt.grid()
"""
menubar.add_cascade(label="Deployments", menu=Deploymentsmenu)

root.config(menu=menubar)

root.mainloop()