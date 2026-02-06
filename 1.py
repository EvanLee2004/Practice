def calculate_circle_area(radius):
    area = 3.14 * radius ** 2
    return area
    
radius = float(input("输入半径:"))

result = calculate_circle_area(radius)

print(result)
