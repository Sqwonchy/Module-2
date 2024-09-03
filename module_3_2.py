def send_email(message, recipient,*,sender):
    send = sender
    if  len(send) ==  0:
        sender = "university.help@gmail.com"
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














send_email("fsdfds", "wefwef@ffe.net", sender="fweff@mail.ru" )
