from tkinter import*
import math


root=Tk()
blank_space=""
root.title(50 * blank_space + "Calculator Develop By Vicky ")
root.resizable(width=FALSE, height=False)
root.geometry("438x500+460+40")


# boder in the first line =====================
converFrame= Frame(root,bd=20,pady=2,bg="orange",relief=RIDGE)
converFrame.grid()


# Boder in the Second Line =================
convermainFrame= Frame(converFrame,bd=10,pady=2,bg="yellow",relief=RIDGE)
convermainFrame.grid()

# box ke under ka boder in the red line =================================================
mainFrame= Frame(convermainFrame,bd=5,pady=2,bg="red",relief=RIDGE)
mainFrame.grid()

class calculater():
    def __init__(self): 
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False


# Button per number System jin the Working In number ( Number per likha huaa number ko press karne per enter number ka system hat )========================================

    def number_Enter(self,num):
        self.result=False
        firstnum=entry_Display.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum==".":
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)

    def display(self,value):
        entry_Display.delete(0,END)
        entry_Display.insert(0,value)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(entry_Display.get())

    def valid_function(self):
        if self.op=="Add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="mul":
            self.total *=self.current
        if self.op=="div":
            self.total /=self.current
        if self.op =="mod":
            self.total %=self.current

        self.input_value=True
        self.check_sum=False
        self.display(self.total)


    def operation(self,op):
        self.current= float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

# backspace  function system in bacnkig=====================================

    def backspace(self): 
        numLen=len(entry_Display.get())
        entry_Display.delete(numLen -1, 'end')
        if numLen==1:
            entry_Display.insert(0,'0')

# Clear function system in bacnkig========================================================

    def Clear_entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True

# all clear  function system in bacnkig========================================================


    def all_Clear_entry(self):
        self.Clear_entry()
        self.total=0
# mathspm function system in bacnkig========================================================


    def mathsPm(self):
        self.result=False
        self.current=-(float(entry_Display.get()))
        self.display(self.current)

# squared  function system in bacnkig========================================================

    def squared(self):
        self.result=False
        self.current= math.sqrt(float(entry_Display.get()))
        self.display(self.current)




            

# output box in the ++++++++++++++++++++++++++++++++++++++++===========
added_value=calculater()        
entry_Display=Entry(mainFrame,font=("arial",18,"bold"),bd=14,width=26,bg='green',justify=RIGHT)
entry_Display.grid(row=0,column=0,columnspan=4,pady=1)
entry_Display.insert(0,"0")

# number box ka code hai ======================================
numpad="789456123"
i=0
btn=[]

for j in range(3,6):
    for k in range(3):
        btn.append(Button(mainFrame,width=6,height=2,bg="red",font=("arial",16,"bold"),bd=4,text=numpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x=numpad[i]:added_value.number_Enter(x)
        i+=1


# ==============Symbol button ==========================================================

btn_Back_Space=Button(mainFrame,width=6,height=2,command=added_value.backspace,font=("arial",16,"bold"),bd=4,text="<-",bg="cadetblue")        
btn_Back_Space.grid(row=1,column=0,pady=1)



btn_clear=Button(mainFrame,width=6,height=2,command=added_value.Clear_entry,font=("arial",16,"bold"),bd=4,text=chr(67),bg="cadetblue")        
btn_clear.grid(row=1,column=1,pady=1)


btn_clear_all=Button(mainFrame,width=6,height=2,command=added_value.all_Clear_entry,font=("arial",16,"bold"),bd=4,text=chr(67)+chr(69),bg="cadetblue")        
btn_clear_all.grid(row=1,column=2,pady=1)


btn_PM=Button(mainFrame,width=6,height=2,command=added_value.mathsPm,font=("arial",16,"bold"),bd=4,text=chr(177),bg="cadetblue")        
btn_PM.grid(row=1,column=3,pady=1)





#==================scientific================================================================

btn_Add=Button(mainFrame,width=6,height=2,font=("arial",16,"bold"),bd=4,text="+",bg="Cadet blue",command=lambda:added_value.operation("Add"))
btn_Add.grid(row=3,column=3,pady=1)

btn_sub=Button(mainFrame,width=6,height=2,font=("arial",16,"bold"),bd=4,text="-",bg="cadet blue",command=lambda:added_value.operation("sub"))
btn_sub.grid(row=4,column=3,pady=2)

btn_mul=Button(mainFrame,width=6,height=2,font=("arial",16,"bold"),bg="cadet blue",bd=4,text="*",command=lambda:added_value.operation("mul"))
btn_mul.grid(row=5,column=3,pady=1)

btn_Div=Button(mainFrame,width=6,height=2,font=("arial",16,"bold"),bd=4,text=chr(247),bg="cadet blue",command=lambda:added_value.operation("div"))
btn_Div.grid(row=6,column=3,pady=1)


btn_Zero=Button(mainFrame,width=6,height=2,font=("arial",16,"bold"),bd=4,text="0",bg="cadet blue",command=lambda:added_value.number_Enter(0))
btn_Zero.grid(row=6,column=0,pady=1)

btn_Dot=Button(mainFrame,width=6,height=2,font=("arial",16,"bold"),bd=4,text=".",bg="cadet blue",command=lambda:added_value.number_Enter("."))
btn_Dot.grid(row=6,column=1,pady=1)

btn_Equal=Button(mainFrame,width=6,height=2,font=("arial",16,"bold"),bd=4,text="=",bg="cadet blue",command=added_value.sum_of_total)
btn_Equal.grid(row=6,column=2,pady=1)









root.mainloop()

