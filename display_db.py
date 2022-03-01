#importing required modules
import sqlite3
from tkinter import *
import main

class display:
    def __init__(self, root):
        #adding gui properties        
        self.root = root
        pad = 3
        self.root.title("Patient Details")
        self.root.geometry("1200x700+320+120")

        #creating frame and adding title
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        left = Frame(self.root, relief="solid")
        left.pack(side="left")

        right = Frame(self.root, relief="solid")
        right.pack(side="left")

        # creating title
        self.label = Label(top, font=('arial', 50, 'bold'), text="Patient Details", fg="#15d3ba", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # creating fname heading
        self.fname_label = Label(left, font=('arial', 20, 'bold'), text="Name", fg="#15d3ba", anchor="center")
        self.fname_label.grid(row=0, column=1, padx=10, pady=10) 

        # creating mobile no heading
        self.mobile_label = Label(right, font=('arial', 20, 'bold'), text="Mobile No.", fg="#15d3ba", anchor="center")
        self.mobile_label.grid(row=0, column=1, padx=10, pady=10)

        # fname showing entry field
        self.fname_entry = Text(left, height=30, width=70)
        self.fname_entry.grid(row=1, column=1, padx=10, pady=10)

        # mobile no  showing entry field
        self.mobile_entry = Text(right, height=30, width=70)
        self.mobile_entry.grid(row=1, column=1, padx=10, pady=10)

        # creating home button
        self.home_button = Button(top, text="Home", font=('arial', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15,fg="black", anchor="center", command=main.hms_ui)
        self.home_button.grid(row=8, column=3, padx=10, pady=10)

        def display_info():
            conn = sqlite3.connect('Hospital.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS dbms_patient(fname TEXT,lname TEXT,address TEXT,mobile_no NUMBER, fees NUMBER)')
            conn.commit()
            with conn:
                cursor.execute("SELECT fname FROM dbms_patient")
                ans = cursor.fetchall()
                for i in ans:
                    self.fname_entry.insert(INSERT, i[0] + '\n')

            with conn:
                cursor.execute("SELECT mobile_no FROM dbms_patient")
                ans = cursor.fetchall()
                for i in ans:
                    self.mobile_entry.insert(INSERT, str(i[0]) + '\n')        

        # creating display button
        self.display_button = Button(top, text="Display", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15,fg="black", anchor="center", command=display_info)
        self.display_button.grid(row=8, column=4, padx=10, pady=10)


def patient_display():
    root = Tk()
    application = display(root)
    root.mainloop()