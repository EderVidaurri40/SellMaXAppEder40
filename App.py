import tkinter as tk
from tkinter import ttk
#from tkfontawesome import icon_to_image
import sqlite3
#import tksvg
from datetime import datetime
#from googledrivefun import *


class DB():
    sqlconnection = sqlite3.connect('DBtienda.db')
    curs = sqlconnection.cursor()

class rootwindow():
   #Create Principal window and theme application 
  root = tk.Tk()
  root.title('SellMax')
  root.iconbitmap("images/store.ico")
  root.withdraw()
  root.tk.call("source", "azure.tcl")             
  root.tk.call("set_theme", "dark")
    
    #Principal size
  root.minsize(1100, 600)
  window_height = 600
  window_width = 1100
  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()
  x_cordinate = int((screen_width/2) - (window_width/2))
  y_cordinate = int((screen_height/2) - (window_height/2))
  root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
  
  for index  in [0, 1, 2]:
    root.rowconfigure(index=index, weight=1)
    root.columnconfigure(index=1, weight=1)
  
class login_window():
    
    #Create login and window theme 
    log = tk.Tk()
    log.title('Iniciar sesion')
    log.iconbitmap("images/store.ico")
    log.resizable(False,False)
    log.tk.call("source", "azure.tcl")
    log.tk.call("set_theme", "dark")
    
    #Set window size and appears always in the middle
    window_height = 500
    window_width = 350
    screen_width = log.winfo_screenwidth()
    screen_height = log.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    log.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
  
#Funciones de la ventana general. EN ESTA PARTE SE HACE EL CAMBIO DE FRAME EN LA MISMA VENTANA. SE OLVIDA Y LUEGO SE DESPLIEGAN LOS NUEVOS ELEMENTOS, SON DOS FUNCIONES
class rootfunction():
  def appearregis():
    dbview.searchercontainer.grid_forget()
    dbview.tableviewcontainer.grid_forget()
    dbview.managecontainer.grid_forget()
    dbview.boxvar.set('')
    dbview.tableview.delete(*dbview.tableview.get_children())
    dbview.tableview["show"]='tree'
    regisfunction.cancelbu()
    Registry.titlecontainer.grid(row=0, column=1, columnspan=2, padx=10, pady=(1, 1), sticky="nsew")
    Registry.treeviewcontainer.grid(row=1, column=1, columnspan=2, sticky="nsew")
    Registry.footercotainer.grid(row=2, column=1, columnspan=2, sticky="nsew")
     
  def appeardb():
    Registry.titlecontainer.grid_forget()
    Registry.treeviewcontainer.grid_forget()
    Registry.footercotainer.grid_forget()
    dbview.boxvar.set('')
    dbview.tableview.delete(*dbview.tableview.get_children())
    dbview.tableview["show"]='tree'
    regisfunction.cancelbu()
    dbview.searchercontainer.grid(row=0, column=1, sticky='sew')
    dbview.tableviewcontainer.grid(row=1, column=1, sticky='nsew')
    dbview.managecontainer.grid(row=2, column=1, sticky='nsew')
   
#Funciones de la ventana de consultas   
    
