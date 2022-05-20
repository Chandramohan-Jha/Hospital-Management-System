from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital")
        self.root.geometry("1550x795+0+0")

        self.B_Ground = ImageTk.PhotoImage(file = "images/image1.jpg")
        lbl_backgroung = Label(self.root, image = self.B_Ground)
        lbl_backgroung.place(x =0, y=0)


        title = Label(self.root, text="Hospital Management System", font = ("times new roman", 40, "bold"), bg = "black", fg = "red", bd = 10, relief = "sunken")
        title.pack(side = TOP, fill = X)
        

    

        self.PatientId_var = StringVar()
        self.PatientName_var = StringVar()
        self.PatientEmail_var = StringVar()
        self.PatientGender_var = StringVar()
        self.PatientContact_var = StringVar()
        self.PatientDob_var = StringVar()
        self.SearchBy_var = StringVar()
        self.SearchValve_Var = StringVar()
        
        
# ==========================Frame 1=====================================
        Frame1 = Frame(self.root, bd=4, relief = "sunken", bg="#773030")
        Frame1.place(x=25, y=100, width=500, height=680)



        m_title = Label(Frame1, text="Manage Patient", bg ="#773030", fg="black", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady = 20)


    #  PatientId
        PatientId = Label(Frame1, text="Patient Id", bg ="#773030", fg="black", font=("times new roman", 20, "bold"))
        PatientId.grid(row=1, column=0, pady = 10, padx =20, sticky="w")

        txt_PatientId = Entry(Frame1, font=("times new roman", 15), bd = 5, relief = "sunken", textvariable=self.PatientId_var)
        txt_PatientId.grid(row=1, column=1, pady = 10, padx =20, sticky="w")


    #  PatientName
        PatientName = Label(Frame1, text="Patient Name", bg ="#773030", fg="black", font=("times new roman", 20, "bold"))
        PatientName.grid(row=2, column=0, pady = 10, padx =20, sticky="w")

        txt_PatientName = Entry(Frame1, font=("times new roman", 15), bd = 5, relief = "sunken", textvariable = self.PatientName_var)
        txt_PatientName.grid(row=2, column=1, pady = 10, padx =20, sticky="w")


    #  PatientEmail
        PatientEmail = Label(Frame1, text="Patient Email", bg ="#773030", fg="black", font=("times new roman", 20, "bold"))
        PatientEmail.grid(row=3, column=0, pady = 10, padx =20, sticky="w")

        txt_PatientEmail = Entry(Frame1, font=("times new roman", 15), bd = 5, relief = "sunken", textvariable = self.PatientEmail_var)
        txt_PatientEmail.grid(row=3, column=1, pady = 10, padx =20, sticky="w")


    #  PatientGender
        PatientGender = Label(Frame1, text="Patient Gender", bg ="#773030", fg="black", font=("times new roman", 20, "bold"))
        PatientGender.grid(row=4, column=0, pady = 10, padx =20, sticky="w")

        txt_PatientGender = ttk.Combobox(Frame1, font=("times new roman", 15), state='readonly', textvariable=self.PatientGender_var)
        txt_PatientGender['values'] = ('Male', 'Female', 'Others')
        txt_PatientGender.grid(row=4, column=1, pady = 10, padx =20, sticky="w")


    #  PatientContact
        PatientContact = Label(Frame1, text="Patient Contact", bg ="#773030", fg="black", font=("times new roman", 20, "bold"))
        PatientContact.grid(row=5, column=0, pady = 10, padx =20, sticky="w")

        txt_PatientContact = Entry(Frame1, font=("times new roman", 15), bd = 5, relief = "sunken", textvariable = self.PatientContact_var)
        txt_PatientContact.grid(row=5, column=1, pady = 10, padx =20, sticky="w")


    #  PatientDOB
        PatientDOB = Label(Frame1, text="Patient D.O.B", bg ="#773030", fg="black", font=("times new roman", 20, "bold"))
        PatientDOB.grid(row=6, column=0, pady = 10, padx =20, sticky="w")

        txt_PatientDOB = Entry(Frame1, font=("times new roman", 15), bd = 5, relief = "sunken", textvariable = self.PatientDob_var)
        txt_PatientDOB.grid(row=6, column=1, pady = 10, padx =20, sticky="w")


    #  PatientAddress
        PatientAddress = Label(Frame1, text="Patient Address", bg ="#773030", fg="black", font=("times new roman", 20, "bold"))
        PatientAddress.grid(row=7, column=0, pady = 10, padx =20, sticky="w")

        self.txt_PatientAddress = Text(Frame1, width = 20, height = 3, font=("times new roman", 15), bd = 5, relief = "sunken")
        self.txt_PatientAddress.grid(row=7, column=1, pady = 10, padx =20, sticky="w")


