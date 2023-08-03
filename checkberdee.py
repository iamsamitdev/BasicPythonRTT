def checkberdee(phone_number):
    # ตัวแปรเก็บผลการทำนาย
    predict = ""

    total = sum(int(c) for c in phone_number)
    # ทำนายผลรวมของเบอร์
    if total in (9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 59, 63, 64, 65):
        return "ดีมาก"
    elif total in (69, 79):
        return "โอกาสประสบความสำเร็จสูง อุปสรรคน้อย"
    elif total in (10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57, 58, 60, 61):
        return "ดีปานกลาง"
    elif total in (62, 65, 68, 74, 75):
        return "เหนื่อย มีอุปสรรค โอกาสประสบความสำเร็จน้อย"
    elif total in (11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73, 76, 77, 78, 80):
        return "เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น"
    else:
        return "ไม่พบข้อมูล"


phone = input("Enter your phone number:")
print(checkberdee(phone))
