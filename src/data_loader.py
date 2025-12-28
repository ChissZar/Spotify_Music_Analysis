import pandas as pd
import logging

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        """Đọc file CSV và trả về DataFrame"""
        try:
            df = pd.read_csv(self.file_path)
            logging.info(f"✅ Đã tải dữ liệu thành công: {self.file_path} ({df.shape[0]} dòng)")
            return df
        except FileNotFoundError:
            logging.error(f"❌ Lỗi: Không tìm thấy file tại đường dẫn: {self.file_path}")
            return None
        except Exception as e:
            logging.error(f"❌ Lỗi không xác định khi đọc file: {e}")
            return None