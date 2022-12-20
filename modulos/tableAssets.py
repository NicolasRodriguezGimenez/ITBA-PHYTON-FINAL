from  tkinter import *

# modulo de conexión
from modulos.conexiondb import *

def tableAssets(main):
    from  tkinter import ttk


    table_asset_frame = Frame(main)
    table_asset_frame.pack(anchor='w')

    table_asset = ttk.Treeview(table_asset_frame)

    table_asset['columns'] = ('Symbol', 'Company Name', 'Industry','FechaDesde','FechaHasta')
    
    table_asset.column("#0", width=0,  stretch=NO)
    table_asset.column("Symbol",anchor=CENTER, width=80)
    table_asset.column("Company Name",anchor=CENTER,width=120)
    table_asset.column("Industry",anchor=CENTER,width=200)
    table_asset.column("FechaDesde",anchor=CENTER,width=190)
    table_asset.column("FechaHasta",anchor=CENTER,width=190)

    #headings
    table_asset.heading("#0",text="",anchor=CENTER)
    table_asset.heading("Symbol",text="Asset",anchor=CENTER)
    table_asset.heading("Company Name",text="Compania",anchor=CENTER)
    table_asset.heading("Industry",text="Industria",anchor=CENTER)
    table_asset.heading("FechaDesde",text="Fecha desde",anchor=CENTER)
    table_asset.heading("FechaHasta",text="Fecha hasta",anchor=CENTER)
    
    # assets
    
    cursor.execute("SELECT A.symbol, A.company_name, A.industry, AD.minDate,AD.maxDate FROM ASSETS as A, (SELECT symbol,min(date) as minDate,max(date) as maxDate FROM ASSETS_DAYS GROUP BY symbol) as AD where A.symbol = AD.symbol")
    rows = cursor.fetchall()
    for row in rows:
        if row[3] is not None:
            fechaDesde = row[3]
        else:
            fechaDesde = "---"
        if row[4] is not None:
            fechaHasta = row[4]
        else:
            fechaHasta = "---"
        table_asset.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],fechaDesde,fechaHasta))

    table_asset.pack()