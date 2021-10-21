from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import time
import random

# ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ TKINTER ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻
m = Tk()
m.configure(background='#333300')
m.title('CROP PRODUCTION')
m.geometry("1600x800+0+0")
m.iconbitmap('icon.ico')
# functions and variables
# income=IntVar()
# cinc=IntVar()
cost1 = IntVar()
cost2 = IntVar()
########################## algorithm ###############
import pandas as pd
#from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# p=PolynomialFeatures()
l = LinearRegression()
df = pd.read_csv('training_data.csv')
x = df.iloc[:, 2:4]
y1 = df.iloc[:, 4:5]
y2 = df.iloc[:, 5:5 + 1]


###
def cost(cost1, cost2):
    l.fit(x, y1)
    c = l.predict([[cost1, cost2]])
    return c


def yield_(cost1, cost2):
    l.fit(x, y2)
    y = l.predict([[cost1, cost2]])
    return y


def score(h, d):
    s = l.score(pred, y1)
    return s


def cost_window():
    check = Toplevel()
    check.configure(background='#1a3300')
    check.geometry("400x400+200+200")
    check.title(" OUTPUT ")
    l = Label(check, text="Cost of Yield(Quintal/ Hectare) ↓↓", bg='#1a3300', font=('arial', 16, 'bold'), bd=6,
              anchor='nw').pack(side=TOP)

    button = Button(check, text="←←←←", command=check.destroy, padx=2, pady=2, bd=3, fg='#ffffff',
                    font=('arial', 25, 'bold'), \
                    bg='#0d1a00', width=7).pack(side=BOTTOM)

    t = Text(check, height=5, width=25)
    t.pack()
    cost1 = int(e3.get())
    cost2 = int(e4.get())
    pred = cost(cost1, cost2)
    pred = list(pred)[0]
    # pred=int(pred)
    # print(pred)
    # print(cost1,cost2)
    #  o=print(pred)
    t.insert(END, pred[0])

    def score(h, hj):
        s = l.score(pred, y1)
        return s

    def accu_window():
        check = Toplevel()
        check.configure(background='#1a3300')
        check.geometry("400x400+200+200")
        check.title(" ACCURACY ↓↓")
        l = Label(check, text="Accuracy ↓↓", bg='#1a3300', font=('arial', 16, 'bold'), bd=6, anchor='nw').pack(side=TOP)

        tt = Text(check, height=5, width=25)
        tt.pack()
        # pred=cost(cost1,cost2)
        #  pred=list(pred)[0]
        a = score(pred, y1)
        a = list(a)
        tt.insert(END, a)

    button = Button(check, text="ACCURACY", command=accu_window, padx=4, pady=4, bd=6, fg='black',
                    font=('arial', 25, 'bold'), \
                    bg='#ffffb3', width=10).pack(side=BOTTOM)


def yield_window():
    check = Toplevel()
    check.configure(background='#1a3300')
    check.geometry("400x300+200+200")
    check.title(" OUTPUT ")
    l = Label(check, text="YIELD(Quintal/ Hectare) ↓↓", bg='#1a3300', font=('arial', 16, 'bold'), bd=6,
              anchor='nw').pack(side=TOP)
    button = Button(check, text="BACK", command=check.destroy, padx=4, pady=6, bd=6, fg='#ffffff',
                    font=('arial', 25, 'bold'), \
                    bg='#0d1a00', width=10).pack(side=BOTTOM)
    t = Text(check, height=5, width=25)
    t.pack()
    cost1 = int(e3.get())
    cost2 = int(e4.get())
    pred = yield_(cost1, cost2)
    pred = list(pred)[0]
    # pred=int(pred)
    # oo=print(pred)
    t.insert(END, pred[0])


def reset():
    cost1.set('')
    cost2.set('')
    # amount.set('')


#  term.set('')

def call():
    mess = messagebox.askyesno("चेतावनी", "क्या आपको यकीन है ?")
    if (mess):
        m.destroy()


