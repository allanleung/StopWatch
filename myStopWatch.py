import tkinter
from datetime import datetime
counter = 0
running = False
def counter_label(label):
	def count():
		if running:
			global counter
			if counter == 0:
				display = "Starting in 3 Sec"
			else:
				tt = datetime.fromtimestamp(counter)
				string = tt.strftime("%H:%M:%S")
				display = string  
			label['text'] = display
			label.after(3000,count)
			counter = counter + 1
	count()

def Start(label):
	global running
	running = True 
	counter_label(label)
	start['state'] = 'disabled'
	stop['state'] = 'normal'
	reset['state'] = 'normal'
	print("Start Method State")
def Stop(label):
	global running 
	start['state'] = 'normal'
	stop['state'] = 'disabled'
	reset['state'] = 'normal'
	running = False
	print("Stop Method State")
def Reset(label):
	global counter
	counter = 0
	if running == False:
		reset['state']	= 'disabled'
		label['text'] = 'StopWatch Restart Soon!'
		print("Reset Method State")
	else:
		label['text'] = 'StopWatch Not Working'

root = tkinter.Tk()
root.title('myStopWatch')
root.minsize(width=300, height=100)
label = tkinter.Label(root,texts="StopWatch", fg="black", font="Verdana 24 bold")
label.pack()
f = tkinter.Frame(root)
start = tkinter.Button(f, text = 'Start', width=6, command = lambda:Start(label))
stop = tkinter.Button(f, text = 'Stop', width=6, state = 'disabled', command = lambda:Stop(label))
reset = tkinter.Button(f, text = 'Reset', width=6, state = 'disabled', command = lambda:Reset(label))

f.pack(anchor = 'center', pady=5)
start.pack(side = 'left')
stop.pack(side = 'left')
reset.pack(side = 'left')
root.mainloop()