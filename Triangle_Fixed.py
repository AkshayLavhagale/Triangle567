""" Name - Akshay Lavhagale
    HW 02: Improving triangle classification function
    The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral,
    and whether it is a right triangle as well. """


def classifyTriangle(a, b, c):
    # This function will tell us whether the triangle is scalene, isosceles, equilateral or right triangle
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return 'InvalidInput'

    if any([a > 200, b > 200, c > 200]) or any([a <= 0, b <= 0, c <= 0]):
        return 'InvalidInput'
    [a, b, c] = sorted([a, b, c])
    if (a + b) > c and (a + c) > b and (b + c) > a:
        if round(((a ** 2) + (b ** 2)), 2) == round((c ** 2), 2):
            if a == b or b == c or c == a:
                return 'Right Isosceles'
            else:
                return 'Right Scalene'
        elif a == b == c:
            return 'Equilateral'
        elif a == b or b == c or a == c:
            return 'Isosceles'
        else:
            return 'Scalene'
    else:
        return 'NotATriangle'
