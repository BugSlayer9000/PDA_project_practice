from pathlib import Path
import csv

class CSVFileHandling():
    csv_file_path = Path("files\\books.csv")
    csv_file_path.touch(exist_ok=True)
    
    
    def __init__(self) -> None:
        self._initialize_file()
    
    def _initialize_file(self):
        with open(self.csv_file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title","author","genre","year","price"])
    
    def load_file(self):
        with open(self.csv_file_path, "r") as f:
            reader = csv.reader(f)
            next(reader)
            return list(reader)
    
    