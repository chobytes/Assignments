class Complex:
    def __init__(self,R:float = 0,I:float = 0) -> None:
        self.R = R 
        self.I = I
    
    def __str__(self) -> str:
        if self.I > 0:
            return f"({self.R} + {self.I}i)"
        elif self.I == 0:
            return f"({self.R})"
        else:
            return f"({self.R} - {-self.I}i)"

    def __add__(self,other:"Complex") -> "Complex":
        # (a+c)+(b+d)i
        return Complex(self.R + other.R, self.I + other.I)

    def __sub__(self,other:"Complex") -> "Complex":
        # (a-c)+(b-d)i
        return Complex(self.R - other.R, self.I - other.I)

    def __mul__(self,other:"Complex") -> "Complex":
        #(ac-bd)+(bc+ad)i
        return Complex(self.R * other.R - self.I * other.I, self.I * other.R + self.R * other.I)
    
    def __truediv__(self,other:"Complex") -> "Complex":
        #(ac+bd)/(c^2+d^2)+(bc-ad)/(c^2+d^2)
        return Complex((self.R * other.R + self.I * other.I)/(other.R**2 + other.I**2), (self.I * other.R - self.R * other.I)/(other.R**2 + other.I**2))

    def __abs__(self) -> str:
        return str((self.R**2 + self.I**2)**0.5)

    def get_realpart(self) -> float:
        return self.R
    
    def get_imaginarypart(self) -> float:
        return self.I

def TEST():
    R_1,I_1 = [float(x) for x in input("Enter the first complex number: ").split(",")]
    R_2,I_2 = [float(x) for x in input("Enter the second complex number: ").split(",")]

    alpha = Complex(R_1,I_1)
    beta = Complex(R_2,I_2)

    print(f"{alpha} + {beta} = {alpha + beta}")
    print(f"{alpha} - {beta} = {alpha - beta}")
    print(f"{alpha} * {beta} = {alpha * beta}")
    print(f"{alpha} / {beta} = {alpha / beta}")
    print(f"|{alpha}| = {abs(alpha)}")

if __name__ == "__main__":
    TEST()