class dbfunction():
  def search(event):
    if dbview.boxvar.get() == "Clientes":
      dbview.tableview.delete(*dbview.tableview.get_children() )
      dbview.tableview["columns"] = ("1","2","3","4","5")
      dbview.tableview["show"]= 'headings' 
      dbview.tableview.column("1", width=20, anchor='c')
      dbview.tableview.column("2", width=20, anchor='c')
      dbview.tableview.column("3", width=20, anchor='c')
      dbview.tableview.column("4", width=20, anchor='c')
      dbview.tableview.column("5", width=20, anchor='c')
      dbview.tableview.heading("1", text='Id_cliente')
      dbview.tableview.heading("2", text='Nombre')
      dbview.tableview.heading("3", text='Apellido')
      dbview.tableview.heading("4", text='email')
      dbview.tableview.heading("4", text='Codigo_cliente')
      DB.curs.execute("SELECT * FROM Clientes")
      clientresult = DB.curs.fetchall()
      for row in clientresult:
        dbview.tableview.insert("", tk.END, values=row)
        
    elif dbview.boxvar.get() == "Productos": 
      dbview.tableview.delete(*dbview.tableview.get_children() )
      dbview.tableview["columns"] = ("1","2","3","4","5","6","7","8")
      dbview.tableview["show"]= 'headings' 
      dbview.tableview.column("1", width=20, anchor='c')
      dbview.tableview.column("2", width=20, anchor='c')
      dbview.tableview.column("3", width=20, anchor='c')
      dbview.tableview.column("4", width=20, anchor='c')
      dbview.tableview.column("5", width=20, anchor='c')
      dbview.tableview.column("6", width=20, anchor='c')
      dbview.tableview.column("7", width=20, anchor='c')
      dbview.tableview.column("8", width=20, anchor='c')
      dbview.tableview.heading("1", text='Id_producto')
      dbview.tableview.heading("2", text='Nombre')
      dbview.tableview.heading("3", text='Tipo')
      dbview.tableview.heading("4", text='Genero')
      dbview.tableview.heading("5", text='Codigo_producto')
      dbview.tableview.heading("6", text='Proveedor')
      dbview.tableview.heading("7", text='Talla')
      dbview.tableview.heading("8", text='Precio')
      DB.curs.execute("SELECT * FROM Productos")
      productresult = DB.curs.fetchall()
      for row1 in productresult:
        dbview.tableview.insert("", tk.END, values=row1)
        
    elif dbview.boxvar.get() == "Ventas":
      dbview.tableview.delete(*dbview.tableview.get_children() )
      dbview.tableview["columns"] = ("1","2","3","4","5","6")
      dbview.tableview["show"]= 'headings' 
      dbview.tableview.column("1", width=20, anchor='c')
      dbview.tableview.column("2", width=20, anchor='c')
      dbview.tableview.column("3", width=20, anchor='c')
      dbview.tableview.column("4", width=20, anchor='c')
      dbview.tableview.column("5", width=20, anchor='c')
      dbview.tableview.column("6", width=20, anchor='c')
      dbview.tableview.heading("1", text='Id_venta')
      dbview.tableview.heading("2", text='Nombre_prod')
      dbview.tableview.heading("3", text='Talla_prod')
      dbview.tableview.heading("4", text='Precio_prod')
      dbview.tableview.heading("5", text='Fecha')
      dbview.tableview.heading("6", text='Codigo_prod')
      DB.curs.execute("SELECT * FROM Ventas")
      productresult = DB.curs.fetchall()
      for row2 in productresult:
        dbview.tableview.insert("", tk.END, values=row2)
    
    elif dbview.boxvar.get() == "Usuarios":
      dbview.tableview.delete(*dbview.tableview.get_children() )
      dbview.tableview["columns"] = ("1","2","3","4","5")
      dbview.tableview["show"]= 'headings' 
      dbview.tableview.column("1", width=20, anchor='c')
      dbview.tableview.column("2", width=20, anchor='c')
      dbview.tableview.column("3", width=20, anchor='c')
      dbview.tableview.column("4", width=20, anchor='c')
      dbview.tableview.column("5", width=20, anchor='c')
      dbview.tableview.heading("1", text='Id_usuario')
      dbview.tableview.heading("2", text='Usuario')
      dbview.tableview.heading("3", text='Contraseña')
      dbview.tableview.heading("4", text='Nombre')
      dbview.tableview.heading("5", text='email')
      DB.curs.execute("SELECT * FROM usuarios")
      productresult = DB.curs.fetchall()
      for row3 in productresult:
        dbview.tableview.insert("", tk.END, values=row3)
    else: 
      pass
    
  def deleteregistry():
    if dbview.boxvar.get() == "Clientes":
      selectedrow = dbview.tableview.focus()
      idresult = dbview.tableview.set(selectedrow, "1")
      DB.curs.execute("DELETE FROM Clientes WHERE Id_cliente = ?", (idresult,) )
      DB.sqlconnection.commit()
      dbview.tableview.delete(selectedrow)
      
    elif dbview.boxvar.get() == "Productos":
      selectedrow1 = dbview.tableview.focus()
      idresult1 = dbview.tableview.set(selectedrow1, "1")
      DB.curs.execute("DELETE FROM Productos WHERE Id_producto = ?", (idresult1,) )
      DB.sqlconnection.commit()
      dbview.tableview.delete(selectedrow1) 
      
    elif dbview.boxvar.get() == "Ventas":
      selectedrow2 = dbview.tableview.focus()
      idresult2 = dbview.tableview.set(selectedrow2, "1")
      DB.curs.execute("DELETE FROM Ventas WHERE Id_venta = ?", (idresult2,) )
      DB.sqlconnection.commit()
      dbview.tableview.delete(selectedrow2)
      
    elif dbview.boxvar.get() == "Usuarios":
      selectedrow3 = dbview.tableview.focus()
      idresult3 = dbview.tableview.set(selectedrow3, "1")
      DB.curs.execute("DELETE FROM usuarios WHERE iduser = ?", (idresult3,) )
      DB.sqlconnection.commit()
      dbview.tableview.delete(selectedrow3)
        
    else:
      pass
  
