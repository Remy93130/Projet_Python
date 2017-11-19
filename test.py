from time import *


def main():
    tempsDebut=time()
    minute = 0
    while(True):
        tempsATM=int(time()-tempsDebut)
        if tempsATM >= 60:
            tempsATM = 0
            tempsDebut = time()
            minute += 1
        print(str(minute) + ':' + str(tempsATM))
        sleep(1)


if __name__ == '__main__':
    main()

