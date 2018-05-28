class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        self.privileges = Privileges(['read post'])

    def describe_user(self):
        print(self.first_name, self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(['create post', 'delete post', 'read post'])


class Privileges():

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Uprawnienia użytkownika to: ")
        for p in self.privileges:
            print(p)



user = User('Adam', 'Nowak')
admin = Admin('Jan', 'Kowalski')

user.privileges.show_privileges()
admin.privileges.show_privileges()