from string import digits


def occurrencies(x, y):
    c = 0
    for i in y:
        c += x.count(i)
    return c


class Pw:
    def __init__(self, password):
        self.password = password
    
    def validate(self):
        if self.check_pw_length() and self.check_special_characters() and self.check_digits():
            print('Strong')
        else:
            print('Weak')

    def check_pw_length(self):
        if len(self.password) >= 7:
            return True
    
    def check_special_characters(self):
        if occurrencies(self.password, self.special_characters) >= 2:
            return True
    
    def check_digits(self):
        if occurrencies(self.password, list(digits)) >= 2:
            return True

    special_characters = ('!', '@', '#', '$', '%', '&', '*')
    


Pw(input()).validate()
