
    da = input("начать тест: Да/Нет \n ваши ошибки: 0")
    if a == 'Да' or a == 'да':
        print("Росло 3 березы. На каждой березе по 7 больших веток. На каждой большой ветке по 7 маленьких веток. \n На каждой маленькой ветке – по 3 яблока. Сколько всего яблок?")
        ot1 = input()
        if ot1 == "Ни одного" or ot1 == "ни одного":
            print("Правильный ответ")
            print("За какие административные правонарушения в области дорожного движения предусмотрено наказание в виде обязательных работ? \n 1. За управление транспортным средством водителем, не имеющим права управления транспортным средством (за исключением учебной езды). \n 2. За управление транспортным средством водителем, лишенным права управления транспортными средствами. \n 3. За передачу управления транспортным средством лицу, заведомо не имеющему права управления (за исключением учебной езды) или лишенному такого права. \n 4. За все перечисленные правонарушения.")
            ot2 = input()
            if ot2 == "2":
                print("Правильный ответ")
                print("Сколько фотонов с длиной волны 0,56 мкм излучает лампа мощностью 40 Вт в 1 с, если ее тепловая отдача 5%?")
                ot3 == input()
                if ot3 == "5.64*10^18" or ot3 == "5.64*10**18":
                    print("Правильный ответ \n Вы прошли!")
                else:
                    print("Ошибка \n Ваши ошибки1: 1")
            else: 
                print("Неравильный ответ")
                print("Сколько фотонов с длиной волны 0,56 мкм излучает лампа мощностью 40 Вт в 1 с, если ее тепловая отдача 5%?")
                ot3 == input()
                if ot3 == "5.64*10^18" or ot3 == "5.64*10**18":
                    print("Правильный ответ \n Ваши ошибки1: 1")
                else:
                    print("Ошибка \n Ваши ошибки1: 2")
        else:
             print("Нкправильный ответ")
            print("За какие административные правонарушения в области дорожного движения предусмотрено наказание в виде обязательных работ?", end="\n","1. За управление транспортным средством водителем, не имеющим права управления транспортным средством (за исключением учебной езды).", end="\n","2. За управление транспортным средством водителем, лишенным права управления транспортными средствами.", end="\n","3. За передачу управления транспортным средством лицу, заведомо не имеющему права управления (за исключением учебной езды) или лишенному такого права.", end="\n","4. За все перечисленные правонарушения.")
            ot2 = input()
            if ot2 == "2":
                print("Правильный ответ")
                print("Сколько фотонов с длиной волны 0,56 мкм излучает лампа мощностью 40 Вт в 1 с, если ее тепловая отдача 5%?")
                ot3 == input()
                if ot3 == "5.64*10^18" or ot3 == "5.64*10**18":
                    print("Правильный ответ", end="\n", "Ваши ошибки1: 1")
                else:
                    print("Ошибка", end="\n", "Ваши ошибки1: 2")
            else: 
                print("Неравильный ответ")
                print("Сколько фотонов с длиной волны 0,56 мкм излучает лампа мощностью 40 Вт в 1 с, если ее тепловая отдача 5%?")
                ot3 == input()
                if ot3 == "5.64*10^18" or ot3 == "5.64*10**18":
                    print("Правильный ответ", end="\n", "Ваши ошибки1: 2")
                else:
                    print("Ошибка", end="\n", "Ваши ошибки1: 3")
    else:
        print('Ваши ошибки1: 9999999999999999999999999999')


