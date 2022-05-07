import time
from matplotlib import pyplot as plt
import random
_startbalance = 100
_balance = 100
_dead = False
if _balance <= 0:
    _dead = True

def round5():
    global _balance
    time.sleep(1)
    print("agent: this is the last round")
    time.sleep(1)
    print("agent: we have a quick rising company here")
    time.sleep(2)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10000, 11000, 12500, 13000, 12950, 13500, 14500, 15000, 15050, 15100]

    plt.plot(x, y, c='green')
    plt.title("koetjes")
    plt.ylabel("cow sold")
    plt.xlabel("Time quarterly")
    plt.show()
    time.sleep(2)
    print("agent: again... Invest all or nothing!")
    time.sleep(1)
    print("agent: let me know what your choice is asap")
    time.sleep(1)
    _choice1 = input("would you like to invest all? yes/no: ")
    if _choice1.lower() == "yes":
        time.sleep(2)
        print("okay lets do this")
        n = random.randint(1, 2)
        if n == 1:
            time.sleep(1)
            print("agent: Okay i have recieved the results")
            time.sleep(1)
            print("here we go!")
            time.sleep(2)
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            y = [10000, 11000, 12500, 13000, 12950, 13500, 14500, 15000, 15050, 15100, 26425]

            plt.plot(x, y, c='green')
            plt.title("koetjes")
            plt.ylabel("cow sold")
            plt.xlabel("Time quarterly")
            plt.show()
            time.sleep(2)
            time.sleep(2)
            print("agent: YES! it went up with 75%!!")
            time.sleep(1)
            _endbalance = int(_balance) * int(1.75)
            print("That means our current balance is $" + str(_endbalance))
            time.sleep(1)
            print("nice job!" + _name)
            time.sleep(2)
            print("ended with: $" + str(_balance))
            time.sleep(10)
            exit()
        if n == 2:
            time.sleep(1)
            print("agent: Okay i have recieved the results")
            time.sleep(1)
            print("here we go!")
            time.sleep(2)
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            y = [10000, 11000, 12500, 13000, 12950, 13500, 14500, 15000, 15050, 15100, 3775]

            plt.plot(x, y, c='green')
            plt.title("koetjes")
            plt.ylabel("cow sold")
            plt.xlabel("Time quarterly")
            plt.show()
            time.sleep(2)
            print("agent: ohno, it went down with 75%!!")
            time.sleep(1)
            _endbalance = _balance * 0.25
            print("That means our current balance is $" + str(_balance))
            time.sleep(1)
            print("Not the best job " + _name)
            time.sleep(2)
            print("ended with: $" + str(_endbalance))
            time.sleep(10)
            exit()

