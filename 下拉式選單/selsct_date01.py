# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:49:45 2021

@author: Jay
"""

import tkinter as tk
import tkinter.ttk as tt



def Sel_Day():    
    print(comGrade.get())


window = tk.Tk()
window.title('吳興教會財務報表')
window.resizable(False, False)

labDate = tk.Label(window, text = '日期:', justify=tk.RIGHT, width=50)
labDate.place(x=10, y=10, width=50, height=20)

Date_list = ('2021-02-28','2021-02-21','2021-02-14')

comGrade = tt.Combobox(window, width=50, values=Date_list)
comGrade.place(x=70, y=10, width=100, height=20)

btn = tk.Button(window, text='確認', command = Sel_Day)
btn.place(x=70, y=50, width=50, height=20)

window.mainloop()



