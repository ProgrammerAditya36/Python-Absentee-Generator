import tkinter as tk
from tkinter import filedialog
import pandas as pd
import xlwt
from xlwt import  Workbook
root=tk.Tk()



root.geometry("1000x500")
mainfile=""
def pathchoose(file):

    prog="global "+file+"\n"+file+" = filedialog.askopenfilename( title='Select file',filetypes=(('csv files', '*.csv'), ('all files', '*.*')))"
    exec (prog)

def enter(file):
    mainenter.destroy()
    prog="global "+file+"\npathlabel=tk.Label(root,text='File Chosen:-'+"+file+")\npathlabel.grid(row=1,column=0)"
    exec (prog)
    noflabel.grid(row=3,column=0)
    nofmenu.grid(row=3,column=1)
    btnfinal.grid(row=3, column=2)
def enterfiles():

    btnfilepath.grid(row=int(nof.get())+3, column=2)
    num=(int(nof.get()))
    for i in range(1,num+1):
        snum=str(i)
        prog="global fcheck"+snum+"\nfcbtn"+snum+"=tk.Button(root,text='Choose File "+snum+"',command=lambda:pathchoose('fcheck"+snum+"'))\nfcbtn"+snum+".grid(row="+str(i+3)+",column=0)"
        exec (prog)

def final():
    try:
        dm=pd.read_csv(mainfile)
    except:
        dm=pd.read_csv(mainfile,encoding="utf-16",sep="\t")
    mainlist=list(dm["Full Name"])
    mainlist = list(set(mainlist))
    mainlist.sort()
    finalcount=[]
    final=[]
    li = []
    count=0
    num = (int(nof.get()))
    for i in range(1, num + 1):
        snum = str(i)
        prog="global fcheck{}\npathlabel=tk.Label(root,text='File Chosen:-'+fcheck{})\npathlabel.grid(row=".format(snum,snum)+str(i+3)+",column=1)\nli.append(fcheck"+snum+")\nfor j in li:\n\ttry:\n\t\tdf"+snum+"=pd.read_csv(j)\n\texcept:\n\t\tdf"+snum+"=pd.read_csv(j,encoding='utf-16',sep='\t')\nablist"+snum+"=list(set(df"+snum+"['Full Name']))\nprint(ablist"+snum+")\nfor l in mainlist:\n\tif l not in ablist"+snum+":\n\t\tfinal.append(l)"
        exec(prog)



    print(mainlist)
    print(final)
    for i in mainlist:
        for j in final:
             if (i==j):
                count+=1
        finalcount.append(count)
        count = 0
    print(finalcount)
    wb=Workbook()
    sheet1=wb.add_sheet('Sheet 1')
    sheet1.write(0,0,"Full Name")
    sheet1.write(0,1,"No Of Time Absent")
    print(len(finalcount))
    print(len(mainlist))
    for i in range(0,len(mainlist)):
        label1=tk.Label(root,text=mainlist[i])
        label1.grid(row=i+12,column=0)
        label2=tk.Label(root,text=finalcount[i])
        label2.grid(row=i+12,column=1)
        sheet1.write(i+1,0,mainlist[i])
        sheet1.write(i+1,1,finalcount[i])
    wb.save("absentees.xls")
    labfinal=tk.Label(text="Absentee File Generated Successfully")
    labfinal.grid(row=int(len(mainlist))+12,column=0)

mainbtn=tk.Button(root,text="Choose Main File",command=lambda :pathchoose("mainfile"))
mainenter=tk.Button(root,text="Enter",command=lambda :enter("mainfile"))
nof=tk.StringVar()
nof.set(1)
noflabel=tk.Label(root,text="Choose The Number of Files to be checked:")
nofmenu=tk.OptionMenu(root,nof,*range(1,8))

mainbtn.grid(row=0,column=0)
btnfinal=tk.Button(root,text="Enter",command=enterfiles)
btnfilepath=tk.Button(root,text="Enter",command=final)
mainenter.grid(row=0, column=2)

root.mainloop()