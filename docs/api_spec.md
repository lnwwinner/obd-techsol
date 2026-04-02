# 🔌 API Specification

## POST /data
รับข้อมูลจาก OBD Device

### Request
```json
{
  "vehicle_id": "TRUCK001",
  "lat": 13.75,
  "lon": 100.50,
  "speed": 80,
  "fuel": 50
}
```

### Response
```json
{
  "status": "saved",
  "alerts": []
}
```

---

## GET /health (future)
ตรวจสอบสถานะระบบ

---

## GET /vehicle/{id}/history (future)
ดูข้อมูลย้อนหลัง
