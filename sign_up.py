from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import psycopg2 as pg

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All fields should be filled')
    elif  passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password doesnt match')
    else:
        try:
            conn=pg.connect(host='localhost',database='EliteMarket', port='5432', user='postgres', password='1234560')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established')
            return

        mycursor = conn.cursor()
        query='Select * from userdata where email = %s'
        mycursor.execute(query, (emailEntry.get(),))
        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Email Already Exists')
        else:
            query = 'INSERT INTO userdata(email, username, password) VALUES (%s, %s, %s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Succes', 'Registration is successful')
            clear()
            signup_window.destroy()
            import signin

def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()
signup_window.geometry('1900x1000+50+50')
signup_window.title('Signin Window')


background=ImageTk.PhotoImage(file='Дизайн без названия (6).png')

bgLabel=Label(signup_window, image=background)
bgLabel.grid()

frame=Frame(signup_window, width=50, height=20, bg='#40e0d0')
frame.place(x=850, y=200)

heading=Label(signup_window, text='Create an account', font=('Times New Roman', 23, 'bold'), bg='white', fg='#57a1f8')
heading.place(x=900, y=120)

emailLabel=Label(frame, text='Email', font=('Times New Roman', 16, 'bold'), bg='white', fg='#57a1f8')
emailLabel.grid(row=1, column=0, sticky='w', padx=10)

emailEntry=Entry(frame, width=30,  font=('Times New Roman', 16, 'bold'))
emailEntry.grid(row=2, column=0, sticky='w', padx=10)

usernameLabel=Label(frame, text='Username', font=('Times New Roman', 16, 'bold'), bg='white', fg='#57a1f8')
usernameLabel.grid(row=3, column=0, sticky='w',  padx=10)

usernameEntry=Entry(frame, width=30,  font=('Times New Roman', 16, 'bold'))
usernameEntry.grid(row=4, column=0, sticky='w',  padx=10)

passwordLabel=Label(frame, text='Password', font=('Times New Roman', 16, 'bold'), bg='white', fg='#57a1f8')
passwordLabel.grid(row=5, column=0, sticky='w',  padx=10)

passwordEntry=Entry(frame, width=30,  font=('Times New Roman', 16, 'bold'))
passwordEntry.grid(row=6, column=0, sticky='w',  padx=10)

confirmLabel=Label(frame, text='Confirm Password', font=('Times New Roman', 16, 'bold'), bg='white', fg='#57a1f8')
confirmLabel.grid(row=7, column=0, sticky='w',  padx=10)

confirmEntry=Entry(frame, width=30,  font=('Times New Roman', 16, 'bold'))
confirmEntry.grid(row=8, column=0, sticky='w',  padx=10)

signupButton=Button(frame, width=20,  text='Signup',font=('Times New Roman',15, 'bold'), bg='white', fg='#57a1f8', command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount= Label(frame,text='Already have an account?', font=('Times New Roman',14,), bg='white', fg='#57a1f8')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=20, pady=10)

loginButton=Button(frame, text='Login', font=('Times New Roman',12),
                   command=login_page, bg='white', fg='#57a1f8')
loginButton.place(x=280, y=300)

signup_window.mainloop()