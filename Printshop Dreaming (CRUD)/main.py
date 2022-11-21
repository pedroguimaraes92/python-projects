import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from tkintertable import TableCanvas, TableModel
from tkinter import ttk
from datetime import datetime
from datetime import timedelta
from datetime import date
from tkinter.ttk import Combobox
from ttkthemes import ThemedTk
import time
from time import sleep
import sqlite3
import csv
from reportlab.pdfgen import canvas


conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS usersdata(idpedido TEXT ,cliente TEXT ,telefone TEXT ,prioridade TEXT ,data_entrada DATE ,data_prevista DATE ,horario_entrada TEXT , horario_saida TEXT , status TEXT)')


def add_data(idpedido,cliente,telefone,prioridade,data_entrada,data_prevista,horario_entrada,horario_saida,status):
	c.execute('INSERT INTO usersdata(idpedido,cliente,telefone,prioridade,data_entrada,data_prevista,horario_entrada,horario_saida,status ) VALUES (?,?,?,?,?,?,?,?,?)',(idpedido,cliente,telefone,prioridade,data_entrada,data_prevista,horario_entrada,horario_saida, status))
	conn.commit()



def get_single_user(idpedido):
	c.execute('SELECT * FROM usersdata WHERE idpedido="{}"'.format(idpedido))
	data = c.fetchall()
	# tab2_display.insert(tk.END,data)
	return data

def edit_single_user(idpedido,novo_pedido):
	c.execute('UPDATE usersdata SET idpedido ="{}" WHERE idpedido="{}"'.format(novo_pedido,idpedido))
	conn.commit()
	data = c.fetchall()
	return data
def delete_single_user(idpedido):
	c.execute('DELETE FROM usersdata WHERE idpedido="{}"'.format(idpedido))
	conn.commit()




create_table()




 #Layout
window = ThemedTk(theme = "arc")
window.title("Cadastro e Controle de Pedidos")
window.geometry("1200x750")
window.iconbitmap('icon.ico')
window.resizable(False, False)
#window.attributes('-alpha',0.9)

style = ttk.Style(window)
bg = PhotoImage(file = 'background.png')
mainbg = PhotoImage(file = 'mainbg2.png')
about = PhotoImage (file = 'about.png')
search = PhotoImage (file = 'search.png')
view = PhotoImage (file = 'view.png')
refresh = PhotoImage (file = 'update.png')
export = PhotoImage (file = 'export.png')
style.configure('lefttab.TNotebook', tabposition='wn', image = bg)
style.configure(".", font = ('Helvetica', 10))
style.configure("Treeview.Heading", foreground = 'black', font = ('Helvetica',10))


#Get current_time

#now = datetime.now()
#current_time = now.strftime("%H:%M")


#Creating Tabs
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)


#Adding tabs

tab_control.add(tab1, text=f'{"Home":^60s}')
tab_control.add(tab2, text=f'{"Visualizar":^60s}')
tab_control.add(tab5, text=f'{"Exportar":^60s}')
tab_control.add(tab6, text=f'{"Sobre":^60s}')
tab_control.pack(expand=1, fill='both')

#Creating Background for tabs

bgtab_1 = Label(tab1, image = mainbg)
bgtab_1.place(x = 0, y = 0)

bgtab_2 = Label(tab2, image = view)
bgtab_2.place(x = 0, y = 0)


bgtab_5 = Label(tab5, image = export)
bgtab_5.place(x = 0, y = 0)

bgtab_6 = Label(tab6, image = about)
bgtab_6.place(x = 0, y = 0)


#Functions

def clear():
    entry_id_pedido.delete('0',END)
    entry_telefone.delete('0',END)
    entry_cliente.delete('0',END)
    entry_hr_prev.delete('0',END)
    entry_status.delete('0',END)
    entry_prioridade.delete('0',END)

def clear_update():
    entry_id_pedido_1.delete('0',END)
    entry_telefone_1.delete('0',END)
    entry_cliente_1.delete('0',END)
    entry_hr_ent_1.delete('0',END)
    entry_hr_prev_1.delete('0',END)
    entry_status_1.delete('0',END)
    entry_prioridade_1.delete('0',END)