#Funciones de la ventana de ventas
class regisfunction():
  def selectcod(self):
      DB.curs.execute("SELECT Nombre, Codigo_producto, Talla, Precio FROM Productos WHERE Codigo_producto = ?", (Registry.codprodentry.get(),))
      result = DB.curs.fetchall()
      for row in result:
        print(row)
        Registry.productview.insert("", tk.END, values=row)
      Registry.codprodentry.delete(0,'end')
    
      total = 0
      for item in Registry.productview.get_children():
        cell = float(Registry.productview.set(item, "#4"))
        total+=cell
      Registry.totalvarentry.set("$" + str(total))
      if total>0:
        Registry.regisbutton.config(state='normal')       
      
  def only_numbers(char):
        return char.isdigit()
    
  def cancelbu():
      Registry.codprodentry.delete(0,'end')
      Registry.totalvarentry.set('')    
      Registry.productview.delete(*Registry.productview.get_children() )
      Registry.regisbutton.config(state='disabled')
      
  def registcom():
      for line in Registry.productview.get_children():
        child1 = Registry.productview.set(line, "#1")
        child2 = Registry.productview.set(line, "#2")
        child3 = Registry.productview.set(line, "#3")
        child4 = Registry.productview.set(line, "#4")
        
        DB.curs.execute("INSERT INTO Ventas (Nombre_prod, Codigo_prod, Talla_prod, Precio_prod, Fecha) VALUES (?, ?, ?, ?, ?)", (child1, child2, child3, child4, datetime.date(datetime.now())))
        DB.sqlconnection.commit()
        regisfunction.cancelbu()
        
#Funciones de la ventana login   
class logfunction():
    
    def aparecer():
      rootwindow.root.deiconify() 
      #rootwindow.root.attributes('-zoomed', True) #Only for Linux!
      rootwindow.root.state('zoomed') #Only for Windows!!!
      login_window.log.destroy()
      
      
    def close():
        rootwindow.root.destroy()
        login_window.log.destroy()
        
    def validate():
        DB.curs.execute("SELECT user, pass FROM usuarios WHERE user=? AND pass = ?", (log_view.inuser.get(), log_view.inpass.get(), ))
        uservalidate=DB.curs.fetchall()
        if uservalidate:
           logfunction.aparecer()
        else:
          def acepterror():
            errorwindow.destroy()
            
          errorwindow = tk.Toplevel()
          errorwindow.title("Datos incorrectos")
          errorwindow.iconbitmap("images/store.ico")
          errorwindow.resizable(False, False)
          errorwindow.wait_visibility()
          errorwindow.grab_set_global()
          window_height = 200
          window_width = 400
          screen_width = errorwindow.winfo_screenwidth()
          screen_height = errorwindow.winfo_screenheight()
          x_cordinate = int((screen_width/2) - (window_width/2))
          y_cordinate = int((screen_height/2) - (window_height/2))
          errorwindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
          infolabel = tk.Label(errorwindow, text="El usuario y/o contraseña son incorrectos")
          infolabel.config(font=('Arial', 14))
          infolabel.place(x=40, y=50)
          okbutton = ttk.Button(errorwindow, text="Aceptar", command=acepterror)
          okbutton.place(x=150, y=130)         
