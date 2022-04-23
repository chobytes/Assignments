import time

class Time:
    
    def __init__(self) -> None:
        time_struct = time.localtime()
        self.__hour = time_struct[3]
        self.__minute = time_struct[4]
        self.__second = time_struct[5]
        
    def get_hour(self) -> int:
        return self.__hour

    def get_minute(self) -> int:
        return self.__minute

    def get_second(self) -> int:
        return self.__second

    def get_time(self) -> str:
        return f"{self.__hour}:{self.__minute}:{self.__second}"
    
    def set_time(self,elapsed_time:int) -> None:
        self.__second = elapsed_time%60
        self.__minute = (elapsed_time//60)%60
        self.__hour = (elapsed_time//3600)%24

def TEST():
    T_1 = Time()
    print("Current time is " + T_1.get_time())
    T_1.set_time(int(input("Enter the elapsed time: ")))
    print("The hour:minute:second from the elapsed time is " + T_1.get_time())
    print()

if __name__ == "__main__":
    TEST()


        