# ====================Button 
        BtnFrame = Frame(Frame1, bd=4, relief = "sunken", bg="#773030")
        BtnFrame.place(x=30, y=600, width=430, height=50)

        AddButton = Button(BtnFrame, text="Add", width=10, command=self.add_patient).grid(row=0, column=0, padx=10, pady=5)
        UpdateButton = Button(BtnFrame, text="Update", width=10, command=self.update_dta).grid(row=0, column=1, padx=5, pady=5)
        DeleteButton = Button(BtnFrame, text="Delete", width=10, command=self.delete_dta).grid(row=0, column=2, padx=5, pady=5)
        ClearButton = Button(BtnFrame, text="Clear", width=10, command=self.cleardata).grid(row=0, column=3, padx=10, pady=5)
        
        


# ==========================Frame 2=====================================

        Frame2 = Frame(self.root, bd=4, relief = "sunken", bg="#773030")
        Frame2.place(x=570, y=100, width=940, height=680)


        PatientSearch = Label(Frame2, text="Search Patient By", bg ="#773030", fg="black", font=("times new roman", 20, "bold"))
        PatientSearch.grid(row=0, column=0, pady = 10, padx =20, sticky="w")

        txt_PatientSearch = ttk.Combobox(Frame2, width = 8, font=("times new roman", 15), state='readonly', textvariable=self.SearchBy_var)
        txt_PatientSearch['values'] = ('id', 'name', 'contact')
        txt_PatientSearch.grid(row=0, column=1, pady = 10, padx =10, sticky="w")

        txt_SearchValue = Entry(Frame2, font=("times new roman", 15), bd = 5, relief = "sunken", textvariable=self.SearchValve_Var)
        txt_SearchValue.grid(row=0, column=2, pady = 10, padx =10, sticky="w")

        ShowButton = Button(Frame2, text="Show", width=10, command=self.search_dta).grid(row=0, column=3, padx=10, pady=5)
        ShowallButton = Button(Frame2, text="Showall", width=10, command=self.fetch_patient).grid(row=0, column=4, padx=10, pady=5)


        #=============Table==============
        Table_Frame = Frame(Frame2, bd=4, relief = "ridge", bg="#773030")
        Table_Frame.place(x=10, y=70, width=900, height=580)

        scroll_X = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_Y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.PatientTable = ttk.Treeview(Table_Frame, columns = ('id', 'name', 'email', 'gender', 'contact', 'dob', 'address'), xscrollcommand=scroll_X.set, yscrollcommand=scroll_Y.set)
        scroll_X.pack(side = BOTTOM, fill = X)
        scroll_Y.pack(side = RIGHT, fill = Y)
        scroll_X.config(command=self.PatientTable.xview)
        scroll_Y.config(command=self.PatientTable.yview)

        self.PatientTable.heading("id", text="Patient Id")
        self.PatientTable.heading("name", text="Patient Name")
        self.PatientTable.heading("email", text="Patient Email")
        self.PatientTable.heading("gender", text="Patient Gender")
        self.PatientTable.heading("contact", text="Patient Contact")
        self.PatientTable.heading("dob", text="Patient DOB")
        self.PatientTable.heading("address", text="Patient Address")

        self.PatientTable['show'] = 'headings'

        self.PatientTable.column('id', width=70)
        self.PatientTable.column('name', width=130)
        self.PatientTable.column('email', width=140)
        self.PatientTable.column('gender', width=120)
        self.PatientTable.column('contact', width=130)
        self.PatientTable.column('dob', width=130)
        self.PatientTable.column('address', width=150)

        self.PatientTable.pack(fill = BOTH, expand = 1)
        self.PatientTable.bind('<ButtonRelease-1>', self.fetch_Frame1)
        self.fetch_patient()


       


    def add_patient(self):
        if self.PatientId_var.get()=="" or self.PatientName_var.get()=="" or self.PatientGender_var.get=="":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            con = pymysql.Connect(host = 'localhost', user = 'root', password = "admin", database = 'hms')
            cur = con.cursor()
            cur.execute("insert into hospital values(%s, %s, %s, %s, %s, %s, %s)", (self.PatientId_var.get(), self.PatientName_var.get(), self.PatientEmail_var.get(), self.PatientGender_var.get(), self.PatientContact_var.get(), self.PatientDob_var.get(), self.txt_PatientAddress.get('1.0', END)))

            con.commit()
            self.fetch_patient()
            self.cleardata()
            con.close()
            messagebox.showinfo("Sucess", "Record Submitted")


    def fetch_patient(self):
        con = pymysql.Connect(host = 'localhost', user = 'root', password = "admin", database = 'hms')
        cur = con.cursor()
        cur.execute("select * from hospital")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.PatientTable.delete(*self.PatientTable.get_children())
            for row in rows:
                self.PatientTable.insert('', END, values=row)
            con.commit()
        con.close()


    def cleardata(self):
        self.PatientId_var.set("")
        self.PatientName_var.set("")
        self.PatientEmail_var.set("")
        self.PatientGender_var.set("")
        self.PatientContact_var.set("")
        self.PatientDob_var.set("")
        self.txt_PatientAddress.delete('1.0', END)


    def fetch_Frame1(self, ev):
        get_fetch = self.PatientTable.focus()
        content = self.PatientTable.item(get_fetch)
        row = content['values']
        self.PatientId_var.set(row[0])
        self.PatientName_var.set(row[1])
        self.PatientEmail_var.set(row[2])
        self.PatientGender_var.set(row[3])
        self.PatientContact_var.set(row[4])
        self.PatientDob_var.set(row[5])
        self.txt_PatientAddress.delete('1.0', END)
        self.txt_PatientAddress.insert(END, row[6])
        

    def update_dta(self):
        con = pymysql.Connect(host = 'localhost', user = 'root', password = "admin", database = 'hms')
        cur = con.cursor()
        cur.execute("update hospital set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where id=%s", (self.PatientName_var.get(), self.PatientEmail_var.get(), self.PatientGender_var.get(), self.PatientContact_var.get(), self.PatientDob_var.get(), self.txt_PatientAddress.get('1.0', END), self.PatientId_var.get()))
        con.commit()
        self.fetch_patient()
        self.cleardata()
        con.close()

# 'id', 'name',  email', 'gender', 'contact', 'dob', 'address'

    def delete_dta(self):
        con = pymysql.Connect(host = 'localhost', user = 'root', password = "admin", database = 'hms')
        cur = con.cursor()
        cur.execute("delete from hospital where id=%s", self.PatientId_var.get())
        con.commit()
        con.close()
        self.fetch_patient()
        self.cleardata()


    def search_dta(self):
        con = pymysql.Connect(host = 'localhost', user = 'root', password = "admin", database = 'hms')
        cur = con.cursor()
        cur.execute("select * from hospital where "+str(self.SearchBy_var.get())+" LIKE '%"+str(self.SearchValve_Var.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.PatientTable.delete(*self.PatientTable.get_children())
            for row in rows:
                self.PatientTable.insert('', END, values=row)
            con.commit()
        con.close()




root = Tk()
obj = MainWindow(root)
root.mainloop()