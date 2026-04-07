# Kết quả kiểm thử TravelBuddy (Test Cases)

## Test Case 1: Chào hỏi người dùng
**Input:** "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."

**Log:**
[LOG] 💬 AI đang trả lời trực tiếp...

**Output:**
TravelBuddy: Chào bạn! Thật tuyệt khi bạn đang có kế hoạch đi du lịch. Nếu bạn cần gợi ý về điểm đến, mình có thể giúp bạn tìm kiếm những địa điểm thú vị ở Việt Nam. Bạn có thể cho mình biết ngân sách của bạn và mình sẽ gợi ý cho bạn những nơi phù hợp nhé!

---

## Test Case 2: Tìm kiếm chuyến bay
**Input:** "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"

**Log:**
[LOG] 🌸AI đang gọi công cụ: search_flights với đầu vào: {'origin': 'Hà Nội', 'destination': 'Đà Nẵng'}
[LOG] 💬 AI đang trả lời trực tiếp...

**Output:**
TravelBuddy: 
✈️ **Chuyến bay đề xuất:**
- Hãng bay: Vietnam Airlines
  - Giờ bay: 06:00 - Giờ đến: 07:20
  - Giá vé: 1.450.000 VNĐ/người
- Hãng bay: VietJet Air
  - Giờ bay: 08:30 - Giờ đến: 09:50
  - Giá vé: 890.000 VNĐ/người
- Hãng bay: Bamboo Airways
  - Giờ bay: 11:00 - Giờ đến: 12:20
  - Giá vé: 1.200.000 VNĐ/người
- Hãng bay: Vietnam Airlines
  - Giờ bay: 14:00 - Giờ đến: 15:20
  - Giá vé: 2.800.000 VNĐ/người
Bạn có muốn tìm khách sạn ở Đà Nẵng không? Nếu có, hãy cho tôi biết ngân sách của bạn nhé!

---

## Test Case 3: Kế hoạch du lịch trọn gói
**Input:** "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu"

**Log:**

[LOG] 🌸AI đang gọi công cụ: search_flights với đầu vào: {'origin': 'Hà Nội', 'destination': 'Phú Quốc'}

[LOG] 🌸AI đang gọi công cụ: search_hotels với đầu vào: {'city': 'Phú Quốc', 'max_price_per_night': 
2500000}

[LOG] 🌸AI đang gọi công cụ: calculate_budget với đầu vào: {'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn:1600000'}

[LOG] 💬 AI đang trả lời trực tiếp...

**Output:**
TravelBuddy: 
✈️ **Chuyến bay đề xuất:**
- Hãng bay: VietJet Air
  - Giờ bay: 16:00 - Giờ đến: 18:15
  - Giá vé: 1.100.000 VNĐ/người
🏨 **Khách sạn đề xuất:**
- Tên: Lahana Resort (3⭐)
  - Giá phòng: 800.000 VNĐ/đêm
💰 **Tổng quan tài chính:**
- Tổng chi phí ước tính: 2.700.000 VNĐ
- Ngân sách của bạn: 5.000.000 VNĐ
- Tình trạng: [Vừa ngân sách]
Gợi ý thêm: Khi đến Phú Quốc, bạn nên thử món hải sản tươi ngon và tham gia các hoạt động như lặn biển ngắm san hô. Thời tiết ở Phú Quốc thường rất đẹp, hãy chuẩn bị kem chống nắng nhé!

---

## Test Case 4: Yêu cầu đặt khách sạn (thiếu thông tin)
**Input:** "Tôi muốn đặt khách sạn"
**Log:**
[LOG] 💬 AI đang trả lời trực tiếp...

**Output:**
TravelBuddy: Mình cần biết bạn sẽ đi từ đâu đến đâu và ngân sách của bạn là bao nhiêu để có thể giúp bạn tìm khách sạn phù hợp nhé!

---

## Test Case 5: Từ chối yêu cầu ngoài phạm vi (Lập trình)
**Input:** "Giải giúp tôi bài tập lập trình Python về linked list"

**Log:**
[LOG] 💬 AI đang trả lời trực tiếp...

**Output:**
TravelBuddy: Xin lỗi, nhưng mình không thể giúp bạn với bài tập lập trình. Tuy nhiên, nếu bạn có kế hoạch du lịch hoặc cần tư vấn về chuyến đi, mình rất sẵn lòng hỗ trợ! Bạn có điểm đi, điểm đến và ngân sách không?