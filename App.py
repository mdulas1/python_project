class App:
    def _int_(self,users,storage,username):
        self.users = users
        self.storage = storage
        self.username =  username

    def login(self):
        if self.username == "jibrin" and self.users >= 1:
            print("wellcome", self.username)
            print("your storage is", self.storage)
        else:
            print("login denied")

    def increase_capacity(self,number):
        self.storage += number
        print("updated storage:",self.storage)

product_one =(35,256,"jibrin")
product_one.login()
product_one.increase_capacity(30)
print()

product_two =(50,19,"mt")
product_two.login()

