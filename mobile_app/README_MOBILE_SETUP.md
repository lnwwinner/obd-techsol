# 📱 Mobile App Setup Guide (Test #1)

## 🚀 Overview
Mobile App ใช้เป็น Interface เท่านั้น (ไม่ใช่ source of truth)

---

## 🧠 Requirements
- Android Studio
- Android Device หรือ Emulator
- Internet (เชื่อมต่อ server)

---

## 🔧 Setup Step-by-Step

### 1. เปิดโปรเจค
- เปิด Android Studio
- Import โฟลเดอร์ `mobile_app`

---

### 2. แก้ WebSocket URL
ในไฟล์:

```
WebSocketClient.kt
```

เปลี่ยน:

```
ws://10.0.2.2:8000/ws/TRUCK001
```

เป็น:

```
ws://<YOUR_IP>:8000/ws/TRUCK001?token=xxx&device_id=DEVICE001
```

---

### 3. Build & Run
- กด Run ▶️
- เลือก Device

---

### 4. ทดสอบ

#### ✅ ส่งข้อมูล
```
sendStatus(80, "RUNNING")
```

#### ✅ รับคำสั่ง
```
REDUCE_SPEED
FORCE_STOP
```

---

## 🚨 Test Case สำคัญ

### 1. Disconnect
→ ต้อง reconnect ได้

### 2. No Driver
→ server ต้อง alert

### 3. Fake Data
→ ต้องถูก reject

---

## 💬 หมายเหตุ
- Mobile = UI เท่านั้น
- Server จะเป็นตัวตัดสินทั้งหมด

---

🔥 Ready for TEST #1
