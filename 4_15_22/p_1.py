class Fan:
    
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self,speed:str = "SLOW", radius:int = 5, color:str = "blue", on:bool = False) -> None:
        self.__speed = eval("self."+speed)
        self.__radius = radius  
        self.__color = color
        self.__on = on

    def get_speed(self) -> int:
        return self.__speed
    
    def get_radius(self) -> int:
        return self.__radius

    def get_color(self) -> str:
        return self.__color
    
    def get_on(self) -> bool:
        return self.__on

    def get_status(self) -> str:
        return f"speed:{self.__speed}, radius:{self.__radius}, color:{self.__color}, on:{self.__on}"

    def set_speed(self,n_speed:int) -> None:
        self.__speed = n_speed
    
    def set_radius(self,n_radius:int) -> None:
        self.__radius = n_radius
    
    def set_color(self,n_color:str) -> None:
        self.__color = n_color
    
    def set_on(self,n_on:bool) -> None:
        self.__on = n_on


def TEST():
    Fan_1 = Fan("FAST",10,"yellow",True)
    Fan_2 = Fan("MEDIUM",5,"blue",False)
    print("Fan_1: "+Fan_1.get_status())
    print("Fan_2: "+Fan_2.get_status())
    print()

if __name__ == "__main__":
    TEST()

