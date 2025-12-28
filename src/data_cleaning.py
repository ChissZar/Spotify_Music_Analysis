import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import logging

class DataProcessor:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        """Làm sạch dữ liệu: xóa cột thừa, xóa trùng, xử lý null"""
        if self.df is None:
            return None
            
        initial_rows = len(self.df)
        
        # 1. Xóa cột index thừa nếu có
        if "Unnamed: 0" in self.df.columns:
            self.df = self.df.drop(columns=["Unnamed: 0"])

        # 2. Xóa dữ liệu trùng lặp theo track_id
        self.df = self.df.drop_duplicates(subset=["track_id"])

        # 3. Xử lý giá trị thiếu (dropna cho các cột text quan trọng)
        text_cols = ["artists", "album_name", "track_name", "track_genre"]
        self.df = self.df.dropna(subset=text_cols)

        # 4. Chuẩn hóa text
        for col in text_cols:
            self.df[col] = self.df[col].str.strip().str.lower()

        # 5. Filter dữ liệu hợp lệ
        self.df = self.df[
            (self.df["popularity"].between(0, 100)) &
            (self.df["duration_ms"] > 0) &
            (self.df["danceability"].between(0, 1)) &
            (self.df["energy"].between(0, 1))
        ]
        
        logging.info(f"✅ Đã làm sạch dữ liệu. Giữ lại {len(self.df)}/{initial_rows} dòng.")
        return self.df

    def normalize_audio_features(self):
        """Chuẩn hóa Min-Max cho các đặc trưng âm thanh"""
        audio_cols = [
            "danceability", "energy", "loudness", "speechiness",
            "acousticness", "instrumentalness", "liveness", 
            "valence", "tempo"
        ]
        
        # Kiểm tra xem các cột có tồn tại không trước khi normalize
        valid_cols = [col for col in audio_cols if col in self.df.columns]
        
        if valid_cols:
            scaler = MinMaxScaler()
            self.df[valid_cols] = scaler.fit_transform(self.df[valid_cols])
            logging.info("✅ Đã chuẩn hóa (Normalize) các chỉ số âm thanh.")
        
        return self.df