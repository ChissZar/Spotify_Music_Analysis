# 🎵 PHÂN TÍCH VÀ TRỰC QUAN HÓA DỮ LIỆU NHẠC SPOTIFY
> **Báo cáo Bài tập lớn môn Lập trình Python**
> **Mã lớp:** IPPA233277_25_1_05

![Spotify Banner](https://images.unsplash.com/photo-1614680376593-902f74cf0d41?q=80&w=1000&auto=format&fit=crop) 
*(Hình ảnh minh họa)*

## 👥 Thành Viên Nhóm
| STT | Họ và Tên | Vai trò | MSSV |
|:---:|:---|:---:|:---:|
| 1 | **Nguyễn Phước Minh Triết** | Nhóm trưởng (Leader) | 24110357 |
| 2 | **Dương Thành Đạt** | Thành viên | 24110191 |
| 3 | **Võ Văn Thịnh** | Thành viên | 24110341 |
| 4 | **Nguyễn Ngọc Thịnh** | Thành viên | 24110338 |
| 5 | **Bùi Đức Huy** | Thành viên | 24133021 |

---

## 📖 Giới Thiệu Đề Tài
Dự án này tập trung vào việc phân tích tập dữ liệu các bài hát trên Spotify để tìm ra các xu hướng âm nhạc hiện nay. Chúng tôi sử dụng **Python** để làm sạch, xử lý và trực quan hóa dữ liệu, giúp trả lời các câu hỏi như:
* Thể loại nhạc nào đang phổ biến nhất?
* Các yếu tố âm thanh (Energy, Danceability, Acousticness...) tương quan với nhau như thế nào?
* Độ dài bài hát ảnh hưởng ra sao đến mức độ yêu thích?

Dự án bao gồm cả **Script phân tích tự động** và **Website Dashboard tương tác** (Interactive Web App).

---

## 🛠️ Công Nghệ Sử Dụng
Dự án được xây dựng dựa trên các thư viện Python mạnh mẽ:
* **Ngôn ngữ:** Python 3.8+
* **Xử lý dữ liệu:** `Pandas`, `Numpy`
* **Trực quan hóa:** `Matplotlib`, `Seaborn`
* **Giao diện Web:** `Streamlit`
* **Machine Learning (Preprocessing):** `Scikit-learn` (MinMaxScaler)

---

## 📂 Cấu Trúc Dự Án
Mã nguồn được tổ chức theo mô hình OOP (Hướng đối tượng) và chia Module rõ ràng:

```text
Spotify_Music_Analysis/
│
├── data/
│   └── dataset.csv          # Tập dữ liệu gốc (CSV)
│
├── src/                     # Source Code xử lý chính
│   ├── __init__.py
│   ├── data_loader.py       # Module đọc và kiểm tra dữ liệu
│   ├── data_cleaning.py     # Module làm sạch & chuẩn hóa dữ liệu
│   └── data_visualization.py # Module vẽ biểu đồ
│
├── output/                  # Chứa các biểu đồ xuất ra (.png)
├── app.py                   # Giao diện Web (Streamlit App)
├── main.py                  # Script chạy phân tích tĩnh
└── README.md                # Tài liệu hướng dẫn
```

---

## ⚙️ Hướng Dẫn Cài Đặt
Bước 1: Clone dự án về máy

```bash
git clone https://github.com/ChissZar/Spotify_Music_Analysis.git
cd Spotify_Music_Analysis
```

Bước 2: Cài đặt các thư viện
Chạy lệnh sau trong Terminal (CMD/VSCode) để cài đặt tất cả các thư viện cần thiết:

```bash
pip install pandas matplotlib seaborn scikit-learn streamlit
```

---

## 🚀 Hướng Dẫn Sử Dụng
Cách 1: Chạy Web Dashboard (Khuyên dùng)
Đây là giao diện tương tác chính của đồ án.

```bash
python -m streamlit run app.py
```

👉 Trình duyệt sẽ tự động mở tại địa chỉ: http://localhost:8501

Cách 2: Chạy Script phân tích tĩnh
Script này sẽ xử lý dữ liệu và xuất các biểu đồ vào thư mục output.

```bash
python main.py
```

---

## 📊 Các Chức Năng Chính

1. Xử lý Dữ liệu (Data Processing)
- Cleaning: Loại bỏ các dòng trùng lặp (duplicates), xử lý giá trị thiếu (missing values) ở các cột quan trọng.

- Normalization: Sử dụng MinMaxScaler để chuẩn hóa các chỉ số âm thanh (Loudness, Tempo...) về thang đo [0, 1] để dễ so sánh.


2. Trực quan hóa (Visualization)
Chương trình cung cấp 6 loại biểu đồ phân tích sâu:

- Top Genres: Biểu đồ cột thể hiện các thể loại nhạc phổ biến nhất.

- Correlation Matrix (Heatmap): Ma trận tương quan giữa các đặc trưng (VD: Energy cao thường đi kèm với Loudness cao).

- Distribution: Phân bố độ phổ biến (Popularity) của toàn bộ kho nhạc.

- Scatter Plots: Phân tích mối quan hệ giữa Energy vs Danceability, Acousticness vs Energy.

- Boxplot: So sánh thời lượng bài hát (Duration) giữa các thể loại nhạc.

---

## 📞 Liên Hệ

Nếu có bất kỳ câu hỏi nào về source code, vui lòng liên hệ:

Email: nguyenphuocminhtriet6410@gmail.com

Github: https://github.com/ChissZar


Cảm ơn Thầy Cô và các bạn đã quan tâm đến dự án! ❤️
