import tkinter as tk
from tkinter import filedialog
import pandas as pd
root=tk.Tk()
root.columnconfigure(0,weight=3)
root.geometry("500x300")
root.title("Quick Absentee Generator")
count=0
# MainFile
def mainfile():
    global dm
    file=tk.filedialog.askopenfilename( title='Select file',filetypes=(('csv files', '*.csv'), ('all files', '*.*')))
    try:
        dm=pd.read_csv(file,encoding='utf-16',sep="\t")
    except:
        dm = pd.read_csv(file)
    labelmain=tk.Label(root,text="File Chosen:-"+file)
    labelmain.grid(sticky="EW",row=1,column=0)
    return dm
mainbtn=tk.Button(root,text="Choose Mainfile",command=mainfile)
mainbtn.grid(sticky="EW",row=0,column=0)
# AttendFile
def attendfile():
    global da
    file=tk.filedialog.askopenfilename( title='Select file',filetypes=(('csv files', '*.csv'), ('all files', '*.*')))
    try:
        da = pd.read_csv(file, encoding='utf-16',sep="\t")
    except:
        da = pd.read_csv(file)
    labelattend=tk.Label(root,text="File Chosen:-"+file)
    labelattend.grid(sticky="EW",row=3,column=0)
    return da
attendbtn=tk.Button(root,text="Choose Absentee file",command=attendfile)
attendbtn.grid(sticky="EW",row=2,column=0)
# Enter
def enter():

    global dm,da,count

    criteria="Full Name"
    mainlist = list(dm[criteria])
    attendlist = list(da[criteria])
    mainlist=list(set(mainlist))

    mainlist.sort()

    absentees = []
    for i in mainlist:
        if i not in attendlist:
            absentees.append(i)
            attendlist.append(i)
            count += 1
    for i in range(0, len(absentees)):
        cur_label = 'label' + str(i)
        cur_label = tk.Label(root, text=absentees[i])

        cur_label.grid(sticky='EWS', row=i + 7, column=0)
    labelcount = tk.Label(root, text="Absentees:-{}".format(str(count)))
    labelcount.grid(sticky='EWS', row=1+len(mainlist), column=0)

enterbtn=tk.Button(root,text="Enter",command=enter)
enterbtn.grid(sticky="EW",row=4,column=0)
root.mainloop()