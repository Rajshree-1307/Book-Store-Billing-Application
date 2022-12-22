# Libraries
###############################################################################
from tkinter import *  # GUI Creation
import datab           # Database Module
from tkinter import messagebox

###############################################################################

#create a window

root=Tk()
root.configure(bg="#CAFAFE")

# set the dimensions of the window

root.geometry("1500x770")

title = Label(root, text="Book Store Billing Application",bd=10,relief=GROOVE, font=("Times New Roman", 40,"bold"), bg="#0f2862", fg="#FFFFFF")
title.pack(side=TOP, fill=X)




#####var decln
book1a=IntVar()
book2a=IntVar()
book3a=IntVar()
book4a=IntVar()
book5a=IntVar()
book6a=IntVar()
book7a=IntVar()
book8a=IntVar()

book1b=IntVar()
book2b=IntVar()
book3b=IntVar()
book4b=IntVar()
book5b=IntVar()
book6b=IntVar()
book7b=IntVar()
book8b=IntVar()

book1c=IntVar()
book2c=IntVar()
book3c=IntVar()
book4c=IntVar()
book5c=IntVar()
book6c=IntVar()
book7c=IntVar()
book8c=IntVar()

tot=StringVar()
tottax=StringVar()
total_books_p=StringVar()
final_tot=StringVar()
c_name=StringVar()
c_phn=StringVar()
c_addr=StringVar()

##########################


def menu():
    roott=Tk()
    roott.geometry("1500x1000")
    roott.title("Price Menu")
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="Books",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=0,column=0)
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="Cost",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=0,column=3)
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="============",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=1,column=0)
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="============",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=1,column=3)
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="7 Habits",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=2,column=0)
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="299",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=2,column=3)
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="The Alchemist",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=3,column=0)
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="299",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=3,column=3)
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="Think, Grow and Rich",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=4,column=0)
    lblinfo=Label(roott,font=("Times New Roman",20,"bold"),text="299",fg="blue",bd=10,anchor="w")
    lblinfo.grid(row=4,column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The Secret", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="199", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The Magic by Rhonda byrne", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The Power By Rhonda Byrne", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="99", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=7, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The Twilight Saga", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=8, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="Harry Potter Series (All 1-7)", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=9, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="1299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=9, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="Wings of Fire", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=10, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The Sage's Secret", fg="blue", bd=10,anchor="w")
    lblinfo.grid(row=11, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="199", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=11, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="A brief History of Time", fg="blue", bd=10,anchor="w")
    lblinfo.grid(row=12, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=12, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The fault in our Stars", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=13, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="1299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=13, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The diary of a Young girl", fg="blue", bd=10,anchor="w")
    lblinfo.grid(row=14, column=0)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=14, column=3)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="Theory of Everything", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=3, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="99", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=3, column=8)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="You Can Win by shiva khera", fg="blue", bd=10,anchor="w")
    lblinfo.grid(row=4, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="199", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=4, column=8)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The Shiva Trilogy", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=5, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=5, column=8)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="Mahabharata", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=6, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=6, column=8)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="A Thousand Splendid Suns", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=7, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=7, column=8)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The 5 AM Club", fg="blue", bd=10,anchor="w")
    lblinfo.grid(row=8, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=8, column=8)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="The Secret Letters", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=9, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="199", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=9, column=8)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="Good Vibes, Good Life", fg="blue", bd=10,anchor="w")
    lblinfo.grid(row=10, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="299", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=10, column=8)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="Inner Engineering", fg="blue", bd=10,anchor="w")
    lblinfo.grid(row=11, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="99", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=11, column=8)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="Einstein: His Life and Universe", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=12, column=6)
    lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="199", fg="blue", bd=10, anchor="w")
    lblinfo.grid(row=12, column=8)

    roott.mainloop()

#frame1
Frame1 =  LabelFrame(root, bd=5, relief=GROOVE, text = "Customer Details", font=("Times New Roman", 15,"bold"),fg="#200A4E", bg="#CAFAFE")
Frame1.place(x=5,y=75,relwidth=1)

cname_lbl=Label(Frame1,text = "Customer Full Name", font=("Times New Roman", 15,"bold"), bg="#CAFAFE").grid(row=0,column=0,padx=15,pady=5)
cname_txt = Entry(Frame1, width = 17,textvariable=c_name, font = ("MS Sans Serif", 15), bd= 7, relief=SUNKEN).grid(row=0, column=1, pady= 5, padx=10)

