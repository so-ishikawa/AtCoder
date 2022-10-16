import math

def rotate(target_point: tuple, origin_point: tuple, rad: float=math.pi/2) -> tuple:
    """
    target_pointをorigin_pointに対してradだけ回転させる
    
    target_point : tuple
        (x, y)形式 動かされる対象の2次元座標
    prigin_point : tuple
        (x, y)形式 回転の原点となる2次元座標
    rad : float
        回転する角度 デフォルトでは90度(パイ/2)
    """
    x = target_point[0] - origin_point[0]
    y = target_point[1] - origin_point[1]
    rotated_x = x * math.cos(rad) + y * -1 * math.sin(rad)
    rotated_y = x * math.sin(rad) + y * math.cos(rad)
    moved_x = int(rotated_x + origin_point[0])
    moved_y = int(rotated_y + origin_point[1])
    return (moved_x, moved_y)

# print(rotate((1,1),(2,4)))

"""
for i in range(10):
    for j in range(i+1, 10):
        print(i, j)
"""

s = int(input())
point_list = []
for i in range(s):
    point_list.append(tuple(map(int, input().split())))
check_set = set(point_list)

max_length_pow = 0
for i in range(len(point_list)):
    for j in range(i+1, len(point_list)):
        start_point = point_list[i]
        end_point = point_list[j]
        length_pow = pow((start_point[0] - end_point[0]), 2) + pow((start_point[1]-end_point[1]), 2)
        if max_length_pow > length_pow:
            continue
        rad = math.pi / 2
        rotated_point = rotate(start_point, end_point, rad)
        if rotated_point not in check_set:
            rad = -rad
            rotated_point = rotate(start_point, end_point, rad)
            if rotated_point not in check_set:
                continue

        start_point = end_point
        end_point = rotated_point

        rotated_2_point = rotate(start_point, end_point, rad)
        if rotated_2_point not in check_set:
            continue

        start_point = end_point
        end_point = rotated_2_point

        if rotate(start_point, end_point, rad) == point_list[i]:
            max_length_pow = length_pow
print(max_length_pow)
