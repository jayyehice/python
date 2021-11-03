# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:49:45 2021

@author: Jay
"""

import tkinter as tk
import tkinter.ttk as tt



def Sel_Day():    
    print(date_chose.get())
    labchange.config(text = date_chose.get())


window = tk.Tk()
window.title('吳興教會財務報表')
window.resizable(False, False)#取消縮放視窗

labDate = tk.Label(window, text = '日期:', justify=tk.RIGHT, width=50)
labDate.place(x=10, y=10, width=50, height=20)

Date_list = ('2021-02-28','2021-02-21','2021-02-14')

#下拉式選單
date_chose = tt.Combobox(window, width=50, values=Date_list)
date_chose.place(x=70, y=10, width=100, height=20)

btn = tk.Button(window, text='確認', command = Sel_Day)
btn.place(x=70, y=50, width=50, height=20)

labchange = tk.Label(window, text = '請選擇日期', justify=tk.RIGHT, width=50)
labchange.place(x=70, y=100, width=70, height=20)

window.mainloop()



