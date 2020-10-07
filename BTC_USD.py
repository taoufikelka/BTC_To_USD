
# BTC to USD, GUI with Tkinter

import Tkinter as tk
import time
import requests
import json

class App():

    def __init__(self):
     self.root = tk.Tk()
     self.root.title("Btc to USD")
     self.icon = tk.Image("photo", file="BTC_USD_files/BtcToUsd.png")
     self.root.tk.call('wm','iconphoto',self.root._w,self.icon)
     self.root.resizable(width=False, height=False)
     self.label1 = tk.Label(text="", padx=8, pady=8)
     self.label1.pack()
     self.label2 = tk.Label(text="", padx=8, pady=8)
     self.label2.pack()
     self.update()
     self.root.mainloop()

    def update_price(self):
     r1 = requests.get("https://api.coindesk.com/site/headerdata.json", headers={'Accept': 'application/json'})
     r2 = requests.get("https://blockchain.info/ticker", headers={'Accept': 'application/json'})
     j1 = json.loads(r1.text)
     j2 = json.loads(r2.text)
     nowprice = "Coindesk : "+str(j1['bpi']['USD']['rate_float'])+" $\nBlockchain : "+str(j2['USD']['last'])+" $"
     self.label2.configure(text=nowprice,font=("Times",35,"bold italic"))
     self.root.after(1000, self.update_price)
    
    def update_time(self):
     self.label1.configure(text=time.strftime("%H:%M"),font=("Times",35,"bold"))
     self.root.after(1000, self.update_time)
    
    def update(self):
     self.update_time()
     self.update_price()

app=App()