cphn_lbl=Label(Frame1,text = "Customer's Contact Number", font=("Times New Roman", 15,"bold"), bg="#CAFAFE").grid(row=0,column=3,padx=15,pady=5)
cphn_txt = Entry(Frame1, width = 16,textvariable=c_phn,font = ("MS Sans Serif", 15), bd= 7, relief=SUNKEN).grid(row=0, column=4, pady= 5, padx=10)

caddr_lbl=Label(Frame1,text = "Customer Address", font=("Times New Roman", 15,"bold"), bg="#CAFAFE").grid(row=0,column=5,padx=15,pady=5)
caddr_txt = Entry(Frame1, width = 17,textvariable=c_addr, font = ("MS Sans Serif", 15), bd= 7, relief=SUNKEN).grid(row=0, column=6, pady= 5, padx=10)

menu_btn=Button(Frame1, text="Menu", width=10, bd=7,font=("Times New Roman", 13,"bold"),command=menu ).grid(row=0, column=8, pady=8, padx=10)
Frame1.pack()


#######Inspirational Books
leftf1=LabelFrame(root, bd=7, relief=GROOVE, text = "Ocean of Literature", font=("Times New Roman", 15,"bold"),fg="#200A4E", bg="#CAFAFE")
leftf1.place(x=18,y=170,width=373,height=480)

