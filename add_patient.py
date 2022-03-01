#importing required modules
import sqlite3
from tkinter import *
from tkinter import messagebox
import main

class add:
    def __init__(self, root):
        #adding gui properties        
        self.root = root
        pad = 3
        self.root.title("Add Patient")
        self.root.geometry("1200x700+320+120")


        self.top = LabelFrame(self.root)
        self.top.pack(side="top")

        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")

        self.checkbox = Frame(self.root)
        self.checkbox.pack(side="top")

        # display Title
        self.label = Label(self.top, font=('arial', 50, 'bold'), text="Add Patient", fg="#15d3ba", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        #fname label
        self.fname_label = Label(self.bottom, font=('arial', 20, 'bold'), text="FIRST NAME :", fg="#15d3ba",anchor="w")
        self.fname_label.grid(row=0, column=2, padx=10, pady=10)
        self.fname_var = StringVar()

        # fname entry field
        self.fname_entry = Entry(self.bottom, width=50, textvar=self.fname_var)
        self.fname_entry.grid(row=0, column=3, padx=10, pady=10)

        #lname label
        self.lname_label = Label(self.bottom, font=('arial', 20, 'bold'), text="LAST NAME :", fg="#15d3ba",anchor="w")
        self.lname_label.grid(row=1, column=2, padx=10, pady=10)
        self.lname_var = StringVar()

        # lname entry field field
        self.lname_entry = Entry(self.bottom, width=50, textvar=self.lname_var)
        self.lname_entry.grid(row=1, column=3, padx=10, pady=10)


        # address label
        self.address_label = Label(self.bottom, font=('arial', 20, 'bold'), text="ADDRESS :", fg="#15d3ba",anchor="w")
        self.address_label.grid(row=2, column=2, padx=10, pady=10)

        # address entry field
        self.address_var = StringVar()
        self.address_entry = Entry(self.bottom, width=50, textvar=self.address_var)
        self.address_entry.grid(row=2, column=3, padx=10, pady=10)

        # mobile no label
        self.mobile_label = Label(self.bottom, font=('arial', 20, 'bold'), text="MOBILE NUMBER :",fg="#15d3ba",anchor="w")
        self.mobile_label.grid(row=3, column=2, padx=10, pady=10)

        # mobile no entry field
        self.mobile_var = IntVar()
        self.mobile_entry = Entry(self.bottom, width=50, text=self.mobile_var)
        self.mobile_entry.grid(row=3, column=3, padx=10, pady=10)

        # fees charged Label
        self.fees_label = Label(self.bottom, font=('arial', 20, 'bold'), text="FEES :",fg="#15d3ba",anchor="w")
        self.fees_label.grid(row=4, column=2, padx=10, pady=10)

        # fees entry field
        self.fees_var = IntVar()
        self.fees_entry = Entry(self.bottom, width=50, text=self.fees_var)
        self.fees_entry.grid(row=4, column=3, padx=10, pady=10)

        def submit_info():
            global ans
            fname = self.fname_entry.get()
            lname = self.lname_entry.get()
            address = self.address_entry.get()
            fees = self.fees_entry.get()

            while True:
                self.h = str(self.mobile_entry.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    mobile = self.h
                    ans = TRUE
                    break
                else:
                    ans = False
                    messagebox.showerror("Error", "Please Enter 10 Digit Mobile Number")
                    break

            if ans == TRUE :
                conn = sqlite3.connect('Hospital.db')
                with conn:
                    cursor = conn.cursor()
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS dbms_patient(fname TEXT,lname TEXT,address TEXT,mobile_no NUMBER, fees NUMBER)')
                cursor.execute('INSERT INTO dbms_patient(fname,lname,address,mobile_no,fees) '
                               'VALUES(?,?,?,?,?)', (fname,lname,address,mobile,fees))
                conn.commit()
                with conn:
                    cursor.execute("SELECT * FROM dbms_patient")
                    print(cursor.fetchall())
           
            self.fname_var.set('')
            self.lname_var.set('')
            self.address_var.set('')
            self.mobile_var.set('')
            self.fees_var.set('')
            
#creating reset button
        def reset():
            
            self.fname_entry.delete(0, END)
            self.fname_entry.insert(0, "")

            self.lname_entry.delete(0, END)
            self.lname_entry.insert(0, "")

            self.mobile_entry.delete(0, END)
            self.mobile_entry.insert(0, "")

            self.address_entry.delete(0, END)
            self.address_entry.insert(0, "")

            self.fees_entry.delete(0, END)
            self.fees_entry.insert(0, "")

# creating submit button
        self.submit_button = Button(self.checkbox, text="SUBMIT", font=('arial', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15,fg="black", anchor="center", command=submit_info)
        self.submit_button.grid(row=5, column=1, padx=10, pady=10)

# creating back to home page button

        self.back_home_button = Button(self.checkbox, text="HOME", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2,width=15,fg="black", anchor="center", command=main.hms_ui)
        self.back_home_button.grid(row=5, column=2, padx=10, pady=10)

        Button(self.checkbox, text="reset", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15, fg="black",anchor="center", command=reset).grid(row=5, column=3)


def add_patient_ui():
    root = Tk()
    application = add(root)
    root.mainloop()

