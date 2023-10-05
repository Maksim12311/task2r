import json

registr = {'login':'passw'}

def reg(login, paswd):
    registr[login] = paswd
    with open('registration', 'w') as f:
            json.dump(registr, f)
    return registr


print("Введите логин")
login = input()
print("Введите пароль")
paswd = input()
if login in registr.keys():
    print('Логин занят')
else:
    result = reg(login, paswd)
    print(result)
    