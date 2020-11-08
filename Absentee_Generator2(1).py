import tkinter as tk
from tkinter import filedialog
import pandas as pd
import xlwt
from xlwt import  Workbook
root=tk.Tk()
root.title("Absentee Generator 2")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(1000,weight=1)
count = 0
root.geometry("1500x600")
mainfile=""
pathlabel=""


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=0)
def pathchoose(file,label):


    prog="global pathlabel\nglobal "+file+"\n"+file+" = filedialog.askopenfilename( title='Select file',filetypes=(('csv files', '*.csv'), ('all files', '*.*')))\npathlabel=tk.Label(root,text='File Chosen:-'+"+file+")\npathlabel.grid(sticky='SEW',row="+str(label)+",column=0)"
    exec (prog)




    noflabel.grid(sticky='N',row=2,column=0)
    nofmenu.grid(sticky='NEW',row=2,column=1)
    btnfinal.grid(sticky='NEW',row=2, column=2)
def enterfiles():

    btnfilepath.grid(sticky='NEW',row=int(nof.get())+3, column=2)
    num=(int(nof.get()))
    for i in range(1,num+1):


        snum=str(i)
        prog="global fcheck"+snum+"\nfcbtn"+snum+"=tk.Button(root,text='Choose File "+snum+"',command=lambda:pathchoose('fcheck"+snum+"',"+str(2*i+1)+"))\nfcbtn"+snum+".grid(sticky='NEW',row="+str(2*i)+",column=0)"
        exec (prog)

def final():
    global datelist1
    global ablistmain1
    try :
        dm=pd.read_csv(mainfile)
    except:
        dm=pd.read_csv(mainfile,encoding="utf-16",sep="\t")
    wb = Workbook()
    sheet1 = wb.add_sheet("Sheet")

    mainlist=list(dm["Full Name"])
    mainlist = list(set(mainlist))


    mainlist.sort()
    finalcount=[]
    final=[]
    li = []
    count=0
    num = (int(nof.get()))
    var2=str(num)
    for i in range(1, num + 1):

        snum = str(i)
        prog="global fcheck"+snum+"\nglobal datelist"+snum+"\nglobal ablistmain"+snum+"\nablistmain"+snum+"=[]\nli.append(fcheck"+snum+")\nfor j in li:\n\ttry:\n\t\tdf"+snum+"=pd.read_csv(j)\n\texcept:\n\t\tdf"+snum+"=pd.read_csv(j,encoding='utf-16',sep='\t')\nablist"+snum+"=list(set(df"+snum+"['Full Name']))\nfor l in mainlist:\n\tif l not in ablist"+snum+":\n\t\tfinal.append(l)\n\t\tablistmain"+snum+".append(l)\ndatelist"+snum+"=str(df"+snum+"['Timestamp'][1])\ndatelist"+snum+"=datelist"+snum+"[:datelist"+snum+".find(',')]\nfor j in range(0,len(ablistmain"+snum+")):\n\tsheet1.write(j+1,"+str(int(snum)+2)+",ablistmain"+snum+"[j])\nsheet1.write(0,"+str(int(snum)+2)+",datelist"+snum+")"
        exec(prog)




    for i in mainlist:
        for j in final:
             if (i==j):
                count+=1
        finalcount.append(count)
        count = 0



    sheet1.write(0,0,"Full Name")
    sheet1.write(0,1,"No Of Time Absent")

    for i in range(0,len(mainlist)):

        sheet1.write(i+1,0,mainlist[i])
        sheet1.write(i+1,1,finalcount[i])

    wb.save("absentees.xls")
    labfinal=tk.Label(text="Absentee File Generated Successfully")
    labfinal.grid(sticky='NEW',row=int(len(mainlist))+12,column=0)


mainbtn=tk.Button(root,text="Choose Main File",command=lambda :pathchoose("mainfile",1))

nof=tk.StringVar()
nof.set(1)
noflabel=tk.Label(root,text="Choose The Number of Files to be checked:")
nofmenu=tk.OptionMenu(root,nof,*range(1,8))

mainbtn.grid(sticky='NEW',row=0,column=0,columnspan=3)
btnfinal=tk.Button(root,text="Enter",command=enterfiles)
btnfilepath=tk.Button(root,text="Enter",command=final)
labelcredit=tk.Label(root,text="Created By Aditya Amit Kinjawadekar. For More Details mail to k.aditya2004@gmail.com")
labelcredit.grid(sticky="SEW",row=1000,column=0,columnspan=5)
root.mainloop()

