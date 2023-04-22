import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql


# Crear Funciones
# -------------------------------------------------------------

def insertarDatos():
    try:
        bd = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='Python_TKinter_PyMySQL'
        )
        cursor = bd.cursor()
        
        # Consulta SQL con parámetros
        sql = "INSERT INTO registro(id, nombre, apellido_paterno, apellido_materno, cedula_identidad, email) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (id1.get() ,nom.get(), apeP.get(), apeM.get(), ci.get(), email.get())
        
        # Ejecución segura de la consulta
        cursor.execute(sql, valores)
        bd.commit()
        nom.delete(0, 'end')
        apeP.delete(0, 'end')
        apeM.delete(0, 'end')
        ci.delete(0, 'end')
        email.delete(0, 'end')
        id1.delete(0, 'end')
        show()
        messagebox.showinfo(message='Registro Exitoso', title='Aviso')
    except pymysql.Error as e:
        # Mensaje de error en caso de fallo en la conexión o ejecución de la consulta
        messagebox.showinfo(message='Error en la conexión o consulta: {}'.format(str(e)), title='Aviso')
        bd.rollback()
    finally:
        cursor.close()
        bd.close()


def eliminar():
    if messagebox.askyesno("Confirmar eliminación", "¿Está seguro que desea eliminar el registro?"):
        try:
            bd = pymysql.connect(
                host='localhost',
                user='root',
                passwd='',
                db='Python_TKinter_PyMySQL'
            )
            cursor = bd.cursor()

            # Consulta SQL con parámetros
            sql = "DELETE FROM registro WHERE id=%s"

            # Ejecución segura de la consulta
            cursor.execute(sql, (id1.get(),))
            bd.commit()
            nom.delete(0, 'end')
            apeP.delete(0, 'end')
            apeM.delete(0, 'end')
            ci.delete(0, 'end')
            email.delete(0, 'end')
            id1.delete(0, 'end')
            show()
            messagebox.showinfo(message='Se Elimino el Registro', title='Aviso')
        except pymysql.Error as e:
            # Mensaje de error en caso de fallo en la conexión o ejecución de la consulta
            messagebox.showinfo(message='No se Elimino el Registro {}'.format(str(e)), title='Aviso')
            bd.rollback()
        finally:
            cursor.close()
            bd.close()
    else:
        # Acciones a realizar si el usuario decide no eliminar el registro
        pass


def actualizar():
    try:
        bd = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='Python_TKinter_PyMySQL'
        )
        cursor = bd.cursor()

        # Consulta SQL con parámetros
        sql = "UPDATE registro SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, cedula_identidad=%s, email=%s WHERE id=%s"

        # Ejecución segura de la consulta
        cursor.execute(sql, (nom.get(), apeP.get(), apeM.get(), ci.get(), email.get(), id1.get()))
        bd.commit()
        nom.delete(0, 'end')
        apeP.delete(0, 'end')
        apeM.delete(0, 'end')
        ci.delete(0, 'end')
        email.delete(0, 'end')
        id1.delete(0, 'end')
        show()
        messagebox.showinfo(message='Se actualizó el registro', title='Aviso')
    except pymysql.Error as e:
        # Mensaje de error en caso de fallo en la conexión o ejecución de la consulta
        messagebox.showinfo(message='No se actualizó el registro: {}'.format(str(e)), title='Aviso')
        bd.rollback()
    finally:
        cursor.close()
        bd.close()


def consulta():
    if(id1.get()==""):
        messagebox.showinfo("Obteniendo Datos de Consulta")
    else:
        try:
            bd = pymysql.connect(
                host='localhost',
                user='root',
                passwd='',
                db='Python_TKinter_PyMySQL'
            )
            cursor = bd.cursor()
            cursor.execute("SELECT * FROM registro WHERE id=%s", (id1.get(),))

            nom.delete(0, 'end')
            apeP.delete(0, 'end')
            apeM.delete(0, 'end')
            ci.delete(0, 'end')
            email.delete(0, 'end')

            row = cursor.fetchone()
            if row:
                nom.insert(0, row[1])
                apeP.insert(0, row[2])
                apeM.insert(0, row[3])
                ci.insert(0, row[4])
                email.insert(0, row[5])
            else:
                messagebox.showinfo("Aviso", "No se encontró ningún registro con ese ID")

            bd.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", "Ocurrió un error en la consulta: {}".format(e))


def show():
    bd = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='Python_TKinter_PyMySQL'
    )
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM registro")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertarDatos = f"{row[0]} {row[1]} {row[2]} {row[3]}"
        list.insert(list.size() + 1, insertarDatos)

    bd.close()


def salir():
    ventana.destroy()