################# MENU COMMANDS FOR NEW WINDOW
def introduction():
    intro = Toplevel()
    intro.configure(background='#b3ffc6')
    intro.geometry("800x600+120+100")
    intro.title("Introduction")
    button = Button(intro, text="BACK", command=intro.destroy, padx=4, pady=6, bd=6, fg='black',
                    font=('arial', 14, 'bold'), \
                    width=5).pack(side=BOTTOM)


def project():
    proj = Toplevel()
    proj.configure(background='#b3ffc6')
    proj.geometry("1500x750")
    proj.title("About_Project")
    button = Button(proj, text="BACK", command=proj.destroy, padx=4, pady=6, bd=6, fg='black',
                    font=('arial', 16, 'bold'), \
                    width=5).pack(side=BOTTOM)


def mentor():
    ment = Toplevel()
    ment.configure(background='#b3ffc6')
    ment.geometry("1200x650")
    ment.title("About_Mentor")
    button = Button(ment, text="BACK", command=ment.destroy, padx=4, pady=6, bd=6, fg='black',
                    font=('arial', 16, 'bold'), \
                    width=5).pack(side=BOTTOM)


def developers():
    dev = Toplevel()
    ment.configure(background='#b3ffc6')
    dev.geometry("1200x650")
    dev.title("About_Developers")
    button = Button(dev, text="BACK", command=dev.destroy, padx=4, pady=6, bd=6, fg='black', font=('arial', 16, 'bold'), \
                    width=5).pack(side=BOTTOM)


def college():
    clg = Toplevel()
    clg.configure(background='#b3ffc6')
    clg.geometry("1600x800")
    clg.title("About_College")
    button = Button(clg, text="BACK", command=clg.destroy, padx=4, pady=6, bd=6, fg='black', font=('arial', 16, 'bold'), \
                    width=5).pack(side=BOTTOM)


def gcet():
    gc = Toplevel()
    gcet.configure(background='#b3ffc6')
    gc.geometry("1200x650")
    gc.title("GCET_GALLERY")
    button = Button(gc, text="BACK", command=gc.destroy, padx=4, pady=6, bd=6, fg='black', font=('arial', 16, 'bold'), \
                    width=5).pack(side=BOTTOM)


# creating drop down menues.↓↓
main_menu = Menu(m)
m.config(menu=main_menu)
firstMenu = Menu(main_menu)
viewMenu = Menu(main_menu)
exitMenu = Menu(main_menu)

main_menu.add_cascade(label="Menu", menu=firstMenu)
firstMenu.add_command(label="Intro", font=('arial', 12, 'bold'),
                      command=introduction)  # here we can use (command=something) and we can derive something above.
firstMenu.add_separator()
about_menu = Menu(firstMenu)
firstMenu.add_cascade(label="About", font=('arial', 12, 'bold'), menu=about_menu)
about_menu.add_command(label="About_Project", font=('arial', 10, 'bold'), command=project)
about_menu.add_separator()
about_menu.add_command(label="About_Mentor", font=('arial', 10, 'bold'), command=mentor)
about_menu.add_separator()
about_menu.add_command(label="About_Developers", font=('arial', 10, 'bold'), command=developers)
about_menu.add_separator()
about_menu.add_command(label="About_College", font=('arial', 10, 'bold'), command=college)

main_menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="GCET", font=('arial', 12, 'bold'), command=gcet)

main_menu.add_cascade(label="Exit", command=call)

# ********************  FRAMES    ***********************
top = Frame(m, height=40, width=1600, relief=SUNKEN, bg='#333300')
top.pack(side=TOP)
f1 = Frame(m, height=750, width=1000, relief=SUNKEN, bg='#333300')
f1.pack(side=LEFT)
f2 = Frame(m, height=750, width=600, relief=SUNKEN, bg='#333300')
f2.pack()


# ********************   TIME    ***********************
# localtime=time.asctime(time.localtime(time.time()))
def get_time():
    time_string = time.strftime("%I:%M:%S %p")
    clock.config(text=time_string)
    clock.after(200, get_time)


