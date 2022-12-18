#Import tkinter module and creating tk as the alias for tkinter 
from tkinter import Tk, ttk, Label, Button, Entry, BOTH, PhotoImage, scrolledtext
import tkinter as tk
from userinput import userInput
from PIL import Image, ImageTk
import re
from functools import *

global username_entry, password_entry, first_name_entry, last_name_entry, user_entry, pass_entry, occupation_entry, type_id_entry, edit_stock_entry, product_brand_entry, type_id_2_entry, modal_entry, sell_entry, stocks_entry, description_entry, category_check, category_check_2, int1, type_id_3_entry, type_id_4_entry, modal_2_entry, sell_2_entry

y = 45
be4 = ""
television_clicked = False
refrigerator_clicked = False
category_clicked = False
brand_dict = {}
stock = Tk()                                                           #Creating Tkinter window
stock.title("Store Stock")                                             #Change the name of the window to "Stock"     
stock.configure(bg = "#333333")   
stock.geometry("600x500")          
stock.resizable(False, False) 
int1 = tk.IntVar()
# stock.iconbitmap()      