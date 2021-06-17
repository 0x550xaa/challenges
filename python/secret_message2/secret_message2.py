class SecretMessage:
    def __init__(self, x):
        self.x = x

    def encrypt(self):
        encrypted_string = ''
        for character in list(self.x):
            if 97 <= ord(character) <= 105:
                encrypted_string += str(ord(character) - 96)
            elif 106 <= ord(character) <= 122:
                encrypted_string += f'{ord(character) - 96}#'
            else:
                return
        return encrypted_string
            

    def decrypt(self):
        skip = 0
        decrypted_string = ''
        for i, j in enumerate(list(self.x)):
            if skip == 0:
                if j.isnumeric():
                    if i + 2 < len(self.x):
                        if list(self.x)[i + 2] == '#':
                            if f'{self.x[i:i + 2]}'.isnumeric():
                                if 10 <= int(f'{self.x[i:i + 2]}') <= 26:
                                    decrypted_string += chr(int(f'{self.x[i:i + 2]}') + 96)
                                else:
                                    return
                            else:
                                return
                            skip = 2
                        else:
                            if 1 <= int(j) <= 9:
                                decrypted_string += chr(int(j) + 96)
                            else:
                                return
                    else:
                        if 1 <= int(j) <= 9:
                            decrypted_string += chr(int(j) + 96)
                        else:
                            return
                else:
                    return
            else:
                skip -= 1
        return decrypted_string
