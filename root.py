from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import tkinter as tk
import psycopg2 as pg

basket = []  # To store selected products

# Establish connection to the database
def create_connection():
    conn = pg.connect(
        host='localhost',
        database='EliteMarket',
        port='5432',
        user='postgres',
        password='1234560'
    )
    return conn

def signin_page():
    root.destroy()
    import signin

def fetch_product_prices():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT p_name, price_in_$ FROM products")
    prices = {row[0]: row[1] for row in cursor.fetchall()}

    conn.close()
    return prices

# Function to calculate the total price of the products in the basket
def calculate_total_price(prices):
    total_price = sum(prices.get(item[1], 0) for item in basket)
    return total_price

# Search products based on user input
def search_products():
    search_term = entry_search.get()
    conn = create_connection()
    cursor = conn.cursor()

    query = "SELECT product_id, p_name, price_in_$, quantity, p_categories FROM products WHERE p_name ILIKE %s"
    cursor.execute(query, ('%' + search_term + '%',))
    rows = cursor.fetchall()

    conn.close()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row)

# Add selected product to basket
def add_to_basket():
    selected = listbox.curselection()
    if selected:
        selected_product = listbox.get(selected)
        basket.append(selected_product)
        messagebox.showinfo("Added to Basket", f"{selected_product[1]} added to your basket.")

# Display items in the basket
def view_basket():
    basket_window = tk.Toplevel(root)
    basket_window.title("My Basket")

    basket_listbox = tk.Listbox(basket_window, width=400, height=500, bg = '#40e0d0', fg = 'black', font=("Arial", 24))
    basket_listbox.pack(padx=20, pady=20)

    for item in basket:
        basket_listbox.insert(tk.END, item)

# Buy selected product from the basket
def buy_product():
    selected = listbox.curselection()
    if selected:
        selected_product = listbox.get(selected)
        # Perform action to buy the product
        messagebox.showinfo("Purchase", f"You have bought: {selected_product[1]}")
        listbox.delete(selected)  # Remove item from the listbox
    else:
        messagebox.showwarning("No Selection", "Please select a product to buy.")

def buy_product():
    selected = listbox.curselection()
    if selected:
        selected_product = listbox.get(selected)
        basket.remove(selected_product)
        prices = fetch_product_prices()
        total_price = calculate_total_price(prices)
        messagebox.showinfo("Purchase", f"You have bought: {selected_product[1]}\nTotal Price: ${total_price}")
        listbox.delete(selected)  # Remove item from the listbox
    else:
        messagebox.showwarning("No Selection", "Please select a product to buy.")



# Log out function
def log_out():
    # Perform any necessary log out actions
    messagebox.showinfo("Logged Out", "You have been logged out.")
    root.destroy()  # Close the window or redirect to login screen

# About Us function
def about_us():
    aboutus_window = tk.Toplevel() #new windowww
    aboutus_window.title("About Us")

    img = Image.open("About us (2).png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(aboutus_window, image=photo)
    label.image = photo
    label.pack()

# Tkinter setup
root = tk.Tk()
root.title("Elite Market")
root.geometry("1900x1000+50+50")

# Background colors
frame_bg_color = "#40e0d0"
button_bg_color = "#f2faf2"
button_fg_color = "black"
button_hover_bg_color = "#f2faf2"
button_hover_fg_color = "black"
root.config(bg=frame_bg_color)

frame_search = tk.Frame(root, bg=frame_bg_color)
frame_search.place(x=500, y=20)

label_search = tk.Label(frame_search, text="Search Product:", font=("Times New Roman", 25), bg=frame_bg_color)
label_search.pack(side=tk.LEFT)

entry_search = tk.Entry(frame_search, font=("Times New Roman", 25))
entry_search.pack(side=tk.LEFT, padx=10)

button_search = tk.Button(frame_search, text="Search", command=search_products, font=("Times New Roman", 25),
                          bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                          activeforeground=button_hover_fg_color)
button_search.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=30, font=("Times New Roman", 15))
listbox.place(x=500, y=150)

img = tk.PhotoImage(file='Дизайн без названия (2).png')
save = tk.Canvas(root, width=400, height=500)
save.place(x=20, y=20)
save.create_image(200, 200, image=img)

button_add_to_basket = tk.Button(root, text="Add to Basket", command=add_to_basket, font=("Times New Roman", 25),
                                 bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                                 activeforeground=button_hover_fg_color)
button_add_to_basket.place(x=1100, y=150)

button_view_basket = tk.Button(root, text="My Basket", command=view_basket, font=("Times New Roman", 25),
                               bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                               activeforeground='black')
button_view_basket.place(x=1100, y=250)

button_buy = tk.Button(root, text="Buy", command=buy_product, font=("Times New Roman", 25),
                       bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                       activeforeground=button_hover_fg_color)
button_buy.place(x=1100, y=350)

button_about_us = tk.Button(root, text="About Us", command=about_us, font=("Times New Roman", 25),
                            bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                            activeforeground=button_hover_fg_color)
button_about_us.place(x=700, y=550)

button_log_out = tk.Button(root, text="Log Out", command=log_out, font=("Times New Roman", 25),
                           bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                           activeforeground=button_hover_fg_color)
button_log_out.place(x=900, y=550)

root.mainloop()