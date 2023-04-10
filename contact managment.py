from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import neg6

db = neg6.Database('e:/negah.db')
 
def populate_list():
    listbox.delete(0,END)
    for i in db.fetch():
        listbox.insert(END,i )    


def add ():
    
    if entry_name.get() == '' or entry_lastname.get() == '' or entry_adress.get() == '' or entry_phone_number.get() == '':
        messagebox.showerror('ERROR','همه فیلد های خالی باید پر شود.')
        return
    db.insert(entry_name.get(), entry_lastname.get() , entry_adress.get(), entry_phone_number.get())
    clear()
    populate_list()
    
    messagebox.showinfo('اخطار','اطلاعات ثبت شد')
   
    
def clear():
    entry_name.delete(0,END)
    entry_lastname.delete(0,END)
    entry_adress.delete(0,END)
    entry_phone_number.delete(0,END)
    
    entry_name.focus_set()

def remove_item():
    index = listbox.curselection()
    record = listbox.get(index)
    db.remove(record[0])
    populate_list()


def select_item(event):
    global select
    
    index = listbox.curselection()
    select = listbox.get(index)
    
    entry_name.delete(0,END)
    entry_name.insert(END,select[1])

    entry_lastname.delete(0,END)
    entry_lastname.insert(END,select[2])
    
    entry_adress.delete(0,END)
    entry_adress.insert(END,select[3])
    
    entry_phone_number.delete(0,END)
    entry_phone_number.insert(END,select[4])



def update():
    db.update(select[0], entry_name.get(), entry_lastname.get(), entry_adress.get(), entry_phone_number.get())
  
    populate_list()
    


    
def search():
    listbox.delete(0,END)
    search1 = db.search(entry_search.get())
    
    if search1 == []:
        s = entry_search.get()
        messagebox.showinfo(' عدم وجود فیلد جستجو شده',f'The field {s} is not found .')
        entry_search.delete(0,END)
        return
    for i in search1:
        listbox.insert(END,i)
        entry_search.delete(0,END)




def show_form():
    
    def add2 ():
        
            if entry_name2.get() == '' or entry_password.get() == '':
                messagebox.showerror('ERROR','فیلد های خالی باید پر شود.')
            else:
                name = entry_name2.get()
                password = entry_password.get()
                if len(name) <= 10:
                    
                    
                    if  len(password) == 5:
                    
                        entry_name2.delete(0,END)
                        entry_password.delete(0,END)
                        label_truepass.configure(text = '')
                        messagebox.showinfo('موفق','.اطلاعات ثبت شد')
                        entry_name2.focus_set()
                        
                    elif len(password) < 5:
                        label_truepass.configure(text = '.گذرواژه نباید کمتر از 5 باشد')
                        entry_password.delete(0,END)
                        entry_password.focus_set()
                        

                    elif len(password) > 5:
                        label_truepass.configure(text = '.گذرواژه نباید بیشتر از 5 باشد')
                        entry_password.delete(0,END)
                        entry_password.focus_set()
        
                else :
                    messagebox.showinfo('اخطار','.نام کاربری وارد شده صحیح نمی باشد')
                    entry_name2.delete(0,END)
                    entry_name2.focus()

    def exite():
        res = messagebox.askquestion('خروج','آیا می خواهید از برنامه خارج شوید؟')   
        if res == 'yes':
            time.sleep(2)
            win2.destroy()
        
    # ========================= information of window =================================
    win2 = Tk()

    win2.title("ورود به سیستم")
    win2.geometry('350x150+150+150')
    win2.config(bg = 'pink')
    
    # ==================== label ======================
    label_name2 = Label(win2 , text = 'Username   :',bg = 'pink')
    label_name2.place(x = 10,y = 5)
    
    label_password = Label(win2 , text = 'PASSWORD   : ',bg = 'pink')
    label_password.place(x = 10,y = 35)
    
    label_truepass= Label(win2 ,bg = 'pink',fg = 'red')
    label_truepass.place(x = 205,y = 60)
    

    # ==================== entry ======================

    entry_name2 = Entry(win2,width = 35)
    entry_name2.place(x =115, y =5)
    entry_name2.focus_set()
    
    entry_password = Entry(win2,width = 35,show = '*')
    entry_password.place(x = 115, y =35)
    
    
    # ==================== button ======================
    btn_add2 = Button(win2,text = 'LOGIN',width = 8,command = add2)
    btn_add2.place(x = 135 , y = 75)

    btn_exit2 = Button(win2,text = "exit",font = 'arial 12 ' ,width = 35,command = exite)
    btn_exit2.place(x = 10 , y = 110)


    
    win2.mainloop()









