# Efiens CTF 2019 Round 2 -RE Challenges Write Up #
---

Ngày 24/10/2019 câu lạc bộ An toàn thông tin ĐH BKHCM - Efiens tổ chức tuyển thành viên round2. Đây là writeup của mình cho toàn bộ bài mảng RE.
## Picture Cipher ##
Ở bài này, người ra đề cho ta 3 file: plaintexGen.py, PictureCipher.exe và encrypted.png

Theo thói quen thì mở file code python ra đọc trước:
![](https://i.imgur.com/YDBHY31.png)

File này khá đơn giản, nó lấy từng ký tự của flag ra bỏ vào đầu dòng sau đó thêm một đống ký tự cho dòng dài ra rồi cuối cùng bỏ hết vào một file có tên là plaintext.txt

Tiếp đến là file PictureCipher.exe. File run trên window kìa, chạy thử phát

![](https://i.imgur.com/7i6ictU.png)

ĐÙ!!!!
Hóa ra đây là file để mã hóa từ cái plaintext.txt kia ra encrypt.png, có cả hàm decrypt nữa kìa chạy thử đê :v.


Đời méo như là mơ, có mỗi hàm encrypt là hoạt động, hàm decrypt thì méo thực thi được.

Check lại cái file phát nhẹ:
![](https://i.imgur.com/CUPfM1Q.png)

File .net asembly, bật dnSpy thôi :v

![](https://i.imgur.com/eAAYEyx.png)

Hàm encypt cũng khá là đơn giản, dựa vào mỗi hàng trong file plaintext thì chúng sẽ in ra màu theo ký tự trong hàng đó, vậy nên mình chỉ cần lấy được màu sắc của ô đầu tiên của mỗi hàng sau đó truy ngược lại cái số alpha là xong eazy game 

Mình viết một đoạn code python nhỏ nhỏ trong file solve.py:

    
    from PIL import Image
    
    im= Image.open('encrypted.png')
    pix=im.load()
    print(im.size)
    print(pix[0,0])
    a=[]
    for i in range(im.size[1]):
    a.append(chr(pix[0,i][3]))
    
    print("".join(a))

tèn tèn ra được flag: EFIENSCTF{If\_you\_spy\_this\_you\_are\_good\_in\_reversing\_C#}


## TAP TAP Flag

Source cho mình một file apk: taptap.apk

Mình run thử thì nó hiện ra một màn hình với số lần tap vô cùng lớn còn lại và một dòng có form của flag(tiếc quá submit cái này méo được). Mỗi lần tap thì flag sẽ thay đổi và hình như tap về 0 thì flag sẽ đúng.

![](https://i.imgur.com/999xNmj.png)
Mình có thử cheat một tí sửa luôn caí con số tap tap to bà bố kia về 0, nhưng mà nó méo ra đúng flag.

Thôi làm bình thường với apk vậy

Dùng apktools parse nó ra, sau đó dùng dextojar để chuyển file.class về file java. Dùng jd-gui mở lên mình được source của chương trình:

![](https://i.imgur.com/LWPvH5i.png)

Sau một hồi đọc code java mình nhận ra là đúng, mỗi lần tap thì flag sẽ decode 1 lần, tap=0 you win. Nhưng số lớn thế thì máy chạy cũng méo xong chứ huống chi là nhấn tay. Dựa vào hint của ban tổ chức: "(A + B) mod C = (A mod C + B mod C) mod C"

![](https://i.imgur.com/XiGY9Eb.png)

Đọc kỹ lại mình thấy mỗi lần mình decode thì nó sẽ dựa vào vị trí cũ cộng với số tap còn lại rồi modulo. Mỗi lần nó đều làm như vậy. Vậy thôi mình làm hộ nó cộng hết từ 1 -> tap một lần luôn đi cho lẹ :v

Mình có viết một đoạn script python để solve: 

    flag="Q806R554767513UR32QS4Q4120T00V91"
    tap=1628775989156
    sum1=tap*(tap+1)//2
    def take_table(param):
    	if param.isdigit():
    	return ("0123456789",(ord(param)-ord('0')))
    	else:
    	return ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",(ord(param)-ord('A')))
    def decode(param):
    	table,index=take_table(param)
    	print(sum1,table,i,table[(int)(sum1+index)%len(table)])
    	return table[(int)(sum1+index)%len(table)]
    a=[]
    for i in flag:
    	a.append(decode(i))
    print("EFIENSCTF{"+"".join(a)+"}")

Hè hè lần này flag submit được rồi : EFIENSCTF{A462B110323179EB98AC0A0786D66F57}


## License2 
Lần này đề cho một file ELF64 như thói quen thôi mình bỏ vào ida và bắt đầu vọc.

Mò tới hàm main mình thấy có mỗi hàm validate_flag là có giá trị:

Vào hàm này coi thì mình nhận ra: flag sẽ được in ra sau một số lần mình nhập đúng input password thôi, mà input password thì nó lồ lộ trong hàm này luôn rồi.

![](https://i.imgur.com/TUovsle.png) 

Có mỗi một khó khăn ở đây là hàm stoi() sử dụng đến các cơ số khác thôi, vì vây input mình nhập vào sau khi chuyển về cơ số mười bằng với giá trị so sánh là ok

Mình có viết một script ngăn ngắn để tính lại giá trị và nhập luôn vào file cho tiện:

  ` value=[196,2880,6892,5853,93,1986,7891,9872,235,687,3477,4911,5762,5766,9512,9457,9913,299,1656,1929,430,5390,4272,7516,3276]`

    base=[10,16,8,13,12,16,2,10,17,3,21,23,19,18,14,26,4,2,9,15,7,24,6,22,20]
    table="0123456789abcdefghijklmnopq"
    def convert(val,bas):
    	a=[]
    	while (val >= bas):
        	a.append(table[(val%bas)])
        	val=int(val/bas)
    	a.append(table[val])
    	return a[::-1]
    print("1")
    for i in range(len(value)):
    	print("".join(convert(value[i],base[i])))

   ![](https://i.imgur.com/fGRxcVO.png)
Vậy là xong :v
