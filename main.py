class Login():
    def __init__(self , username ,password):
        self.username = username
        self.password = password
    def login(self):
        if self.username == 'admin' and self.password == '2097':
            print('Done')
        else :
            print('Wrong')
            return  get_user_pass()
def get_user_pass():
    username = input('username :')
    password = input('password :')
    return username ,password

username ,password = get_user_pass()
Login(username, password).login()

