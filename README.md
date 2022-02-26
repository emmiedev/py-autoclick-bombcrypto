# Auto click แบบบ้านๆสไตล์ EmmieDev
## ทดสอบบน MacOS แล้ว Worked! ไว้ทำเสร็จแล้วจะทำสำหรับ Windows และ Linux อีกทีครับผม
ต้องบอกก่อนว่า ทำเล่น ๆ เพื่อการศึกษาการเขียนโปรแกรม จะนำไปพัฒนาต่อก็จัดได้เลยครับ ไม่ต้องให้เครดิตก็ได้ครับ ^^ 
ใครใจดีก็บริจาคได้นะครับคนละนิดละนิดละหน่อย บริจาคได้ที่ 

BSC : 0x55dBA6cb9eA827D518FfDEcF92f2c706A803581e

ผมพัฒนาต่อยอดเรื่อยๆตามการใช้งานของผมเองครับ ติดอะไรผมก็ปรับไปเรื่อย ตอนนี้ผมมีจอเดียว ถ้ามีหลายจออาจจะได้ทำแบบกดหลายจอให้ใช้กันด้วยครับผม
ตอนนี้มีแผนจะทำแบบ image recognition จะได้ไม่ต้องมานั่งใส่พิกัด X, Y กันให้ยุ่งยาก 😍

# ติดตั้ง Library
```
pip install -r requirements.txt
```

# การตั้งค่าที่ไฟล์ config.json

```{
    "refresh_btn": {
        "x": 84,
        "y": 84
    },
    "connect_btn_pos": {
        "x": 961,
        "y": 655
    },
    "sign_bnt_pos": {
        "x": 1817,
        "y": 590
    },
    "strat_game": {
        "x": 952,
        "y": 457
    },
    "get_bomber_pos": {
        "x": 964,
        "y": 740
    },
    "all_work_btn_pos": {
        "x": 882,
        "y": 324
    },
    "close_btn_pos": {
        "x": 1015,
        "y": 277
    },
    
    "loop_time": 50
}
```
```
refresh_btn = พิกัด x,y ปุ่มรีเฟรชของเบราเซอร์

connect_btn_pos = พิกัดปุ่ม Connect metamask

sign_bnt_pos = พิกัดปุ่ม sign บน Metamask

start_game = พิกัดปุ่มเข้าเล่นโหมดล่าสมบัติ

get_bomber_pos = พิกัดปุ่มแสดงไอคอมบอมเบอร์ (ปุ่มโชว์เมนูตัวละคร)

all_work_btn_pos = พิกัดปุ่ม ALL ที่เปิดการทำงานตัวละคร

close_btn_pos = พิกัดปุ่มปิดเมนูตัวละคร

loop_time = หน่วงเวลาทำทุกๆ ... นาที
```

# หลังตั้งค่าเสร็จก็รันด้วย python v3.3+
```
python3 start_all.py
```

### Update ด้วยคำสั่ง
```
git pull origin main
```


เคยทดสอบแค่บน MacOS นะครับ แต่ใช้ Python บน Windows ก็ไม่น่าจะมีปัญหาอะไรครับผม

# Development
Contributions are what make the open source community such an amazing place to be learn, inspire, and create.
Any contributions you make to the `Python Auto click project` are greatly appreciated.

How to help?

- Fork the Project
- Create your feature branch
- Commit your changes
- Make sure everything works as intended
- Open a pull request


# ฝาก MQTT Broker ของผมด้วยครับ ทำให้ใช้กันเล่น ๆ

https://emmiedev.com

อย่ายิงนะครับ ไม่มี Firewall แถมรันบน Raspberry pi 4 เองครับ 5555 เห็นใจข้าน้อยด้วย