# Crear la ventana
# -------------------------------------------------------------
ventana = tk.Tk()
# Agregar título
ventana.title("Formulario de Registro")
# Establecer tamaño de la ventana
ventana.geometry("355x620")
# No permitir cambiar el tamaño de la ventana
ventana.resizable(False, False)
# Color de Fondo
ventana.configure(background="light cyan")
# Cargamos una imagen utilizando el método PhotoImage() y especificando la ruta de la imagen en el argumento file
imagen = tk.PhotoImage(file='../Imagenes/tkinter.png')
# Utilizamos el método subsample() para reducir el tamaño de la imagen por un factor de 6
imagen = imagen.subsample(6, 6)
# Creamos una etiqueta con el método Label() y especificando la imagen en el argumento image y el color de fondo de la imagen
label = tk.Label(image=imagen, bg="light cyan")
# Empaquetamos la etiqueta dentro de la ventana con el método pack()
label.place(x=1, y=1)

# Crear Etiquetas y Cuadros de Textos
# --------------------------------------------------------------
# Insertando etiquetas 'Id'
e0 = tk.Label(ventana, text='Id', bg='gray', fg='white')
e0.place(x=10, y=imagen.height() + 20)
# Cuadro de texto que almacena el 'Id'
id1 = tk.Entry(ventana, width=23)
id1.place(x=10, y=imagen.height() + 50)

# Insertando etiquetas 'Nombre'
e1 = tk.Label(ventana, text='Nombre', bg='gray', fg='white')
e1.place(x=10, y=imagen.height() + 90)
# Cuadro de texto que almacena el 'Nombre'
nom = tk.Entry(ventana, width=23)
nom.place(x=10, y=imagen.height() + 120)

# Insertando etiquetas 'Apellido Paterno'
e2 = tk.Label(ventana, text='Apellido Paterno', bg='gray', fg='white')
e2.place(x=10, y=imagen.height() + 160)
# Cuadro de texto que almacena el 'Apellido Paterno'
apeP = tk.Entry(ventana, width=23)
apeP.place(x=10, y=imagen.height() + 190)

# Insertando etiquetas 'Apellido Materno'
e3 = tk.Label(ventana, text='Apellido Materno', bg='gray', fg='white')
e3.place(x=10, y=imagen.height() + 230)
# Cuadro de texto que almacena el 'Apellido Materno'
apeM = tk.Entry(ventana, width=23)
apeM.place(x=10, y=imagen.height() + 260)

# Insertando etiquetas 'Cedula de Identidad'
e4 = tk.Label(ventana, text='Cedula de Identidad', bg='gray', fg='white')
e4.place(x=10, y=imagen.height() + 300)
# Cuadro de texto que almacena el 'Cedula de Identidad'
ci = tk.Entry(ventana, width=23)
ci.place(x=10, y=imagen.height() + 330)

# Insertando etiquetas 'Email'
e5 = tk.Label(ventana, text='Email', bg='gray', fg='white')
e5.place(x=10, y=imagen.height() + 370)
# Cuadro de texto que almacena el 'Email'
email = tk.Entry(ventana, width=23)
email.place(x=10, y=imagen.height() + 400)

# Crear Botones
# -------------------------------------------------------------
# Insertando Boton 'Registrar'
boton1 = tk.Button(ventana, text='Registrar', fg='Black', width=15, command=insertarDatos)
boton1.place(x=40, y=imagen.height() + 440)

# Insertando Boton 'Consultar'
boton2 = tk.Button(ventana, text='Consultar', fg='Black', width=15, command=consulta)
boton2.place(x=boton1.winfo_x() + boton1.winfo_width() + 180, y=imagen.height() + 440)

# # Insertando Boton 'Actualizar'
boton3 = tk.Button(ventana, text='Actualizar', fg='Black', width=15, command=actualizar)
boton3.place(x=40, y=imagen.height() + 470)

# # Insertando Boton 'Eliminar'
boton4 = tk.Button(ventana, text='Eliminar', fg='Black', width=15, command=eliminar)
boton4.place(x=boton3.winfo_x() + boton3.winfo_width() + 180, y=imagen.height() + 470)

# # Insertando Boton 'Salir'
boton5 = tk.Button(ventana, text='Salir', fg='red', width=15, font=('Arial', 8, 'bold'), command=salir)
boton5.place(x=40, y=imagen.height() + 500)

# # Insertando Boton 'Show'
boton6 = tk.Button(ventana, text='Ver DataBase', fg='blue', width=15, font=('Arial', 8, 'bold'), command=show)
boton6.place(x=boton5.winfo_x() + boton5.winfo_width() + 180, y=imagen.height() + 500)

# Crear Lista
# -------------------------------------------------------------
list = Listbox(ventana)
list.configure(width=30, height=25)
list.place(x=160, y=100)

# -------------------------------------------------------------
# Ejecutar el bucle principal de eventos
ventana.mainloop()
