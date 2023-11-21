from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

        #============================================Variable==============================================
        self.var_ref=StringVar() 
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar() 
        self.var_gender=StringVar()

        self.var_post=StringVar() 
        self.var_mobile=StringVar()
        self.var_email=StringVar() 
        self.var_nationality=StringVar() 
        self.var_adderss=StringVar() 
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

        # Title label
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 40, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=140, width=1295, height=50)

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Customer Reference
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0)
        enty_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=22, font=("times new roman", 13, "bold"), state="readonly")
        enty_ref.grid(row=0, column=1)

        # Customer Name
        cname = Label(labelframeleft, font=("arial", 12, "bold"), text="Customer Name: ", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name ,font=("arial", 13, "bold"), width=29)
        txtcname.grid(row=1, column=1)

        # Mother Name
        lblmname = Label(labelframeleft, font=("arial", 12, "bold"), text="Mother Name: ", padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_mother, font=("arial", 13, "bold"), width=29)
        txtmname.grid(row=2, column=1)

        # Gender ComboBox
        label_gender = Label(labelframeleft, font=("arial", 12, "bold"), text="Gender: ", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state='readonly')
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Postcode
        lblPostCode = Label(labelframeleft, font=("arial", 12, "bold"), text="PostCode: ", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft,textvariable=self.var_post, font=("arial", 13, "bold"), width=29)
        txtPostCode.grid(row=4, column=1)

        # Mobile Number
        lblMobile = Label(labelframeleft, font=("arial", 12, "bold"), text="Mobile: ", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=5, column=1)

        # Email
        lblEmail = Label(labelframeleft, font=("arial", 12, "bold"), text="Email: ", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft,textvariable=self.var_email, font=("arial", 13, "bold"), width=29)
        txtEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(labelframeleft, font=("arial", 12, "bold"), text="Nationality: ", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_Nationality["values"] = ("Indian", "American", "British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # Id Proof Type ComboBox
        lblIdProof = Label(labelframeleft, font=("arial", 12, "bold"), text="Id Proof Type: ", padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)
        combo_id = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_id["values"] = ("AdharCard", "Driving Licence", "Passport")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # Id Number
        lblIdNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="Id Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_id_number, font=("arial", 13, "bold"), width=29)
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, font=("arial", 12, "bold"), text="Address: ", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft,textvariable=self.var_adderss, font=("arial", 13, "bold"), width=29)
        txtAddress.grid(row=10, column=1)


        # =======================btns======= ======
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412, height=40)

        btnAdd=Button (btn_frame, text="Add",command=self.add_data ,font=("arial", 11, "bold"), bg="black", fg="gold",width=10)
        btnAdd.grid (row=0,column=0, padx=1)

        btnUpadate=Button (btn_frame, text="Update", font=("arial", 11, "bold"), bg="black", fg="gold",width=10)
        btnUpadate.grid (row=0, column=1, padx=1)

        btnDelete=Button (btn_frame, text="Delete", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid (row=0, column=2, padx=1)

        btnReset=Button (btn_frame, text="Reset", command= self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

    # =================tabel frame========================
        
      # =================tabel frame========================

        Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="VIew Deatils And Seaarch System", font=("arial", 12, "bold"))
        Table_Frame.place(x=435, y=50, width=860,height=490)
        lb1SearchBy=Label (Table_Frame, font=("arial", 12, "bold"), text="Search By: ", bg="red",fg="white")
        lb1SearchBy.grid (row=0, column=0, sticky=W)

        self.search_var=StringVar()
        combo_Serach=ttk. Combobox (Table_Frame, textvariable= self.search_var, font=("arial", 12, "bold"), width=27,state="readonly")
        combo_Serach ["value"]=("Mobile","Ref")
        combo_Serach. current (0)
        combo_Serach.grid(row=0, column=1)
      
        self.txt_search=StringVar()
        txtSearch=ttk. Entry (Table_Frame,textvariable=self.txt_search, font=("arial", 13, "bold"),width=24) 
        txtSearch.grid (row=0, column=2, padx=2)

        btnSearch=Button (Table_Frame, text="Search", command=self.search, font=("arial",11, "bold"), bg="black", fg="gold",width=10) 
        btnSearch.grid (row=0, column=3, padx=1)
        btnShowA11=Button (Table_Frame, text="Show All",command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold",width=10) 
        btnShowA11.grid(row=0, column=4, padx=1)


        # ==================Show data Table===================
        details_table=Frame (Table_Frame, bd=2, relief=RIDGE) 
        details_table.place(x=0, y=50,width=860,height=350)
        scroll_x=ttk.Scrollbar (details_table, orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar (details_table, orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table, column=("ref", "name", "mother", "gender","post", "mobile", 
                                                                  "email","nationality","idproof", "idnumber","address"), xscrollcommand=scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview) 
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self. Cust_Details_Table.heading("ref", text="Refer No") 
        self. Cust_Details_Table.heading("name", text= "Name")
        self. Cust_Details_Table.heading ("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode") 
        self.Cust_Details_Table.heading ("mobile", text="Mobile") 
        self.Cust_Details_Table.heading("email", text="Email")
        self. Cust_Details_Table.heading("nationality", text="Nationality") 
        self.Cust_Details_Table.heading("idproof",text="Id Proof") 
        self. Cust_Details_Table.heading ( "idnumber", text="Id Number") 
        self.Cust_Details_Table.heading ("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self. Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column ("name", width=100) 
        self. Cust_Details_Table.column ("mother",width=100) 
        self.Cust_Details_Table.column ("gender",width=100) 
        self. Cust_Details_Table.column ("post",width=100) 
        self.Cust_Details_Table.column ("mobile",width=100)
        self. Cust_Details_Table.column("email",width=100) 
        self. Cust_Details_Table.column ("nationality", width=100) 
        self.Cust_Details_Table.column ("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self. Cust_Details_Table.column ("address",width=100) 

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.fetch_data

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="": 
          messagebox.showerror("Error", "All fields are requaired" )

        else:
            try:
              conn=mysql.connector.connect(host="localhost",username="root",password="Aryan123", database="new_schema")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into customer values (%s , %s, %s , %s , %s , %s , %s, %s , %s, %s, %s)", (
                                                                                          self.var_ref.get(),
                                                                                          self.var_cust_name.get(),
                                                                                          self.var_mother.get(), 
                                                                                          self.var_gender.get(),
                                                                                          self.var_post.get(),

                                                                                          self.var_mobile.get(),
                                                                                          self.var_email.get(),
                                                                                          self.var_nationality.get(),
                                                                                          self.var_id_proof.get(),
                                                                                          self.var_id_number.get(), 
                                                                                          self.var_adderss.get()
                                                                                      ))
              conn.commit()
              self.fetch_data()
              self.fetch_data()
              conn.close()

              messagebox.showinfo ("Success","customer has been added", parent=self.root)
            except Exception as es:
                  messagebox.showwarning("Warning", f"Some thing went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
      conn=mysql.connector.connect (host="localhost", username="root", password="Aryan123", database="new_schema") 
      my_cursor=conn.cursor()
      my_cursor.execute("select * from customer")
      rows=my_cursor.fetchall()
      if len(rows) !=0:
        self. Cust_Details_Table.delete(*self. Cust_Details_Table.get_children()) 
      for i in rows:
        self.Cust_Details_Table.insert("",END, values=i)


      conn.commit()
      conn.close()
             
    
    def reset(self):
      self.var_ref.set(""),
      self. var_cust_name.set(""), 
      self. var_mother.set(""), 
      self.var_gender.set(""), 
      self.var_post.set(""), 
      self.var_mobile.set(""), 
      self.var_email.set(""),
      self. var_nationality.set(""), 
      self.var_id_proof.set(""), 
      self.var_id_number.set(""), 
      self.var_adderss.set("")

      x=random.randint(1000,9999)
      self.var_ref.set(str(x))


  
    def search (self):
      conn=mysql.connector.connect (host="localhost", username="root",password="Aryan123", database="new_schema") 
      my_cursor=conn.cursor()
      my_cursor.execute("select * from customer where "+str(self.search_var.get) + "'Like%" + str(self.txt_search.get() + "%'"))
      rows = my_cursor.fetchall
      if len (rows) !=0:
        self.Cust_Details_Table.delete (*self. Cust_Details_Table.get_children())
        for i in rows:
          self. Cust_Details_Table.insert("",END, values=i)
      conn.commit()






            


__name__ == "__main__"
root = Tk()
obj = Cust_Win(root)
root.mainloop()

