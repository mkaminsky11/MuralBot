canvas_x = 5 * 12 # 5 feet
canvas_y = 5 * 12 # 5 feet

res_x = 2 # 1 inch
res_y = 2 # 1 inch

px_x = int(round(canvas_x / res_x))
px_y = int(round(canvas_y / res_y))

cam_pin = 12
# d1 = left
d1_pin = 16
d2_pin = 20
g_pin = 19
r_pin = 26
b_pin = 4

# speed_str # straight line speed (inches/sec)
# d1_speed_str
# d2_speed_str
# cam_t # how long to hold
# cam_angle # angle for cam
# turn_t
# d1_speed_turn
# d2_speed_turn