def add_details():
    idpedido = str(entry_id_pedido.get())
    cliente = str(entry_cliente.get())
    telefone = str(entry_telefone.get())
    prioridade = str(entry_prioridade.get())
    data_entrada = str(cal.get())
    data_prevista = str(cal.get())
    horario_entrada = str(entry_hr_ent.get())
    horario_saida = str(entry_hr_prev.get())
    status = str(entry_status.get())
    add_data(idpedido,cliente,telefone,prioridade,data_entrada,data_prevista,horario_entrada,horario_saida,status)
    result = '\nID Pedido:{},\nCliente:{},\nTelefone:{},\nPrioridade:{},\nData de Entrada:{},\nData Prevista:{},\nHorário de Entrada:{},\nHorário de Saída:{},\nStatus:{}\n'.format(idpedido,cliente,telefone,prioridade,data_entrada,data_prevista,horario_entrada,horario_saida,status)
    #tab1_display.insert(tk.END,result)
    messagebox.showinfo(title = "Cadastro de Pedidos", message = "Pedido adicionado com sucesso!")

def clear_display_result():
	tab1_display.delete('1.0',END)

def clear_display_view_2():
    tree_display.delete('1.0',END)

def search_user_by_id():
	idpedido = str(entry_search.get())
	result = get_single_user(idpedido)
	c.execute('SELECT * FROM usersdata WHERE idpedido="{}"'.format(idpedido))
	data = c.fetchall()
	print(result)
	tab2_display.insert(tk.END,result)


def clear_display_view():
	tab2_display.delete('1.0',END)


def clear_entered_search():
	entry_search.delete('0',END)

#def clear_tree_view():
	#tab2_display.delete('1.0',END)
	#tree.delete('1.0',END)




#Registration - Tab1

pedido_raw_entry = StringVar()
entry_id_pedido = Entry(tab1,textvariable = pedido_raw_entry, width = 20, font = 'Helvetica 12')
entry_id_pedido.place(x = 160, y = 230)

telefone_raw_entry = StringVar()
entry_telefone = Entry(tab1, textvariable = telefone_raw_entry, width = 20, font = 'Helvetica 12')
entry_telefone.place(x = 360, y = 230)



cliente_raw_entry = StringVar()
entry_cliente = Entry(tab1, textvariable = cliente_raw_entry, width = 42, font = 'Helvetica 12')
entry_cliente.place(x = 160, y = 290)



dat_ent_raw_entry = StringVar()
cal = DateEntry(tab1, width=22, textvariable = dat_ent_raw_entry,font = 'Helvetica 10', selectbackground ='black', background='#3237c2',foreground='#c7c8f0',borderwidth=2, year=2022, date_pattern="dd/mm/yyyy", locale = "pt", state="readonly")
cal.place(x = 160, y = 350)


prev_raw_entry = StringVar()
cal = DateEntry(tab1, width=22, textvariable = prev_raw_entry,font = 'Helvetica 10', selectbackground ='black', background='#3237c2',foreground='#c7c8f0', borderwidth=2, year=2022, date_pattern="dd/mm/yyyy", locale = "pt", state ="readonly")
cal.place(x = 360, y = 350)

def time():
    global string
    clock = datetime.now()
    string = clock.strftime("%H:%M:%S")
    lbl.config(text = string)
    lbl.after(1000, time)
    hr_ent_raw_entry.set (string)
lbl = Label(window, font = ('digital-7 1'))
lbl.pack(anchor = 'center')


hr_ent_raw_entry = StringVar()
hr_ent_raw_entry.set (time)
entry_hr_ent = Entry(tab1, textvariable = hr_ent_raw_entry, width = 20, font = 'Helvetica 12')
entry_hr_ent.place(x = 160, y = 410)

time()


hr_prev_raw_entry = StringVar()
entry_hr_prev = Entry(tab1, textvariable = hr_prev_raw_entry, width = 20, font = 'Helvetica 12')
entry_hr_prev.place(x = 360, y = 410)


raw_entry = StringVar()
data = ("Baixa","Média","Alta")
entry_prioridade = Combobox(tab1, values = data, width = 22,font = 'Helvetica 10')
entry_prioridade.place(x = 160, y = 470)



status_raw_entry = StringVar()
datastatus = ['Pendente', 'OK']
entry_status = Combobox(tab1, textvariable = status_raw_entry, values = datastatus, width = 22, font = 'Helvetica 9')
entry_status.place(x = 360, y = 470)



#Buttons

def press(_):
	button2.config(image = addpress, border = 0)
def release(_):
	button2.config(image = addrelease, border = 0)

addpress = PhotoImage(file = 'add1.gif')
addrelease = PhotoImage(file = 'add.gif')

