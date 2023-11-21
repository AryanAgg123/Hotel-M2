from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox



class DeatailsRoom:
    def __init__ (self, root):
        self.root= root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")



    # ==============title======== ====
        lbl_title=Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0,width=1295,height=50)

        #====== ==== =logo=====: =====
        img2= Image.open(r"C:\Users\aryan\Desktop\Python\Hotel Managment Software for College Project\hotel1.jpeg")
        img2=img2.resize((100, 40))
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root, image=self.photoimg2, bd=0,relief=RIDGE)
        lblimg.place(x= 5, y=2,width=100, height=40)
        # ===============labelFrame=================
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room ADD",font=("times new roman", 18, "bold"), bg="", fg="gold")
        labelframeleft.place(x= 5, y=50, width=540, height=350)

        #Floor
        lbl_floor=Label(labelframeleft, text="Floor", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid (row=0, column=0, sticky=W, padx=20)

        self.var_floor = StringVar()
        enty_floor=ttk. Entry (labelframeleft,textvariable=self.var_floor, font=("arial", 13, "bold"),width=20)
        enty_floor.grid (row=0, column=1, sticky=W)

        # Room No
        lb1_RoomNo=Label(labelframeleft, text="Room No", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_RoomNo.grid (row=1, column=0, sticky=W, padx=20)

        self.var_roomno = StringVar()
        enty_RoomNo=ttk. Entry(labelframeleft,textvariable=self.var_roomno, font= ("arial",13,"bold"), width=20)
        enty_RoomNo.grid (row=1, column=1, sticky=W)

        # Room Type
        lb1_RoomType=Label (labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_RoomType.grid (row=2, column=0, sticky=W, padx=20)

        self.var_RoomType = StringVar()
        enty_RoomType=ttk. Entry (labelframeleft,textvariable=self.var_RoomType, font=("arial",13, "bold"),width=20)
        enty_RoomType.grid(row=2, column=1, sticky=W)


        #========= ============btns=========== =========
        btn_frame=Frame (labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place (x=0, y=200, width=200,height=40)

        btnAdd=Button (btn_frame, text= "Add",command=self.add_data ,font=("arial",11,"bold"),bg="black", fg="gold", width=10)
        btnAdd.grid (row=0, column=0, padx=1)
    
        btnReset=Button(btn_frame, text="Reset",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold", width=10)
        btnReset.grid (row=0, column=3, padx=1)

        # =================tabel frame search system =====‒‒‒‒‒‒‒‒‒‒‒‒‒‒=====
        Table_Frame=LabelFrame (self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("arial", 12,"bold"))
        Table_Frame.place (x=600, y=55,width=600, height=350)
        scroll_x=ttk.Scrollbar (Table_Frame, orient=HORIZONTAL)
        scroll_y=ttk. Scrollbar (Table_Frame, orient=VERTICAL)
        self.room_table =ttk. Treeview (Table_Frame, column=("floor", "roomno" , "roomtype"), xscrollcommand=scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config (command=self.room_table.yview)

       
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading ("roomno", text="Room No ")
        self.room_table.heading ("roomtype", text="Room Type")
      

        self.room_table["show"]="headings"

        self.room_table.column("floor", width=100)
        self.room_table.column ("roomno", width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.bind("<ButtonRelease - 1>" , self.get_cuersor)
        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_data

    def add_data(self):
            if self.var_floor.get()=="" or self.var_RoomType.get()=="":
                 messagebox.showerror("Error","All fields are requaired",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Aryan123", datatbase= "new_schema")
                    my_cursor= conn.cursor()
                    my_cursor.execute("insert into customer values (%s , %s, %s)", (
                                                                                          self.var_floor.get(),
                                                                                          self.var_roomNo.get(),
                                                                                          self.RoomType.get(), 
                                                                                      ))
                    conn.commit()                                 

                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo( "Success","New Room Added Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning","Some thing went wrong: (str(es)}",parent=self.root)

    def fetch_data(self):
      conn=mysql.connector.connect (host="localhost", username="root", password="Aryan123", database="new_schema") 
      my_cursor=conn.cursor()
      my_cursor.execute("select * from details")
      rows=my_cursor.fetchall()
      if len(rows) !=0:
        self.room_table.delete(*self. Cust_Details_Table.get_children()) 
      for i in rows:
        self.room_table.insert("",END, values=i)


      conn.commit()
      conn.close()

    # getcursor
    def get_cuersor(self, event=""):
        cusrsor_row=self.room_table. focus()
        content=self.room_table.item( cusrsor_row)
        row=content [ "values"]
        self. var_floor.set(row[0]),
        self. var_roomno.set (row[1]),
        self. var_RoomType.set(row [2])


    def reset_data(self):
        self. var_floor.set(""),
        self. var_roomno.set(""),
        self. var_RoomType.set("")



__name__ == "__main__"
root = Tk()
obj = DeatailsRoom(root)
input()
root.mainloop()
