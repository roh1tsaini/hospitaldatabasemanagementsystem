#importing required modules
from tkinter import *
import add_patient #importing add_patient.py
import display_db #importing display_db.py

#creating class
class Hospital:
    def __init__(self,root):
        #adding gui properties 
        self.root = root
        self.root.title("Hospital Management System by Rohit Saini")
        self.root.geometry("1000x500+320+120")
        self.root.config(bg="#071A52")

        #creating frame and adding title
        top = Frame(self.root)
        top.pack(side="top")
        self.label = Label(top, font=('arial', 50, 'bold'),text="Hospital Management System", fg="#D82148",bg="#071A52", anchor="center")
        self.label.grid(row=0, column=3)        

        #creating frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        #creating add patient button
        self.add_patient = Button(bottom, text="Add Patient", font=('arial', 20), bg="#D82148", height=2,width=50,fg="#151D3B", anchor="center",command=add_patient.add_patient_ui)
        self.add_patient.grid(row=0, column=2, padx=10, pady=10)


        # create display patient Button
        self.show_patient = Button(bottom, text="Display Patient", font=('arial', 20), bg="#D82148",relief=RIDGE,height=2, width=50, fg="#151D3B", anchor="center",command=display_db.patient_display)        
        self.show_patient.grid(row=1, column=2, padx=10, pady=10)

        # exit button
        self.exit_button = Button(bottom,text="Exit",font=('arial',20),bg="#D82148",relief=RIDGE,height=2,width=50,fg="#151D3B",anchor="center",command=quit)
        self.exit_button.grid(row=2, column=2, padx=10, pady=10)

def hms_ui():
    root = Tk()
    application = Hospital(root)
    root.mainloop()

if __name__ == '__main__':
    hms_ui()