button2 = Button(tab1, image = addrelease, command = add_details, border = 0, background = '#16A0C7', activebackground = '#16A0C7')
button2.place(x = 180, y = 555)
button2.bind('<Enter>', press)
button2.bind('<Leave>', release)



def press(_):
	button1.config(image = cleanpress, border = 0)
def release(_):
	button1.config(image = cleanrelease, border = 0)

cleanpress = PhotoImage(file = 'clean1.gif')
cleanrelease = PhotoImage(file = 'clean.gif')

button1 = Button(tab1, image = cleanrelease, command = clear, border = 0, background = '#23ACD0', activebackground = '#23ACD0')
button1.place(x = 350, y = 555)
button1.bind('<Enter>', press)
button1.bind('<Leave>', release)



#View - Tab2

#Setting the current day

today = date.today()
date = today.strftime("%d/%m/%Y")


#SQL Query for single day orders

def view_all_users():
    for i in tree.get_children():
        tree.delete(i)
        #pedidos.update()
    c.execute(f"SELECT idpedido, cliente, data_prevista, horario_saida, prioridade, status FROM usersdata WHERE data_prevista = '{date}' ORDER BY prioridade, horario_saida ASC")
    data = c.fetchall()
    for row in data:
	    print(row)
	    #return data
    for row in data:
	    print(row)
	    tree.insert("", tk.END, values = row)


#SQL Query for the week orders (day-by-day until the end of the week)


def view_all_users_week():
    for i in tree.get_children():
        tree.delete(i)
    dt = datetime.now()
    if dt.weekday() == 0:
        monday = datetime.now()
        monday_1 = monday.strftime("%d/%m/%Y")
        friday = datetime.now() + timedelta(days = 4)
        friday_1 = friday.strftime("%d/%m/%Y")
        c.execute(f"SELECT idpedido, cliente, data_prevista, horario_saida, prioridade, status FROM usersdata WHERE data_prevista BETWEEN '{monday_1}' AND '{friday_1}' ORDER BY data_prevista, prioridade, horario_saida ASC")
        data = c.fetchall()
        for row in data:
            print(row)
        for row in data:
            tree.insert("", tk.END, values = row)
    elif dt.weekday() == 1:
        dt = datetime.now()
        tuesday = datetime.now()
        tuesday_1 = tuesday.strftime("%d/%m/%Y")
        friday = datetime.now() + timedelta(days = 3)
        friday_1 = friday.strftime("%d/%m/%Y")
        c.execute(f"SELECT idpedido, cliente, data_prevista, horario_saida, prioridade, status FROM usersdata WHERE data_prevista BETWEEN '{tuesday_1}' AND '{friday_1}' ORDER BY data_prevista, prioridade, horario_saida ASC")
        data = c.fetchall()
        for row in data:
            print(row)
        for row in data:
            tree.insert("", tk.END, values = row)
    elif dt.weekday() == 2:
        dt = datetime.now()
        wednesday = datetime.now()
        wednesday_1 = wednesday.strftime("%d/%m/%Y")
        friday = datetime.now() + timedelta(days = 2)
        friday_1 = friday.strftime("%d/%m/%Y")
        c.execute(f"SELECT idpedido, cliente, data_prevista, horario_saida, prioridade, status FROM usersdata WHERE data_prevista BETWEEN '{wednesday_1}' AND '{friday_1}' ORDER BY data_prevista, prioridade, horario_saida ASC")
        data = c.fetchall()
        for row in data:
            print(row)
        for row in data:
            tree.insert("", tk.END, values = row)
    elif dt.weekday() == 3:
        dt = datetime.now()
        thursday = datetime.now()
        thursdayy_1 = thursday.strftime("%d/%m/%Y")
        friday = datetime.now() + timedelta(days = 1)
        friday_1 = friday.strftime("%d/%m/%Y")
        c.execute(f"SELECT idpedido, cliente, data_prevista, horario_saida, prioridade, status FROM usersdata WHERE data_prevista BETWEEN '{thursday_1}' AND '{friday_1}' ORDER BY data_prevista, prioridade, horario_saida ASC")
        data = c.fetchall()
        for row in data:
            print(row)
        for row in data:
            tree.insert("", tk.END, values = row)
    elif dt.weekday() == 4:
        friday = datetime.now()
        friday_1 = friday.strftime("%d/%m/%Y")
        c.execute(f"SELECT idpedido, cliente, data_prevista, horario_saida, prioridade, status FROM usersdata WHERE data_prevista = '{friday_1}' ORDER BY prioridade, horario_saida ASC")
        data = c.fetchall()
        for row in data:
            print(row)
        for row in data:
            tree.insert("", tk.END, values = row)
    elif dt.weekday() == 5:
        saturday = datetime.now()
        saturday_1 = saturday.strftime("%d/%m/%Y")
        friday = datetime.now() + timedelta(days = 6)
        friday_1 = friday.strftime("%d/%m/%Y")
        c.execute(f"SELECT idpedido, cliente, data_prevista, horario_saida, prioridade, status FROM usersdata WHERE data_prevista BETWEEN '{saturday_1}' AND '{friday_1}' ORDER BY data_prevista, prioridade, horario_saida ASC")
        data = c.fetchall()
        for row in data:
            print(row)
        for row in data:
            tree.insert("", tk.END, values = row)
    else:
        sunday = datetime.now()
        sunday_1 = sunday.strftime("%d/%m/%Y")
        friday = datetime.now() + timedelta(days = 5)
        friday_1 = friday.strftime("%d/%m/%Y")
        c.execute(f"SELECT idpedido, cliente, data_prevista, horario_saida, prioridade, status FROM usersdata WHERE data_prevista BETWEEN '{sunday_1}' AND '{friday_1}' ORDER BY data_prevista, prioridade, horario_saida ASC")
        data = c.fetchall()
        for row in data:
            print(row)
        for row in data:
            tree.insert("", tk.END, values = row)



