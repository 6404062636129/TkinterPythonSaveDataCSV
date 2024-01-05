from tkinter import *
import csv
mywin = Tk()
mywin.minsize()
mywin.title("ประวัติพนักงาน")

s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()
s6 = StringVar()
s7 = StringVar()
s8 = StringVar()
s9 = StringVar()
s10 = StringVar()
s11 = StringVar()
s12 = StringVar()
s13 = StringVar()


def save():
    lst = [["รหัส:{} ชื่อ:{} นามสกุล:{}\nเลขบัตรประชาชน:{} ชื่อเล่น:{}\nวันที่เกิด:{} อายุ:{} กรุ๊ปเลือด:{} "
            "เพศ:{} สัญชาติ:{}\nศาสนา:{} สถานภาพ:{} ที่อยู่:{} จังหวัด:{} รหัสไปรษณีย์:{}\nเบอร์โทรติดต่อ:{} อีเมล:{}"
            .format(s1.get(),variable.get(), s2.get(), s3.get(), s4.get(), s5.get(), s6.get(),
            s7.get(), s8.get(), variable2.get(), s9.get(), variable3.get(), variable4.get(),
                    variable5.get(), s10.get(), s11.get(), s12.get(), s13.get())]]

    with open("บันทึกพนักงาน.csv", "a+", encoding="utf8") as f:
        write = csv.writer(f)
        write.writerows(lst)

    mywin2 = Tk()
    mywin2.minsize()
    mywin.destroy()

def sh():
    with open("บันทึกพนักงาน.csv", "r", encoding="utf8") as f:
        rd = csv.reader(f)
        lst_sh = list(rd)
    for sha in lst_sh:
        print(sha)



ID = Label(mywin, text="รหัสพนักงาน").grid(row=0, column=1)
EnID = Entry(mywin, textvariable=s1).grid(row=0, column=2)

inch = Button(mywin, text="ค้นหา", command=sh).grid(row=0, column=3)


ID1 = Label(mywin, text="ขื่อ").grid(row=1, column=0)

def selected(choice):
    choice = variable.get()
    print(choice)
lst_ID = ["นาย", "นางสาว", "นาง"]
variable = StringVar()
variable.set(lst_ID[0])

dropdown = OptionMenu(mywin, variable, *lst_ID, command=selected)
dropdown.grid(row=1, column=1)

stID = Entry(mywin, textvariable=s2)
stID.grid(row=1, column=2)

ID2 = Label(mywin, text="นามสกุล").grid(row=1, column=3)
ndID = Entry(mywin, textvariable=s3)
ndID.grid(row=1, column=4)

ID3 = Label(mywin, text="เลขบัตรประชาชน").grid(row=2, column=0)
RID = Entry(mywin, textvariable=s4)
RID.grid(row=2, column=1)

ID4 = Label(mywin, text="ชื่อเล่น").grid(row=2, column=3)
nickname = Entry(mywin, textvariable=s5)
nickname.grid(row=2, column=4)

ID5 = Label(mywin, text="วันที่เกิด(วว/ดด/ปป)").grid(row=3, column=0)
b1 = Entry(mywin, textvariable=s6)
b1.grid(row=3, column=1)

age = Label(mywin, text="อายุ").grid(row=3, column=3)
ageent = Entry(mywin, textvariable=s7)
ageent.grid(row=3, column=4)

b2 = Label(mywin, text="กรุ๊ปเลือด").grid(row=4, column=0)
b2ent = Entry(mywin, textvariable=s8).grid(row=4, column=1)

b3 = Label(mywin, text="เพศ").grid(row=4, column=3)

def selected2(choice2):
    choice2 = variable2.get()
    print(choice2)

lst_sex = ["ชาย", "หญิง", "ไม่ระบุ"]
variable2 = StringVar()
variable2.set(lst_sex[0])

dropdown2 = OptionMenu(mywin, variable2, *lst_sex, command=selected2)
dropdown2.grid(row=4, column=4)

b4 = Label(mywin, text="สัญชาติ").grid(row=5, column=0)
b4ent = Entry(mywin, textvariable=s9).grid(row=5, column=1)

