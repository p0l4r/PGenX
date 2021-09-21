'''
This is the pgenx.py module, providing the PGenX class. PGenX is a random password generator.
It also includes a database so that every user can have their password saved for future use. 
'''
import random
import string

class PGenX:
    def __init__(self, min_len=None):
        if min_len is None:
            self.min_len = random.randint(10, 20)
        else:
            self.min_len = min_len
        self.password = self.password_generator()
    
    def password_generator(self):
        '''
        This function generates a random password.
        '''
        password = ''
        special_char_list= ['!', '@', '#', '$', '_','.']
        for i in range(self.min_len):
            special_char_one = random.choice(special_char_list)
            special_char_two = random.choice(special_char_list)
            special_char_three = random.choice(special_char_list)
            special_char_four = random.choice(special_char_list)
            special_char_five = random.choice(special_char_list)
            special_char_six = random.choice(special_char_list)
            password += random.choice(string.ascii_letters + string.digits + special_char_one + special_char_two + 
                                      special_char_three + special_char_four + special_char_five + special_char_six)
        return password