#Esta es mi ventana de ventas
        
class Registry():
  
  menucontainer = ttk.Labelframe(rootwindow.root)
  menucontainer.grid(row=0,rowspan=3, column=0, sticky='nsew')
  menuimg = tk.PhotoImage(file = "images/cash-register-solid.png", master=menucontainer)
  regismenu = ttk.Button(menucontainer, width=5, image=menuimg, command=rootfunction.appearregis)
  regismenu.grid(row=0, column=0,pady=(80,1), sticky='s')
  dbimg = tk.PhotoImage(file= "images/database-solid.png", master=menucontainer)
  dbmenu = ttk.Button(menucontainer, width=5, image=dbimg, command=rootfunction.appeardb)
  dbmenu.grid(row=1, column=0,pady=30, sticky='n')
      
  stylebutton = ttk.Style()
  stylebutton.configure('my.TButton', font=('Arial', 31))
  styletreeview = ttk.Style()
  styletreeview.configure("Treeview.Heading", font=(None, 20))
  styletreeview.configure("Treeview", rowheight= 37,font=(None, 25))
      
  titlecontainer = tk.LabelFrame(rootwindow.root, borderwidth=0)
  titlecontainer.grid(row=0, column=1, columnspan=2, padx=10, pady=(1, 1), sticky="nsew")
    
  titlev = tk.Label(titlecontainer, text = "Registro de ventas")
  titlev.config(font =('Palace Script MT', 70))
  titlev.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="n")
    
  listlab = tk.Label(titlecontainer, text="Lista de productos")
  listlab.config(font=('Arial', 27))
  listlab.grid(row = 1,column=0, padx=1,  pady=(5,0), sticky='ws')
    
  codproduct = tk.Label(titlecontainer, text="Codigo producto:")
  codproduct.config(font=('Arial', 27))
  codproduct.grid(row = 1,column=2, pady=(1,0), sticky="es")
    
  validation = titlecontainer.register(regisfunction.only_numbers)
  codprodentry = ttk.Entry(titlecontainer, validate="key", validatecommand=(validation, '%S'))
  codprodentry.config(font=('Arial', 20), width=15)
  codprodentry.grid(row=1, column=3, padx=1, pady=(5,0), sticky="wse")
  codprodentry.bind('<Return>', regisfunction.selectcod)
    
  treeviewcontainer = tk.LabelFrame(rootwindow.root, borderwidth=0)
  treeviewcontainer.grid(row=1, column=1, columnspan=2, sticky="nsew")
  productview = ttk.Treeview(treeviewcontainer, height=5)
  productview.grid(row=0, column=0,padx=1, sticky="nsew")
  scrollview = ttk.Scrollbar(treeviewcontainer, orient="vertical", command= productview.yview)
  scrollview.grid(row = 0, column=1, sticky='ns')
  productview.configure(yscrollcommand=scrollview.set)
  productview["columns"] = ("1","2","3","4")
  productview["show"]= 'headings' 
  productview.column("1", width=30, anchor='c')
  productview.column("2", width=30, anchor='c')
  productview.column("3", width=30, anchor='c')
  productview.column("4", width=30, anchor='c')
  productview.heading("1", text='Nombre')
  productview.heading("2", text='Codigo')
  productview.heading("3", text='Talla')
  productview.heading("4", text='Precio')
    
  footercotainer=tk.LabelFrame(rootwindow.root, borderwidth=0)
  footercotainer.grid(row=2, column=1, columnspan=2, sticky="nsew")
    
  regisbutton = ttk.Button(footercotainer, text="Registrar", width=10, style = 'my.TButton', state='disabled', command=regisfunction.registcom)
  regisbutton.grid(row=0, column=0)
    
  cancelbutton = ttk.Button(footercotainer, text="Cancelar", style='my.TButton', command=regisfunction.cancelbu)
  cancelbutton.grid(row=0, column=1)
    
  totalab = tk.Label(footercotainer, text= "Total:")
  totalab.config(font=('Arial',31))
  totalab.grid(row = 0,column=2, sticky="e")
    
  totalvarentry = tk.StringVar()
  totalentr = ttk.Entry(footercotainer, textvariable=totalvarentry, state='disabled')
  totalentr.config(font=('Arial', 23))
  totalentr.grid(row=0, column=3, sticky="ew")
     
  for a in [0, 1]:
        menucontainer.columnconfigure(index = 0, weight=1)
        menucontainer.rowconfigure(index= a, weight=1)
    
      
  for b in [0, 1, 2, 3]:
        titlecontainer.columnconfigure(index = b, weight=1)
      
  for c in [0, 1]:
        titlecontainer.rowconfigure(index = c, weight=1)
      
  for d in [0]:
        treeviewcontainer.columnconfigure(index = d, weight=1)
        treeviewcontainer.rowconfigure(index= d, weight=1)
      
  for e in [0, 1, 2, 3, 4]:
        footercotainer.columnconfigure(index = e, weight=1)
        footercotainer.rowconfigure(index= 0, weight=1)
    