#Creating table


tree_display = ScrolledText(tab2, height = 18)
tree_display.place(x = 10 ,y = 250)
tree = ttk.Treeview(tab2, column=("column1", "column2", "column3","column4", "column5","column6"), show='headings', height = 18)
tree.heading("#1", text="ID Pedido")
tree.column("#1",minwidth=10,width=150, anchor = 'center')
tree.heading("#2", text="Cliente")
tree.column("#2",minwidth=10,width=210, anchor = 'center')
tree.heading("#3", text="Data Prevista")
tree.column("#3",minwidth=10,width=125, anchor = 'center')
tree.heading('#4',text="Hora Entrega")
tree.column("#4",minwidth=10,width=100, anchor = 'center')
tree.heading('#5',text="Prioridade")
tree.column("#5",minwidth=10,width=100, anchor = 'center')
tree.heading('#6',text="Status")
tree.column("#6",minwidth=10,width=125, anchor = 'center')
tree.place(x = 10, y = 250)


#Creating Radio Buttons for SQL search

search_1 = tk.IntVar()
search_1.set(1)

def ShowChoice():
    print(v.get())

tk.Radiobutton(tab2, variable = search_1, value = 1, bg = '#28A3CD', activebackground = '#28A3CD', borderwidth = 0, command = view_all_users).place(x = 195, y = 200)
tk.Radiobutton(tab2, variable = search_1, value = 2,  bg = '#28A3CD', activebackground = '#46B3D1', borderwidth = 0, relief = 'sunken', command = view_all_users_week).place(x = 355, y = 200)


#Search - Tab3


# Export Database - Tab 4

def export_as_csv():
    filename = str(entry_filename.get())
    myfilename = filename + '.csv'
    with open(myfilename, 'w') as f:
	    writer = csv.writer(f)
	    c.execute('SELECT * FROM usersdata')
	    data = c.fetchall()
	    writer.writerow(['idpedido','cliente','telefone','prioridade','data_entrada','data_prevista','horario_entrada','horario_saida','status'])
	    writer.writerows(data)
	    messagebox.showinfo(title = "Exportar Arquivo", message = 'Exportado para {}'.format(myfilename))



filename_raw_entry = StringVar()
entry_filename = Entry(tab5, textvariable = filename_raw_entry, width=40)
entry_filename.place(x = 120,y = 165)



#CSV GIF Button

def press(_):
	button_export1.config(image = csvpress, border = 0)
def release(_):
	button_export1.config(image = csvrelease, border = 0)

csvpress = PhotoImage(file = 'csv1.gif')
csvrelease = PhotoImage(file = 'csv.gif')

button_export1 = Button(tab5, image = csvrelease, border = 0, command=export_as_csv, background = '#119AC7', activebackground = '#119AC7')
button_export1.place(x = 105, y = 260)
button_export1.bind('<Enter>', press)
button_export1.bind('<Leave>', release)



# About TAB - Tab 5


#time()
window.mainloop()
