# Importar Bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import sqlite3

# Desarrollo de la Interfaz grafica
root=Tk()
root.title("Farmacia")
root.geometry("600x350")

id=StringVar()
nombre=StringVar()
laboratorio=StringVar()
precio=StringVar()

def crearBD():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()

	try:
		cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
						ID INTEGER PRIMARY KEY AUTOINCREMENT,
						NOMBRE VARCHAR (50) NOT NULL,
						LABORATORIO VARCHAR (50) NOT NULL,
						PRECIO INT NOT NULL)
						''')
		messagebox.showinfo("CONEXION","Base de Datos Creada exitosamente")
	except:
		messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")

def eliminarBD():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()
	if messagebox.askyesno(message="¿Los Datos se perderan definitivamente, Desea continuar?", title="ADVERTENCIA"):
		cursor.execute("DROP TABLE producto")
	else:
		pass
	limpiarCampos()
	mostrar()

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	id.set("")
	nombre.set("")
	laboratorio.set("")
	precio.set("")

def mensaje():
	acerca='''
	Sistema de ventas Farmacia
	Version 1.0
	Tecnología Python Tkinter
	'''
	messagebox.showinfo(title="INFORMACION", message=acerca)

################################ Métodos CRUD ##############################

def crear():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()
	try:
		datos=nombre.get(),laboratorio.get(),precio.get()
		cursor.execute("INSERT INTO producto VALUES(NULL,?,?,?)", (datos))
		conexion.commit()
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BD")
		pass
	limpiarCampos()
	mostrar()

def mostrar():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()
	registros=tree.get_children()
	for elemento in registros:
		tree.delete(elemento)

	try:
		cursor.execute("SELECT * FROM producto")
		for row in cursor:
			tree.insert("",0,text=row[0], values=(row[1],row[2],row[3]))
	except:
		pass

                ################################## Tabla ################################
tree=ttk.Treeview(height=10, columns=('#0','#1','#2'))
tree.place(x=0, y=130)
tree.column('#0',width=100)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre del Producto", anchor=CENTER)
tree.heading('#2', text="Laboratorio", anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#3', text="Precio", anchor=CENTER)

def seleccionarUsandoClick(event):
	item=tree.identify('item',event.x,event.y)
	id.set(tree.item(item,"text"))
	nombre.set(tree.item(item,"values")[0])
	laboratorio.set(tree.item(item,"values")[1])
	precio.set(tree.item(item,"values")[2])

tree.bind("<Double-1>", seleccionarUsandoClick)



def actualizar():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()
	try:
		datos=nombre.get(),laboratorio.get(),precio.get()
		cursor.execute("UPDATE producto SET NOMBRE=?, LABORATORIO=?, PRECIO=?, WHERE ID="+id.get(), (datos))
		conexion.commit()
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
		pass
	limpiarCampos()
	mostrar()

def borrar():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()
	try:
		if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
			cursor.execute("DELETE FROM producto WHERE ID="+id.get())
			conexion.commit()
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
		pass
	limpiarCampos()
	mostrar()

###################### Colocar widgets en la VISTA ######################
########## Creando Los menus ###############
menubar=Menu(root)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/Conectar Base de Datos", command=crearBD)
menubasedat.add_command(label="Eliminar Base de Datos", command=eliminarBD)
menubasedat.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)

############## Creando etiquetas y cajas de texto ###########################
e1=Entry(root, textvariable=id)

l2=Label(root, text="Nombre")
l2.place(x=20,y=10)
e2=Entry(root, textvariable=nombre, width=50)
e2.place(x=100, y=10)

l3=Label(root, text="Laboratorio")
l3.place(x=20,y=40)
e3=Entry(root, textvariable=laboratorio)
e3.place(x=100, y=40)

l4=Label(root, text="Precio")
l4.place(x=280,y=40)
e4=Entry(root, textvariable=precio, width=10)
e4.place(x=320, y=40)

l5=Label(root, text="$")
l5.place(x=380,y=40)

################# Creando botones ###########################

b1=Button(root, text="Crear Registro", command=crear)
b1.place(x=50, y=90)
b2=Button(root, text="Modificar Registro", command=actualizar)
b2.place(x=180, y=90)
b3=Button(root, text="Mostrar Lista", command=mostrar)
b3.place(x=320, y=90)
b4=Button(root, text="Eliminar Registro",bg="red", command=borrar)
b4.place(x=450, y=90)


root.config(menu=menubar)


root.mainloop()