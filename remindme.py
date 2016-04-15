# -*- coding: utf-8 -*-

from Tkinter import *  #引入模块

def center_window(w=300, h=200):  
    # get screen width and height  
    ws = root.winfo_screenwidth()  
    hs = root.winfo_screenheight()  
    # calculate position x, y  
    x = (ws/2) - (w/2)     
    y = (hs/2) - (h/2)  
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
root=Tk()   #主窗口
root.wm_attributes('-topmost',1)  # 窗口置顶
#root.geometry('600x400')  #设置了主窗口的初始大小600x400
center_window(600, 400)

label=Label(root,text='工作25分钟了，休息一下吧！',font='Helvetica -35 bold')  #设置标签字体的初始大小
label.pack(fill=Y,expand=1)

mainloop()
