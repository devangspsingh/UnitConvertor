from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image 
import time
import os
import sys

def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'


photoimage_list=[]
credits = "created by @devangspsingh"

Unit_Tuple=("Mili","Centi","Deci","","Deca","Hecto","Kilo")
Unit_Number_Tuple=(1,2,3,4,5,6,7)
Unit_Dictionary = dict(zip(Unit_Tuple, Unit_Number_Tuple)) 

def main_convertor(unit_name_attribute,window,p,q):
    
    def Unit_Name(unit_name="Metre"):

        Unit_Tuple=("Mili","Centi","Deci","","Deca","Hecto","Kilo")
        Unit_Names=[]
        for i in Unit_Tuple:
            Unit_Names.append(i+unit_name)
        return tuple(Unit_Names)

    MainFrame_main=Frame(window,bg="orange",border=8,relief=RIDGE)
    MainFrame_main.pack(side=BOTTOM,padx=60,pady=50,fill=X,ipady=5,ipadx=10)
    
    value1=IntVar()
    value1_entry=Entry(MainFrame_main,textvariable=value1,font=('calibre',10,'normal'),borderwidth=4,relief=SUNKEN,width=20)
    
    unit1 = StringVar()
    Unit_Names1=ttk.Combobox(MainFrame_main, textvariable = unit1,state="readonly",width=25,)
    Unit_Names1['values']=Unit_Name(unit_name_attribute) 
    Unit_Names1.current(3)

    unit2 = StringVar()
    Unit_Names2=ttk.Combobox(MainFrame_main, textvariable = unit2,state="readonly",width=25)
    Unit_Names2['values']=Unit_Name(unit_name_attribute) 
    Unit_Names2.current(6)

    value2=IntVar()

    def conversion(name, index, mode):
        a=Unit_Dictionary.get((unit1.get())[p:q])
        b=Unit_Dictionary.get((unit2.get())[p:q])
        final_unit=a-b
        value2.set((value1.get())*(10**final_unit))

    unit1.trace("w",conversion)
    unit2.trace("w",conversion)
    value1.trace("w",conversion)
    value2.trace("w",conversion)
    value1.set(1)

    
    value2_output=Label(MainFrame_main,anchor=W,textvariable=value2,font=('calibre',10,'normal'),borderwidth=4,relief=SUNKEN,bg="white",width=18)

    value1_entry.grid(row=0,column=0,padx=10,pady=35)
    Unit_Names1.grid(row=0,column=1,padx=10,pady=35)
    value2_output.grid(row=1,column=0,padx=10,pady=35,)
    Unit_Names2.grid(row=1,column=1,padx=10,pady=35)

def Weight():
    WeightWindow=Toplevel()
    image_maker(WeightWindow,get_path("WeightImage.png"))
    windowCreater(WeightWindow,"Weight - Convertor")    
    titleCreator(WeightWindow,"Weight Convertor")
    main_convertor("Gram",WeightWindow,0,-4)

def Length():
    LengthWindow=Toplevel()
    image_maker(LengthWindow,get_path("LengthImage.png"))
    windowCreater(LengthWindow,"Length - Convertor") 
    titleCreator(LengthWindow,"Length Convertor")
    main_convertor("Metre",LengthWindow,0,-5)

def Volume():
    VolumeWindow=Toplevel()
    image_maker(VolumeWindow,get_path("VolumeImage.png"))
    windowCreater(VolumeWindow,"Volume - Convertor") 
    titleCreator(VolumeWindow,"Volume Convertor")
    main_convertor("Litre",VolumeWindow,0,-5)

def windowCreater(root,title_name):
    h=500
    w=500
    root.geometry(f"{h}x{w}")
    root.maxsize(h,w)
    root.minsize(h,w)

    root.title(title_name)
    root.iconbitmap(get_path("logo.ico"))
    
    status_frame=Frame(root,bg="royal blue",border=5,relief=FLAT)
    status_bar=Label(status_frame,bg="royal blue",fg="white",justify=LEFT,anchor=W)
    status_frame.pack(side=BOTTOM,fill=X)
    status_bar.pack(side=LEFT)
    Label(status_frame,text=credits,bg="royal blue",fg="white",font="times 10",justify="right",anchor=E,).pack(side=RIGHT)
    def clock():
        time_string=time.strftime('%I:%M:%S:%p',time.localtime())
        if time_string!='':
            status_bar.config(text=time_string,font='times 10',padx=10)
        root.after(100,clock)
    clock()

def image_maker(window,name):
    background_image=Image.open(name)
    background_image=background_image.resize((500,500),Image.ANTIALIAS)
    background_image=ImageTk.PhotoImage(background_image)
    photoimage_list.append(background_image)
    background_image_label=Label(window,image=background_image)
    background_image_label.place(x=0,y=0)

def titleCreator(window,text):
    TitleFrame=Frame(window,bg="blue",border=5,relief=RIDGE)
    TitleLabel=Label(TitleFrame,text=text,font="compact 20 bold",padx=5,fg="maroon1",bg="blue")
    TitleFrame.pack(side=TOP,fill=X,padx=15,pady=8)
    TitleLabel.pack(side=TOP,pady=15)

def ButtonMaker(ButtonFrame,Text,Command):
    Button(ButtonFrame,text=Text,font="compact 12",command=Command,bg="orange",activebackground="red").pack(expand=YES,padx=8,pady=5,fill=X,anchor=W)
    
root=Tk()
image_maker(root,get_path("Logo.png"))
windowCreater(root,'Unit Convertor')
titleCreator(root,"Unit Convertor")

OptionFrame=Frame(root,bg="orange",border=8,relief=RIDGE)
OptionLabel=Label(OptionFrame,text="Select from below:-",font="compact 12 bold",padx=5,fg="blue",bg="orange")
OptionFrame.pack(side=BOTTOM,padx=120,pady=50,fill=X)
OptionLabel.pack(side=TOP,pady=20,padx=15)

ButtonFrame=Frame(OptionFrame,bg="maroon1",border=8,relief=RIDGE)

ButtonMaker(ButtonFrame,"1.Weight",Weight)
ButtonMaker(ButtonFrame,"2.Length",Length)
ButtonMaker(ButtonFrame,"3.Volume",Volume)

ButtonFrame.pack(side=TOP,padx=20,pady=20,fill=BOTH,anchor=W)

root.mainloop()