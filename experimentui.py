#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Apr 18, 2024 12:12:30 PM EDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import experimentui_support

_bgcolor = 'cornsilk3'
_fgcolor = 'black'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran: return        
    try: experimentui_support.root.tk.call('source',
                os.path.join(_location, 'themes', 'cornsilk-light.tcl'))
    except: pass
    style = ttk.Style()
    style.configure('.', font = "TkDefaultFont")
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("770x619+132+72")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="black")
        top.configure(highlightbackground="cornsilk3")
        top.configure(highlightcolor="black")

        self.top = top

        _style_code()
        self.TLabelframe1 = ttk.Labelframe(self.top)
        self.TLabelframe1.place(relx=0.288, rely=0.864, relheight=0.118
                , relwidth=0.439)
        self.TLabelframe1.configure(relief='')

        self.dealertext = ttk.Label(self.TLabelframe1)
        self.dealertext.place(relx=0.03, rely=0.26, height=40, width=313
                , bordermode='ignore')
        self.dealertext.configure(font="-family {DejaVu Sans} -size 10")
        self.dealertext.configure(relief="flat")
        self.dealertext.configure(anchor='w')
        self.dealertext.configure(justify='left')
        self.dealertext.configure(text='''Dealer text''')
        self.dealertext.configure(compound='center')

        self.TLabelframe6 = ttk.Labelframe(self.top)
        self.TLabelframe6.place(relx=0.013, rely=0.016, relheight=0.118
                , relwidth=0.188)
        self.TLabelframe6.configure(relief='')

        self.TLabel5 = ttk.Label(self.TLabelframe6)
        self.TLabel5.place(relx=0.069, rely=0.397, height=30, width=129
                , bordermode='ignore')
        self.TLabel5.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')
        self.TLabel5.configure(text='''Dealer Card Value:''')
        self.TLabel5.configure(compound='left')

        self.TLabelframe5 = ttk.Labelframe(self.top)
        self.TLabelframe5.place(relx=0.201, rely=0.016, relheight=0.118
                , relwidth=0.075)
        self.TLabelframe5.configure(relief='')

        self.dcards = ttk.Label(self.TLabelframe5)
        self.dcards.place(relx=0.172, rely=0.397, height=30, width=42
                , bordermode='ignore')
        self.dcards.configure(font="-family {DejaVu Sans} -size 10")
        self.dcards.configure(relief="flat")
        self.dcards.configure(anchor='w')
        self.dcards.configure(justify='left')
        self.dcards.configure(text='''0''')
        self.dcards.configure(compound='left')

        self.atframe = ttk.Labelframe(self.top)
        self.atframe.place(relx=0.881, rely=0.845, relheight=0.134, relwidth=0.1)

        self.atframe.configure(relief='')

        self.winnings = ttk.Label(self.top)
        self.winnings.place(relx=0.892, rely=0.897, height=30, width=52)
        self.winnings.configure(font="-family {DejaVu Sans} -size 10")
        self.winnings.configure(relief="flat")
        self.winnings.configure(anchor='w')
        self.winnings.configure(justify='left')
        self.winnings.configure(text='''0''')
        self.winnings.configure(compound='left')

        self.TLabelframe2 = ttk.Labelframe(self.top)
        self.TLabelframe2.place(relx=0.742, rely=0.845, relheight=0.134
                , relwidth=0.136)
        self.TLabelframe2.configure(relief='')

        self.TLabel2 = ttk.Label(self.top)
        self.TLabel2.place(relx=0.773, rely=0.91, height=20, width=81)
        self.TLabel2.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Winnings:''')
        self.TLabel2.configure(compound='left')

        self.TLabelframe4 = ttk.Labelframe(self.top)
        self.TLabelframe4.place(relx=0.204, rely=0.858, relheight=0.118
                , relwidth=0.075)
        self.TLabelframe4.configure(relief='')

        self.pcards = ttk.Label(self.TLabelframe4)
        self.pcards.place(relx=0.328, rely=0.397, height=21, width=43
                , bordermode='ignore')
        self.pcards.configure(font="-family {DejaVu Sans} -size 10")
        self.pcards.configure(relief="flat")
        self.pcards.configure(anchor='w')
        self.pcards.configure(justify='left')
        self.pcards.configure(text='''0''')
        self.pcards.configure(compound='left')

        self.TLabelframe3 = ttk.Labelframe(self.top)
        self.TLabelframe3.place(relx=0.021, rely=0.858, relheight=0.118
                , relwidth=0.188)
        self.TLabelframe3.configure(relief='')

        self.TLabel1 = ttk.Label(self.TLabelframe3)
        self.TLabel1.place(relx=0.131, rely=-1.74, height=21, width=43
                , bordermode='ignore')
        self.TLabel1.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Tlabel''')
        self.TLabel1.configure(compound='left')

        self.TLabel3 = ttk.Label(self.TLabelframe3)
        self.TLabel3.place(relx=0.131, rely=0.26, height=40, width=130
                , bordermode='ignore')
        self.TLabel3.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Your Card Value:''')
        self.TLabel3.configure(compound='left')

        self.menubar = tk.Menu(top, font="TkMenuFont", bg='cornsilk3'
                ,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.start = tk.Button(self.top)
        self.start.place(relx=0.818, rely=0.0, height=91, width=141)
        self.start.configure(activebackground="#d9d9d9")
        self.start.configure(background="red")
        self.start.configure(disabledforeground="#9a9685")
        self.start.configure(font="-family {DejaVu Sans} -size 10")
        self.start.configure(highlightbackground="cornsilk3")
        self.start.configure(text='''Start game''')

        self.dcard8 = tk.Label(self.top)
        self.dcard8.place(relx=0.066, rely=0.153, height=111, width=77)
        self.dcard8.configure(activebackground="#d9d9d9")
        self.dcard8.configure(anchor='w')
        self.dcard8.configure(background="cornsilk3")
        self.dcard8.configure(compound='left')
        self.dcard8.configure(disabledforeground="#9a9685")
        self.dcard8.configure(font="-family {DejaVu Sans} -size 10")
        self.dcard8.configure(highlightbackground="cornsilk3")

        self.dcard7 = tk.Label(self.top)
        self.dcard7.place(relx=0.175, rely=0.153, height=111, width=77)
        self.dcard7.configure(activebackground="#d9d9d9")
        self.dcard7.configure(anchor='w')
        self.dcard7.configure(background="cornsilk3")
        self.dcard7.configure(compound='left')
        self.dcard7.configure(disabledforeground="#9a9685")
        self.dcard7.configure(font="-family {DejaVu Sans} -size 10")
        self.dcard7.configure(highlightbackground="cornsilk3")

        self.dcard6 = tk.Label(self.top)
        self.dcard6.place(relx=0.284, rely=0.153, height=111, width=77)
        self.dcard6.configure(activebackground="#d9d9d9")
        self.dcard6.configure(anchor='w')
        self.dcard6.configure(background="cornsilk3")
        self.dcard6.configure(compound='left')
        self.dcard6.configure(disabledforeground="#9a9685")
        self.dcard6.configure(font="-family {DejaVu Sans} -size 10")
        self.dcard6.configure(highlightbackground="cornsilk3")

        self.dcard1 = tk.Label(self.top)
        self.dcard1.place(relx=0.394, rely=0.153, height=111, width=77)
        self.dcard1.configure(activebackground="#d9d9d9")
        self.dcard1.configure(anchor='w')
        self.dcard1.configure(background="cornsilk3")
        self.dcard1.configure(compound='left')
        self.dcard1.configure(disabledforeground="#9a9685")
        self.dcard1.configure(font="-family {DejaVu Sans} -size 10")
        self.dcard1.configure(highlightbackground="cornsilk3")

        self.dcard5 = tk.Label(self.top)
        self.dcard5.place(relx=0.838, rely=0.153, height=111, width=77)
        self.dcard5.configure(activebackground="#d9d9d9")
        self.dcard5.configure(anchor='w')
        self.dcard5.configure(background="cornsilk3")
        self.dcard5.configure(compound='left')
        self.dcard5.configure(disabledforeground="#9a9685")
        self.dcard5.configure(font="-family {DejaVu Sans} -size 10")
        self.dcard5.configure(highlightbackground="cornsilk3")

        self.dcard4 = tk.Label(self.top)
        self.dcard4.place(relx=0.727, rely=0.153, height=111, width=77)
        self.dcard4.configure(activebackground="#d9d9d9")
        self.dcard4.configure(anchor='w')
        self.dcard4.configure(background="cornsilk3")
        self.dcard4.configure(compound='left')
        self.dcard4.configure(disabledforeground="#9a9685")
        self.dcard4.configure(font="-family {DejaVu Sans} -size 10")
        self.dcard4.configure(highlightbackground="cornsilk3")

        self.dcard2 = tk.Label(self.top)
        self.dcard2.place(relx=0.503, rely=0.153, height=111, width=77)
        self.dcard2.configure(activebackground="#d9d9d9")
        self.dcard2.configure(anchor='w')
        self.dcard2.configure(background="cornsilk3")
        self.dcard2.configure(compound='left')
        self.dcard2.configure(disabledforeground="#9a9685")
        self.dcard2.configure(font="-family {DejaVu Sans} -size 10")
        self.dcard2.configure(highlightbackground="cornsilk3")
        photo_location = os.path.join(_location,"./dickerson.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.dcard2.configure(image=_img0)

        self.dcard3 = tk.Label(self.top)
        self.dcard3.place(relx=0.617, rely=0.153, height=111, width=77)
        self.dcard3.configure(activebackground="#d9d9d9")
        self.dcard3.configure(anchor='w')
        self.dcard3.configure(background="cornsilk3")
        self.dcard3.configure(compound='left')
        self.dcard3.configure(disabledforeground="#9a9685")
        self.dcard3.configure(font="-family {DejaVu Sans} -size 10")
        self.dcard3.configure(highlightbackground="cornsilk3")

        self.pcard10 = tk.Label(self.top)
        self.pcard10.place(relx=0.122, rely=0.46, height=111, width=77)
        self.pcard10.configure(activebackground="#d9d9d9")
        self.pcard10.configure(anchor='w')
        self.pcard10.configure(background="cornsilk3")
        self.pcard10.configure(compound='left')
        self.pcard10.configure(disabledforeground="#9a9685")
        self.pcard10.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard10.configure(highlightbackground="cornsilk3")

        self.pcard9 = tk.Label(self.top)
        self.pcard9.place(relx=0.013, rely=0.46, height=111, width=77)
        self.pcard9.configure(activebackground="#d9d9d9")
        self.pcard9.configure(anchor='w')
        self.pcard9.configure(background="cornsilk3")
        self.pcard9.configure(compound='left')
        self.pcard9.configure(cursor="fleur")
        self.pcard9.configure(disabledforeground="#9a9685")
        self.pcard9.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard9.configure(highlightbackground="cornsilk3")

        self.pcard11 = tk.Label(self.top)
        self.pcard11.place(relx=0.232, rely=0.46, height=111, width=77)
        self.pcard11.configure(activebackground="#d9d9d9")
        self.pcard11.configure(anchor='w')
        self.pcard11.configure(background="cornsilk3")
        self.pcard11.configure(compound='left')
        self.pcard11.configure(disabledforeground="#9a9685")
        self.pcard11.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard11.configure(highlightbackground="cornsilk3")

        self.pcard12 = tk.Label(self.top)
        self.pcard12.place(relx=0.344, rely=0.46, height=111, width=77)
        self.pcard12.configure(activebackground="#d9d9d9")
        self.pcard12.configure(anchor='w')
        self.pcard12.configure(background="cornsilk3")
        self.pcard12.configure(compound='left')
        self.pcard12.configure(disabledforeground="#9a9685")
        self.pcard12.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard12.configure(highlightbackground="cornsilk3")

        self.pcard13 = tk.Label(self.top)
        self.pcard13.place(relx=0.455, rely=0.46, height=111, width=77)
        self.pcard13.configure(activebackground="#d9d9d9")
        self.pcard13.configure(anchor='w')
        self.pcard13.configure(background="cornsilk3")
        self.pcard13.configure(compound='left')
        self.pcard13.configure(disabledforeground="#9a9685")
        self.pcard13.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard13.configure(highlightbackground="cornsilk3")

        self.pcard14 = tk.Label(self.top)
        self.pcard14.place(relx=0.566, rely=0.46, height=111, width=77)
        self.pcard14.configure(activebackground="#d9d9d9")
        self.pcard14.configure(anchor='w')
        self.pcard14.configure(background="cornsilk3")
        self.pcard14.configure(compound='left')
        self.pcard14.configure(disabledforeground="#9a9685")
        self.pcard14.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard14.configure(highlightbackground="cornsilk3")

        self.pcard15 = tk.Label(self.top)
        self.pcard15.place(relx=0.677, rely=0.46, height=111, width=77)
        self.pcard15.configure(activebackground="#d9d9d9")
        self.pcard15.configure(anchor='w')
        self.pcard15.configure(background="cornsilk3")
        self.pcard15.configure(compound='left')
        self.pcard15.configure(disabledforeground="#9a9685")
        self.pcard15.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard15.configure(highlightbackground="cornsilk3")

        self.pcard16 = tk.Label(self.top)
        self.pcard16.place(relx=0.786, rely=0.46, height=111, width=77)
        self.pcard16.configure(activebackground="#d9d9d9")
        self.pcard16.configure(anchor='w')
        self.pcard16.configure(background="cornsilk3")
        self.pcard16.configure(compound='left')
        self.pcard16.configure(disabledforeground="#9a9685")
        self.pcard16.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard16.configure(highlightbackground="cornsilk3")

        self.pcard17 = tk.Label(self.top)
        self.pcard17.place(relx=0.896, rely=0.46, height=111, width=77)
        self.pcard17.configure(activebackground="#d9d9d9")
        self.pcard17.configure(anchor='w')
        self.pcard17.configure(background="cornsilk3")
        self.pcard17.configure(compound='left')
        self.pcard17.configure(disabledforeground="#9a9685")
        self.pcard17.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard17.configure(highlightbackground="cornsilk3")

        self.pcard7 = tk.Label(self.top)
        self.pcard7.place(relx=0.719, rely=0.656, height=111, width=77)
        self.pcard7.configure(activebackground="#d9d9d9")
        self.pcard7.configure(anchor='w')
        self.pcard7.configure(background="cornsilk3")
        self.pcard7.configure(compound='left')
        self.pcard7.configure(disabledforeground="#9a9685")
        self.pcard7.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard7.configure(highlightbackground="cornsilk3")

        self.pcard8 = tk.Label(self.top)
        self.pcard8.place(relx=0.827, rely=0.656, height=111, width=77)
        self.pcard8.configure(activebackground="#d9d9d9")
        self.pcard8.configure(anchor='w')
        self.pcard8.configure(background="cornsilk3")
        self.pcard8.configure(compound='left')
        self.pcard8.configure(disabledforeground="#9a9685")
        self.pcard8.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard8.configure(highlightbackground="cornsilk3")

        self.pcard3 = tk.Label(self.top)
        self.pcard3.place(relx=0.61, rely=0.656, height=111, width=77)
        self.pcard3.configure(activebackground="#d9d9d9")
        self.pcard3.configure(anchor='w')
        self.pcard3.configure(background="cornsilk3")
        self.pcard3.configure(compound='left')
        self.pcard3.configure(disabledforeground="#9a9685")
        self.pcard3.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard3.configure(highlightbackground="cornsilk3")

        self.pcard2 = tk.Label(self.top)
        self.pcard2.place(relx=0.504, rely=0.656, height=111, width=77)
        self.pcard2.configure(activebackground="#d9d9d9")
        self.pcard2.configure(anchor='w')
        self.pcard2.configure(background="cornsilk3")
        self.pcard2.configure(compound='left')
        self.pcard2.configure(disabledforeground="#9a9685")
        self.pcard2.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard2.configure(highlightbackground="cornsilk3")

        self.pcard1 = tk.Label(self.top)
        self.pcard1.place(relx=0.394, rely=0.656, height=111, width=77)
        self.pcard1.configure(activebackground="#d9d9d9")
        self.pcard1.configure(anchor='w')
        self.pcard1.configure(background="cornsilk3")
        self.pcard1.configure(compound='left')
        self.pcard1.configure(disabledforeground="#9a9685")
        self.pcard1.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard1.configure(highlightbackground="cornsilk3")

        self.pcard4 = tk.Label(self.top)
        self.pcard4.place(relx=0.286, rely=0.656, height=111, width=77)
        self.pcard4.configure(activebackground="#d9d9d9")
        self.pcard4.configure(anchor='w')
        self.pcard4.configure(background="cornsilk3")
        self.pcard4.configure(compound='left')
        self.pcard4.configure(disabledforeground="#9a9685")
        self.pcard4.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard4.configure(highlightbackground="cornsilk3")

        self.pcard5 = tk.Label(self.top)
        self.pcard5.place(relx=0.175, rely=0.656, height=111, width=77)
        self.pcard5.configure(activebackground="#d9d9d9")
        self.pcard5.configure(anchor='w')
        self.pcard5.configure(background="cornsilk3")
        self.pcard5.configure(compound='left')
        self.pcard5.configure(disabledforeground="#9a9685")
        self.pcard5.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard5.configure(highlightbackground="cornsilk3")

        self.pcard6 = tk.Label(self.top)
        self.pcard6.place(relx=0.065, rely=0.656, height=111, width=77)
        self.pcard6.configure(activebackground="#d9d9d9")
        self.pcard6.configure(anchor='w')
        self.pcard6.configure(background="cornsilk3")
        self.pcard6.configure(compound='left')
        self.pcard6.configure(disabledforeground="#9a9685")
        self.pcard6.configure(font="-family {DejaVu Sans} -size 10")
        self.pcard6.configure(highlightbackground="cornsilk3")

def start_up():
    experimentui_support.main()

if __name__ == '__main__':
    experimentui_support.main()




