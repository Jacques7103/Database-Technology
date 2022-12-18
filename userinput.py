import mysql.connector
from mysql.connector import Error
import module

check_user = False
user = "INSERT INTO user(username, password, occupation, user_id) values(%s, %s, %s, %s)"
sql_user = "SELECT * FROM user"
sql_category = "SELECT * FROM category"
sql_worker = "SELECT MAX(user_id) FROM worker"
worker = "INSERT INTO worker(occupation, first_name, last_name) values(%s, %s, %s)"
category = "INSERT INTO category(category, product_brand) values(%s, %s)"
sql_television = "SELECT * FROM television"
sql_refrigerator = "SELECT * FROM refrigerator"
stock = "UPDATE %s SET stocks = %s WHERE type_id = %s"

class userInput:
    def userLogin():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                username = module.username_entry.get()
                password = module.password_entry.get()
                global check_user, user_login, occupation
                # occupation = ""
                user_login = []
                cursor.execute(sql_user)
                record = cursor.fetchall()
                for row in record:
                    if check_user == False:
                        if username == row[0]:
                            if password == row[1]:
                                occupation = row[2].lower()
                                check_user = True
                
                if check_user == False:
                    user_login.append(check_user)
                    return user_login
                else:
                    user_login.append(check_user)
                    user_login.append(occupation)
                    check_user = False
                    return user_login
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        
    def userRegister():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                first_name = module.first_name_entry.get()
                last_name = module.last_name_entry.get()
                username = module.user_entry.get()
                password = module.pass_entry.get()
                occupation = module.occupation_entry.get().lower()
                global check_user, user_register
                
                if first_name == "" or last_name == "" or username == "" or password == "" or occupation == "":
                    user_register = []
                    check_user = False
                    user_register.append(check_user)
                    return user_register
                
                cursor.execute(sql_user)
                record = cursor.fetchall()
                if len(record) == 0:
                    user_register = []
                    if occupation == "auditor" or occupation == "marketing" or occupation == "storekeeper":
                        value1 = (occupation, first_name, last_name)
                        cursor.execute(worker, value1)
                        cursor.execute(sql_worker)
                        record = cursor.fetchall()
                        for row in record:
                            user_id = row[0]
                        value2 = (username, password, occupation, user_id)
                        cursor.execute(user, value2)
                        connection.commit()
                        check_user = True
                        user_register.append(check_user)
                        user_register.append(occupation)
                        return user_register
                    else:
                        check_user = False
                        user_register.append(check_user)
                        return user_register
                for row in record:
                    user_register = []
                    if username == row[0]:
                        check_user = False
                        user_register.append(check_user)
                        return user_register
                    elif username != row[0]:
                        if occupation == "auditor" or occupation == "marketing" or occupation == "storekeeper":
                            value1 = (occupation, first_name, last_name)
                            cursor.execute(worker, value1)
                            cursor.execute(sql_worker)
                            record = cursor.fetchall()
                            for row in record:
                                user_id = row[0]
                            value2 = (username, password, occupation, user_id)
                            cursor.execute(user, value2)
                            connection.commit()
                            check_user = True
                            user_register.append(check_user)
                            user_register.append(occupation)
                            return user_register
                        else:
                            check_user = False
                            user_register.append(check_user)
                            return user_register
                        
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def getCategory():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                global category_list, category_item, brand
                category_list = []
                category_item = []
                brand = []
                cursor.execute(sql_category)
                record = cursor.fetchall()
                for row in record:
                    category_item.append(row[0])
                    brand.append(row[1])
                    
                category_list.append(category_item)
                category_list.append(brand)
                return category_list
            
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def getTV():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                cursor.execute(sql_television)
                record = cursor.fetchall()
                return record
                    
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def getFridge():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                cursor.execute(sql_refrigerator)
                record = cursor.fetchall()
                return record
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def editStock(int1):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                record = userInput.getTV()
                record2 = userInput.getFridge()
                television_id = []
                fridge_id = []
                dict_id = {}
                lcv = True
                brand = {}
                global check_user, edit_stock
                
                for row in record:
                    brand[row[1]] = row[0]
                    television_id.append(row[1])
                for row in record2:
                    brand[row[1]] = row[0]
                    fridge_id.append(row[1])
                    
                dict_id["Television"] = television_id
                dict_id["Refrigerator"] = fridge_id
                    
                type_id = module.type_id_entry.get()
                stock_num = module.edit_stock_entry.get()
                
                if stock_num.isdigit():
                    stock_num = int(stock_num)
                else:
                    edit_stock = []
                    check_user = False
                    edit_stock.append(check_user)
                    return edit_stock
                
                if module.int1.get() == 1:
                    category = "Refrigerator"
                elif module.int1.get() == 2:
                    category = "Television"
                else:
                    category = ""
                
                if category == "Refrigerator":
                    fridge = dict_id.get(category)
                    if type_id in fridge:
                        lcv = False
                elif category == "Television":
                    tv = dict_id.get(category)
                    if type_id in tv:
                        lcv = False
                else:
                    lcv = True
                
                if type_id == "" or stock_num == "" or int1.get() == 0 or lcv:
                    edit_stock = []
                    check_user = False
                    edit_stock.append(check_user)
                    return edit_stock
                
                edit_stock = []
                userInput.update_stock(category, stock_num, type_id)
                check_user = True
                brand_name = brand.get(type_id)
                edit_stock.append(check_user)
                edit_stock.append(category)
                edit_stock.append(brand_name)
                return edit_stock
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def update_stock(category, stock_num, type_id):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()   
                stock = f"UPDATE {category} SET stocks = {stock_num} WHERE type_id = '{type_id}'"
                cursor.execute(stock)
                connection.commit()           
                        
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def addData():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()  
                brand = module.product_brand_entry.get()
                type_id = module.type_id_2_entry.get()
                modal = module.modal_entry.get()
                sell = module.sell_entry.get()
                stocks = module.stocks_entry.get()
                desc = module.description_entry.get("1.0", "end-1c")
                global check_user, edit_stock
                
                if brand == "" or type_id == "" or modal == "" or sell == "" or stocks == "" or desc == "":
                    edit_stock = []
                    check_user = False
                    edit_stock.append(check_user)
                    return edit_stock
                
                try:
                    modal = float(modal)
                    sell = float(sell)
                    stocks = float(stocks)
                    if len(desc) > 200:
                        edit_stock = []
                        check_user = False
                        edit_stock.append(check_user)
                        return edit_stock
                except ValueError:
                    edit_stock = []
                    check_user = False
                    edit_stock.append(check_user)
                    return edit_stock
                
                if module.int1.get() == 1:
                    category = "Refrigerator"
                elif module.int1.get() == 2:
                    category = "Television"
                else:
                    edit_stock = []
                    check_user = False
                    edit_stock.append(check_user)
                    return edit_stock
                
                userInput.putData(category, brand, type_id, modal, sell, stocks, desc)
                edit_stock = []
                check_user = True
                edit_stock.append(check_user)
                edit_stock.append(category)
                edit_stock.append(brand)
                return edit_stock
        
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def putData(category, brand, type_id, modal, sell, stocks, desc):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()  
                data = f"INSERT INTO {category}(product_brand, type_id, modal_price, selling_price, stocks, description) values('{brand}', '{type_id}', '{modal}', '{sell}', '{stocks}', '{desc}')"
                cursor.execute(data)
                connection.commit()
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def removeData():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                type_id = module.type_id_3_entry.get()
                global check_user, edit_stock, brand
                
                if module.int1.get() == 1:
                    category = "Refrigerator"
                    cursor.execute(sql_refrigerator)
                    record = cursor.fetchall()
                    type_id_2 = []
                    check_brand = {}
                    for row in record:
                        type_id_2.append(row[1])
                        check_brand[row[1]] = row[0]
                    if type_id in type_id_2:
                        userInput.xData(category, type_id)
                        brand = check_brand.get(type_id)
                        edit_stock = []
                        check_user = True
                        edit_stock.append(check_user)
                        edit_stock.append(category)
                        edit_stock.append(brand)
                        return edit_stock
                    else:
                        edit_stock = []
                        check_user = False
                        edit_stock.append(check_user)
                        return edit_stock
                elif module.int1.get() == 2:
                    category = "Television"
                    cursor.execute(sql_television)
                    record = cursor.fetchall()
                    type_id_2 = []
                    check_brand = {}
                    for row in record:
                        type_id_2.append(row[1])
                        check_brand[row[1]] = row[0]
                    if type_id in type_id_2:
                        userInput.xData(category, type_id)
                        brand = check_brand.get(type_id)
                        edit_stock = []
                        check_user = True
                        edit_stock.append(check_user)
                        edit_stock.append(category)
                        edit_stock.append(brand)
                        return edit_stock
                    else:
                        edit_stock = []
                        check_user = False
                        edit_stock.append(check_user)
                        return edit_stock
                else:
                    edit_stock = []
                    check_user = False
                    edit_stock.append(check_user)
                    return edit_stock
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def xData(category, type_id):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                remove = f"DELETE FROM {category} where type_id = '{type_id}'"
                cursor.execute(remove)
                connection.commit()
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def changePrice():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                type_id = module.type_id_4_entry.get()
                modal = module.modal_2_entry.get()
                sell = module.sell_2_entry.get()
                global check_user, edit_stock
                check_brand = {}
                
                if module.int1.get() == 1:
                    category = "Refrigerator"
                    cursor.execute(sql_refrigerator)
                    record = cursor.fetchall()
                    for row in record:
                        check_brand[row[1]] = row[0]
                elif module.int1.get() == 2:
                    category = "Television"
                    cursor.execute(sql_television)
                    record = cursor.fetchall()
                    for row in record:
                        check_brand[row[1]] = row[0]
                else:
                    edit_stock = []
                    check_user = False
                    edit_stock.append(check_user)
                    return edit_stock
                
                try:
                    modal = float(modal)
                    sell = float(sell)
                    userInput.putPrice(category, modal, sell, type_id)
                    brand = check_brand.get(type_id)
                    edit_stock = []
                    check_user = True
                    edit_stock.append(check_user)
                    edit_stock.append(category)
                    edit_stock.append(brand)
                    return edit_stock
                except ValueError:
                    edit_stock = []
                    check_user = False
                    edit_stock.append(check_user)
                    return edit_stock
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def putPrice(category, modal, sell, type_id):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='stocks',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                mprice = f"UPDATE {category} SET modal_price = {modal} WHERE type_id = '{type_id}'"
                sprice = f"UPDATE {category} SET selling_price = {sell} WHERE type_id = '{type_id}'"
                cursor.execute(mprice)
                cursor.execute(sprice)
                connection.commit()
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()