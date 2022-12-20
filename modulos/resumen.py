from tkinter import *
from modulos.conexiondb import *

def resumen(app,asset,fechaDesde,fechaHasta):
    app_resumen = Tk()
    app_resumen.geometry("900x800")
    from  tkinter import ttk

    Label(app_resumen, text=asset.get(),font=("Arial", 25)).pack()

    table_asset_frame = Frame(app_resumen)
    table_asset_frame.pack(anchor='w')

    table_asset = ttk.Treeview(table_asset_frame, height=100)

    table_asset['columns'] = ('Date', 'v', 'vw','o','c','h','l','n')
    
    table_asset.column("#0", width=0,  stretch=NO)
    table_asset.column("Date",anchor=CENTER, width=100)
    table_asset.column("v",anchor=CENTER, width=110)
    table_asset.column("vw",anchor=CENTER, width=110)
    table_asset.column("o",anchor=CENTER, width=110)
    table_asset.column("c",anchor=CENTER, width=110)
    table_asset.column("h",anchor=CENTER, width=110)
    table_asset.column("l",anchor=CENTER, width=110)
    table_asset.column("n",anchor=CENTER, width=110)


    #headings
    table_asset.heading("#0",text="",anchor=CENTER)
    table_asset.heading("Date",text="Fecha",anchor=CENTER)
    table_asset.heading("v",text="Volumen",anchor=CENTER)
    table_asset.heading("vw",text="VWAP (Precio prom. ponderado por volumen)",anchor=CENTER)
    table_asset.heading("o",text="Precio de apertura",anchor=CENTER)
    table_asset.heading("c",text="Precio de cierre",anchor=CENTER)
    table_asset.heading("h",text="Máximo",anchor=CENTER)
    table_asset.heading("l",text="Minimo",anchor=CENTER)
    table_asset.heading("n",text="Número de transacciones",anchor=CENTER)
    
    # assets
    
    cursor.execute("SELECT date, v, vw,o,c,h,l,n FROM ASSETS_DAYS WHERE symbol = '"+asset.get()+"'  and date >= '"+fechaDesde.get()+"' and date <= '"+fechaHasta.get()+"' ORDER BY date DESC")
    rows = cursor.fetchall()
    for row in rows:
        table_asset.insert(parent='',index='end',text='',values=(row))

    table_asset.pack()