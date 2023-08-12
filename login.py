from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("login")
root.geometry('350x500')
root.config(background='#0096DC')


img=Image.open('Flipkart-Emblem.png')
resized_img=img.resize((70,70))
img=ImageTk.PhotoImage(resized_img)
img_label= Label(root,image=img)
img_label.pack(pady=(10,10))



text_label=Label(root,text='Flipkart' ,fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))


email_label = Label(root,text="Enter Email",fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label = Label(root,text="Enter Password",fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root,text='Login Here',fg='#242020',bg='white',width=15,height=1)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',14))


root.mainloop()