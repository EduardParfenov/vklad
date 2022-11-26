########## Урок 26 ##########

# задача из предыдущего урока/ делаем с подключением файлов

from customer import Customer
from call_plan import CostumerFree2ndMinuteAfter10, CustomerTwiceCheaperFirst5Minutes

if __name__ == "__main__":

    ivan = Customer("Иван Петров", 100)

    elena = CostumerFree2ndMinuteAfter10("Елена Миронова", 100)
    ekaterina = CostumerFree2ndMinuteAfter10("Екатерина Ефимова", 100)
    sergey = CustomerTwiceCheaperFirst5Minutes("Сергей Васильев", 100)


    ivan.record_call("Г", 20)
    elena.record_call("Г", 20)
    ekaterina.record_call("М", 20)
    sergey.record_call("Г", 20)

    print(ivan)
    print(elena)
    print(ekaterina)
    print(sergey)

##########

# Банк предлагает ряд вкладов для физических лиц:
# Срочный вклад: расчет прибыли осуществляется по формуле простых процентов;
# Бонусный вклад: бонус начисляется в конце периода как % от прибыли, если
# вклад больше определенной суммы;
# Вклад с капитализацией процентов.
# Реализуйте приложение, которое бы позволило подобрать клиенту вклад по
# заданным параметрам.

from client import Client
from vklad import SuperVklad, CapitalVklad

# if __name__ == "__main__":
#
#     ivan = Client("Иван петров", 400000, 8, 12)
#     elena = SuperVklad("Елена Петрова", 600000, 9, 12)
#     ekaterina = SuperVklad("Екатерина Долгова", 450000, 8, 16)
#     sergey = CapitalVklad("Сергей Иванов", 670000, 12, 14)
#
#     print(ivan)
#     print(ivan.vklad(),"\n")
#     print(elena)
#     print(elena.vklad(),"\n")
#     print(ekaterina)
#     print(ekaterina.vklad(),"\n")
#     print(sergey)
#     print(sergey.vklad(),"\n")
