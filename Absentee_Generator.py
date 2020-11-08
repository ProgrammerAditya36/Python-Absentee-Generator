import tkinter as tk
import pandas as pd

root=tk.Tk()
root.title("Absentee Generator")
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.geometry("750x200")

#-------Main File Input--------
labelmain=tk.Label(text="Enter the Main file name:- ")
inputmain=tk.Entry(root)
ffm=tk.StringVar()
fileformatmain=tk.OptionMenu(root,ffm,"xlsx","csv")


#-------Checked File Input--------
labelattend=tk.Label(text="Enter the file name to be checked:- ")
inputattend=tk.Entry(root)
ffa=tk.StringVar()
fileformatattend=tk.OptionMenu(root,ffa,"xlsx","csv")
#-----------------------------------
labelmain.grid(sticky='EWS',  row=0,column=0)
labelattend.grid(sticky='EWS',  row=1,column=0)
inputmain.grid(sticky='EWS',  row=0,column=1)
inputattend.grid(sticky='EWS',  row=1,column=1)
fileformatmain.grid(sticky="EWS",row=0,column=2)
fileformatattend.grid(sticky="EWS",row=1,column=2)


#--------------------------------------
def enter():
    count = 0

    filemainname=inputmain.get()
    fileattendname=inputattend.get()
    if ffm.get() == "xlsx":
        mainfile = filemainname + ".xlsx"
        dm = pd.read_excel(mainfile)
    elif ffm.get() == "csv":
        mainfile = filemainname + ".csv"
        dm = pd.read_csv(mainfile)


    if ffa.get()=="xlsx":
        attendfile=fileattendname+".xlsx"
        da=pd.read_excel(attendfile)
    elif ffa.get()=="csv":
        attendfile = fileattendname + ".csv"
        da= pd.read_csv(attendfile)
    criteria="Full Name"
    mainlist=list(dm[criteria])
    attendlist=list(da[criteria])
    absentees=[]
    for i in mainlist:
        if i not in attendlist:
            absentees.append(i)
            attendlist.append(i)
            count+=1
    for i in range(0,len(absentees)):
        cur_label='label'+str(i)
        cur_label=tk.Label(root,text=absentees[i])
        cur_label.grid(sticky='EWS',  row=i+4,column=0)
    labelcount=tk.Label(root,text="Absentees:-{}".format(str(count)))
    labelcount.grid(sticky='EWS',  row=5,column=1)


buttonenter=tk.Button(root,text="Enter",command=enter)
buttonenter.grid(sticky='EWS',  row=3,column=2)
root.mainloop()
