import time
# i = 1

# while i <= 10:
#     print(i)
#     # if i == 3:
#     #     continue
#     if i == 5:
#         break
#     i = i+1


# Infinity loop
r = 1
while True:
    if r > 20:
        break
    if r % 2 == 1:
        print(r, "On")
    else:
        print(r, "Off")
    r = r + 1

    # ทำการ sleep 1 วินาที
    time.sleep(0.5)