def round4():
    global _balance
    time.sleep(3)
    print("here are another two companies:")
    time.sleep(1)
    print("one is selling music boxes:")
    time.sleep(2)
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [500, 985, 1000, 875, 1118, 1580, 1480, 1225]

    plt.plot(x, y, c='green')
    plt.title("grixx")
    plt.ylabel("boxes sold")
    plt.xlabel("Time quarterly")
    plt.show()
    print("the other company is selling clothes")
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600]

    plt.plot(x, y, c='green')
    plt.title("h&g")
    plt.ylabel("clothes sold")
    plt.xlabel("Time quarterly")
    plt.show()
    _choice1 = input("wich company would you like to invest in? grixx or h&g: ")
    if _choice1.lower() == "grixx":
        investering1 = input("how much money would you like to invest in grixx? ")
        n = random.randint(1, 5)
        if n == 1:
            _callagent = input("action bar: ")
            if _callagent.lower() == "call agent":
                time.sleep(1)
                print("agent: lets view the results!")
                time.sleep(2)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [500, 985, 1000, 875, 1118, 1580, 1480, 1225, 612.5]

                plt.plot(x, y, c='green')
                plt.title("grixx")
                plt.ylabel("boxes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                print("agent: sadly ours went down with 50% and the h&g went up with 100%")
                _lossplayer1 = int(investering1) / 2
                _balance -= _lossplayer1
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600, 3200]

                plt.plot(x, y, c='green')
                plt.title("h&g")
                plt.ylabel("clothes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                if _balance < 0:
                    print("You have lost all of your money")
                    time.sleep(1)
                    print("Game over....")
                    time.sleep(5)
                    exit()
                if _balance > 0:
                    print("agent: well we still have some money left so lets continue!")
                    time.sleep(2)
                    time.sleep(2)
                    _keuze2 = input("continue or check balance?")
                    if _keuze2.lower() == "check balance":
                        time.sleep(1)
                        print("Your current balance is: $" + str(_balance))
                        round5()
                    if _keuze2.lower() == "continue":
                        round5()
        if n == 2:
            _callagent = input("action bar: ")
            if _callagent.lower() == "call agent":
                time.sleep(1)
                print("agent: lets view the results!")
                time.sleep(2)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [500, 985, 1000, 875, 1118, 1580, 1480, 1225, 1837.5]

                plt.plot(x, y, c='green')
                plt.title("grixx")
                plt.ylabel("boxes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                print("agent: YES! ours went up with 50%")
                _gainplayer1 = int(investering1) * 1.5
                _balance += _gainplayer1
                time.sleep(2)
                print("still some sad news... the other company went up with 100%")
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600, 3200]

                plt.plot(x, y, c='green')
                plt.title("h&g")
                plt.ylabel("clothes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                print("agent: well we still won somebits.")
                time.sleep(2)
                _keuze2 = input("continue or check balance?")
                if _keuze2.lower() == "check balance":
                    time.sleep(1)
                    print("Your current balance is: $" + str(_balance))
                    round5()
                if _keuze2.lower() == "continue":
                    round5()
                round5()
        if n == 3:
            _callagent = input("action bar: ")
            if _callagent.lower() == "call agent":
                time.sleep(1)
                print("agent: lets view the results!")
                time.sleep(2)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [500, 985, 1000, 875, 1118, 1580, 1480, 1225, 2450]

                plt.plot(x, y, c='green')
                plt.title("grixx")
                plt.ylabel("boxes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                print("agent: YES! ours went up with 100%")
                _gainplayer1 = int(investering1) * 2
                _balance += _gainplayer1
                time.sleep(2)
                print("Yes the other company went down with 50%!")
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600, 800]

                plt.plot(x, y, c='green')
                plt.title("h&g")
                plt.ylabel("clothes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                _keuze2 = input("continue or check balance?")
                if _keuze2.lower() == "check balance":
                    time.sleep(1)
                    print("Your current balance is: $" + str(_balance))
                    round5()
                if _keuze2.lower() == "continue":
                    round5()
        if n == 4:
            _callagent = input("action bar: ")
            if _callagent.lower() == "call agent":
                time.sleep(1)
                print("agent: lets view the results!")
                time.sleep(2)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [500, 985, 1000, 875, 1118, 1580, 1480, 1225, 612.5]

                plt.plot(x, y, c='green')
                plt.title("grixx")
                plt.ylabel("boxes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                print("agent: sadly ours went down with 50% but the h&g went down with 100%")
                _lossplayer1 = int(investering1) / 2
                _balance -= _lossplayer1
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600, 0]

                plt.plot(x, y, c='green')
                plt.title("h&g")
                plt.ylabel("clothes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                if _balance < 0:
                    print("You have lost all of your money")
                    time.sleep(1)
                    print("Game over....")
                    time.sleep(5)
                    exit()
                if _balance > 0:
                    print("agent: well we still have some money left so lets continue!")
                    time.sleep(2)
                    time.sleep(2)
                    _keuze2 = input("continue or check balance?")
                    if _keuze2.lower() == "check balance":
                        time.sleep(1)
                        print("Your current balance is: $" + str(_balance))
                        round5()
                    if _keuze2.lower() == "continue":
                        round5()

    if _choice1.lower() == "h&g":
        investering1 = input("how much money would you like to invest in h&g? ")
        n = random.randint(1, 5)
        if n == 1:
            _callagent = input("action bar: ")
            if _callagent.lower() == "call agent":
                time.sleep(1)
                print("agent: lets view the results!")
                time.sleep(2)

                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600, 800]

                plt.plot(x, y, c='green')
                plt.title("h&g")
                plt.ylabel("clothes sold")
                plt.xlabel("Time quarterly")
                plt.show()

                time.sleep(2)
                print("agent: sadly ours went down with 50% and the Grixx went up with 100%")
                _lossplayer1 = int(investering1) / 2
                _balance -= _lossplayer1
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600, 3200]

                plt.plot(x, y, c='green')
                plt.title("grixx")
                plt.ylabel("boxes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                if _balance < 0:
                    print("You have lost all of your money")
                    time.sleep(1)
                    print("Game over....")
                    time.sleep(5)
                    exit()
                if _balance > 0:
                    print("agent: well we still have some money left so lets continue!")
                    time.sleep(2)
                    time.sleep(2)
                    _keuze2 = input("continue or check balance?")
                    if _keuze2.lower() == "check balance":
                        time.sleep(1)
                        print("Your current balance is: $" + str(_balance))
                        round5()
                    if _keuze2.lower() == "continue":
                        round5()
        if n == 2:
            _callagent = input("action bar: ")
            if _callagent.lower() == "call agent":
                time.sleep(1)
                print("agent: lets view the results!")
                time.sleep(2)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600, 2400]

                plt.plot(x, y, c='green')
                plt.title("h&g")
                plt.ylabel("clothes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                print("agent: YES! ours went up with 50%")
                _gainplayer1 = int(investering1) * 1.5
                _balance += _gainplayer1
                time.sleep(2)
                print("still some sad news... the other company went up with 100%")
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [500, 985, 1000, 875, 1118, 1580, 1480, 1225, 2450]

                plt.plot(x, y, c='green')
                plt.title("grixx")
                plt.ylabel("boxes sold")
                plt.xlabel("Time quarterly")
                plt.show()

                time.sleep(2)
                print("agent: well we still won somebits.")
                time.sleep(2)
                _keuze2 = input("continue or check balance?")
                if _keuze2.lower() == "check balance":
                    time.sleep(1)
                    print("Your current balance is: $" + str(_balance))
                    round5()
                if _keuze2.lower() == "continue":
                    round5()
                round5()
        if n == 3:
            _callagent = input("action bar: ")
            if _callagent.lower() == "call agent":
                time.sleep(1)
                print("agent: lets view the results!")
                time.sleep(2)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600, 3200]

                plt.plot(x, y, c='green')
                plt.title("h&g")
                plt.ylabel("clothes sold")
                plt.xlabel("Time quarterly")
                plt.show()

                time.sleep(2)
                print("agent: YES! ours went up with 100%")
                _gainplayer1 = int(investering1) * 2
                _balance += _gainplayer1
                time.sleep(2)
                print("Yes the other company went down with 50%!")
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [500, 985, 1000, 875, 1118, 1580, 1480, 1225, 612,5]

                plt.plot(x, y, c='green')
                plt.title("grixx")
                plt.ylabel("boxes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                _keuze2 = input("continue or check balance?")
                if _keuze2.lower() == "check balance":
                    time.sleep(1)
                    print("Your current balance is: $" + str(_balance))
                    round5()
                if _keuze2.lower() == "continue":
                    round5()
        if n == 4:
            _callagent = input("action bar: ")
            if _callagent.lower() == "call agent":
                time.sleep(1)
                print("agent: lets view the results!")
                time.sleep(2)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [1000, 1560, 1500, 1670, 2000, 1500, 1560, 1600, 0]

                plt.plot(x, y, c='green')
                plt.title("h&g")
                plt.ylabel("clothes sold")
                plt.xlabel("Time quarterly")
                plt.show()

                time.sleep(2)
                print("agent: sadly ours went down with 50% but the grixx went down with 100%")
                _lossplayer1 = int(investering1) / 2
                _balance -= _lossplayer1
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                y = [500, 985, 1000, 875, 1118, 1580, 1480, 1225, 612.5]

                plt.plot(x, y, c='green')
                plt.title("grixx")
                plt.ylabel("boxes sold")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                if _balance < 0:
                    print("You have lost all of your money")
                    time.sleep(1)
                    print("Game over....")
                    time.sleep(5)
                    exit()
                if _balance > 0:
                    print("agent: well we still have some money left so lets continue!")
                    time.sleep(2)
                    time.sleep(2)
                    _keuze2 = input("continue or check balance?")
                    if _keuze2.lower() == "check balance":
                        time.sleep(1)
                        print("Your current balance is: $" + str(_balance))
                        round5()
                    if _keuze2.lower() == "continue":
                        round5()

def round3():
    global _balance
    time.sleep(3)
    print("welcome to the 3th round")
    time.sleep(2)
    print("agent: Big investing oppertunity alert!")
    time.sleep(1)
    print("agent: but there is a big risk to it tho")
    time.sleep(1)
    print("agent: you will invest all of your money into one company. that is selling high-tech lights")
    time.sleep(1)
    print("agent: there will be a 66,66% change of succes and you will have earned a lot of money")
    time.sleep(2)
    print("agent: but you can also lose all of your money")
    time.sleep(1)
    print("agent: with a 33,33% change of failure")
    time.sleep(3)
    print("agent: i will let you take a look at the graph")
    time.sleep(3)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2000, 3400, 4000, 4364, 4300, 5000, 5500, 5532, 6400]

    plt.plot(x, y, c='green')
    plt.title("Phillups")
    plt.ylabel("Lamps sold")
    plt.xlabel("Time quarterly")
    plt.show()
    time.sleep(2)
    print("agent: let me know what your choice is asap")
    _choice1 = input("would you like to invest? yes/no: ")
    if _choice1.lower() == "yes":
        time.sleep(2)
        print("okay lets do this")
        _investering1 = int(_balance)
        n = random.randint(1, 3)
        if n == 1:
            _balance += _investering1
            time.sleep(1)
            print("agent: Okay i have recieved the results")
            time.sleep(1)
            print("here we go!")
            time.sleep(2)
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            y = [2000, 3400, 4000, 4364, 4300, 5000, 5500, 5532, 6400, 12800]

            plt.plot(x, y, c='green')
            plt.title("Phillups")
            plt.ylabel("Lamps sold")
            plt.xlabel("Time quarterly")
            plt.show()
            time.sleep(2)
            print("agent: YES! it went up with 100%!!")
            time.sleep(1)
            print("That means our current balance is $" + str(_balance))
            time.sleep(1)
            print("great job" + _name)
            time.sleep(2)
            print("lets continue")
            time.sleep(1)
            round4()
        if n == 2:
            _balance += _investering1
            time.sleep(1)
            print("agent: Okay i have recieved the results")
            time.sleep(1)
            print("here we go!")
            time.sleep(2)
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            y = [2000, 3400, 4000, 4364, 4300, 5000, 5500, 5532, 6400, 12800]

            plt.plot(x, y, c='green')
            plt.title("Phillups")
            plt.ylabel("Lamps sold")
            plt.xlabel("Time quarterly")
            plt.show()
            time.sleep(2)
            print("agent: YES! it went up with 100%!!")
            time.sleep(1)
            print("That means our current balance is $" + str(_balance))
            time.sleep(1)
            print("great job" + _name)
            time.sleep(2)
            print("lets continue")
            round4()
        if n == 3:
            _balance += _investering1
            time.sleep(1)
            print("agent: Okay i have recieved the results")
            time.sleep(1)
            print("here we go!")
            time.sleep(2)
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            y = [2000, 3400, 4000, 4364, 4300, 5000, 5500, 5532, 6400, 0]

            plt.plot(x, y, c='green')
            plt.title("Phillups")
            plt.ylabel("Lamps sold")
            plt.xlabel("Time quarterly")
            plt.show()
            time.sleep(2)
            print("agent: i appears the company has gone bankrupt. i heard their boss was corrupt...")
            time.sleep(1)
            print("agent: well im going to find a new job. bye!")
            time.sleep(1)
            print("You have lost all of your money")
            time.sleep(1)
            print("Game over....")
            time.sleep(5)
            exit()

        elif _choice1.lower() != "yes":
            print("agent: okay. maby it was a good choice maby not")
            time.sleep(2)
            print("agent: lets continue to the next investing round!")
            time.sleep(1)
            round4()
def round2():
    global _balance
    time.sleep(3)
    print("welcome to your second choice of investing")
    time.sleep(1)
    print("before we start")
    time.sleep(1)
    print("i have developed an upgrade for you!")
    print("you will now, before investing see the graph of a company")
    time.sleep(4)
    print("to continue, you must always close the graph")
    time.sleep(4)
    print("lets start!")
    time.sleep(1)
    print("this first company is a touring company")
    time.sleep(3)
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [3000, 2500, 4500, 4000, 5000, 4250, 4000]

    plt.plot(x, y, c='green')
    plt.title("Paradise Travel (company)")
    plt.ylabel("bookings")
    plt.xlabel("Time quarterly")
    plt.show()
    input("press any button to continue")
    time.sleep(2)
    print("the other company is a now still failing milkshake company")
    time.sleep(1)
    print("i have heard roumors that it might be making a come back. but will you take that risk?")
    time.sleep(3)
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [2000, 1500, 1700, 1400, 1000, 880, 850]

    plt.plot(x, y, c='green')
    plt.title("melkshake (company)")
    plt.ylabel("orders")
    plt.xlabel("Time quarterly")
    plt.show()
    # ik was bezig met zorgen dat ze tegelijk open kunnen blijven staan.#
    input("press any button to continue")
    print("would you like to invest in Paradise Travel or Melkshake?")
    _keuze1 = input("Please awnser here: ")
    if _keuze1 == "Paradise Travel":
        time.sleep(1)
        _investering1 = input("how much do you want to invest? $")
        if int(_investering1) >= int(_balance):
            time.sleep(1)
            print("you dont have that on your account! please try again")
            round2()
        else:
            print("investment complete, you invested $" + str(_investering1) + " in Paradise Travel")
            time.sleep(1)
            print("call agent to view result")
            _callagent1 = input("action bar: ")
            if _callagent1.lower() == "call agent":
                print("agent:  Yes mate good call! i have just recieved the graph and it went up!")
                time.sleep(4)
                print("agent: i haven't yet recieved the result of Melkshake yet but i'll show you asap")
                time.sleep(3)
                print("meanwhile here are our results!")
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8]
                y = [3000, 2500, 4500, 4000, 5000, 4250, 4000, 5000]

                plt.plot(x, y, c='green')
                plt.title("Paradise Travel (company)")
                plt.ylabel("bookings")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                print("agent: Our stock went up with 125%!")
                _gainplayer1 = int(_investering1) * 2.25
                _balance += int(_gainplayer1)
                print("agent: That mean we have earned" + str(_gainplayer1) + "nice job!")
                time.sleep(3)
                print("agent: i have just recieved the other graph")
                time.sleep(1)
                print("agent: your not gonna like this.")
                x = [1, 2, 3, 4, 5, 6, 7, 8]
                y = [2000, 1500, 1700, 1400, 1000, 880, 850, 1500]

                plt.plot(x, y, c='green')
                plt.title("melkshake (company)")
                plt.ylabel("orders")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(1)
                print("agent: that went up with 176.47%")
                time.sleep(1)
                print("agent: at least we also made some money!")
                print("continue or check balance?")
                _keuze2 = input("action bar: ")
                if _keuze2.lower() == "check balance":
                    time.sleep(1)
                    print("Your current balance is: $" + str(_balance))
                    round3()
                if _keuze2.lower() == "continue":
                    round3()
    if _keuze1 == "Melkshake":
        time.sleep(1)
        _investering1 = input("how much do you want to invest? $")
        if int(_investering1) >= int(_balance):
            time.sleep(1)
            print("you dont have that on your account! please try again")
            round2()
        else:
            print("investment complete, you invested $" + str(_investering1) + " in Melkshake")
            time.sleep(1)
            print("call agent to view result")
            _callagent1 = input("action bar: ")
            if _callagent1.lower() == "call agent":
                print("agent:  Yes mate good call! i have just recieved the graph and it went up!")
                time.sleep(4)
                print("agent: i haven't yet recieved the result of Paradise Travel yet but i'll show you asap")
                time.sleep(3)
                print("agent: meanwhile here are our results!")
                time.sleep(1)
                x = [1, 2, 3, 4, 5, 6, 7, 8]
                y = [2000, 1500, 1700, 1400, 1000, 880, 850, 1500]

                plt.plot(x, y, c='green')
                plt.title("melkshake (company)")
                plt.ylabel("orders")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                print("agent: we went up with 176.47%!")
                _gainplayer1 = int(_investering1) * 2.77
                _balance += int(_gainplayer1)
                time.sleep(1)
                print("agent: oooh your gonna like this!")
                time.sleep(1)
                print("agent: the other company only went up with 125%!")
                time.sleep(2)
                print("agent: You made the right choice!")
                time.sleep(1)
                print("agent: here look at there graph!")
                time.sleep(3)
                x = [1, 2, 3, 4, 5, 6, 7, 8]
                y = [3000, 2500, 4500, 4000, 5000, 4250, 4000, 5000]

                plt.plot(x, y, c='green')
                plt.title("Paradise Travel (company)")
                plt.ylabel("bookings")
                plt.xlabel("Time quarterly")
                plt.show()
                time.sleep(2)
                print("continue or check balance?")
                _keuze2 = input("action bar: ")
                if _keuze2.lower() == "check balance":
                    time.sleep(1)
                    print("Your current balance is: $" + str(_balance))
                    round3()
                if _keuze2.lower() == "continue":
                    round3()

def round1():
        global _balance
        global _dead
        time.sleep(3)
        print("here are two companies:")
        time.sleep(2)
        # eerste bedrijf
        print("the first one is a company that is selling cars wich can go extremely fast")
        time.sleep(2)
        print("and they are selling them at a very low price")
        time.sleep(2)
        # tweede bedrijf
        print("the second company is a company giving away Free computers!!")
        time.sleep(2)
        # keuze
        print("would you like to invest in Quickies.com or indiancomputerNOVIRUS.com?")
        _keuze1 = input("Please awnser here: ")
        if _keuze1 == "Quickies.com":
            time.sleep(1)
            _investering1 = input("how much do you want to invest? $")
            if int(_investering1) >= int(_balance):
                time.sleep(1)
                print("you dont have that on your account! please try again")
                round1()
            else:
                print("investment complete, you invested $" + str(_investering1) + " in Quickies.com")
                time.sleep(1)
                print("call agent to view result")
                _callagent1 = input("")
                if _callagent1.lower() == "call agent":
                    print("good one, the other company was a scam obviously haha.")
                    time.sleep(1)
                    print("your investment went up with 150%")
                    _gainplayer1 = int(_investering1) * 2.5
                    _balance += int(_gainplayer1)
                    print("continue or check balance?")
                _keuze2 = input("action bar: ")
                if _keuze2.lower() == "check balance":
                    time.sleep(1)
                    print("Your current balance is: $" + str(_balance))
                    round2()
                if _keuze2.lower() == "continue":
                    round2()
        if _keuze1 == "indiancomputerNOVIRUS.com":
            time.sleep(0.25)
            time.sleep(0.25)
            time.sleep(0.25)
            print("uykdghffgdfg348237987d9f87dfgdfsahj2g3j123")
            time.sleep(0.25)
            print("312434!#*&$(*283798347938172349834234h")
            time.sleep(0.25)
            print("gdfdsfz*(&!@*(2hjhjfhd88971237dfjjdjf")
            time.sleep(0.25)
            print("E*&*(@&#Hjfh98d7f9*(*&98f7d987f9*&98f79df")
            time.sleep(0.25)
            print("*&797394873928ew74238972384")
            time.sleep(0.25)
            print("*&797394873928ew74238972384")
            time.sleep(0.25)
            print("it")
            time.sleep(0.25)
            print("uykdghffgdfg348237987d9f87dfgdfsahj2g3j123")
            time.sleep(0.25)
            print("appears")
            time.sleep(0.25)
            print("uykdghffgdfg348237987d9f87dfgdfsahj2g3j123")
            time.sleep(0.25)
            print("we")
            time.sleep(0.25)
            print("E*&*(@&#Hjfh98d7f9*(*&98f7d987f9*&98f79df")
            time.sleep(0.25)
            print("have")
            time.sleep(0.25)
            print("*&797394873928ew74238972384")
            time.sleep(0.25)
            print("been")
            time.sleep(0.25)
            print("E*&*(@&#Hjfh98d7f9*(*&98f7d987f9*&98f79df")
            time.sleep(0.25)
            print("HacKed")
            time.sleep(3)
            print("You have lost all of your money")
            time.sleep(1)
            print("Game over....")
            time.sleep(5)
            exit()


print("Welcome")
time.sleep(1)
_name = input("Please enter your name: ")
time.sleep(1)
print("oh hello " + _name)
time.sleep(1)
print("Lets get you started on this thing")
time.sleep(0.5)
print("This is your starter balance: $" + str(_startbalance))
time.sleep(3)
print("here we have a investment oppertunity")
time.sleep(1)
_choice1 = input("Would you like to invest $50 in this company? ")
if _choice1.lower() == "no":
    print("Fuck off!")
    time.sleep(1)
    exit()
else:
    time.sleep(1)
    print("nice lets view the result")
    time.sleep(0.5)
    print("to see your results you need to call your agent")
    time.sleep(2)
    print("to do that you have to type 'call agent' in the action bar")
    _whattodo1 = input("action bar: ")
    if _whattodo1 == "call agent" or "Call agent":
        print("your investment went the good way! went up by 100%, you have earned $100")
        _balance =+ 100
    else:
        print("something went wrong")
        exit()
    print("now that you have earned your first cash lets check your balance")
    time.sleep(1)
    print("to do that you need to type 'balance check' in the action bar")
    _whattodo2 = input("action bar: ")
    if _whattodo2.lower() == "balance check":
        print("Your current balance is: " + str(_balance))
        print("now its up to you to choose wich is best to invest in..."
            "i wish you good luck!")
        time.sleep(3)
        print("if something new comes up i'll let you know")
        round1()
    if _whattodo2.lower() == "round 2":
        round2()
    if _whattodo2.lower() == "round 3":
        round3()
    if _whattodo2.lower() == "round 4":
        round4()
    if _whattodo2.lower() == "round 5":
        round5()


