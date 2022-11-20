import mysql
from mysql.connector import connect


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='iejahjoU1', database='workwear')

    # READ

    def read_employees(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM employee")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def read_workwear(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM workwear")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def read_issuance(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM issuance")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def read_entrance(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM entrance")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def read_types_of_workwear(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM type_of_workwear")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def read_supplier(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM supplier")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def read_issuance(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM issuance")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    # INSERT

    def insert_employee(self, surname, name, lastName, profession, post):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO employee VALUES (NULL, %s, %s, %s, %s, %s)",(surname, name, lastName, profession, post))
        cursor.close()
        self.conn.commit()

    def insert_type_of_workwear(self, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO type_of_workwear VALUES (NULL, %s)", (name,))
        cursor.close()
        self.conn.commit()

    def insert_entrance(self, date_of_entrance, supplier, quantity):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO entrance VALUES (NULL, %s, %s, %s)",
                       (date_of_entrance, supplier, quantity))
        cursor.close()
        self.conn.commit()

    def insert_workwear(self, name, type, cost, admission_data):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO workwear VALUES (NULL, %s, %s, %s, %s)", (name, type, cost, admission_data))
        self.conn.commit()
        cursor.close()

    def insert_issuance(self, date_issuance, employee, term_of_use, workwear):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO issuance VALUES (NULL, %s, %s, %s, %s)", (date_issuance, employee, term_of_use, workwear))
        self.conn.commit()
        cursor.close()

    def insert_supplier(self, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO supplier VALUES (NULL, %s)", (name,))
        self.conn.commit()
        cursor.close()

    # UPDATE

    def update_issuance(self, id, date, employee, term, workwear):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE issuance set Date_of_issuance='{date}', Employee='{employee}', Term_of_use='{term}', workwear='{workwear}' WHERE ID_Issuance='{id}'")
        self.conn.commit()
        cursor.close()

    def update_employee(self, id, surname, name, lastname, profession, post):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE employee set Surname='{surname}', Name='{name}', Last_name='{lastname}', Profession='{profession}', Post='{post}' WHERE ID_Employee='{id}'")
        self.conn.commit()
        cursor.close()

    def update_entrance(self, doc, date, supplier, quantity):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE entrance set Date_Of_Entrance='{date}', Supplier='{supplier}', Quantity='{quantity}' WHERE Doc='{doc}'")
        self.conn.commit()
        cursor.close()

    def update_workwear(self, id, name, type, cost, data):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE workwear set name_workwear ='{name}', Type='{type}', Cost='{cost}', Admission_data='{data}' WHERE ID_Workwear='{id}'")
        self.conn.commit()
        cursor.close()

    def update_type_of_workwear(self, id, type):
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE type_of_workwear set Name='{type}' WHERE ID_Type='{id}'")
        self.conn.commit()
        cursor.close()

    def update_supplier(self, id, name):
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE supplier set name_supplier='{name}' WHERE id_supplier='{id}'")
        self.conn.commit()
        cursor.close()

    # DELETE

    def delete_employee(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM employee WHERE ID_Employee='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_workwear(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM workwear WHERE ID_Workwear='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_type_of_workwear(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM type_of_workwear WHERE ID_Type='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_entrance(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM entrance WHERE Doc='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_issuance(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM issuance WHERE ID_Issuance='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_supplier(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM supplier WHERE id_supplier='{id}'")
        self.conn.commit()
        cursor.close()

    #GET

    def get_employees(self):
        employee = ''
        employees = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Surname, Name, Last_name FROM employee")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                employee += j
                employee += ' '
            employees.append(employee[0:-1])
            employee = ''
        return employees
        cursor.close()

    def get_workwear(self):
        workwear = ''
        workwears = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT name_workwear FROM workwear")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                workwear += j
                workwear += ' '
            workwears.append(workwear[0:-1])
            workwear = ''
        return workwears
        cursor.close()

    def get_supplier(self):
        supplier = ''
        suppliers = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT name_supplier FROM supplier")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                supplier += j
                supplier += ' '
            suppliers.append(supplier[0:-1])
            supplier = ''
        return suppliers
        cursor.close()

    def get_type(self):
        type = ''
        types = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Name FROM type_of_workwear")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                type += j
                type += ' '
            types.append(type[0:-1])
            type = ''
        return types
        cursor.close()

    def get_entrance(self):
        entrances = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Doc FROM entrance")
        rows = cursor.fetchall()

        for i in rows:
            entrances.append(str(i)[1:-2])
        return entrances
        cursor.close()

    #GET ID

    def get_id_workwear(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT ID_Workwear FROM workwear WHERE name_workwear='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_id_employee(self, surname, name, lastname):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT ID_Employee FROM employee WHERE surname='{surname}' and name='{name}' and last_name='{lastname}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_id_type(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT ID_Type FROM type_of_workwear WHERE Name='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_id_supplier(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id_supplier FROM supplier WHERE name_supplier='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()
