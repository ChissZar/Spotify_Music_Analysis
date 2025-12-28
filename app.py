import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import DataLoader
from src.data_cleaning import DataProcessor

# 1. Cấu hình trang Web
st.set_page_config(page_title="Spotify Music Analysis", layout="wide", page_icon="🎵")

# Tiêu đề chính
st.markdown("<h1 style='text-align: center; color: #1DB954;'>🎵 PHÂN TÍCH DỮ LIỆU NHẠC SPOTIFY 🎵</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Báo cáo Bài tập lớn Lập trình Python (IPPA233277)</h4>", unsafe_allow_html=True)

st.write("---")

col_info1, col_info2 = st.columns([1, 1])

with col_info1:
    st.info("🎓 **THÔNG TIN ĐỒ ÁN**") # Khung màu xanh dương
    st.markdown("""
    * **Môn học:** Lập trình Python
    * **Mã lớp:** IPPA233277_25_1_05
    * **Giảng viên hướng dẫn:** TS. Phan Thị Thể
    * **Đề tài:** Phân tích và trực quan hóa dữ liệu bài hát trên Spotify
    """)

with col_info2:
    st.success("👥 **THÀNH VIÊN NHÓM**") # Khung màu xanh lá
    st.markdown("""
    1.  **Nguyễn Phước Minh Triết** (Nhóm trưởng) 🌟
    2.  **Dương Thành Đạt**
    3.  **Võ Văn Thịnh**
    4.  **Nguyễn Ngọc Thịnh**
    5.  **Bùi Đức Huy**
    """)

st.write("---")

# 2. Sidebar (Menu bên trái)
st.sidebar.header("Tùy chọn dữ liệu")
uploaded_file = st.sidebar.file_uploader("Tải lên file CSV của bạn", type=["csv"])

if uploaded_file is not None:
    file_path = uploaded_file
else:
    file_path = "data/dataset.csv"
    st.sidebar.info("Đang sử dụng dữ liệu mẫu (dataset.csv)")

# 3. Load và Xử lý dữ liệu
@st.cache_data
def load_and_process_data(path):
    try:
        if isinstance(path, str):
            loader = DataLoader(path)
            df = loader.load_csv()
        else:
            df = pd.read_csv(path)
            
        if df is not None:
            processor = DataProcessor(df)
            df = processor.clean_data()
            df = processor.normalize_audio_features()
            return df
        return None
    except Exception as e:
        st.error(f"Lỗi khi xử lý dữ liệu: {e}")
        return None

df = load_and_process_data(file_path)

if df is not None:
    # 4. Hiển thị dữ liệu
    with st.expander("Xem dữ liệu gốc (Click để mở rộng)"):
        st.dataframe(df.head(10))
    
    st.write("---")

    # 5. Bộ lọc (Filter)
    st.subheader("🔍 Khám phá theo Thể loại")
    all_genres = df['track_genre'].unique()
    # Mặc định chọn 3 thể loại đầu tiên để biểu đồ không bị trống
    selected_genres = st.multiselect("Chọn thể loại nhạc:", all_genres, default=all_genres[:5])
    
    if not selected_genres:
        st.warning("Vui lòng chọn ít nhất một thể loại nhạc.")
        filtered_df = df # Nếu không chọn gì thì hiển thị hết (hoặc xử lý tùy ý)
    else:
        filtered_df = df[df['track_genre'].isin(selected_genres)]
        st.success(f"Đang hiển thị {len(filtered_df)} bài hát.")

    # 6. TRỰC QUAN HÓA 
    st.subheader("📈 Biểu đồ Phân tích")

    # Tạo 3 Tab chính
    tab1, tab2, tab3 = st.tabs(["📊 Tổng quan & Xu hướng", "🎵 Đặc tính Âm thanh", "🎻 Phân tích Chuyên sâu"])

    with tab1:
        st.write("### Xu hướng Thể loại & Độ phổ biến")
        # Chia 2 cột nhưng hình sẽ to hơn vì tab rộng
        t1_col1, t1_col2 = st.columns(2)
        
        with t1_col1:
            st.markdown("**1. Top Thể loại phổ biến**")
            fig1, ax1 = plt.subplots(figsize=(10, 6)) # Tăng kích thước hình
            top_genres = filtered_df['track_genre'].value_counts().head(10)
            sns.barplot(x=top_genres.index, y=top_genres.values, palette="viridis", ax=ax1)
            ax1.set_xlabel("Thể loại")
            ax1.set_ylabel("Số lượng")
            plt.xticks(rotation=45)
            st.pyplot(fig1)
            
        with t1_col2:
            st.markdown("**2. Phân bố Độ phổ biến**")
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            sns.histplot(filtered_df['popularity'], bins=20, kde=True, color="green", ax=ax2)
            ax2.set_xlabel("Độ phổ biến (0-100)")
            st.pyplot(fig2)

    with tab2:
        st.write("### Mối quan hệ giữa các đặc tính âm nhạc")
        t2_col1, t2_col2 = st.columns(2)
        
        with t2_col1:
            st.markdown("**3. Energy (Năng lượng) vs Danceability (Độ 'quẩy')**")
            fig3, ax3 = plt.subplots(figsize=(10, 6))
            sns.scatterplot(data=filtered_df, x='energy', y='danceability', hue='track_genre', alpha=0.6, ax=ax3)
            st.pyplot(fig3)
            
        with t2_col2:
            st.markdown("**4. Acousticness (Độ mộc) vs Energy**")
            fig4, ax4 = plt.subplots(figsize=(10, 6))
            sns.scatterplot(data=filtered_df, x='acousticness', y='energy', color="orange", alpha=0.5, ax=ax4)
            st.pyplot(fig4)

    with tab3:
        st.write("### Phân tích thống kê chi tiết")
        # Phần này để 1 cột cho hình thật to, dễ soi
        st.markdown("**5. Thời lượng bài hát theo thể loại**")
        fig5, ax5 = plt.subplots(figsize=(12, 6))
        top_plot_genres = filtered_df['track_genre'].value_counts().head(10).index # Lấy top 10 vẽ cho đẹp
        plot_df = filtered_df[filtered_df['track_genre'].isin(top_plot_genres)]
        sns.boxplot(data=plot_df, x="track_genre", y="duration_ms", palette="Set2", ax=ax5)
        plt.xticks(rotation=45)
        st.pyplot(fig5)

        st.markdown("**6. Ma trận tương quan (Heatmap)**")
        fig6, ax6 = plt.subplots(figsize=(10, 8))
        numeric_df = filtered_df.select_dtypes(include=['float64', 'int64'])
        sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax6) # annot=True để hiện số
        st.pyplot(fig6)

else:
    st.warning("Chưa có dữ liệu. Vui lòng kiểm tra file dataset.csv")