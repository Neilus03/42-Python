class Vector:
    def __init__(self, values: list, shape: tuple):
        self.values = values
        if len(values) == 1:
            self.shape = (1, len(values[0]))
        else:
            self.shape = (len(values), 1)
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('la operación de suma solo se puede realizar entre vectores')
        if self.shape != other.shape:
            raise ValueError('Las dimensiones de los vectores no coinciden.')
        else:
            return Vector([[x+y for x,y in zip(self.values, other.values)]], self.shape)
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('la operación de suma vecctorial solo se puede realizar entre vectores')
        if self.shape != other.shape:
            raise ValueError('Las dimensiones de los vectores no coinciden.')
        else:
            return Vector([[x-y for x,y in zip(self.values, other.values)]], self.shape)
            
        
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError('la operación de multiplicación solo se puede realizar entre escalar y vector')
        else:
            return Vector([[x*scalar] for x in self.values], self.shape)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError('la operación de división solo se puede realizar entre vector y escalar')
        else:
            return Vector([[x/scalar] for x in self.values], self.shape)
    
    def __rtruediv__(self, scalar):
        raise ArithmeticError('no se puede dividir un escalar por un vector')
    
    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError('la operación "dot product" solo se puede realizar entre vectores')
        if self.shape != other.shape:
            raise ValueError('Las dimensiones de los vectores no coinciden.')
        else:
            dot = sum([x*y for x,y in zip(self.values, other.values)])
            return dot

    def T(self):
        if self.shape == (1, len(self.values[0])):
            self.shape = (len(self.values[0]), 1)
            self.values = [[val] for val in self.values[0]]
            return Vector(self.values, self.shape)
        elif self.shape == (len(self.values), 1):
            self.shape = (1, len(self.values))
            self.values = [val[0] for val in self.values]
            return Vector(self.values, self.shape)
        else:
            raise ValueError("Transpose is not defined for shapes other than (1, n) and (n, 1)")

            
            