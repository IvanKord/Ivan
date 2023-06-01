def zadadka():
    LIFE=1
    while LIFE<=5:
        while LIFE<=5:
            print("Загадка 1: каких камней не бывает в реке?")
            answer1 = input()
            if answer1.lower() == "сухих":
                print("Верно")
                while LIFE<=5:
                    print("Загадка 2: Что не вместится даже в самую большую кастрюлю?")
                    answer2 = input()
                    if answer2.lower() == "крышка этой кастрюли":
                        print("Верно")
                        while LIFE<=5:
                            print("Загадка 3: Полтора судака стоят полтора рубля. Сколько стоят 13 судаков?")
                            answer3 = input()
                            if answer3.lower() == "13 рублей":
                                print("Верно")
                            else:
                                print("Неверно")
                                print(LIFE, "использована попыток из пяти для этой загадкиа")
                                LIFE+=1
                                if LIFE>=5:
                                    print("LIFE кончились")
                    else:
                        print("Неверно")
                        print(LIFE, "использована попыток из пяти для этой загадки")
                        LIFE+=1
                        if LIFE>=5:
                            print("LIFE кончились")
            else:
                print("Неверно")
                print(LIFE, "использована попыток из пяти для этой загадки")
                LIFE+=1
            if LIFE>=5:
                print("LIFE кончились")
zadadka()
