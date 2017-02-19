from shutdown import *


class Control:
    '''
     This class passes the user's choice to the main class
    '''
    def __init__(self):
        choice = input("Enter 1 to shutdown\nEnter 2 to Reboot\nEnter 3 to Hibernate\nEnter 4 to logoff:\n")

        if choice == 1:
            self.shutdown1()
        elif choice == 2:
            self.Reboot()
        elif choice == 3:
            self.Hibernate()
        elif choice==4:
            self.Logoff()

    def shutdown1(self):
        time = input("In how many seconds should your system shut down:\n")
        force = input("Enter 1 for force shutdown and anything else if not force shut down:\n")
        warning = input("Enter 1 to give warning and anything else to not give warning:\n")

        if force == 1:
            force1 = True
        else:
            force1 = False

        if warning == 1:
            warning1 = False
        else:
            warning1 = True
        shutdown(time, force1, warning1)

    def Reboot(self):
        time = input("In how many seconds should your system shut down:\n")
        force = input("Enter 1 for force shutdown and anything else if not force shut down:\n")

        if force == 1:
            force1 = True
        else:
            force1 = False
        restart(time, force1)

    def Hibernate(self):
        force = input("Enter 1 for force shutdown and anything else if not force shut down:\n")
        if force == 1:
            force1 = True
        else:
            force1 = False
        hibernate(force1)

    def Logoff(self):
        force = input("Enter 1 for force shutdown and anything else if not force shut down:\n")

        if force == 1:
            force1 = True
        else:
            force1 = False
        logoff(force1)

if __name__ == '__main__':
    test = Control()