from tkinter import *
from tkinter import ttk
from modulos.conexiondb import *

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


import pandas as pd

def grafico(app,asset,fechaDesde,fechaHasta):
    app_resumen = Tk()
    app_resumen.geometry("1000x1000")
    from  tkinter import ttk
    Label(app_resumen, text=asset.get(),font=("Arial", 25)).pack()
    Label(app_resumen, text=fechaDesde.get() + " - " +fechaHasta.get(),font=("Arial", 25)).pack()
    
    df = pd.read_sql("SELECT date, v, vw,o,c,h,l,n FROM ASSETS_DAYS WHERE symbol = '"+asset.get()+"'  and date >= '"+fechaDesde.get()+"' and date <= '"+fechaHasta.get()+"' ORDER BY date ASC", conexion)
    
    
    # create a figure
    figure = Figure(figsize=(8, 6), dpi=100)


    # create FigureCanvasTkAgg object
    figure_canvas = FigureCanvasTkAgg(figure, app_resumen)

    # create the toolbar
    NavigationToolbar2Tk(figure_canvas, app_resumen)
    
    # create axes
    axes = figure.add_subplot(221)

    # create the barchart
    axes.plot(df['date'], df['c'], 'r', label='Cierre')
    axes.plot(df['date'], df['o'], 'b', label='Apertura')
    axes.set_title('Precio de Apertura vs Precio de Cierre')
    axes.set_ylabel('$')
    axes.set_xlabel('Dias')
    axes.tick_params(axis='x', labelrotation=90)
    axes.legend()
    
     # create axes
    axes = figure.add_subplot(222)

    # create the barchart
    axes.plot(df['date'], df['l'], 'r', label='Minimo')
    axes.plot(df['date'], df['h'], 'b', label='Maximo')
    axes.set_title('Precio Minimo vs Precio Maximo')
    axes.set_ylabel('$')
    axes.set_xlabel('Dias')
    axes.tick_params(axis='x', labelrotation=90)
    axes.legend()
    
    # create axes
    axes = figure.add_subplot(223)
    axes.fill_between(df['date'], df['v'])
    axes.set_title('Volumen de transacciones')
    axes.set_ylabel('Volumen')
    axes.set_xlabel('Dias')
    axes.tick_params(axis='x', labelrotation=90)

    figure.tight_layout()
    figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    
    
