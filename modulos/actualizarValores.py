from tkinter import *
from modulos.conexiondb import *
from datetime import datetime, date, timedelta
import http.client
import json
import time

# modulo de listado de assets
from modulos.tableAssets import *

def actualizarValores(app,asset,fechaDesde,fechaHasta):
    appikey = "gADpAYBU1rq4XS4D9By5n2BUXpd7KWCE"
    Label(app, text="Obteniendo Valores...",font=("Arial", 12)).pack(anchor='w')
    asset = asset.get()
    #verifica intervalo de fecha
    minDate = datetime.strptime(fechaDesde.get(), '%Y-%m-%d')- timedelta(days=1)
    maxDate = datetime.strptime(fechaHasta.get(), '%Y-%m-%d')+ timedelta(days=1)
    if minDate > maxDate:
        Label(app, text="Error en fechas...",font=("Arial", 12)).pack(anchor='w')
        return False
    # traigo el rango
    conn = http.client.HTTPSConnection("api.polygon.io")
    payload = ''
    headers = {}
    conn.request("GET", "/v2/aggs/ticker/"+asset+"/range/1/day/"+minDate.strftime('%Y-%m-%d')+"/"+maxDate.strftime('%Y-%m-%d')+"?adjusted=true&sort=asc&limit=365&apiKey="+appikey, payload, headers)

    res = conn.getresponse()
    data = json.loads(res.read())['results']
    for d in data:
        fecha = datetime.fromtimestamp(d["t"]/1000)
        cursor.execute("SELECT id FROM ASSETS_DAYS WHERE symbol = '"+asset+"' AND date = '"+fecha.strftime('%Y-%m-%d')+"'")
        rows = cursor.fetchall()
        if len(rows) == 0:
            sql = "INSERT INTO ASSETS_DAYS(symbol,date,v,vw,o,c,h,l,t,n) VALUES('"+asset+"','"+fecha.strftime('%Y-%m-%d')+"',"+str(d["v"])+","+str(d["vw"])+","+str(d["o"])+","+str(d["c"])+","+str(d["h"])+","+str(d["l"])+","+str(d["t"])+","+str(d["n"])+")"
            cursor.execute(sql)
            conexion.commit() 
    for i in app.winfo_children():
        if i.winfo_class() == "Frame":
            i.destroy()
    time.sleep(5)
    tableAssets(app)
    Label(app, text="Datos actualizados...",font=("Arial", 12)).pack(anchor='w')