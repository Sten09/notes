from datetime import datetime
import reader
import menu

def read_all():
    data = reader.read()
    
    if menu.id_or_time():
        return data
    else:
        lst = data.get("id")
        lst = sorted(lst, key=lambda x: x['time'], reverse=False)
        return lst
    
def read_one():
    data = reader.read()

    if menu.id_or_time():
        id_note = menu.id_()
        return data.get("id")[id_note]
    else:
        print("Format 09/03/23 1:51")
        ftime = input("Какое время вы ищете?\n")

        try:
            ftime = datetime.strptime(ftime, "%d/%m/%y %H:%M")
        except:
            return "Пробовать снова. Посмотрите на формат"

        lst = data.get("id")
        for elem in lst:
            if ftime == elem.get("time"):
                return(elem)
            else:
                continue