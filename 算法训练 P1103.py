class Complex:
    def __init__(self,a,b):
        self.real_part = a
        self.imaginary_part = b

    def get_real_part(self):
        return self.real_part

    def get_imaginary_part(self):
        return self.imaginary_part

    def get_conjugate(self):
        return Complex(self.real_part,-self.imaginary_part)

    def plus(self,c2):
        a = self.real_part + c2.get_real_part()
        b = self.imaginary_part + c2.get_imaginary_part()
        return Complex(a,b)

    def subtract(self,c2):
        a = self.real_part - c2.get_real_part()
        b = self.imaginary_part - c2.get_imaginary_part()
        return Complex(a,b)

    def multiply(self,c2):
        a = self.real_part * c2.get_real_part() - self.imaginary_part * c2.get_imaginary_part()
        b = self.real_part * c2.get_imaginary_part() + self.imaginary_part * c2.get_real_part()
        return Complex(a,b)

    def divide(self,c2):
        c3 = self.multiply(c2.get_conjugate())
        return Complex(c3.get_real_part()/(c2.get_real_part()**2+c2.get_imaginary_part()**2),c3.get_imaginary_part()/(c2.get_real_part()**2+c2.get_imaginary_part()**2))

if __name__ == '__main__':
    opt,c1r,c1i,c2r,c2i = input().split()
    c1 = Complex(float(c1r),float(c1i))
    c2 = Complex(float(c2r),float(c2i))
    if opt == '+':
        c3 = c1.plus(c2)
    elif opt == '-':
        c3 = c1.subtract(c2)
    elif opt == '*':
        c3 = c1.multiply(c2)
    else:
        c3 = c1.divide(c2)
    if -0.05<c3.get_real_part()<0.05:
        a = 0
    else:
        a = c3.get_real_part()
    if -0.05<c3.get_imaginary_part()<0.05:
        b = 0
    else:
        b = c3.get_imaginary_part()
    print("{:.2f}+{:.2f}i".format(a,b))
        
