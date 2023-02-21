import qrcode

# product_item = ["12340", "12341", "12342", "12343", "12344"]

print("QRcode Generate Program")
print("Please type 'quit' to exit program")

while True:
    product_data = input("Enter your product code:")
    if product_data == "quit":
        print("Your exit to program")
        break
    if len(product_data) == 5:
        # print(product_data)
        img = qrcode.make(product_data)
        type(img)
        img.save(f"product_qrcode/{product_data}.png")
    else:
        print("product code must lenght 5 number")

# for item in product_item:
#     # print(item)
#     img = qrcode.make(item)
#     type(img)
#     img.save(f"product_qrcode/{item}.png")
