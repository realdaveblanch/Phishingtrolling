import requests, json, names, random, time, string, datetime
from colorama import Fore, Back, Style

class TrollScammer:

    bad_url: str = ""
    bad_url_method: int = 0
    bad_url_username_name: str = ""
    bad_url_password_name: str = ""
    username_char_between = []
    email_provider = []
    count_request = 0

################################################################################

#                       LA VAINA

################################################################################

    def __init__(self):
        with open('email_provider.json','r') as file:
            self.email_provider = json.loads(file.read())
        self.username_char_between = ["", ".", "-"]

    def get_variables_by_cli(self):
        self.bad_url = self.get_string_cli("Direccion del server:")
        self.bad_url_username_name = self.get_string_cli("Parametro de transferencia para username?")
        self.bad_url_password_name = self.get_string_cli("Parametro de transferencia para password?")
        self.bad_url_method = self.get_numselect_cli("Mando las peticiones como 1) GET or 2) POST?", 2)

    def get_string_cli(self,input_message: str) -> str:
        while True:
            print(Fore.YELLOW+input_message+Style.RESET_ALL)
            input_val = input("> ")
            if isinstance(input_val, str) and len(input_val) >= 1:
                return input_val
            else:
                print(Fore.RED+"valor invalido, intentalo de nuevo"+Style.RESET_ALL)

    def get_numselect_cli(self, input_message: str, max_value: int) -> int:
        while True:
            print(Fore.YELLOW+input_message+Style.RESET_ALL)
            input_val = input("> ")
            if input_val.isnumeric() and int(input_val) >= 1 and int(input_val) <= max_value:
                return int(input_val)
            else:
                print(Fore.RED+"valor invalido, intentalo de nuevo"+Style.RESET_ALL)

################################################################################

#                       INTRO

################################################################################

    def print_query_information(self):
        print(Fore.GREEN+"""HOLA XD"""+Style.RESET_ALL)
        print("-----------------------------------------------")
        print(Fore.GREEN+"OBJETIVO: " + Style.RESET_ALL + self.bad_url)
        if self.bad_url_method == 1:
            print(Fore.GREEN+"METODO:" + Style.RESET_ALL + " GET")
        else:
            print(Fore.GREEN+"METODO:" + Style.RESET_ALL + " POST")
        print(Fore.GREEN+"USERNAME OBJETIVO: " + Style.RESET_ALL + self.bad_url_username_name)
        print(Fore.GREEN+"PASSWORD OBJETIVO: " + Style.RESET_ALL + self.bad_url_password_name)
        print("-----------------------------------------------")

################################################################################

#                       creador de datos random

################################################################################

    def create_username(self) -> str:
        try:
            username: str = ""
            username: str = names.get_full_name()
            username: str = username.replace(" ", random.choice(self.username_char_between))

            if random.randint(0,1) >= 1:
                username = username.lower()
            if random.randint(0,1):
                username = username + "@" + str(random.choice(self.email_provider))
        except Exception as e:
            username = self.create_username()

        return str(username)

    def create_password(self) -> str:
        password = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(random.randint(4, 30)))
        return password

################################################################################

#                       creador de requests

################################################################################

    def create_request(self, username: str, password: str) -> bool:
        # request
        if self.bad_url_method == 1:
            payload = {self.bad_url_username_name:username,self.bad_url_password_name:password}
            result = requests.get(self.bad_url, allow_redirects=False, params=payload)
        else:
            payload = {self.bad_url_username_name:username,self.bad_url_password_name:password}
            result = requests.post(self.bad_url, allow_redirects=False, data=payload)
        self.count_request += 1

        # salida
        format_status = Fore.RED+"[ "+str(result.status_code)+" ]"+Style.RESET_ALL
        if result.status_code == 200:
            format_status = Fore.GREEN+"[ "+str(result.status_code)+" ]"+Style.RESET_ALL

        format_number: str = Style.DIM+self.create_numstring_min_length(str(self.count_request))+Style.RESET_ALL
        format_datetime: str = Fore.BLUE+"["+datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")+"]"+Style.RESET_ALL
        format_username: str = self.create_string_min_length(username, 35)

        format_key_username: str = Fore.YELLOW+"username:"+Style.RESET_ALL
        format_key_password: str = Fore.YELLOW+"password:"+Style.RESET_ALL

        print(f"{format_datetime} {format_status} {format_number} {format_key_username} {format_username} - {format_key_password} {password}")

################################################################################

#                   vainas

################################################################################

    def create_numstring_min_length(self, value: str, min_length: int = 5):
        return self.create_string_min_length(value, min_length, "0", True)

    def create_string_min_length(self, value: str, min_lenth: int, fill_with: str = " ", leading: bool = False) -> str:
        extra_whitespace_len: str = "".join(fill_with for i in range(min_lenth - len(value)))
        if leading:
            return_value: str = extra_whitespace_len + value
        else:
            return_value: str = value + extra_whitespace_len
        return return_value