book1a_lbl= Label(leftf1, text="7 Habits", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=0,column=0,padx=10,pady=10,sticky="w")
book1a_txt=Entry(leftf1, width=10,textvariable=book1a, font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

book2a_lbl= Label(leftf1, text="The Alchemist", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=1,column=0,padx=10,pady=10,sticky="w")
book2a_txt=Entry(leftf1, width=10,textvariable=book2a,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

book3a_lbl= Label(leftf1, text="Think, Grow and Rich", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=2,column=0,padx=10,pady=10,sticky="w")
book3a_txt=Entry(leftf1, width=10,textvariable=book3a,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

book4a_lbl= Label(leftf1, text="The Secret", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=3,column=0,padx=10,pady=10,sticky="w")
book4a_txt=Entry(leftf1, width=10,textvariable=book4a,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

book5a_lbl= Label(leftf1, text="The Magic by Rhonda Byrne", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=4,column=0,padx=10,pady=10,sticky="w")
book5a_txt=Entry(leftf1, width=10,textvariable=book5a,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

book6a_lbl= Label(leftf1, text="The Power by Rhonda Byrne", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=5,column=0,padx=10,pady=10,sticky="w")
book6a_txt=Entry(leftf1, width=10,textvariable=book6a,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

book7a_lbl= Label(leftf1, text="Miracles of your Mind", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=6,column=0,padx=10,pady=10,sticky="w")
book7a_txt=Entry(leftf1, width=10,textvariable=book7a,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

book8a_lbl= Label(leftf1, text="The Twilight Saga", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=7,column=0,padx=10,pady=10,sticky="w")
book8a_txt=Entry(leftf1, width=10,textvariable=book8a,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)
########
########

#######Best Books
leftf2=LabelFrame(root, bd=7, relief=GROOVE, text = "Novels", font=("Times New Roman", 15,"bold"),fg="#200A4E", bg="#CAFAFE")
leftf2.place(x=391,y=170,width=360,height=480)

book1b_lbl= Label(leftf2, text="Harry Potter Series (1-7)", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=0,column=0,padx=10,pady=10,sticky="w")
book1b_txt=Entry(leftf2, width=10,textvariable=book1b,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

book2b_lbl= Label(leftf2, text="Wings of Fire", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=1,column=0,padx=10,pady=10,sticky="w")
book2b_txt=Entry(leftf2, width=10,textvariable=book2b,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

book3b_lbl= Label(leftf2, text="The Sage's Secret", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=2,column=0,padx=10,pady=10,sticky="w")
book3b_txt=Entry(leftf2, width=10,textvariable=book3b,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

book4b_lbl= Label(leftf2, text="A brief History of Time", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=3,column=0,padx=10,pady=10,sticky="w")
book4b_txt=Entry(leftf2, width=10,textvariable=book4b,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

book5b_lbl= Label(leftf2, text="The fault in our stars", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=4,column=0,padx=10,pady=10,sticky="w")
book5b_txt=Entry(leftf2, width=10,textvariable=book5b,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

book6b_lbl= Label(leftf2, text="The Diary of a Young Girl", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=5,column=0,padx=10,pady=10,sticky="w")
book6b_txt=Entry(leftf2, width=10,textvariable=book6b,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

book7b_lbl= Label(leftf2, text="The Theory of Everything", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=6,column=0,padx=10,pady=10,sticky="w")
book7b_txt=Entry(leftf2, width=10,textvariable=book7b,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

book8b_lbl= Label(leftf2, text="You Can Win by Shiv Khera", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=7,column=0,padx=10,pady=10,sticky="w")
book8b_txt=Entry(leftf2, width=10,textvariable=book8b,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)
########
########

#######Best Novels
leftf3=LabelFrame(root, bd=7, relief=GROOVE, text = "Enlightening ones", font=("Times New Roman", 15,"bold"),fg="#200A4E", bg="#CAFAFE")
leftf3.place(x=751,y=170,width=400,height=480)

book1c_lbl= Label(leftf3, text="The Shiva Trilogy", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=0,column=0,padx=10,pady=10,sticky="w")
book1c_txt=Entry(leftf3, width=10,textvariable=book1c,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

book2c_lbl= Label(leftf3, text="Mahabharata", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=1,column=0,padx=10,pady=10,sticky="w")
book2c_txt=Entry(leftf3, width=10,textvariable=book2c,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

book3c_lbl= Label(leftf3, text="A Thousand Splendid Suns", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=2,column=0,padx=10,pady=10,sticky="w")
book3c_txt=Entry(leftf3, width=10,textvariable=book3c,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

book4c_lbl= Label(leftf3, text="The 5 AM Club", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=3,column=0,padx=10,pady=10,sticky="w")
book4c_txt=Entry(leftf3, width=10,textvariable=book4c,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

book5c_lbl= Label(leftf3, text="The Secret Letters", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=4,column=0,padx=10,pady=10,sticky="w")
book5c_txt=Entry(leftf3, width=10,textvariable=book5c,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

book6c_lbl= Label(leftf3, text="Good Vibes, Good Life", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=5,column=0,padx=10,pady=10,sticky="w")
book6c_txt=Entry(leftf3, width=10,textvariable=book6c,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

book7c_lbl= Label(leftf3, text="Inner Engineering", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=6,column=0,padx=10,pady=10,sticky="w")
book7c_txt=Entry(leftf3, width=10,textvariable=book7c,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

book8c_lbl= Label(leftf3, text="Einstein:His Life and Universe", font=("Times New Roman", 13,"bold"),bg="#CAFAFE",fg="#000000").grid(row=7,column=0,padx=10,pady=10,sticky="w")
book8c_txt=Entry(leftf3, width=10,textvariable=book8c,font=("Times New Roman", 12,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)
########
########


######bill
f4=LabelFrame(root, bd=7, bg="#CAFAFE")
f4.place(x=1152,y=178,width=362,height=470)
bill_title=Label(f4, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(f4, orient=VERTICAL)
txtarea=Text(f4, yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH, expand=1)


##########multiple button
f5=LabelFrame(root, bd=7, relief=GROOVE, text = "Billing Menu", font=("Times New Roman", 15,"bold"),fg="#200A4E", bg="#CAFAFE")
f5.place(x=15,y=660,width=1490,height=140)


tot_lbl=Label(f5, text="Total Book's price", font=("Times New Roman", 15,"bold"),bg="#CAFAFE",fg="#200A4E").grid(row=0,column=0, padx=20,pady=15,sticky="w")
tot_txt=Entry(f5, width=17,textvariable=tot,font="arial 15 bold", bd=7, relief=SUNKEN).grid(row=0,column=1,padx=5,pady=15)

tottax_lbl=Label(f5, text="Total Tax", font=("Times New Roman", 15,"bold"),bg="#CAFAFE",fg="#200A4E").grid(row=0,column=2, padx=20,pady=15,sticky="w")
tottax_txt=Entry(f5, width=17,textvariable=tottax,font="arial 15 bold", bd=7, relief=SUNKEN).grid(row=0,column=3,padx=5,pady=15)

############################################################


def totall():
    a1 = (book1a.get() * 299)
    a2 = (book2a.get() * 299)
    a3 = (book3a.get() * 299)
    a4 = (book4a.get() * 199)
    a5 = (book5a.get() * 299)
    a6 = (book6a.get() * 299)
    a7 = (book7a.get() * 99)
    a8 = (book8a.get() * 299)
    b1 = (book1b.get() * 1299)
    b2 = (book2b.get() * 299)
    b3 = (book3b.get() * 199)
    b4 = (book4b.get() * 299)
    b5 = (book5b.get() * 199)
    b6 = (book6b.get() * 299)
    b7 = (book7b.get() * 99)
    b8 = (book8b.get() * 199)
    c1 = (book1c.get() * 299)
    c2 = (book2c.get() * 299)
    c3 = (book3c.get() * 299)
    c4 = (book4c.get() * 299)
    c5 = (book5c.get() * 199)
    c6 = (book6c.get() * 299)
    c7 = (book7c.get() * 99)
    c8 = (book8c.get() * 199)
    costofbook=float((a1+a2+a3+a4+a5+a6+a7+a8+b1+b2+b3+b4+b5+b6+b7+b8+c1+c2+c3+c4+c5+c6+c7+c8))
    ptax=round(((a1+a2+a3+a4+a5+a6+a7+a8+b1+b2+b3+b4+b5+b6+b7+b8+c1+c2+c3+c4+c5+c6+c7+c8)*0.04),2)
    tot.set("Rs. "+str(costofbook))
    tottax.set("Rs. "+str(ptax))
    ftot = float(costofbook + ptax)
    final_tot.set("Rs. " + str(ftot))

############################################################
def welbill():
    txtarea.delete('1.0',END)
    txtarea.insert(END,"      Welcome to Avid Reader's Club")
    txtarea.insert(END,f"\n Customer Name : {c_name.get()}")
    txtarea.insert(END,f"\n Phone Number : {c_phn.get()}")
    txtarea.insert(END, f"\n ======================================")
    txtarea.insert(END, f"\n Books\t\tQty\t\tPrice")
    txtarea.insert(END, f"\n ======================================")


def billarea():
    if c_name.get()=="" and c_phn.get()=="":
        messagebox.showerror("Error","Customer Details must be entered..")
    else:
        welbill()
        if book1a.get() != 0:
            txtarea.insert(END, f"\n 7 Habits\t\t{book1a.get()}\t\t{book1a.get() * 299}")
        if book2a.get() != 0:
            txtarea.insert(END, f"\n Alchemist \t\t{book2a.get()}\t\t{book2a.get() * 299}")
        if book3a.get() != 0:
            txtarea.insert(END, f"\n Think,Grow..\t\t{book3a.get()}\t\t{book3a.get() * 299}")
        if book4a.get() != 0:
            txtarea.insert(END, f"\n The Secret\t\t{book4a.get()}\t\t{book4a.get() * 199}")
        if book5a.get() != 0:
            txtarea.insert(END, f"\n The Magic\t\t{book5a.get()}\t\t{book5a.get() * 299}")
        if book6a.get() != 0:
            txtarea.insert(END, f"\n The Power\t\t{book6a.get()}\t\t{book6a.get() * 99}")
        if book7a.get() != 0:
            txtarea.insert(END, f"\n Miracles..\t\t{book7a.get()}\t\t{book7a.get() * 299}")
        if book8a.get() != 0:
            txtarea.insert(END, f"\n Twilight Saga\t\t{book8a.get()}\t\t{book8a.get() * 299}")
        if book1b.get() != 0:
            txtarea.insert(END, f"\n Harry Potter\t\t{book1b.get()}\t\t{book1b.get() * 1299}")
        if book2b.get() != 0:
            txtarea.insert(END, f"\n Wings of Fire\t\t{book2b.get()}\t\t{book2b.get() * 299}")
        if book3b.get() != 0:
            txtarea.insert(END, f"\n Sage's Secret\t\t{book3b.get()}\t\t{book3b.get() * 199}")
        if book4b.get() != 0:
            txtarea.insert(END, f"\n Brief History..\t\t{book4b.get()}\t\t{book4b.get() * 299}")
        if book5b.get() != 0:
            txtarea.insert(END, f"\n The fault..\t\t{book5b.get()}\t\t{book5b.get() * 199}")
        if book6b.get() != 0:
            txtarea.insert(END, f"\n The Diary..\t\t{book6b.get()}\t\t{book6b.get() * 299}")
        if book7b.get() != 0:
            txtarea.insert(END, f"\n Theory of..\t\t{book7b.get()}\t\t{book7b.get() * 99}")
        if book8b.get() != 0:
            txtarea.insert(END, f"\n You can win\t\t{book8b.get()}\t\t{book8b.get() * 199}")
        if book1c.get() != 0:
            txtarea.insert(END, f"\n Shiva Trilogy\t\t{book1c.get()}\t\t{book1c.get() * 299}")
        if book2c.get() != 0:
            txtarea.insert(END, f"\n Mahabharata\t\t{book2c.get()}\t\t{book2c.get() * 299}")
        if book3c.get() != 0:
            txtarea.insert(END, f"\n A Thousand..\t\t{book3c.get()}\t\t{book3c.get() * 299}")
        if book4c.get() != 0:
            txtarea.insert(END, f"\n The 5 AM Club\t\t{book4c.get()}\t\t{book4c.get() * 299}")
        if book5c.get() != 0:
            txtarea.insert(END, f"\n Secret Letters\t\t{book5c.get()}\t\t{book5c.get() * 199}")
        if book6c.get() != 0:
            txtarea.insert(END, f"\n Good Vibes..\t\t{book6c.get()}\t\t{book6c.get() * 299}")
        if book7c.get() != 0:
            txtarea.insert(END, f"\n Inner..\t\t{book7c.get()}\t\t{book7c.get() * 99}")
        if book8c.get() != 0:
            txtarea.insert(END, f"\n Einsten..\t\t{book8c.get()}\t\t{book8c.get() * 199}")
        txtarea.insert(END, f"\n --------------------------------------")
        if tot.get() != "Rs. 0.0":
            txtarea.insert(END, f"\n   Total Price\t\t\t{tot.get()}")
        txtarea.insert(END, f"\n --------------------------------------")
        if tottax.get() != "Rs. 0.0":
            txtarea.insert(END, f"\n   Total Tax\t\t\t{tottax.get()}")
        txtarea.insert(END, f"\n ======================================")
        if final_tot.get() != "Rs. 0.0":
            txtarea.insert(END, f"\n   Total Tax\t\t\t{final_tot.get()}")
        txtarea.insert(END, f"\n --------------------------------------")

############################################################


def clear():
    book1a.set(0)
    book2a.set(0)
    book3a.set(0)
    book4a.set(0)
    book5a .set(0)
    book6a.set(0)
    book7a.set(0)
    book8a.set(0)

    book1b.set(0)
    book2b.set(0)
    book3b.set(0)
    book4b.set(0)
    book5b.set(0)
    book6b.set(0)
    book7b.set(0)
    book8b.set(0)

    book1c.set(0)
    book2c.set(0)
    book3c.set(0)
    book4c.set(0)
    book5c.set(0)
    book6c.set(0)
    book7c.set(0)
    book8c.set(0)

    tot.set("")
    tottax.set("")
    total_books_p.set("")
    final_tot.set("")
    c_name.set("")
    c_phn.set("")
    c_addr.set("")
    welbill()

############################################################

def exit():
    op=messagebox.askyesno("Exit","Do you really want to exit?")
    if op>0:
        root.destroy()

############################################################



btnf=Frame(f5, bd=7,relief=GROOVE)
btnf.place(x=850, width=570,height=85)

total_btn=Button(btnf,text="Total",command=totall,bg="#0f2862",fg="white",width=15,height=2, font="arial 9 bold").grid(row=0, column=1,padx=10,pady=10)
Gbill_btn=Button(btnf,text="Generate Bill", command=billarea,bg="#0f2862",fg="white",width=15,height=2, font="arial 9 bold").grid(row=0, column=2,padx=10,pady=10)
Clear_btn=Button(btnf,text="Clear",bg="#0f2862",fg="white",width=15,height=2, font="arial 9 bold",command=clear).grid(row=0, column=3,padx=10,pady=10)
Exit_btn=Button(btnf,text="Exit",bg="#0f2862",command=exit,fg="white",width=15,height=2, font="arial 9 bold").grid(row=0, column=4,padx=10,pady=10)
welbill()


root.mainloop()

