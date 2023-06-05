def login(self , username , password):
    self.username = username
    self.password = password
    if self.username == 'admin' and self.password == '123456789':
        return main()