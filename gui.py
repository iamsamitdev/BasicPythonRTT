# โหลด module tkinter
import tkinter as tk


# สร้างฟังก์ชันสำหรับการคำนวณเบอร์โทร
def checkberdee():

    # ตัวแปรเก็บผลการทำนาย
    predict = ""

    total = sum(int(c) for c in phone_number.get())
    # ทำนายผลรวมของเบอร์
    if total in (9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 59, 63, 64, 65):
        predict = "ดีมาก"
    elif total in (69, 79):
        predict = "โอกาสประสบความสำเร็จสูง อุปสรรคน้อย"
    elif total in (10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57, 58, 60, 61):
        predict = "ดีปานกลาง"
    elif total in (62, 65, 68, 74, 75):
        predict = "เหนื่อย มีอุปสรรค โอกาสประสบความสำเร็จน้อย"
    elif total in (11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73, 76, 77, 78, 80):
        predict = "เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น"
    else:
        predict = "ไม่พบข้อมูล"

    display.config(text=predict)
    # print(phone_number.get())


# สร้าง object ของ tkinter
mainFrm = tk.Tk()

# กำหนด title
mainFrm.title("First Program")

# อ่านค่าความกว้าง และ สูง ของหน้าจอผู้ใช้
width = mainFrm.winfo_screenwidth()
height = mainFrm.winfo_screenheight()

# zoom windows
# mainFrm.state('zoomed')

# กำหนดความกว้าง x สูงของ โปรแกรม
mainFrm.geometry("600x200+10+20")
# mainFrm.geometry("%dx%d" % (width, height))

# ลองสร้าง label
label = tk.Label(mainFrm, text="โปรแกรมทำนายผลเบอร์โทร", font=("Tahoma", 24))
label.pack()

# สร้างช่องรับข้อมูล
phone_number = tk.Entry(mainFrm, font=("Tahoma", 24))
phone_number.pack()

# สร้างปุ่ม button
submit_button = tk.Button(
    mainFrm,
    text="ทำนายผล",
    font=("Tahoma", 20),
    command=checkberdee
)
submit_button.pack()

# แสดงผลการทำนาย
display = tk.Label(mainFrm, text="ผลทำนาย", font=("Tahoma", 20))
display.pack()

# คำสั่งแสดงผลหน้า GUI
mainFrm.mainloop()
