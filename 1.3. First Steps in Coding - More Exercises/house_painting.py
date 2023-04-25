x = float(input())    # height of the house
y = float(input())    # length of the house
h = float(input())    # height of the triangular part of the roof

side_wall = x * y
window_area = 1.5 * 1.5
side_walls = side_wall * 2 - (2 * window_area)
back_front_wall = x * x
doors = 1.2 * 2
back_front_walls = back_front_wall * 2 - doors

total_area_house = side_walls + back_front_walls
needed_paint_for_house = total_area_house / 3.4
print(f"{needed_paint_for_house:.2f}")

side_wall_roof = 2 * (x * y)
front_back_side_wall_roof = 2 * (x * h / 2)
total_area_roof = side_wall_roof + front_back_side_wall_roof
needed_paint_for_roof = total_area_roof / 4.3
print(f"{needed_paint_for_roof:.2f}")