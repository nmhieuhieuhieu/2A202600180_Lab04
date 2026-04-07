# 🛫 TravelBuddy - AI Travel Agent (Lab 4)

Dự án này là một phần của chương trình **AI Thực chiến tại VinUni**. Mục tiêu của Lab 4 là xây dựng một **AI Agent** tự động hóa quy trình lập kế hoạch du lịch bằng cách sử dụng **LangGraph** và **OpenAI Function Calling**.

## 🚀 Tổng quan về dự án
TravelBuddy là một trợ lý ảo du lịch có khả năng tư vấn, tìm kiếm thông tin chuyến bay/khách sạn và tính toán ngân sách cá nhân hóa dựa trên yêu cầu của người dùng. Agent có khả năng tự suy luận và chuỗi hóa các công cụ (Tool Chaining) để đưa ra câu trả lời toàn diện thay vì phản hồi rời rạc.

## 🛠️ Kiến trúc hệ thống
- **Framework:** LangGraph (StateGraph).
- **LLM:** `gpt-4o-mini` từ OpenAI.
- **Tools:** 
  - `search_flights`: Tìm kiếm thông tin chuyến bay.
  - `search_hotels`: Tra cứu khách sạn, lọc và sắp xếp theo đánh giá.
  - `calculate_budget`: Xử lý tính toán ngân sách và cảnh báo vượt ngưỡng.

## 📁 Cấu trúc thư mục
```text
LAB04_2A202600180/
├── assets/
│   └── test_results/    # Kết quả 5 test cases
├── .env.example         # Template biến môi trường
├── .gitignore           # Cấu hình bỏ qua các file nhạy cảm/rác
├── README.md            # Tài liệu dự án
├── requirements.txt     # Danh sách các thư viện cần thiết
├── core/
│   ├── agent.py         # Logic chính của Agent (State & Graph)
│   └── tools.py         # Định nghĩa các Custom Tools
├── config/
│   └── system_prompt.txt # Prompt định nghĩa Persona của Agent
└── tests/
    └── test_api.py      # Script kiểm tra kết nối OpenAI API

```




## ⚙️ Cài đặt & Chạy dự án
Khởi tạo môi trường ảo:

``` bash
python -m venv venv
```

Windows:

``` bash
venv\Scripts\activate
```

Mac/Linux:

``` bash
source venv/bin/activate
```

Cài đặt các thư viện cần thiết:

``` bash
pip install -r requirements.txt
```

Cấu hình API: - Tạo file `.env` từ `.env.example`. - Điền OpenAI API Key
vào:

``` env
OPENAI_API_KEY=sk-...
```

Khởi chạy Agent:

``` bash
python core/agent.py
```

## 📚 Tài liệu tham khảo

Dự án được phát triển dựa trên các kiến thức về cách thức hoạt động của
LLM trong việc gọi công cụ và điều phối logic:

-  Function Calling: \[[link](https://viblo.asia/p/huong-dan-chi-tiet-tu-dong-hoa-tac-vu-bang-function-calling-oKLnqq7gJQO)\]
-   LangGraph Documentation: \[[link](https://docs.langchain.com/oss/python/langgraph/overview)\]

Dự án thực hiện cho chương trình AI Thực chiến - VinUni.