b5 = Label(mywin, text="ศาสนา").grid(row=5, column=3)

def selected3(choice3):
    choice3 = variable3.get()
    print(choice3)

lst_religion = ["พุทธ", "อิสลาม", "คริสต์", "พราหมณ์-ฮินดู"]
variable3 = StringVar()
variable3.set(lst_religion[0])

dropdown3 = OptionMenu(mywin, variable3, *lst_religion, command=selected3)
dropdown3.grid(row=5, column=4)

b6 = Label(mywin, text="สถานภาพ").grid(row=6, column=0)

def selected4(choice4):
    choice4 = variable4.get()
    print(choice4)

lst_status = ["โสด", "สมรส", "หย่าร้าง"]
variable4 = StringVar()
variable4.set(lst_status[0])

dropdown4 = OptionMenu(mywin, variable4, *lst_status, command=selected4)
dropdown4.grid(row=6, column=1)

b7 = Label(mywin, text="ที่อยู่").grid(row=7, column=0)
b7ent = Entry(mywin, textvariable=s10).grid(row=7, column=1)

b8 = Label(mywin, text="จังหวัด").grid(row=8, column=0)

def selected5(choice5):
    choice5 = variable5.get()
    print(choice5)

lst_province = ["กรุงเทพมหานคร", "กระบี่", "กาญจนบุรี", "กาฬสินธุ์", "กำแพงเพชร", "ขอนแก่น", "จันทบุรี",
"ฉะเชิงเทรา", "ชลบุรี", "ชัยนาท", "ชัยภูมิ", "ชุมพร", "เชียงราย", "เชียงใหม่",  "ตรัง", "ตราด", "ตาก", "นครนายก",
"นครปฐม", "นครพนม", "นครราชสีมา", "นครศรีธรรมราช", "นครสวรรค์",  "นนทบุรี", "นราธิวาส", "น่าน", "บึงกาฬ",
"บุรีรัมย์", "ปทุมธานี", "ประจวบคีรีขันธ์", "ปราจีนบุรี","ปัตตานี","พระนครศรีอยุธยา", "พะเยา", "พังงา", "พัทลุง",  "พิจิตร",
"พิษณุโลก","เพชรบุรี", "เพชรบูรณ์","แพร่", "ภูเก็ต","มหาสารคาม","มุกดาหาร","แม่ฮ่องสอน","ยโสธร","ยะลา","ร้อยเอ็ด",
"ระนอง","ระยอง","ราชบุรี","ลพบุรี","ลำปาง","ลำพูน","เลย","ศรีสะเกษ","สกลนคร","สงขลา","สตูล","สมุทรปราการ","สมุทรสงคราม",
"สมุทรสาคร","สระแก้ว","สระบุรี","สิงห์บุรี","สุโขทัย","สุพรรณบุรี","สุราษฎร์ธานี","สุรินทร์","หนองคาย","หนองบัวลำภู","อ่างทอง",
"อำนาจเจริญ", "อุดรธานี", "อุตรดิตถ์", "อุทัยธานี", "อุบลราชธานี"]

variable5 = StringVar()
variable5.set(lst_province[0])

dropdown5 = OptionMenu(mywin, variable5, *lst_province, command=selected5)
dropdown5.grid(row=8, column=1)

b9 = Label(mywin, text="รหัสไปรษณีย์").grid(row=8, column=2)
b9ent = Entry(mywin, textvariable=s11).grid(row=8, column=3)


b10 = Label(mywin, text="เบอร์โทรติดต่อ").grid(row=9, column=0)
b10ent = Entry(mywin, textvariable=s12).grid(row=9, column=1)

b11 = Label(mywin, text="อีเมล").grid(row=10, column=0)
b11ent = Entry(mywin, textvariable=s13).grid(row=10, column= 1)


btSAVE = Button(mywin, text="บันทึก", command=save).grid(row=11, columnspan=5, sticky="news")
btClOSE = Button(mywin, text="ออก", command=mywin.destroy).grid(row=12 ,columnspan=5, sticky="news")




mywin.mainloop()