class Contact:
    all_contact = []
    def __init__(self, name, email):
        self.name = name
        self.email = email    


class EmailSender:
    def send_mail(self, msg):
        print(f"Send email to {self.email} with the following content: {msg}")

class EmailableContact(Contact, EmailSender):
    pass

e = EmailableContact("Bank", "bank@gmail.com")
e.send_mail("Hello how are you?")