import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os

class DataVisualizer:
    def __init__(self, df, output_dir="output"):
        self.df = df
        self.output_dir = output_dir
        
        # Tạo thư mục output nếu chưa có
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def save_plot(self, filename):
        """Hàm phụ trợ để lưu biểu đồ ra file ảnh"""
        path = os.path.join(self.output_dir, filename)
        plt.savefig(path)
        logging.info(f"💾 Đã lưu biểu đồ: {path}")
        plt.show() # Hiển thị lên màn hình
        plt.close() # Đóng để giải phóng bộ nhớ

    def plot_top_genres(self):
        plt.figure(figsize=(10, 6))
        top_genres = self.df["track_genre"].value_counts().head(10)
        sns.barplot(x=top_genres.index, y=top_genres.values, palette="viridis")
        plt.title("Top 10 Thể loại nhạc phổ biến nhất")
        plt.xlabel("Thể loại")
        plt.ylabel("Số lượng bài hát")
        plt.xticks(rotation=45)
        plt.tight_layout()
        self.save_plot("top_genres.png")

    def plot_correlation_matrix(self):
        """Vẽ Heatmap tương quan (Tính năng mới)"""
        plt.figure(figsize=(10, 8))
        # Chỉ lấy các cột số để tính tương quan
        numeric_df = self.df.select_dtypes(include=['float64', 'int64'])
        corr = numeric_df.corr()
        
        sns.heatmap(corr, annot=False, cmap='coolwarm', linewidths=0.5)
        plt.title("Biểu đồ nhiệt tương quan giữa các đặc trưng (Heatmap)")
        plt.tight_layout()
        self.save_plot("correlation_heatmap.png")

    def plot_energy_danceability(self):
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=self.df, x="energy", y="danceability", alpha=0.1, color="purple")
        plt.title("Mối quan hệ: Energy vs Danceability")
        self.save_plot("energy_danceability.png")
    
    def plot_popularity_distribution(self):
        """Vẽ biểu đồ phân bố độ phổ biến (Histogram)"""
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["popularity"], bins=30, kde=True, color="green")
        plt.title("Phân bố độ phổ biến của bài hát")
        plt.xlabel("Độ phổ biến (0-100)")
        plt.ylabel("Số lượng")
        self.save_plot("popularity_distribution.png")

    def plot_acousticness_vs_energy(self):
        """Vẽ biểu đồ tán xạ: Nhạc Acoustic vs Năng lượng"""
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x="acousticness", y="energy", alpha=0.1, color="orange")
        plt.title("Tương quan: Độ mộc (Acousticness) vs Năng lượng (Energy)")
        # Nhạc càng mộc thì năng lượng thường càng thấp -> Biểu đồ sẽ dốc xuống
        self.save_plot("acoustic_energy_scatter.png")

    def plot_duration_boxplot(self):
        """Vẽ biểu đồ hộp về thời lượng bài hát theo thể loại"""
        plt.figure(figsize=(12, 8))
        # Lấy top 10 thể loại để vẽ cho đỡ rối
        top_genres_list = self.df["track_genre"].value_counts().head(10).index
        filtered_df = self.df[self.df["track_genre"].isin(top_genres_list)]
        
        sns.boxplot(data=filtered_df, x="track_genre", y="duration_ms", palette="Set2")
        plt.title("Phân bố thời lượng bài hát của Top 10 thể loại")
        plt.xticks(rotation=45)
        self.save_plot("duration_boxplot.png")