# ========================= information of window =================================

win = Tk()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()


win.configure(bg = '#E1A8FA')
win.geometry('800x450+550+150')
win.title('مدیریت مخاطبین')


# ========================= label =================================

label_name = Label(win , text = 'نام' , fg = 'black' , bg = '#E1A8FA', font = ' tahoma 12 bold')
label_name.place(x = 65 ,y = 19)


label_adress = Label(win , text = 'آدرس' , fg = 'black' , bg = '#E1A8FA', font = ' tahoma 12 bold')
label_adress.place(x = 55 ,y = 85)



label_lastname = Label(win , text = 'نام خانوادگی' , fg = 'black' , bg = '#E1A8FA', font = ' tahoma 12 bold')
label_lastname.place(x = 385 ,y = 19)



label_phone_number = Label(win , text = 'شماره تلفن' , fg = 'black' , bg = '#E1A8FA', font = ' tahoma 12 bold')
label_phone_number.place(x = 387 ,y = 85)







# ======================== entry ===========================


entry_name = Entry(win,relief = SOLID)
entry_name.place(x = 155 , y = 19 ,width = 155 ,height = 25)

entry_name.focus()


entry_lastname = Entry(win,relief = SOLID)
entry_lastname.place(x = 555 , y = 19 ,width = 155 ,height = 25)


entry_adress = Entry(win,relief = SOLID)
entry_adress.place(x = 155 , y = 85 ,width = 155 ,height = 25)



entry_phone_number= Entry(win,relief = SOLID)
entry_phone_number.place(x = 555 , y = 85 ,width = 155 ,height = 25)

search_tetx = StringVar()
search_tetx.set(' .فیلد مورد نظر را جستجو کنید')

entry_search = Entry(win,relief = SOLID,textvariable = search_tetx)
entry_search.place(x = 425 , y = 190 ,width = 155 ,height = 25)




# ========================== button =========================

btn_add = Button(win , text = 'اضافه کردن' ,fg = '#65106E',font = 'tahoma 10 bold',bg = 'white', width = 16,bd = 5,command = add )
btn_add.place(x = 25 , y = 145)


btn_show = Button(win , text = 'نمایش رکورد' ,fg = '#65106E',font = 'tahoma 10 bold',bg = 'white', width = 16,bd = 5,command = populate_list)
btn_show.place(x = 25 , y = 190)


btn_delete = Button(win , text = 'حذف کردن' ,fg = '#65106E',font = 'tahoma 10 bold',bg = 'white', width = 16,bd = 5 ,command = remove_item)
btn_delete.place(x = 225 , y = 145)



btn_update = Button(win , text = 'بروزرسانی' ,fg = '#65106E',font = 'tahoma 10 bold',bg = 'white', width = 16,bd = 5,command = update )
btn_update.place(x = 425 , y = 145)



btn_clean = Button(win , text = 'پاک کردن ورودی ها ' ,fg = '#65106E',font = 'tahoma 10 bold',bg = 'white', width = 16,bd = 5,command = clear )
btn_clean.place(x = 625 , y = 145)


btn_search = Button(win , text = 'جستجو' ,fg = '#65106E',font = 'tahoma 10 bold',bg = 'white', width = 16,bd = 5,command = search)
btn_search.place(x = 225 , y = 190)


btn_showform = Button(win , text = 'نمایش فرم' ,fg = '#65106E',font = 'tahoma 10 bold',bg = 'white', width = 16,bd = 5,command = show_form)
btn_showform.place(x = 625 , y = 190)

# =========================== scrollbar ============================

scroll_listbox = Scrollbar(win)
scroll_listbox.place(x = 625,y = 235,height = 188)




# =========================== list box ============================

listbox = Listbox(win,width = 100,height = 11 ,relief = SOLID,bd = 5,yscrollcommand = scroll_listbox.set)

listbox.place(x = 15,y = 235)



scroll_listbox.config(command = listbox.yview)


# =================== binding listbox =================

listbox.bind('<<ListboxSelect>>',select_item)
















win.mainloop()