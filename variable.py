# การสร้างตัวแปรใน python
a = 3
b = 4.95
c = "Python Programming"

print(a)
print(b)
print(c)

print(a, b, c)

x = y = z = 10

print(x, y, z)

j, k = 5, 10

print(j, k)

# Boolean
status = True  # 1
msg = False  # 0

print(status, msg)

print(status == 1)
print(msg == 0)

# การแสดงผลตัวแปรในคำสั่ง print ร่วมกับข้อความ
price = 300.5098339
qty = 10

# แบบที่ 1
print("Product price =", "{:.2f}".format(price), "Product Qty =", qty)
# แบบที่ 2
print("Product price = %.2f Product Qty = %d" % (price, qty))
# แบบที่ 3
print(f"Product price = {price:.2f} Product Qty = {qty}")
