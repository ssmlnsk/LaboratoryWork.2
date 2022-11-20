from database import Database


class Facade:
    def __init__(self):
        self.db = Database()

    def read_employees(self):
        return self.db.read_employees()

    def read_workwear(self):
        return self.db.read_workwear()

    def read_types_of_workwear(self):
        return self.db.read_types_of_workwear()

    def read_issuance(self):
        return self.db.read_issuance()

    def read_entrance(self):
        return self.db.read_entrance()

    def read_supplier(self):
        return self.db.read_supplier()

    def read_issuance(self):
        return self.db.read_issuance()



    def insert_employee(self, surname, name, lastName, profession, post):
        self.db.insert_employee(surname, name, lastName, profession, post)

    def insert_workwear(self, name, type, cost, admission_data):
        self.db.insert_workwear(name, type, cost, admission_data)

    def insert_type_of_workwear(self, name):
        self.db.insert_type_of_workwear(name)

    def insert_entrance(self, date_of_entrance, supplier, quantity):
        self.db.insert_entrance(date_of_entrance, supplier, quantity)

    def insert_issuance(self, date_issuance, employee, term_of_use, workwear):
        self.db.insert_issuance(date_issuance, employee, term_of_use, workwear)

    def insert_supplier(self, name):
        self.db.insert_supplier(name)



    def delete_workwear(self, id):
        self.db.delete_workwear(id)

    def delete_type_of_workwear(self, id):
        self.db.delete_type_of_workwear(id)

    def delete_issuance(self, id):
        self.db.delete_issuance(id)

    def delete_entrance(self, id):
        self.db.delete_entrance(id)

    def delete_employee(self, id):
        self.db.delete_employee(id)

    def delete_supplier(self, id):
        self.db.delete_supplier(id)



    def update_workwear(self, id, name, type, cost, data):
        self.db.update_workwear(id, name, type, cost, data)

    def update_type_of_workwear(self, id, name):
        self.db.update_type_of_workwear(id, name)

    def update_entrance(self, doc, date, supplier, quantity):
        self.db.update_entrance(doc, date, supplier, quantity)

    def update_issuance(self, id, date, emp, term, workwear):
        self.db.update_issuance(id, date, emp, term, workwear)

    def update_employee(self, id, surname, name, lastName, profession, post):
        self.db.update_employee(id, surname, name, lastName, profession, post)

    def update_supplier(self, id, name):
        self.db.update_supplier(id, name)



    def get_employees(self):
        return self.db.get_employees()

    def get_workwear(self):
        return self.db.get_workwear()

    def get_supplier(self):
        return self.db.get_supplier()

    def get_entrance(self):
        return self.db.get_entrance()

    def get_type(self):
        return self.db.get_type()



    def get_id_workwear(self, name):
        return self.db.get_id_workwear(name)

    def get_id_employee(self, surname, name, last_name):
        return self.db.get_id_employee(surname, name, last_name)

    def get_id_type(self, name):
        return self.db.get_id_type(name)

    def get_id_supplier(self, name):
        return self.db.get_id_supplier(name)
