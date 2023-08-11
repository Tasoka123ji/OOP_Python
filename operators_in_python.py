class Complex:
    def __init__(self, real: int, imag: int) -> None:
        self.real = real 
        self.imag = imag 

    def __neg__(self):
        return Complex(-self.real, -self.imag)
    
    def __pos__(self):
        return self
    
    def __abs__(self):
        return (self.real **2 + self.imag ** 2)** 0.5
    
    def __eq__(self, other):
        if self.imag == other.imag:
            return self.real == other.real
        return False 
    
    def __add__(self,other):
        real = self.real + other.real 
        imag = self.imag + other.real 
        return Complex(real, imag)
    
    def __str__(self) -> str:
        return f"({self.imag} + {self.real}j)"
    
    def __repr__(self) -> str:
        pass
    
x = Complex(1,5)
x == 1
