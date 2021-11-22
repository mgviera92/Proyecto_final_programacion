# Importar Bibliotecas
from tkinter import *
import tkinter as tk	
from tkinter import messagebox as mb
from tkinter import ttk 
import sqlite3

conn=sqlite3.connect('inventario_farmacia.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS empleados(Nombre TEXT,Apellido TEXT ,Usuario TEXT,Contraseña TEXT)")
	conn.commit()
	c.close()
	conn.close()

create_table()

ventana=tk.Tk()
ventana.title("_Mi primer Login_")	#Titulo de la ventana principal
ventana.geometry("280x450+300+250")	#Tamaño de nuestra ventana Principal
	
color='#c5e2f6'			#Codigo HEX del color de fondo usado
ventana['bg']=color		#Definimos nuestra ventana 'bg' con el valor 'color'

Label(ventana,bg=color,text="Login",font=("Arial Black",16)).pack()	#Mostramos texto 'Login'

#Abrir imagen para ventana principal
					#Abrimos la imagen 'logo.png'
	#Redimensionamos la imagen a 180x180
				#Le damos nombre a nuestra imagen redimensionada (photoImg)
		#Mostramos la imagen en nuestra ventana
#Abrir imagen para ventana de registro
				#Abrimos la imagen 'rak.jpg'
	#Redimensionamos la imagen
				#Le damos nombre a nuestra imagen redimensionada (photo_reg)
#Cajas de nuestra ventana Principal
Label(ventana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Usuario:'
caja1=Entry(ventana,font=("Arial",10))										#Creamos una caja de texto 'caja1'
caja1.pack()																#Posicion de la 'caja1'
Label(ventana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña:'
caja2=Entry(ventana,show="*")												#Creamos la 'caja2' (contraseña)
caja2.pack()																#Posicion de 'caja2'

db=sqlite3.connect('inventario_farmacia.db')		#Nos conectamos a nuestra base de datos 'login.db'
c=db.cursor()						#Establecemos un cursor

def login():				#Funcion login ... Nos permitira comprobar 'usuario' y 'contraseña' con la base de datos
	usuario=caja1.get()		#Obtenemos el valor de la 'caja1' (usuario)
	contr=caja2.get()		#Obtenemos el valor de la 'caja2' (contraseña)
	c.execute('SELECT * FROM empleados WHERE Usuario = ? AND Contraseña = ?',(usuario,contr))	#Seleccionamos datos '(usuario,contr)'
	if c.fetchall():
		mb.showinfo(title="Login Correcto",message="Usuario y contraseña correctos")		#Mostramos 'Login Correcto'
		ventana.destroy()
	else:
		mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")	#Mostramos 'Login incorrecto'
	#c.close()

def nuevaVentana():							#Funcion nuevaVentana ... Nos permitira el registro de nuevos usuarios
	newVentana=tk.Toplevel(ventana)			#Definimos 'newVentana'
	newVentana.title("Registro de Usuario")	#Le damos el titulo 'Registro de Usuario'
	newVentana.geometry("300x290+800+250")	#Tamaño de la ventana
	newVentana['bg']=color					#Definimos newVentana 'bg' con el valor de 'color'
	
	labelExample=tk.Label(newVentana,text="Registro : ",bg=color,font=("Arial Black",12)).pack(side="top")	#Texto 'Registro'
	

	Label(newVentana,text="Nombre : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Nombre:'
	caja3=Entry(newVentana)															#Creamos 'caja3' (Nombre)
	caja3.pack()
	Label(newVentana,text="Apellidos : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Apellidos'
	caja4=Entry(newVentana)															#Creamos 'caja4' (Apellidos)
	caja4.pack()
	Label(newVentana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Usuario'
	caja5=Entry(newVentana)															#Creamos 'caja5' (Usuario)
	caja5.pack()
	Label(newVentana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña'
	caja6=Entry(newVentana,show="*")												#Creamos 'caja6' (Contraseña)
	caja6.pack()	
	Label(newVentana,text="Repita la Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Repita la Contraseña'
	caja7=Entry(newVentana,show="*")															#Creamos 'caja7' 
	caja7.pack()
	def registro():				#Funcion registro ... Nos permitira escribir los datos a nuestra base de datos
		Nombre=caja3.get()		#Obtenemos el valor de 'caja3'
		Apellido=caja4.get()	#Obtenemos el valor de 'caja4'
		Usr_reg=caja5.get()		#Obtenemos el valor de 'caja5'
		Contra_reg=caja6.get()	#Obtenemos el valor de 'caja6'
		Contra_reg_2=caja7.get() #Obtenemos el valor de 'caja7'
		if(Contra_reg==Contra_reg_2):		#Esta condicion nos permite saber si las contraseñas coinciden
			#El siguiente comando es el encargado de insertar los datos obtenidos en el registro
			c.execute("INSERT INTO empleados values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
			db.commit()			#Confirmamos los datos
			mb.showinfo(title="Registro Correcto",message="Hola "+Nombre+" "+Apellido+" ¡¡ \nSu registro fue exitoso.")
			newVentana.destroy()		#Cerramos la ventana de registro
		else:	#Se ejecutara si las contraseñas no coinciden
			mb.showerror(title="Contraseña Incorrecta",message="Error¡¡¡ \nLas contraseñas no coinciden.")	#Mostramos un mensaje

	#El siguiente comando (boton) nos permite llamar a la funcion registro
	buttons=tk.Button(newVentana,text="Registrar ¡",command=registro,bg=color,font=("Arial Rounded MT Bold",10)).pack(side="bottom")
	
Label(ventana,text=" ",bg=color,font=("Arial",10)).pack()		#Solo es una linea vacia ... (lo use para separar el boton) 
Button(text=" ENTRAR ",command=login,bg='#a6d4f2',font=("Arial Rounded MT Bold",10)).pack()		#Boton ==> funcion 'login'
Label(ventana,text=" ",bg=color,font=("Arial Black",10)).pack()
Label(ventana,text="No tienes una cuenta ? : ",bg=color,font=("Arial Black",10)).pack()		#Simple texto
#La siguiente linea (boton) nos llama ala funcion 'nuevaVentana' ==> ( ventana de registro)
boton1=Button(ventana,text="REGISTRO",bg='#a6d4f2',command=nuevaVentana,font=("Arial Rounded MT Bold",10)).pack()

ventana.mainloop()
# Desarrollo de la Interfaz grafica


root=Tk()
root.title("Farmacia")
root.geometry("600x400")

idProducto=StringVar()
nombre=StringVar()
laboratorio=StringVar()
precio=StringVar()

def crearBD():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()

	try:
		cursor.execute ("""CREATE TABLE IF NOT EXISTS productos(
						idProducto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
						nombre VARCHAR(50) NOT NULL, 
						laboratorio VARCHAR(50) NOT NULL, 
						precio INT NOT NULL)""")
						

		mb.showinfo("CONEXION","Base de Datos Creada exitosamente")
	except:
		mb.showinfo("CONEXION", "Conexión exitosa con la base de datos")
	

def eliminarBD():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()
	if mb.askyesno(message="¿Los Datos se perderan definitivamente, Desea continuar?", title="ADVERTENCIA"):
		cursor.execute("DROP TABLE productos")
	else:
		pass
	limpiarCampos()
	mostrar()

def salirAplicacion():
	valor=mb.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	idProducto.set("")
	nombre.set("")
	laboratorio.set("")
	precio.set("")

def mensaje():
	acerca='''
	Sistema de ventas Farmacia
	Version 1.0
	Tecnología Python Tkinter
	'''
	mb.showinfo(title="INFORMACION", message=acerca)

################################ Métodos CRUD ##############################

def crear():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()
	try:
		datos=nombre.get(),laboratorio.get(),precio.get()
		cursor.execute("INSERT INTO productos VALUES(NULL,?,?,?)", (datos))
		conexion.commit()
	except:
		mb.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BD")
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
		cursor.execute("SELECT * FROM productos")
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
	idProducto.set(tree.item(item,"text"))
	nombre.set(tree.item(item,"values")[0])
	laboratorio.set(tree.item(item,"values")[1])
	precio.set(tree.item(item,"values")[2])

tree.bind("<Double-1>", seleccionarUsandoClick)

def actualizar():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()
	try:
		datos=nombre.get(),laboratorio.get(),precio.get()
		cursor.execute("UPDATE productos SET nombre=?, laboratorio=?, precio=?, WHERE idProducto="+idProducto.get(), (datos))
		conexion.commit()
	except:
		mb.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
		pass
	limpiarCampos()
	mostrar()

def borrar():
	conexion=sqlite3.connect("inventario_farmacia.db")
	cursor=conexion.cursor()
	try:
		if mb.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
			cursor.execute("DELETE FROM productos WHERE idProducto="+idProducto.get())
			conexion.commit()
	except:
		mb.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
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
e1=Entry(root, textvariable=idProducto)

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