from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import psycopg2 as pg

bgPic = None
#funct part
def forget_pass():
    global bgPic
    def change_password():
        if email_entry.get()=='' or password_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error', 'All Fields Are Required', parent=windows)
        elif password_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'Passwords arent matching', parent=windows)
        else:
            conn = pg.connect(host='localhost', database='EliteMarket', port='5432', user='postgres', password='1234560')
            mycursor = conn.cursor()

            query = 'select * from userdata where email=%s'
            mycursor.execute(query, (email_entry.get(),))
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'User with this email doesnt exist', parent=windows)
            else:
                query='update userdata set password=%s where email=%s'
                mycursor.execute(query, (password_entry.get(), email_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Succes', 'Password is reset', parent=windows)
                windows.destroy()


    windows = Toplevel()
    windows.title('Change Password')

    bgPic= ImageTk.PhotoImage(file='Дизайн без названия (6).png')
    bg2Label = Label(windows, image=bgPic)
    bg2Label.grid()

    heading_label = Label(windows, text='RESET PASSWORD', font=('Times New Roman', 23, 'bold'), bg='white', fg='#57a1f8')
    heading_label.place(x=900, y=120)

    emailLabel = Label(windows, text='Email', font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    emailLabel.place(x=900, y=170)

    email_entry = Entry(windows, width=25, font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    email_entry.place(x=900, y=170)

    Frame(windows, width=900, height=3, bg='#40e0d0').place(x=900, y=160)

    passwordLabel = Label(windows, text='New Password', font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    passwordLabel.place(x=900, y=210)

    password_entry = Entry(windows, width=25, font=('Times New Roman', 18), bd=0,bg='white', fg='#57a1f8')
    password_entry.place(x=900, y=210)

    Frame(windows, width=900, height=3, bg='#40e0d0').place(x=900, y=200)

    confirmpassLabel = Label(windows, text='Confirm Password', font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    confirmpassLabel.place(x=900, y=250)

    confirmpass_entry=Entry(windows, width=25, font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    confirmpass_entry.place(x=900, y=250)

    Frame(windows, width=350, height=3, bg='#40e0d0').place(x=850, y=260)

    submitButton = Button(windows, text='Submit',font=('Times New Roman', 20),
                        bg='white', fg='#57a1f8', cursor='hand2', bd=0, width=15, command=change_password)
    submitButton.place(x=900, y=290)

def login_user():
    if usernameEntry.get() == 'saya.juz40@gmail.com' and passwordEntry.get() == '1234':
        root()
    else:
        if usernameEntry.get()=='' or passwordEntry.get()=='':
             messagebox.showerror('Error', 'All fields are required to fill')

        else:
         try:
             conn = pg.connect(host='localhost', database='EliteMarket', port='5432', user='postgres', password='1234560')
             mycursor=conn.cursor()
             pass
         except:
             messagebox.showerror('Error', 'Connection is not established')
             return

         mycursor = conn.cursor()
         query='Select * from userdata where username=%s and passwordd=%s'
         mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
         row=mycursor.fetchone()
         if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
         else:
            root()


def root():
    login_window.destroy()
    import root

def signup_page():
    login_window.destroy()
    import sign_up

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0, END)

#main part
login_window = Tk()
login_window.geometry('1900x1000+50+50')
login_window.resizable(1,1)
login_window.title('Login page')

bgImage = ImageTk.PhotoImage(file='Дизайн без названия (6).png')

bgLabel=Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)


heading=Label(login_window, text='User login', font=('Times New Roman',40, 'bold'), bg='white', fg='#57a1f8')
heading.place(x=900,y=100)

usernameEntry = Entry(login_window, width=25, font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
usernameEntry.place(x=900, y=180)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

frame1 =Frame(login_window, width=300, height=3, bg='#40e0d0')
frame1.place(x=900, y=180)

passwordEntry = Entry(login_window, width=25, font=('Times New Roman', 18), bd=0 ,bg='white', fg='#57a1f8')
passwordEntry.place(x=900, y=230)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)


frame2 =Frame(login_window, width=300, height=3, bg='#40e0d0')
frame2.place(x=900, y=230)

forgetButton =Button(login_window,text='Forget password?', bd=0, bg='white', fg='#57a1f8',
                      cursor='hand2', font=('Times New Roman', 14, 'underline'), command=forget_pass)
forgetButton.place(x=1000, y=260)

loginButton= Button(login_window, text='Login', font=('Times New Roman Sans', 20, 'bold'),
                    bg='white', fg='#57a1f8', cursor='hand2', bd=0, width=15, command=login_user)
loginButton.place(x=900 , y=300)

newaccountButton=Button(login_window, text='Create an account',font=('Times New Roman', 14, 'underline'),
                    bg='white', fg='#57a1f8', cursor='hand2', bd=0, width=20, command=signup_page)
newaccountButton.place(x=920, y=360)


login_window.mainloop()