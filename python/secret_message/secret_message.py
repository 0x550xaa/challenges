from string import ascii_lowercase


class SecretMessage:
    def __init__(self, msg):
        self.msg = msg
    
    def translate(self):
        secret_message = ''.join([self.invert_char(i) for i in list(self.msg)])
        print(secret_message)
    
    def invert_char(self, x):
        if x.lower() in ascii_lowercase:
            return chr(122 - (ord(x.lower()) - 97))
        return x



SecretMessage(input()).translate()