#Esta es mi ventana o elementos de la parte de las consultas
class dbview():
  stylebutton1 = ttk.Style()
  stylebutton1.configure('my1.TButton', font=('Arial', 28))
  
  searchercontainer = tk.LabelFrame(rootwindow.root, borderwidth=0)
  boxvar = tk.StringVar()
  tablebox = ttk.Combobox(searchercontainer, state='readonly',textvariable=boxvar, values=("Clientes", "Productos", "Ventas", "Usuarios"),)
  tablebox.bind("<<ComboboxSelected>>", dbfunction.search )
  tablebox.config(font=('Arial', 28))
  tablebox.grid(row=0, column=0,padx=20,pady=20, sticky='ws')

  tableviewcontainer = tk.LabelFrame(rootwindow.root, borderwidth=0)
  tableview = ttk.Treeview(tableviewcontainer)
  tableview.grid(row=0, column=0, sticky='nsew')
  yscrollview = ttk.Scrollbar(tableviewcontainer, orient="vertical", command= tableview.yview)
  yscrollview.grid(row=0, column=1, sticky='ns')
  tableview.configure(yscrollcommand=yscrollview.set)
  
  managecontainer = tk.LabelFrame(rootwindow.root, borderwidth=0)
  deletebutton = ttk.Button(managecontainer, text="Eliminar registro", style='my1.TButton', command=dbfunction.deleteregistry)
  deletebutton.grid(row=0,column=0,padx=100, sticky='e')

  for f in [0]:
    searchercontainer.columnconfigure(index=f, weight=1)
    searchercontainer.rowconfigure(index= f, weight=1)
  
  for g in [0]:
    tableviewcontainer.columnconfigure(index=g, weight=1)
    tableviewcontainer.rowconfigure(index=g, weight=1)
    managecontainer.columnconfigure(index=g, weight=1)
    managecontainer.rowconfigure(index=g, weight=1)
    
#Esta es mi venta de login
class log_view():
        
    boton = ttk.Button(login_window.log, text = 'INGRESAR', command=logfunction.validate, padding=(35,15))
    boton.place(x=100, y=350)
    
    imguser = tk.PhotoImage(file="images/circle-user-solid.png", master=login_window.log) #The "master" is so important. Not only for this case
    imgpaste = tk.Label(login_window.log, image= imguser)
    imgpaste.place(x= 120, y=40)
    
    lbuser = ttk.Label(login_window.log, text="USUARIO")
    lbuser.place(x=95, y=180)
    
    inuser = ttk.Entry(login_window.log)
    inuser.place(x=95,y=200, width=150, height=30)
    
    lbpass = ttk.Label(login_window.log, text="CONTRASEÑA")
    lbpass.place(x=95, y=240)
  
    inpass=ttk.Entry(login_window.log, show="*")
    inpass.place(x=95, y=260, width=150, height=30)
    
    login_window.log.protocol("WM_DELETE_WINDOW", logfunction.close)
   

    
    
if __name__ == "__main__":
  rootwindow.root.mainloop()
  login_window.log.mainloop()
    

   
        
    
    
    
