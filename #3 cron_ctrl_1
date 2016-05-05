from Tkinter import *
import tkMessageBox
import commands
 
class Application(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()
 
  def createWidgets(self):
    self.nameInput = Entry(self)
    self.nameInput.pack()
    self.alertButton1 = Button(self, text='stop', command=self.hello1)
    self.alertButton1.pack()
    self.alertButton2 = Button(self, text='start', command=self.hello2)
    self.alertButton2.pack()
    self.alertButton3 = Button(self, text='list', command=self.hello3)
    self.alertButton3.pack()
	
 
  def hello1(self):
    name = self.nameInput.get() or 'world'
    tkMessageBox.showinfo('Message', 'Hello, %s' % name)
    command1='./cron_ctrl '+self.nameInput.get()+' --stop'
    print command1
    commands.getstatusoutput(command1)
    #./cron_ctrl jobname1 --stop
  def hello2(self):
    name = self.nameInput.get() or 'world'
    tkMessageBox.showinfo('Message', 'Hello, %s' % name)
    command2='./cron_ctrl '+self.nameInput.get()+' --start'
    print command2
    #commands.getstatusoutput(command2)
     #./cron_ctrl jobname1 --start
  def hello3(self):
    name = self.nameInput.get() or 'world'
    tkMessageBox.showinfo('Message', 'Hello, %s' % name)
    command3='./cron_ctrl '+self.nameInput.get()+' --list'
    print command3
    #commands.getstatusoutput(command3)
    #./cron_ctrl jobname1 --list
  
app = Application()
app.master.title('Hello World')
app.mainloop()
