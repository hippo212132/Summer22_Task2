class user:
    def __init__(self, id, type,  first_name, last_name, email, password):
        self.id = id
        self.type = type
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class student(user):
    def __init__(self, id, first_name, last_name, email, password):
        super().__init__(id, "student", first_name, last_name, email, password)
        







