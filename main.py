# main.py
import logging
from src.data_loader import DataLoader
from src.data_cleaning import DataProcessor 
from src.data_visualization import DataVisualizer

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MusicAnalysisApp:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def run(self):
        logging.info("🎵 BẮT ĐẦU CHƯƠNG TRÌNH PHÂN TÍCH NHẠC 🎵")
        
        # 1. Load
        loader = DataLoader(self.data_path) 
        self.df = loader.load_csv()
        
        if self.df is None:
            logging.error("Dừng chương trình do không tải được dữ liệu.")
            return

        # 2. Clean & Normalize
        processor = DataProcessor(self.df) 
        self.df = processor.clean_data()
        self.df = processor.normalize_audio_features()
        
        logging.info(f"Dữ liệu sau khi xử lý: {self.df.shape}")

        # 3. Visualize
        visualizer = DataVisualizer(self.df)
        
        logging.info("Đang vẽ biểu đồ...")
        
        # --- VẼ CÁC BIỂU ĐỒ ---
        visualizer.plot_top_genres()
        visualizer.plot_correlation_matrix()
        visualizer.plot_energy_danceability()
        visualizer.plot_popularity_distribution()
        visualizer.plot_acousticness_vs_energy()
        visualizer.plot_duration_boxplot()
        
        logging.info("✅ Chương trình hoàn tất! Kiểm tra thư mục 'output' để xem đủ 6 ảnh.")

if __name__ == "__main__":

    app = MusicAnalysisApp("data/dataset.csv")
    app.run()