clock = Label(top, font=("time", 20, "bold"), bg="#ffffff")
get_time()
# ********************  title and time   ***********************
lblinfo = Label(top, font=('arial', 50, 'bold'), text="INPUT", \
                fg='#ffffff', bg='#333300', anchor='w', bd=10)
lblinfo.grid(row=0)

clock.grid(row=1)
# lblinfo=Label(top,text=get_time(),\
#               anchor='w',bg='#EBDEF0')

########  ☺ ☻ labels  ♫  ↓↓
l1 = Label(f1, text="Crop                        : ", bg='#333300', font=('arial', 16, 'bold'), bd=10, anchor='nw',
           fg='Black')  # .grid(row=8)
l1.grid(row=0, sticky='nw')
Depen = ['ARHAR', 'COTTON', 'GRAM', 'GROUNDNUT', 'MAIZE', 'MOONG', 'PADDY',
         'RAPESEED AND MUSTARD', 'SUGARCANE', 'WHEAT']
# vc=StringVar()
combo = Combobox(f1, values=Depen, height=4, font=('arial', 16, 'bold'))
combo.set("Select")
combo.grid(row=0, column=1)

l2 = Label(f1, text="State                       : ", bg='#333300', font=('arial', 16, 'bold'), bd=10, anchor='nw',
           fg='Black')  # .grid(row=8)
l2.grid(row=1, column=0, sticky='nw')
Depen = ['Uttar Pradesh', 'Karnataka', 'Gujarat', 'Andhra Pradesh',
         'Maharashtra', 'Punjab', 'Haryana', 'Rajasthan', 'Madhya Pradesh',
         'Tamil Nadu', 'Bihar', 'Orissa', 'West Bengal']
# vc=StringVar()
combo = Combobox(f1, values=Depen, height=4, font=('arial', 16, 'bold'))
combo.set("Select")
combo.grid(row=1, column=1)

l3 = Label(f1, text='Cost of Cultivation :', font=('arial', 16, 'bold'), \
           bd=10, bg='#333300', anchor='nw', fg='Black')
l3.grid(row=2, column=0, sticky='nw')
e3 = Entry(f1, font=('arial', 16, 'bold'), bd=10, \
           justify='right', bg='#333300', textvariable=cost1, insertwidth=4)
e3.grid(row=2, column=1)

l4 = Label(f1, text='Cost of Fertilizers   :', font=('arial', 16, 'bold'), \
           bd=10, bg='#333300', anchor='nw', fg='Black')
l4.grid(row=3, column=0, sticky='nw')
e4 = Entry(f1, font=('arial', 16, 'bold'), bd=10, \
           justify='right', bg='#333300', textvariable=cost2, insertwidth=4)
e4.grid(row=3, column=1)

#################### Machine learning algorithms ################


# #####################  buttons##########################
breset = Button(f1, text='RESET', padx=4, pady=5, bd=6, fg='black', font=('arial', 25, 'bold'), \
                width=10, command=reset, bg='#cc9900').grid(row=4, column=0, sticky="S")
bexit = Button(f1, text='EXIT', padx=4, pady=5, bd=6, fg='black', font=('arial', 25, 'bold'), \
               width=10, command=call, bg='#4d0000').grid(row=4, column=1, sticky="S")
byield = Button(f2, text='Yield (Quintal/ Hectare)', padx=4, pady=15, bd=10, fg='white', font=('arial', 20, 'bold'), \
                command=yield_window, width=25, height=2, bg='#003300').grid(row=1, sticky="s")
bcost = Button(f2, text='Cost of Yield(Quintal/ Hectare)', padx=4, pady=15, bd=10, fg='white',
               font=('arial', 20, 'bold'), \
               command=cost_window, width=25, height=2, bg='#003300').grid(row=2, sticky="s")
bacc = Button(f2, text="ACCURACY OF MODEL", padx=4, pady=15, bd=10, fg='white', font=('arial', 20, 'bold'), \
              width=25, height=2, bg='#003300').grid(row=3, sticky="s")
m.mainloop()