import math
rings = '01234'
rads = 'abcdefgh'
y = (2 - 2 * math.cos(math.pi / 4))**(1/2)

start_point = input('start: ').lower()
final_point = input('final: ').lower()

st_rad = min(ord(start_point[0]) - 97, ord(final_point[0]) - 97)
fl_rad = max(ord(start_point[0]) - 97, ord(final_point[0]) - 97)

if chr(st_rad + 97) in start_point:
    st_ring = int(start_point[1])
    fl_ring = int(final_point[1])
else:
    st_ring = int(final_point[1])
    fl_ring = int(start_point[1])

# выделение только тех радиан, которые образуют между начальной и конечной точками угол <= 180 градусов
web = []
if fl_rad - st_rad > 4:
    for i in range(9 - (fl_rad - st_rad)):
        for j in range(fl_ring + 1):
            web.append(chr((i+fl_rad) % 8 + 97) + str(rings[j]))

else:
    for i in range(st_rad, fl_rad + 1):
        for j in range(max(st_ring, fl_ring) + 1):
            web.append(chr(i + 97) + str(rings[j]))

print(web)
# заполение графа от начальной точки пока не встретится конечная
# объеденить точки a0, b0, c0,... в точку O ({O:{a1:1, b1:1, c1:1, d1:1, e1:1, f1:1, g1:1, g1:1}})
# {St_Rad St_Ring:{
#       St_Rad-1 St_Ring:y*Ring,
#       St_Rad+1 St_Ring:y*Ring,
#       St_Rad St_Ring-1:1,
#       St_Rad St_Ring+1:1},
#  St_Rad-1 St_Ring:{...},
#  ...}
graph = {}
