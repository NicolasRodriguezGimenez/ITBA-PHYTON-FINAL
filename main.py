#!/usr/bin/env python
# coding: utf-8

# In[1]:


from modulos.conexiondb import *

# modulo de listado de assets
from modulos.tableAssets import *

# modulo de actualizar valores
from modulos.actualizarValores import *

# modulo de resumen
from modulos.resumen import *

# modulo de grafico
from modulos.grafico import *


# In[2]:


def get_list_assets():
    
    cursor.execute("SELECT symbol FROM ASSETS")
    rows = cursor.fetchall()
    lista = []
    for row in rows:
        lista.append(row[0])
    return lista


# In[3]:


from tkinter import *
from tkinter import ttk

app = Tk()
# Configuración ventana
app.geometry("800x800")
app.title("TP Final ITBA")

# titulo
Label(app, text="Bienvenido al programa de visualización de assets",font=("Arial", 25)).pack()

# Actualización de valores 
# titulo
Label(app, text="Actualización de valores",font=("Arial", 18)).pack(anchor='w')
Label(app, text="Asset",font=("Arial", 14)).pack(anchor='w')
# asset
select_asset = StringVar()
combobox = ttk.Combobox(app, textvariable=select_asset,values = get_list_assets())
combobox.pack(anchor='w')
combobox.set(get_list_assets()[0])
# fecha desde
Label(app, text="Fecha desde (YYYY-MM-DD)",font=("Arial", 14)).pack(anchor='w')
fechaDesde = StringVar()
fechaDesde_entry = Entry(app,textvariable=fechaDesde).pack(anchor='w')
# fecha hasta
Label(app, text="Fecha hasta (YYYY-MM-DD)",font=("Arial", 14)).pack(anchor='w')
fechaHasta = StringVar()
fechaHasta_entry = Entry(app,textvariable=fechaHasta).pack(anchor='w')
# boton
boton = Button(app, text="Actualizar",font=("Arial", 16),command=lambda: actualizarValores(app,select_asset,fechaDesde,fechaHasta)).pack(anchor='w')
# tabla assets
tableAssets(app)

# Visualización de valores 
# titulo
Label(app, text="Visualización de valores",font=("Arial", 18)).pack(anchor='w')
Label(app, text="Asset",font=("Arial", 14)).pack(anchor='w')
# asset
select_asset2 = StringVar()
combobox = ttk.Combobox(app, textvariable=select_asset2,values = get_list_assets())
combobox.pack(anchor='w')
combobox.set(get_list_assets()[0])
# fecha desde
Label(app, text="Fecha desde (YYYY-MM-DD)",font=("Arial", 14)).pack(anchor='w')
fechaDesde2 = StringVar()
fechaDesde_entry2 = Entry(app,textvariable=fechaDesde2).pack(anchor='w')
# fecha hasta
Label(app, text="Fecha hasta (YYYY-MM-DD)",font=("Arial", 14)).pack(anchor='w')
fechaHasta2 = StringVar()
fechaHasta_entry2 = Entry(app,textvariable=fechaHasta2).pack(anchor='w')
# botones
boton = Button(app, text="Resumen",font=("Arial", 16),command=lambda: resumen(app,select_asset2,fechaDesde2,fechaHasta2)).pack(anchor='w')
boton = Button(app, text="Grafico",font=("Arial", 16),command=lambda: grafico(app,select_asset2,fechaDesde2,fechaHasta2)).pack(anchor='w')






app.mainloop()


# In[ ]:




