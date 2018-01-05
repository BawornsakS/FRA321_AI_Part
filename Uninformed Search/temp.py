'''

#bronze 6

ณ ถนนแห่งหนึ่ง มีผู้ชายคนหนึ่งมีนิสัยชอบเดินปิดเปิดไฟบนถนนเส้นนั้น ถนนเส้นนั้นมีไฟอยู่ n ดวง 
แต่ละดวงมีเลขติดอยู่เรียงตามลำดับ 1 ถึง n และมี switch ติดอยู่ เมื่อถูกกดครั้งแรก ไฟจะติด ถ้ากดอีกครั้ง ไฟจะดับ สลับไปเรื่อยๆ

ผู้ชายคนนั้นจะเดินไปกลับ n รอบ โดยแต่ละรอบ (i) ถ้าเบอร์บนดวงไฟหารด้วย i ลงตัว ผู้ชายคนนั้นจะกดสวิตซ์ 1 ครั้ง 
จงเขียน function ชื่อ light ที่รับตัวแปร n (จำนวนไฟบนถนน) และ return ค่าว่า เมื่อผ่านไป n รอบ ไฟดวงสุดท้าย จะติดหรือดับ ถ้าติดให้ return “yes” ถ้าดับให้ return “no”
'''


def light(n):
    return "yes" if (math.floor(n**(1/2))**2 == n) else "no"


#testcase
print(light(6241))
print(light(3))
print(light(8191))
print(light(25))

'''

# bronze 7

ลำดับ Fibonacci, F(n) = F(n-1) + F(n-2), คือลำดับที่ตัวเลขที่ n จะเกิดจากตัวเลขที่ n-1 รวมกับตัวเลขที่ n-2 โดย F(1) = 1, F(2) = 2 เช่น
	1	1	2	3	5	8	13	21	34	…

กำหนดให้ตัวเลขมา 2 ตัว a และ b จงเขียน function ชื่อ nFibs(a,b) ที่จะ return ว่าระหว่าง a และ b มีจำนวน Fibonacci กี่ตัว
'''


def nFibs(m, n):
    count = 0
    previous = 1
    current = 1

    while current < n:

        temp = current
        current = previous + current
        previous = current

        if current >= m and current < n:
            count += 1

    return count
print(nFibs(10,100))
print(nFibs(5,21))
print(nFibs(141,311))
print(nFibs(1234567890,9876543210))


'''
Silver #2: Palindrome is back (with the numbers).

Palindrome คือข้อความที่พับครึ่งแล้วตัวอักษรจะเหมือนกัน เช่น aba, abba, abcba, moom, rotator

จงเขียน function ชื่อ reverseAndAdd(n) ที่ใส่ตัวเลข n เข้ามา นำตัวเลข n และตัวเลขที่กลับด้านของตัวเลข n มารวมกัน 
ถ้าผลรวมเป็น palindrome จึงจะหยุด และ return ค่า palindrome นั้นออกมา ไม่เช่นนั้นจะทำไปเรื่อยๆ 

เช่น reverseAndAdd(195) จะมี process ดังนี้
195 + 591 = 786
786 + 687 = 1473
1473 + 3741 = 5214
5214 + 4125 = 9339	<= palindrome 
'''


# silver

def reverseAndAdd(n):
    s = ""

    while 1:

        pal = True

        m = int(str(n)[::-1])
        s = str(n + m)

        for i in range(math.floor(len(s) / 2)):
            if (s[i] == s[len(s) - i - 1]):
                pal &= True
            else:
                pal &= False

        if pal:
            break
        n = int(s)

    return s

print(reverseAndAdd(750))
print(reverseAndAdd(195))
print(reverseAndAdd(265))
print(reverseAndAdd(1990))



'''

Gold #1: The Minesweeper

เกม Minesweeper เป็นเกมตารางขนาด a x b โดยช่องแต่ละช่องจะมีระเบิดอยู่หรือตัวเลขบอกว่ารอบข้างช่องนั้น(บน ล่าง ซ้าย ขวา แนวแทยง) มีระเบิดกี่ลูก 

จงเขียน function minesweep(a,b,s) ที่รับค่า a, b, และ s เข้ามา โดย a,b คือขนาดของตารางแนวนอนและแนวตั้ง 
และ s จะเป็น string ความยาว a x b โดยใน s จะมีเพียง 2 เครื่องหมายคือ * (แทนช่องที่มีระเบิด) และ . (แทนช่องที่ไม่มีระเบิด) 

function นี้จะ return board ที่มีตัวเลขใส่มาทั้งหมด เป็นลิสต์ 2 มิติ

เช่น
minesweep(5,3, "**.........*...")
>>>[['*', '*', 1, 0, 0], [3, 3, 2, 0, 0], [1, '*', 1, 0, 0]]
'''


def minesweep(a, b, s):
    l = []
    r = []
    for i in range(b):
        l += [[None] * a]
        r += [[0] * a]

    for i in range(b):
        for j in range(a):

            l[i][j] = s[(i * a) + j]

            if s[(i * a) + j] == "*":
                for m in range(j - 1, j + 2):
                    for n in range(i - 1, i + 2):
                        if (m >= 0 and m < a) and (n >= 0 and n < b):
                            r[n][m] += 1

    for i in range(b):
        for j in range(a):
            if l[i][j] == "*":
                r[i][j] = "*"
    return r

print(minesweep(4,4, "*........*......"))
print(minesweep(5,3, "**.........*..."))