import tkinter
import PIL
from PIL import Image,ImageTk
root=tkinter.Tk()
import tkinter.messagebox as MessageBox
#function
#BLL
def btn_click():
    email=var_email.get()
    password=var_password.get()
    MessageBox.showinfo("Insert Status","Username and Password are successfully login")
    print("Email:",email,"Password:",password)
root.title("LOGIN FORM")
# label_1=tkinter.Label(text="Welcome to Login Form!!!!!")
# label_1.grid()

root.configure(bg="green")
img_load=Image.open("login677.png")
img_load=img_load.resize((root.winfo_screenwidth(),root.winfo_screenheight()),Image.ANTIALIAS)
img=ImageTk.PhotoImage(img_load)
label_2=tkinter.Label(master=root,image=img)
label_2.pack(side='top',expand=True,fill='both')
label_3=tkinter.Label(master=label_2,text="Username",font=('Calibri',40,'bold'),relief='solid')
label_3.grid(row=0,column=20,ipadx=10,ipady=10)
label_4=tkinter.Label(master=label_2,text="Password",font=('Calibri',40,'bold'),relief='solid')
label_4.grid(row=1,column=20,ipadx=10,ipady=10)
var_email=tkinter.StringVar()
txt_1=tkinter.Entry(master=label_2,textvariable=var_email)
txt_1.grid(row=0,column=22)
var_password=tkinter.StringVar()
txt_2=tkinter.Entry(master=label_2,textvariable=var_password)
txt_2.grid(row=1,column=22)
btn_login=tkinter.Button(master=label_2,text="Login",bg="yellow",font=('Calibri',20,'bold'),relief='sunken',command=btn_click,width=50)
btn_login.grid(row=10,column=24,padx=10,pady=10)
root.mainloop()