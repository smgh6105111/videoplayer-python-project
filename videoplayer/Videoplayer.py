from tkinter import*
import os,glob

def selectvideo(event):
	ind=list.curselection()
	sel=list.get(ind)
	os.startfile(sel)
	
	
	
root=Tk()
root.geometry('450x700')
mp4=glob.glob('*mp4')

list=Listbox(root,width=50,height=30,bg='khaki4')
list.bind('<Double-Button>',selectvideo)
list.pack(pady=20)
for movie in mp4:
	list.insert(END,movie)
	
	



root.mainloop()