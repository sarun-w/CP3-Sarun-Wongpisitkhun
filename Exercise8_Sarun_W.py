"""

เขียนโปรแกรมร้านขายของโดยดัดแปลงจากโปรแกรมใน Lecture 40
ในการเข้าใช้งานโปรแกรมให้ผู้ล็อคอินโดยใช้ Username และ Password(ผู้เรียนกำหนดเอง)
หากสำเร็จ โปรแกรมจะขึ้นหน้าต้อนรับและแสดงรายการสินค้าพร้อมราคา (ผู้เรียนกำหนดเอง)
เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ
หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด

"""

checkStatus = True

while checkStatus:
    usernameInput = input("Username: ")
    passwordInput = input("Password: ")

    totalPrices = 0


    if usernameInput == "admin" or usernameInput == "client":
        if passwordInput == "1234":
            print("# Login Successes")
            # Product and Price.
            applePrice = 3
            bananaPrice = 6
            coconutPrice = 20
            doraemonPrice = 360
            
            print("------ Welcome to Market ------")
            print("1.Apple                    " + str(applePrice) + "฿")
            print("2.Banana                   " + str(bananaPrice) + "฿")
            print("3.Coconut                 " + str(coconutPrice) + "฿")
            print("4.Doraemon               " + str(doraemonPrice) + "฿")
            print("Please select your products per each.")

            if input("Apple? (Y/N) :") == "Y":
                totalPrices += int(input("How many do you want?: ")) * applePrice
            if input("Banana? (Y/N) :") == "Y":
                totalPrices += int(input("How many do you want?: ")) * bananaPrice
            if input("Coconut? (Y/N) :") == "Y":
                totalPrices += int(input("How many do you want?: ")) * coconutPrice
            if input("Doraemon? (Y/N) :") == "Y":
                totalPrices += int(input("How many do you want?: ")) * doraemonPrice

            if totalPrices != 0:
                print("Total product price: " + str(totalPrices) + "฿\nTHANK YOU, Have a nice day sir. :D")
            else:
                print("See you next time. :D")

            checkStatus = False

        else:
            print("# Username or password invalid. Please try again...")
    else:
        print("# Username or password invalid. Please try again...")
