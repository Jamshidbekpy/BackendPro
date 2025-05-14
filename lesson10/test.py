def process_point(p):
    match p:
        case (0, 0):
            return "Boshlanish nuqtasi"
        case (0, y):
            return f"Y o‘qi bo‘ylab: y={y}"
        case (x, 0):
            return f"X o‘qi bo‘ylab: x={x}"
        case (x, y):
            return f"Nuqta: ({x}, {y})"
        case _:
            return "Boshqa nuqta"
        
print(process_point((0, 0)))
print(process_point((0, 1)))
print(process_point((1, 0)))
print(process_point((1, 1)))
print(process_point((1, 2)))
print(process_point((2, 1)))