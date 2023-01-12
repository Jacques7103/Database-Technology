#Importing the module to create the GUI and get the data from database
from module import *
import module

class createGUI(Tk):
    def __init__(self, stock):
        """To initialize and run the main loop"""
        self.stock = stock
        self.loginWindow()
        self.stock.mainloop()
        
    def openRegister(self, frame):
        """Open Register Window"""
        frame.destroy()
        self.registerWindow()
        
    def openLogin(self, frame):
        """Open Login Window"""
        frame.destroy()
        self.loginWindow()
        
    def openAudit(self, frame):
        """Open Audit Window"""
        frame.destroy()
        self.auditPanel()
        
    def openMarket(self, frame):
        """Open Market Window"""
        frame.destroy()
        self.marketPanel()
        
    def openStore(self, frame):
        """Open Storekeeper Window"""
        frame.destroy()
        self.storePanel()
        
    def backLogin(self, window):
        """Going back to login window after logout"""
        self.loginWindow()
        self.stock.deiconify()
        window.withdraw()
        
    def loginWindow(self):    
        """Create GUI for login window"""
        self.stock.configure(bg = "#333333")
        login_frame = tk.Frame(self.stock, bg = "#333333")
        login_frame.pack()
        login_label = Label(login_frame, text = "Login", font = "Poppins, 25", bg = "#333333", fg = "#ffffff")
        username_label = Label(login_frame, text = "Username", font = "Poppins, 15", bg = "#333333", fg = "#ffffff")
        module.username_entry = Entry(login_frame, font = "Poppins, 15")
        password_label = Label(login_frame, text = "Password", font = "Poppins, 15", bg = "#333333", fg = "#ffffff")
        module.password_entry = Entry(login_frame, show = "*", font = "Poppins, 15")
        login_button = Button(login_frame, text = "Login", font = "Poppins, 15", bg = "#333333", fg = "#ffffff")
        create_account_label = Label(login_frame, text = "Create Account", font = "Poppins, 15", bg = "#333333", fg = "#3366CC")
        create_account_label.bind("<Button-1>", lambda e:self.openRegister(login_frame))
        login_button.bind("<Button-1>", lambda e:[userInput.userLogin(), createGUI.check_login(self, login_frame, create_account_label)])
        
        login_label.grid(row = 0, column = 0, columnspan = 2, pady = (100,0), sticky = "news")
        username_label.grid(row = 1, column = 0, pady = 2, padx = 5, sticky = "w")
        module.username_entry.grid(row = 2, column = 0, pady = 2, padx = 5)
        password_label.grid(row = 3, column = 0, pady = 2, padx = 5, sticky = "w")
        module.password_entry.grid(row = 4, column = 0, pady = 2, padx = 5)
        login_button.grid(row = 5, column = 0, columnspan = 2, pady = 15, padx = 5, sticky = "news")
        create_account_label.grid(row = 6, column = 0)
        
    def registerWindow(self):
        """Create GUI for register window"""
        self.stock.configure(bg = "#333333")   
        register_frame = tk.Frame(self.stock, bg = "#333333")
        register_frame.pack()
        register_label = Label(register_frame, text = "Register", font = "Poppins, 25", bg = "#333333", fg = "#ffffff")
        first_name_label = Label(register_frame, text = "First Name", font = "Poppins, 15", bg = "#333333", fg = "#ffffff")
        module.first_name_entry = Entry(register_frame, font = "Poppins, 15")
        last_name_label = Label(register_frame, text = "Last Name", font = "Poppins, 15", bg = "#333333", fg = "#ffffff")
        module.last_name_entry = Entry(register_frame, font = "Poppins, 15")
        username_label = Label(register_frame, text = "Username", font = "Poppins, 15", bg = "#333333", fg = "#ffffff")
        module.user_entry = Entry(register_frame, font = "Poppins, 15")
        password_label = Label(register_frame, text = "Password", font = "Poppins, 15", bg = "#333333", fg = "#ffffff")
        module.pass_entry = Entry(register_frame, font = "Poppins, 15")
        occupation_label = Label(register_frame, text = "Occupation (Auditor, Marketing, Storekeeper)", font = "Poppins, 15", bg = "#333333", fg = "#ffffff")
        module.occupation_entry = Entry(register_frame, font = "Poppins, 15")
        register_button = Button(register_frame, text = "Register", font = "Poppins, 15", bg = "#333333", fg = "#ffffff", command = lambda:userInput.userRegister())
        login_label = Label(register_frame, text = "Login?", font = "Poppins, 15", bg = "#333333", fg = "#3366CC")  
        login_label.bind("<Button-1>", lambda e:self.openLogin(register_frame))
        register_button.bind("<Button-1>", lambda e:createGUI.check_register(self, register_frame, login_label))
        
        register_label.grid(row = 0, column = 0, columnspan = 2, pady = (5,0), sticky = "news")
        first_name_label.grid(row = 1, column = 0, pady = 2, sticky = "w")
        module.first_name_entry.grid(row = 2, column = 0, pady = 2, sticky = "we")
        last_name_label.grid(row = 3, column = 0, pady = 2, sticky = "w")
        module.last_name_entry.grid(row = 4, column = 0, pady = 2, sticky = "we")
        username_label.grid(row = 5, column = 0, pady = 2, sticky = "w")
        module.user_entry.grid(row = 6, column = 0, pady = 2, sticky = "we")
        password_label.grid(row = 7, column = 0, pady = 2, sticky = "w")
        module.pass_entry.grid(row = 8, column = 0, pady = 2, sticky = "we")
        occupation_label.grid(row = 9, column = 0, pady = 2, sticky = "w")
        module.occupation_entry.grid(row = 10, column = 0, pady = 2, sticky = "we")
        register_button.grid(row = 11, column = 0, pady = 15, sticky = "news")
        login_label.grid(row = 12, column = 0)
        
    def auditPanel(self):
        """Create GUI for audit window"""
        global category_button, audit, y, audit_frame
        self.stock.withdraw()
        audit = tk.Toplevel()
        audit.title("Store Stock")
        audit.configure(bg = "#222222")
        audit.geometry("1320x500")
        unused = tk.Frame(audit)
        unused = tk.Frame(audit)
        audit_frame = tk.Frame(audit, bg = "#222222", height = 500, width = 150)
        audit_frame.grid(row = 0, column = 0)
        category_button = Button(audit_frame, text = "Category", font = "Poppins, 15", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff")
        category_button.bind("<Button-1>", lambda e:self.dropCategory(audit_frame, None, stock_button, None, None))
        
        category_button.place(x = -15, y = 10)
        
        self.rightCategory(audit, audit_frame)
        self.stockButton(audit_frame)
        self.logout(audit_frame, audit)
        audit.resizable(False, False)
        audit.mainloop()
        
    def stockButton(self, frame):
        """Creating the button to edit stock"""
        global stock_button
        stock_button = Button(frame, text = "Edit Stock", font = "Poppins, 15", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff")
        stock_button.bind("<Button-1>", lambda e:self.editStock())
        
        stock_button.place(x = -10, y = 45)
        
    def editStock(self):
        """Function to edit the stock"""
        self.int1 = module.int1
        self.int1.set(0)
        self.stock_frame = tk.Toplevel()
        self.stock_frame.title("Store Stock")
        self.stock_frame.configure(bg = "#222222")
        self.stock_frame.geometry("310x260")
        self.stock_frame.resizable(False, False)
        unused = tk.Frame(self.stock_frame)
        unused = tk.Frame(self.stock_frame)
        stock_frame_2 = tk.Frame(self.stock_frame, bg = "#222222")
        stock_frame_2.pack()
        type_id_label = Label(stock_frame_2, text = "Type ID", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.type_id_entry = Entry(stock_frame_2, font = "Poppins, 15")
        edit_stock_label = Label(stock_frame_2, text = "Remaining Stock", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.edit_stock_entry = Entry(stock_frame_2, font = "Poppins, 15")
        button = []
        text = ["", "Refrigerator", "Television"]
        for i in range(1, 3):
            button.append(tk.Checkbutton(stock_frame_2, text = text[i], font = "Poppins, 12", bg = "#222222", fg = "#ffffff", selectcolor = "#000000", activebackground = "#ffffff", variable = self.int1, onvalue = i))
        add_button = Button(stock_frame_2, text = "Edit", font = "Poppins, 15", bg = "#333333", fg = "#ffffff", command = lambda:createGUI.update_brand(self, stock_frame_2))

        type_id_label.grid(row = 0, column = 0, columnspan = 2, pady = (15, 0), sticky = "w")
        module.type_id_entry.grid(row = 1, column = 0, pady = 2, sticky = "we")
        edit_stock_label.grid(row = 2, column = 0, columnspan = 2, sticky = "w")
        module.edit_stock_entry.grid(row = 3, column = 0, pady = 2, sticky = "we")
        button[0].grid(row = 4, column = 0, padx = (0,150))
        button[1].grid(row = 4, column = 0, padx = (165,0))
        add_button.grid(row = 5, column = 0, pady = (15,5), sticky = "news")
        
    def update_brand(self, frame, event=None):
        """Opening the category that has been edited after clicked 'edit'"""
        user = userInput.editStock(module.int1)
        if len(user) == 1:
            check = user[0]
        elif len(user) == 3:
            check = user[0]
            category = user[1]
            brand = user[2]
        else:
            check = False
            
        if check:
            if category == "Television":
                self.getTV(frame, brand)
                self.stock_frame.withdraw()
            elif category == "Refrigerator":
                self.getFridge(frame, brand)
                self.stock_frame.withdraw()
        else:
            self.failLogin(frame, "Stock", None)
            
    
    def marketPanel(self):
        """Create GUI for market window"""
        global category_button, market, market_frame
        self.stock.withdraw()
        market = tk.Toplevel()
        market.title("Store Stock")
        market.configure(bg = "#222222")
        market.geometry("1320x500")
        unused = tk.Frame(market)
        market_frame = tk.Frame(market, bg = "#222222", height = 500, width = 150)
        market_frame.grid(row = 0, column = 0)
        category_button = Button(market_frame, text = "Category", font = "Poppins, 15", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff")
        category_button.bind("<Button-1>", lambda e:self.dropCategory(market_frame, None, add_button, remove_button, change_price))
        
        category_button.place(x = -15, y = 10)
        
        self.rightCategory(market, market_frame)
        self.addButton(market_frame)
        self.logout(market_frame, market)
        market.resizable(False, False)
        market.mainloop()
        
    def addButton(self, frame):
        """Create the button to add data, remove data, and change the price of a data"""
        global add_button, remove_button, change_price
        add_button = Button(frame, text = "Add Data", font = "Poppins, 15", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff")
        add_button.bind("<Button-1>", lambda e:self.addData())
        remove_button = Button(frame, text = "Remove Data", font = "Poppins, 15", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff")
        remove_button.bind("<Button-1>", lambda e:self.removeData())
        change_price = Button(frame, text = "Change Price", font = "Poppins, 15", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff")
        change_price.bind("<Button-1>", lambda e:self.changePrice())
        
        add_button.place(x = -13, y = 45)
        remove_button.place(x = 5, y = 80)
        change_price.place(x = 4, y = 115)
        
    def changePrice(self):
        """Function to change the price of a data"""
        self.int1 = module.int1
        self.int1.set(0)
        self.change_frame = tk.Toplevel()
        self.change_frame.title("Store Stock")
        self.change_frame.configure(bg = "#222222")
        self.change_frame.geometry("310x300")
        self.change_frame.resizable(False, False)
        unused = tk.Frame(self.change_frame)
        change_frame = tk.Frame(self.change_frame, bg = "#222222")
        change_frame.pack()
        type_id_4_label = Label(change_frame, text = "Type ID", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.type_id_4_entry = Entry(change_frame, font = "Poppins, 15")
        modal_label = Label(change_frame, text = "Modal Price", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.modal_2_entry = Entry(change_frame, font = "Poppins, 15")
        sell_label = Label(change_frame, text = "Selling Price", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.sell_2_entry = Entry(change_frame, font = "Poppins, 15")
        button = []
        text = ["", "Refrigerator", "Television"]
        for i in range(1, 3):
            button.append(tk.Checkbutton(change_frame, text = text[i], font = "Poppins, 12", bg = "#222222", fg = "#ffffff", selectcolor = "#000000", activebackground = "#ffffff", variable = self.int1, onvalue = i))
        change_button = Button(change_frame, text = "Change", font = "Poppins, 15", bg = "#333333", fg = "#ffffff", command = lambda:createGUI.checkData3(self, change_frame))
    
        type_id_4_label.grid(row = 0, column = 0, columnspan = 2, pady = (8, 0), sticky = "w")
        module.type_id_4_entry.grid(row = 1, column = 0, pady = 2, sticky = "we")
        modal_label.grid(row = 2, column = 0, columnspan = 2, sticky = "w")
        module.modal_2_entry.grid(row = 3, column = 0, columnspan = 2, sticky = "we")
        sell_label.grid(row = 4, column = 0, columnspan = 2, sticky = "w")
        module.sell_2_entry.grid(row = 5, column = 0, columnspan = 2, sticky = "we")
        button[0].grid(row = 6, column = 0, padx = (0,151))
        button[1].grid(row = 6, column = 0, padx = (165,0))
        change_button.grid(row = 7, column = 0, pady = (10, 5), sticky = "news")
        
    def checkData3(self, frame, event=None):
        """Show the category that price has been changed"""
        user = userInput.changePrice()
        if len(user) == 1:
            check = user[0]
        elif len(user) == 3:
            check = user[0]
            category = user[1]
            brand = user[2]
        else:
            check = False
            
        if check:
            if category == "Television":
                self.getTV(frame, brand)
                self.change_frame.withdraw()
            elif category == "Refrigerator":
                self.getFridge(frame, brand)
                self.change_frame.withdraw()
        else:
            self.failLogin(frame, "Price", None)

    def removeData(self):
        """Function to remove a certain data"""
        self.int1 = module.int1
        self.int1.set(0)
        self.remove_frame = tk.Toplevel()
        self.remove_frame.title("Store Stock")
        self.remove_frame.configure(bg = "#222222")
        self.remove_frame.geometry("310x190")
        self.remove_frame.resizable(False, False)
        unused = tk.Frame(self.remove_frame)
        remove_frame = tk.Frame(self.remove_frame, bg = "#222222")
        remove_frame.pack()
        type_id_3_label = Label(remove_frame, text = "Type ID", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.type_id_3_entry = Entry(remove_frame, font = "Poppins, 15")
        button = []
        text = ["", "Refrigerator", "Television"]
        for i in range(1, 3):
            button.append(tk.Checkbutton(remove_frame, text = text[i], font = "Poppins, 12", bg = "#222222", fg = "#ffffff", selectcolor = "#000000", activebackground = "#ffffff", variable = self.int1, onvalue = i))
        remove_button = Button(remove_frame, text = "Remove", font = "Poppins, 15", bg = "#333333", fg = "#ffffff", command = lambda:createGUI.checkData2(self, remove_frame))
        
        type_id_3_label.grid(row = 0, column = 0, columnspan = 2, pady = (8, 0), sticky = "w")
        module.type_id_3_entry.grid(row = 1, column = 0, pady = 2, sticky = "we")
        button[0].grid(row = 2, column = 0, padx = (0,151))
        button[1].grid(row = 2, column = 0, padx = (165,0))
        remove_button.grid(row = 3, column = 0, pady = (10, 5), sticky = "news")
        
    def checkData2(self, frame, event=None):
        """Show the category that data has been removed"""
        user = userInput.removeData()
        if len(user) == 1:
            check = user[0]
        elif len(user) == 3:
            check = user[0]
            category = user[1]
            brand = user[2]
        else:
            check = False
            
        if check:
            if category == "Television":
                self.getTV(frame, brand)
                self.remove_frame.withdraw()
            elif category == "Refrigerator":
                self.getFridge(frame, brand)
                self.remove_frame.withdraw()
        else:
            self.failLogin(frame, "Data", None)
        
    def addData(self):
        """Function to add a data"""
        self.int1 = module.int1
        self.int1.set(0)
        self.add_frame = tk.Toplevel()
        self.add_frame.title("Store Stock")
        self.add_frame.configure(bg = "#222222")
        self.add_frame.geometry("310x550")
        self.add_frame.resizable(False, False)
        unused = tk.Frame(self.add_frame)
        add_frame = tk.Frame(self.add_frame, bg = "#222222")
        add_frame.pack()
        product_brand_label = Label(add_frame, text = "Product Brand", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.product_brand_entry = Entry(add_frame, font = "Poppins, 15")
        type_id_2_label = Label(add_frame, text = "Type ID", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.type_id_2_entry = Entry(add_frame, font = "Poppins, 15")
        modal_label = Label(add_frame, text = "Modal Price", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.modal_entry = Entry(add_frame, font = "Poppins, 15")
        sell_label = Label(add_frame, text = "Selling Price", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.sell_entry = Entry(add_frame, font = "Poppins, 15")
        stocks_label = Label(add_frame, text = "Stock", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.stocks_entry = Entry(add_frame, font = "Poppins, 15")
        description_label = Label(add_frame, text = "Description (200 Char MAX)", font = "Poppins, 15", bg = "#222222", fg = "#ffffff")
        module.description_entry = scrolledtext.ScrolledText(add_frame, width = 1, height = 4, font = "Poppins, 15", wrap = tk.WORD)
        button = []
        text = ["", "Refrigerator", "Television"]
        for i in range(1, 3):
            button.append(tk.Checkbutton(add_frame, text = text[i], font = "Poppins, 12", bg = "#222222", fg = "#ffffff", selectcolor = "#000000", activebackground = "#ffffff", variable = self.int1, onvalue = i))
        add_button = Button(add_frame, text = "Add", font = "Poppins, 15", bg = "#333333", fg = "#ffffff", command = lambda:createGUI.checkData(self, add_frame))
        
        product_brand_label.grid(row = 0, column = 0, columnspan = 2, pady = (8, 0), sticky = "w")
        module.product_brand_entry.grid(row = 1, column = 0, pady = 2, sticky = "we")
        type_id_2_label.grid(row = 2, column = 0, columnspan = 2, sticky = "w")
        module.type_id_2_entry.grid(row = 3, column = 0, pady = 2, sticky = "we")
        modal_label.grid(row = 4, column = 0, columnspan = 2, sticky = "w")
        module.modal_entry.grid(row = 5, column = 0, columnspan = 2, sticky = "we")
        sell_label.grid(row = 6, column = 0, columnspan = 2, sticky = "w")
        module.sell_entry.grid(row = 7, column = 0, columnspan = 2, sticky = "we")
        stocks_label.grid(row = 8, column = 0, columnspan = 2, sticky = "w")
        module.stocks_entry.grid(row = 9, column = 0, columnspan = 2, sticky = "we")
        description_label.grid(row = 10, column = 0, columnspan = 2, sticky = "w")
        module.description_entry.grid(row = 11, column = 0, columnspan = 2, pady = (0, 10), sticky = "we")
        button[0].grid(row = 12, column = 0, padx = (0,151))
        button[1].grid(row = 12, column = 0, padx = (165,0))
        add_button.grid(row = 13, column = 0, pady = (10, 5), sticky = "news")
    
    def checkData(self, frame, event=None):
        """Show the category that data has been added"""
        user = userInput.addData()
        if len(user) == 1:
            check = user[0]
        elif len(user) == 3:
            check = user[0]
            category = user[1]
            brand = user[2]
        else:
            check = False
            
        if check:
            if category == "Television":
                self.getTV(frame, brand)
                self.add_frame.withdraw()
            elif category == "Refrigerator":
                self.getFridge(frame, brand)
                self.add_frame.withdraw()
        else:
            self.failLogin(frame, "Data", None)
        
    def storePanel(self):
        """Create GUI for storekeeper window"""
        global category_button, store, store_frame
        self.stock.withdraw()
        store = tk.Toplevel()
        store.title("Store Stock")
        store.configure(bg = "#222222")
        store.geometry("1210x500")
        store_frame = tk.Frame(store, bg = "#222222", height = 500, width = 150)
        store_frame.grid(row = 0, column = 0)
        category_button = Button(store_frame, text = "Category", font = "Poppins, 15", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff")
        category_button.bind("<Button-1>", lambda e:self.dropCategory(store_frame, None, None, None, None))
        
        category_button.place(x = -15, y = 10)
        
        self.rightCategory(store, store_frame)
        self.logout(store_frame, store)
        store.resizable(False, False)
        store.mainloop()
        
    def dropCategory(self, frame, category_click, button, button2, button3):
        """Creating a manual drop down when the button 'category' is clicked"""
        self.destroyCategory(frame, button, button2, button3)
        category_list = userInput.getCategory()
        category = category_list[0]
        global y, refrigerator_label, television_label, category_remove, be4, category_clicked
        category_remove = []
        category_clicked = False
        y = 45
        
        for i in category:
            if i == be4:
                pass
            elif i == "Refrigerator":
                refrigerator_label = Button(frame, text = i, font = "Poppins, 12", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff", anchor = "w")
                refrigerator_label.bind("<Button-1>", lambda e:[self.dropCategory(frame, "Refrigerator", button, button2, button3), self.getFridge(frame, None)])
                refrigerator_label.place(x = 25, y = y)
                category_remove.append(refrigerator_label)
                y += 35
                be4 = i
                if category_click == "Refrigerator":
                    self.dropBrand(frame, "Refrigerator", button, button2, button3)
            else:
                television_label = Button(frame, text = i, font = "Poppins, 12", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff", anchor = "w")
                television_label.bind("<Button-1>", lambda e:[self.dropCategory(frame, "Television", button, button2, button3), self.getTV(frame, None)])
                television_label.place(x = 25, y = y)
                category_remove.append(television_label)
                y += 35
                be4 = i
                if category_click == "Television":
                    self.dropBrand(frame, "Television", button, button2, button3)
                    
        if button != None:
            button.place(x = -10, y = y)
            if button2 != None:
                button2.place(x = 5, y = y + 35)
                if button3 != None:
                    button3.place(x = 4, y = y + 70)
                    
        category_button.bind("<Button-1>", lambda e:self.destroyCategory(frame, button, button2, button3))
                
    def destroyCategory(self, frame, button, button2, button3):
        """Hide the drop down category after the 'category' button is clicked"""
        global y, television_clicked, refrigerator_clicked, category_clicked, ref_temp, tv_temp, check_position, check_position2
        
        try:
            for i in range(len(category_remove)):
                category_remove[i].destroy()
                if television_clicked:
                    category_clicked = True
                    self.destroyBrand(frame, "Television", button, button2, button3)
                if refrigerator_clicked:
                    category_clicked = True
                    self.destroyBrand(frame, "Refrigerator", button, button2, button3)
            
            y = y - (35 * len(category_remove))
            if button != None:
                button.place(x = -10, y = y)
                if button2 != None:
                    button2.place(x = 5, y = y + 35)
                    if button3 != None:
                        button3.place(x = 4, y = y + 70)

            category_button.bind("<Button-1>", lambda e:self.dropCategory(frame, None, button, button2, button3))
            
        except NameError:
            pass
    
    def dropBrand(self, frame, category, button, button2, button3):
        """Creating a manual drop down when the product brand button is clicked"""
        category_list = userInput.getCategory()
        category_item = category_list[0]
        brand = category_list[1]
        global y, brand_label, brand_list, brand_list, television_clicked, refrigerator_clicked
        brand_list = []
        for x in range(len(category_item)):
            if category_item[x] == category:
                if category == "Television":
                    brand_label = Button(frame, text = brand[x], command = partial(self.getTV, frame, brand[x]), font = "Poppins, 10", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff", anchor = "w")
                    brand_label.place(x = 40, y = y)
                    y += 35
                    brand_list.append(brand_label)
                else:
                    brand_label = Button(frame, text = brand[x], command = partial(self.getFridge, frame, brand[x]), font = "Poppins, 10", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff", anchor = "w")
                    brand_label.place(x = 40, y = y)
                    y += 35
                    brand_list.append(brand_label)
                
        brand_dict[category] = brand_list
        if category == "Television":
            television_label.bind("<Button-1>", lambda e:[self.destroyBrand(frame, category, button, button2, button3), self.getTV(frame, None)])
            television_clicked = True
        elif category == "Refrigerator":
            refrigerator_label.bind("<Button-1>", lambda e:[self.destroyBrand(frame, category, button, button2, button3), self.getFridge(frame, None)])
            refrigerator_clicked = True
        if button != None:
            button.place(x = -10, y = y)
            if button2 != None:
                button2.place(x = 5, y = y + 35)
                if button3 != None:
                        button3.place(x = 4, y = y + 70)
                
    def destroyBrand(self, frame, category, button, button2, button3):
        """Hide the drop down brand after the product brand button is clicked"""
        global y, television_clicked, refrigerator_clicked, category_clicked
        
        y = y - (35 * len(brand_list))
        
        for x in range(len(brand_dict)):
            if category == "Television":
                television = brand_dict.get(category)
                for i in range(len(television)):
                    television[i].destroy()
                television_clicked = False
                if category_clicked == False:
                    television_label.bind("<Button-1>", lambda e:[self.dropCategory(frame, category, button, button2, button3), self.getTV(frame, None)])
                    self.destroyCategory(frame, button, button2, button3)
                    self.dropCategory(frame, None, button, button2, button3)
            elif category == "Refrigerator":
                refrigerator = brand_dict.get(category)
                for i in range(len(refrigerator)):
                    refrigerator[i].destroy()
                refrigerator_clicked = False
                if category_clicked == False:
                    refrigerator_label.bind("<Button-1>", lambda e:[self.dropCategory(frame, category, button, button2, button3), self.getFridge(frame, None)])
                    self.destroyCategory(frame, button, button2, button3)
                    self.dropCategory(frame, None, button, button2, button3)
        
        if button != None:
            button.place(x = -10, y = y)
            if button2 != None:
                button2.place(x = 5, y = y + 35)
                if button3 != None:
                    button3.place(x = 4, y = y + 70)
                
    def rightCategory(self, window, frame):
        """Creating the panel in the right window"""
        global right_frame
        text = frame.__str__()
        check = re.search(".+frame$", text)
        check2 = re.search(".+frame2$", text)
        check3 = re.search(".+frame3$", text)
        right_frame = tk.Frame(window, bg = "#333333", width = 1260, height = 500)
        right_frame.grid(row = 0, column = 1)
        
        search = tk.Entry(right_frame, font = "Poppins, 15")
        
        images = Image.open("find.png")
        images = images.resize((26, 26))
        images = ImageTk.PhotoImage(images)
        find = tk.Button(right_frame, image = images, bg = "#333333", fg = "#ffffff", height = 26, width = 26, borderwidth = 1, highlightthickness = 0, activebackground = "#333333", activeforeground = "#333333")
        find.photo = images
        find.bind("<Button-1>", lambda e:self.getSearch(frame, search.get()))
        
        if check:
            search.place(x = 30, y = 20, width = 965)
            find.place(x = 1010, y = 20)
        elif check2:
            search.place(x = 30, y = 20, width = 1072)
            find.place(x = 1117, y = 20)
        elif check3:
            search.place(x = 30, y = 20, width = 1072)
            find.place(x = 1117, y = 20)
    
    def failLogin(self, frame, check, label):
        """Function that run if user failed to login"""
        if check == "Login":
            wrong = Label(frame, text = "Username or Password", font = "Poppins, 12", bg = "#333333", fg = "#ffffff")
            wrong2 = Label(frame, text = "is incorrect !!", font = "Poppins, 12", bg = "#333333", fg = "#ffffff")
            wrong.grid(row = 6, column = 0)
            wrong2.grid(row = 7, column = 0)
            label.grid(row = 8, column = 0)
        elif check == "Register":
            wrong = Label(frame, text = "Input is incorrect !!", font = "Poppins, 12", bg = "#333333", fg = "#ffffff")
            wrong.grid(row = 12, column = 0)
            label.grid(row = 13, column = 0)
        elif check == "Stock":
            wrong = Label(frame, text = "Input is incorrect !!", font = "Poppins, 12", bg = "#222222", fg = "#ffffff")
            wrong.grid(row = 6, column = 0)
        elif check == "Data":
            wrong = Label(frame, text = "Input is incorrect !!", font = "Poppins, 12", bg = "#222222", fg = "#ffffff")
            wrong.grid(row = 14, column = 0)
        else:
            wrong = Label(frame, text = "Input is incorrect !!", font = "Poppins, 12", bg = "#222222", fg = "#ffffff")
            wrong.grid(row = 8, column = 0)
    
    def check_login(self, login_frame, label, event=None):
        """Check whether user's login input is correct and run the window based on their occupation"""
        user = userInput.userLogin()
        for i in range(2):
            if len(user) == 1:
                check = user[0]
            else:
                check = user[0]
                occupation = user[1]
        
        if check:
            if occupation == "auditor":
                self.openAudit(login_frame)
            elif occupation == "marketing":
                self.openMarket(login_frame)
            elif occupation == "storekeeper":
                self.openStore(login_frame)
        else:
            self.failLogin(login_frame, "Login", label)
            
    def check_register(self, register_frame, label, event=None):
        """Check whether the user's register is correct and run the window based on their occupation"""
        user = userInput.userRegister()
        if len(user) == 1:
            check = user[0]
        else:
            check = user[0]
            occupation = user[1]
        
        if check:
            if occupation == "auditor":
                self.openAudit(register_frame)
            elif occupation == "marketing":
                self.openMarket(register_frame)
            elif occupation == "storekeeper":
                self.openStore(register_frame)
        else:
            self.failLogin(register_frame, "Register", label)
            
    def logout(self, frame, window):
        """Creating the logout button"""
        logout = Button(frame, text = "Logout", font = "Poppins, 15", bg = "#222222", fg = "#ffffff", width = 12, borderwidth = 0, highlightthickness = 0, activebackground = "#222222", activeforeground = "#ffffff", anchor = "w")
        logout.bind("<Button-1>", lambda e:self.backLogin(window))
        logout.place(x = 12, y = 450)
        
    def getSearch(self, frame, user_input):
        """Creating the search bar and button"""
        record = userInput.getTV()
        record2 = userInput.getFridge()
        text = frame.__str__()
        check = re.search(".+frame$", text)
        check2 = re.search(".+frame2$", text)
        check3 = re.search(".+frame3$", text)
        
        if check:
            output = []
            for row in record:
                store_none = []
                if user_input in row[0] or user_input in row[1] or user_input in str(row[2]) or user_input in str(row[3]) or user_input in str(row[4]) or user_input in row[5]:
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            for row in record2:
                store_none = []
                if user_input in row[0] or user_input in row[1] or user_input in str(row[2]) or user_input in str(row[3]) or user_input in str(row[4]) or user_input in row[5]:
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            
            style = ttk.Style(right_frame)
            style.theme_use("clam")
            style.configure("Treeview", background = "#333333", fieldbackground = "#333333", foreground = "white", rowheight = 30)
                    
            table = ttk.Treeview(right_frame, style = "Treeview", height = 13, columns = ("Product Brand", "Type ID", "Price", "Stock", "Description"), show = "headings")
            table.heading("Product Brand", text = "Product Brand")
            table.heading("Type ID", text = "Type ID")
            table.heading("Price", text = "Price")
            table.heading("Stock", text = "Stock")
            table.heading("Description", text = "Description")
            
            table.column("Product Brand", width = 90, minwidth = 90, anchor = "center")
            table.column("Type ID", width = 100, minwidth = 100, anchor = "center")
            table.column("Price", width = 50, minwidth = 50, anchor = "center")
            table.column("Stock", width = 50, minwidth = 50, anchor = "center")
            table.column("Description", width = 700, minwidth = 700, anchor = "center")
            
            for row in output:
                table.insert('', tk.END, values = row)
            
            scroll = ttk.Scrollbar(right_frame, orient = "vertical", command = table.yview)
            scroll.place(x = 1022, y = 60, height = 419)
            
            table.configure(yscrollcommand = scroll.set)
            table.place(x = 30, y = 60)
        elif check2:
            output = []
            for row in record:
                store_none = []
                if user_input in row[0] or user_input in row[1] or user_input in str(row[2]) or user_input in str(row[3]) or user_input in str(row[4]) or user_input in row[5]:
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[2])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            for row in record2:
                store_none = []
                if user_input in row[0] or user_input in row[1] or user_input in str(row[2]) or user_input in str(row[3]) or user_input in str(row[4]) or user_input in row[5]:
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[2])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            
            style = ttk.Style(right_frame)
            style.theme_use("clam")
            style.configure("Treeview", background = "#333333", fieldbackground = "#333333", foreground = "white", rowheight = 30)
                    
            table = ttk.Treeview(right_frame, style = "Treeview", height = 13, columns = ("Product Brand", "Type ID", "Buying Price", "Selling Price", "Stock", "Description"), show = "headings")
            table.heading("Product Brand", text = "Product Brand")
            table.heading("Type ID", text = "Type ID")
            table.heading("Buying Price", text = "Buying Price")
            table.heading("Selling Price", text = "Selling Price")
            table.heading("Stock", text = "Stock")
            table.heading("Description", text = "Description")
            
            table.column("Product Brand", width = 90, minwidth = 90, anchor = "center")
            table.column("Type ID", width = 100, minwidth = 100, anchor = "center")
            table.column("Buying Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Selling Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Stock", width = 50, minwidth = 50, anchor = "center")
            table.column("Description", width = 710, minwidth = 710, anchor = "center")
            
            for row in output:
                table.insert('', tk.END, values = row)
                
            scroll = ttk.Scrollbar(right_frame, orient = "vertical", command = table.yview)
            scroll.place(x = 1132, y = 60, height = 419)
            
            table.configure(yscrollcommand = scroll.set)
            table.place(x = 30, y = 60)
        elif check3:
            output = []
            for row in record:
                store_none = []
                if user_input in row[0] or user_input in row[1] or user_input in str(row[2]) or user_input in str(row[3]) or user_input in str(row[4]) or user_input in row[5]:
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[2])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            for row in record2:
                store_none = []
                if user_input in row[0] or user_input in row[1] or user_input in str(row[2]) or user_input in str(row[3]) or user_input in str(row[4]) or user_input in row[5]:
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[2])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            
            style = ttk.Style(right_frame)
            style.theme_use("clam")
            style.configure("Treeview", background = "#333333", fieldbackground = "#333333", foreground = "white", rowheight = 30)
                    
            table = ttk.Treeview(right_frame, style = "Treeview", height = 13, columns = ("Product Brand", "Type ID", "Buying Price", "Selling Price", "Stock", "Description"), show = "headings")
            table.heading("Product Brand", text = "Product Brand")
            table.heading("Type ID", text = "Type ID")
            table.heading("Buying Price", text = "Buying Price")
            table.heading("Selling Price", text = "Selling Price")
            table.heading("Stock", text = "Stock")
            table.heading("Description", text = "Description")
            
            table.column("Product Brand", width = 90, minwidth = 90, anchor = "center")
            table.column("Type ID", width = 100, minwidth = 100, anchor = "center")
            table.column("Buying Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Selling Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Stock", width = 50, minwidth = 50, anchor = "center")
            table.column("Description", width = 710, minwidth = 710, anchor = "center")
            
            for row in output:
                table.insert('', tk.END, values = row)
                
            scroll = ttk.Scrollbar(right_frame, orient = "vertical", command = table.yview)
            scroll.place(x = 1132, y = 60, height = 419)
            
            table.configure(yscrollcommand = scroll.set)
            table.place(x = 30, y = 60)
    
    def getTV(self, frame, user_input):
        """Showing the TV categroy data based on the product brand that is clicked or searched"""
        record = userInput.getTV()
        text = frame.__str__()
        check = re.search(".+frame$", text)
        check2 = re.search(".+frame2$", text)
        check3 = re.search(".+frame3$", text)
        
        if check:
            if user_input == None:
                output = []
                for row in record:
                    store_none = []
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            else:
                output = []
                for row in record:
                    store_none = []
                    if user_input == row[0]:
                        store_none.append(row[0])
                        store_none.append(row[1])
                        store_none.append(row[3])
                        store_none.append(row[4])
                        store_none.append(row[5])
                        output.append(store_none)
                    elif user_input in row[0] or user_input in row[1]:
                        store_none.append(row[0])
                        store_none.append(row[1])
                        store_none.append(row[3])
                        store_none.append(row[4])
                        store_none.append(row[5])
                        output.append(store_none)
                    
            style = ttk.Style(right_frame)
            style.theme_use("clam")
            style.configure("Treeview", background = "#333333", fieldbackground = "#333333", foreground = "white", rowheight = 30)
                    
            table = ttk.Treeview(right_frame, style = "Treeview", height = 13, columns = ("Product Brand", "Type ID", "Price", "Stock", "Description"), show = "headings")
            table.heading("Product Brand", text = "Product Brand")
            table.heading("Type ID", text = "Type ID")
            table.heading("Price", text = "Price")
            table.heading("Stock", text = "Stock")
            table.heading("Description", text = "Description")
            
            table.column("Product Brand", width = 90, minwidth = 90, anchor = "center")
            table.column("Type ID", width = 100, minwidth = 100, anchor = "center")
            table.column("Price", width = 50, minwidth = 50, anchor = "center")
            table.column("Stock", width = 50, minwidth = 50, anchor = "center")
            table.column("Description", width = 700, minwidth = 700, anchor = "center")
            
            for row in output:
                table.insert('', tk.END, values = row)
            
            scroll = ttk.Scrollbar(right_frame, orient = "vertical", command = table.yview)
            scroll.place(x = 1022, y = 60, height = 419)
            
            table.configure(yscrollcommand = scroll.set)
            table.place(x = 30, y = 60)
        elif check2:
            if user_input == None:
                output = []
                for row in record:
                    store_none = []
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[2])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            else:
                output = []
                for row in record:
                    store_none = []
                    if user_input == row[0]:
                        store_none.append(row[0])
                        store_none.append(row[1])
                        store_none.append(row[2])
                        store_none.append(row[3])
                        store_none.append(row[4])
                        store_none.append(row[5])
                        output.append(store_none)
                    
            style = ttk.Style(right_frame)
            style.theme_use("clam")
            style.configure("Treeview", background = "#333333", fieldbackground = "#333333", foreground = "white", rowheight = 30)
                    
            table = ttk.Treeview(right_frame, style = "Treeview", height = 13, columns = ("Product Brand", "Type ID", "Buying Price", "Selling Price", "Stock", "Description"), show = "headings")
            table.heading("Product Brand", text = "Product Brand")
            table.heading("Type ID", text = "Type ID")
            table.heading("Buying Price", text = "Buying Price")
            table.heading("Selling Price", text = "Selling Price")
            table.heading("Stock", text = "Stock")
            table.heading("Description", text = "Description")
            
            table.column("Product Brand", width = 90, minwidth = 90, anchor = "center")
            table.column("Type ID", width = 100, minwidth = 100, anchor = "center")
            table.column("Buying Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Selling Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Stock", width = 50, minwidth = 50, anchor = "center")
            table.column("Description", width = 710, minwidth = 710, anchor = "center")
            
            for row in output:
                table.insert('', tk.END, values = row)
                
            scroll = ttk.Scrollbar(right_frame, orient = "vertical", command = table.yview)
            scroll.place(x = 1132, y = 60, height = 419)
            
            table.configure(yscrollcommand = scroll.set)
            table.place(x = 30, y = 60)
        elif check3:
            if user_input == None:
                output = []
                for row in record:
                    store_none = []
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[2])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            else:
                output = []
                for row in record:
                    store_none = []
                    if user_input == row[0]:
                        store_none.append(row[0])
                        store_none.append(row[1])
                        store_none.append(row[2])
                        store_none.append(row[3])
                        store_none.append(row[4])
                        store_none.append(row[5])
                        output.append(store_none)
                    
            style = ttk.Style(right_frame)
            style.theme_use("clam")
            style.configure("Treeview", background = "#333333", fieldbackground = "#333333", foreground = "white", rowheight = 30)
                    
            table = ttk.Treeview(right_frame, style = "Treeview", height = 13, columns = ("Product Brand", "Type ID", "Buying Price", "Selling Price", "Stock", "Description"), show = "headings")
            table.heading("Product Brand", text = "Product Brand")
            table.heading("Type ID", text = "Type ID")
            table.heading("Buying Price", text = "Buying Price")
            table.heading("Selling Price", text = "Selling Price")
            table.heading("Stock", text = "Stock")
            table.heading("Description", text = "Description")
            
            table.column("Product Brand", width = 90, minwidth = 90, anchor = "center")
            table.column("Type ID", width = 100, minwidth = 100, anchor = "center")
            table.column("Buying Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Selling Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Stock", width = 50, minwidth = 50, anchor = "center")
            table.column("Description", width = 710, minwidth = 710, anchor = "center")
            
            for row in output:
                table.insert('', tk.END, values = row)
                
            scroll = ttk.Scrollbar(right_frame, orient = "vertical", command = table.yview)
            scroll.place(x = 1132, y = 60, height = 419)
            
            table.configure(yscrollcommand = scroll.set)
            table.place(x = 30, y = 60)

    def getFridge(self, frame, user_input):
        """Showing the Refrigerator categroy data based on the product brand that is clicked or searched"""
        record = userInput.getFridge()
        text = frame.__str__()
        check = re.search(".+frame$", text)
        check2 = re.search(".+frame2$", text)
        check3 = re.search(".+frame3$", text)
        
        if check:
            if user_input == None:
                output = []
                for row in record:
                    store_none = []
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            else:
                output = []
                for row in record:
                    store_none = []
                    if user_input == row[0]:
                        store_none.append(row[0])
                        store_none.append(row[1])
                        store_none.append(row[3])
                        store_none.append(row[4])
                        store_none.append(row[5])
                        output.append(store_none)
                    
            style = ttk.Style(right_frame)
            style.theme_use("clam")
            style.configure("Treeview", background = "#333333", fieldbackground = "#333333", foreground = "white", rowheight = 30)
                    
            table = ttk.Treeview(right_frame, style = "Treeview", height = 13, columns = ("Product Brand", "Type ID", "Price", "Stock", "Description"), show = "headings")
            table.heading("Product Brand", text = "Product Brand")
            table.heading("Type ID", text = "Type ID")
            table.heading("Price", text = "Price")
            table.heading("Stock", text = "Stock")
            table.heading("Description", text = "Description")
            
            table.column("Product Brand", width = 90, minwidth = 90, anchor = "center")
            table.column("Type ID", width = 100, minwidth = 100, anchor = "center")
            table.column("Price", width = 50, minwidth = 50, anchor = "center")
            table.column("Stock", width = 50, minwidth = 50, anchor = "center")
            table.column("Description", width = 700, minwidth = 700, anchor = "center")
            
            for row in output:
                table.insert('', tk.END, values = row)
                
            scroll = ttk.Scrollbar(right_frame, orient = "vertical", command = table.yview)
            scroll.place(x = 1022, y = 60, height = 419)
            
            table.configure(yscrollcommand = scroll.set)
            table.place(x = 30, y = 60)
        elif check2:
            if user_input == None:
                output = []
                for row in record:
                    store_none = []
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[2])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            else:
                output = []
                for row in record:
                    store_none = []
                    if user_input == row[0]:
                        store_none.append(row[0])
                        store_none.append(row[1])
                        store_none.append(row[2])
                        store_none.append(row[3])
                        store_none.append(row[4])
                        store_none.append(row[5])
                        output.append(store_none)
                    
            style = ttk.Style(right_frame)
            style.theme_use("clam")
            style.configure("Treeview", background = "#333333", fieldbackground = "#333333", foreground = "white", rowheight = 30)
                    
            table = ttk.Treeview(right_frame, style = "Treeview", height = 13, columns = ("Product Brand", "Type ID", "Buying Price", "Selling Price", "Stock", "Description"), show = "headings")
            table.heading("Product Brand", text = "Product Brand")
            table.heading("Type ID", text = "Type ID")
            table.heading("Buying Price", text = "Buying Price")
            table.heading("Selling Price", text = "Selling Price")
            table.heading("Stock", text = "Stock")
            table.heading("Description", text = "Description")
            
            table.column("Product Brand", width = 90, minwidth = 90, anchor = "center")
            table.column("Type ID", width = 100, minwidth = 100, anchor = "center")
            table.column("Buying Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Selling Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Stock", width = 50, minwidth = 50, anchor = "center")
            table.column("Description", width = 710, minwidth = 710, anchor = "center")
            
            for row in output:
                table.insert('', tk.END, values = row)
                
            scroll = ttk.Scrollbar(right_frame, orient = "vertical", command = table.yview)
            scroll.place(x = 1132, y = 60, height = 419)
            
            table.configure(yscrollcommand = scroll.set)
            table.place(x = 30, y = 60)
        elif check3:
            if user_input == None:
                output = []
                for row in record:
                    store_none = []
                    store_none.append(row[0])
                    store_none.append(row[1])
                    store_none.append(row[2])
                    store_none.append(row[3])
                    store_none.append(row[4])
                    store_none.append(row[5])
                    output.append(store_none)
            else:
                output = []
                for row in record:
                    store_none = []
                    if user_input == row[0]:
                        store_none.append(row[0])
                        store_none.append(row[1])
                        store_none.append(row[2])
                        store_none.append(row[3])
                        store_none.append(row[4])
                        store_none.append(row[5])
                        output.append(store_none)
                    
            style = ttk.Style(right_frame)
            style.theme_use("clam")
            style.configure("Treeview", background = "#333333", fieldbackground = "#333333", foreground = "white", rowheight = 30)
                    
            table = ttk.Treeview(right_frame, style = "Treeview", height = 13, columns = ("Product Brand", "Type ID", "Buying Price", "Selling Price", "Stock", "Description"), show = "headings")
            table.heading("Product Brand", text = "Product Brand")
            table.heading("Type ID", text = "Type ID")
            table.heading("Buying Price", text = "Buying Price")
            table.heading("Selling Price", text = "Selling Price")
            table.heading("Stock", text = "Stock")
            table.heading("Description", text = "Description")
            
            table.column("Product Brand", width = 90, minwidth = 90, anchor = "center")
            table.column("Type ID", width = 100, minwidth = 100, anchor = "center")
            table.column("Buying Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Selling Price", width = 75, minwidth = 75, anchor = "center")
            table.column("Stock", width = 50, minwidth = 50, anchor = "center")
            table.column("Description", width = 710, minwidth = 710, anchor = "center")
            
            for row in output:
                table.insert('', tk.END, values = row)
                
            scroll = ttk.Scrollbar(right_frame, orient = "vertical", command = table.yview)
            scroll.place(x = 1132, y = 60, height = 419)
            
            table.configure(yscrollcommand = scroll.set)
            table.place(x = 30, y = 60)