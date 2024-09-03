def send_email(message, recipient,*,sender="university.help@gmail.com"):
    Dog = "@"
    chek_S = Dog in set(recipient)
    chek_R = Dog in set(sender)
    if recipient==sender:
        print("Нельзя отправить письмо самому себе!")
    elif chek_S == False or chek_R == False:
        print("Этот адрес нечитаем")
    elif sender[-4:] != ".com" and sender[-4:] != ".net" and sender[-3:] !=  ".ru":
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient[-4:] != ".com" and recipient[-4:] != ".net" and recipient[-3:] != ".ru":
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender != "university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender}  на адрес {recipient}')
    else:
        print(f'Письмо успешно отправлено с адреса {sender}  на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

