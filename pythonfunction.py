# ฟังก์ชันแบบไม่มีการ return
def hello():
    print("Hello Python")


# เรียกใช้งานฟังก์ชัน hello()
hello()


# ฟังก์ชันแบบมีการรับค่า
def info(msg=""):
    print("Welcome", msg)


# เรียกใช้งานฟังก์ชัน info(msg)
info("Samit")


# ฟังก์ชันที่มีการรับค่าและมีการ return ค่าออกมา
def area(width=0, height=0, *other):
    return width * height


# เรียกใช้งาน area()
# area(5, 3)
print("Area is ", area())
print("Area is ", area(5, 3))
print("Area is ", area(3))
print("Area is ", area(3, 2, 5))
