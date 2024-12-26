import random as r
import pyperclip as pclip

class RandomPassword:
    def get_pass(self, password_box):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_']

        nr_letters = r.randint(6, 8)
        nr_symbols = r.randint(1, 3)
        nr_numbers = r.randint(2, 4)

        password_list = []
        for char in range(nr_letters):
            password_list.append(r.choice(letters))
        for char in range(nr_symbols):
            password_list += r.choice(symbols)
        for char in range(nr_numbers):
            password_list += r.choice(numbers)

        r.shuffle(password_list)
        random_password = "".join(password_list)

        pclip.copy(random_password)
        password_box.delete(0, 'end')
        password_box.insert('end', random_password)
