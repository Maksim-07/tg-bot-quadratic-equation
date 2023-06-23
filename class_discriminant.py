from math import sqrt


class Discriminant:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.equation = ""
        self.discriminant = 0
        self.discriminant_view = ""
        self.roots_discriminant = ""

    def complete_equation(self):
        if self.b < 0:
            if self.c < 0:
                self.equation = f"{self.a}x² - {abs(self.b)}x - {abs(self.c)} = 0"
                return
            self.equation = f"{self.a}x² - {abs(self.b)}x + {self.c} = 0"
            return
        else:
            if self.c < 0:
                self.equation = f"{self.a}x² + {self.b}x - {abs(self.c)} = 0"
                return
            self.equation = f"{self.a}x² + {self.b}x + {self.c} = 0"
            return

    def complete_discriminant(self):
        a = self.a if self.a > 0 else f'({self.a})'
        c = self.c if self.c > 0 else f'({self.c})'
        self.discriminant_view = f"D = {self.b}² - 4 × {a} × {c} = {self.discriminant}"

    def disc(self):
        if self.a == 0:
            return 'a != 0'
        self.discriminant = self.b * self.b - 4 * self.a * self.c
        if self.discriminant > 0:
            x1 = (-self.b + sqrt(self.discriminant)) / (2 * self.a)
            x2 = (-self.b - sqrt(self.discriminant)) / (2 * self.a)
            if self.b < 0:
                self.roots_discriminant = f"x₁ = ({abs(self.b)} + √{self.discriminant}) / (2 × {self.a}) " \
                                          f"= {'%.2f' % x1}\n" \
                                          f"x₂ = ({abs(self.b)} - √{self.discriminant}) / (2 × {self.a}) " \
                                          f"= {'%.2f' % x2}\n" \
                                          f"Имеет два корня: {'%.2f' % x1} и {'%.2f' % x2}"
            else:
                self.roots_discriminant = f"x₁ = (-{self.b} + √{self.discriminant}) / (2 × {self.a}) " \
                                          f"= {'%.2f' % x1}\n" \
                                          f"x₂ = (-{self.b} - √{self.discriminant}) / (2 × {self.a}) " \
                                          f"= {'%.2f' % x2}\n" \
                                          f"Имеет два корня: {'%.2f' % x1} и {'%.2f' % x2}"
        elif self.discriminant == 0:
            x = -self.b / (2 * self.a)
            if self.b < 0:
                self.roots_discriminant = f"x = {abs(self.b)} / (2 × {self.a}) = {x}\n" \
                                          f"Имеет один корень: {x}"
            else:
                self.roots_discriminant = f"x = -{self.b} / (2 × {self.a}) = {x}\n" \
                                          f"Имеет один корень: {x}"
        else:
            self.roots_discriminant = 'Дискриминант отрицательный. Корней нет.'

    def __str__(self):
        if self.a == 0:
            return 'a ≠ 0'
        self.complete_equation()
        self.disc()
        self.complete_discriminant()
        full_solution = f"{self.equation}\n{self.discriminant_view}\n{self.roots_discriminant}"
        return full_solution
