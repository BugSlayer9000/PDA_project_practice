from pathlib import Path
import csv

class CSVFileHandling():
    csv_file_path = Path("files\\books.csv")
    csv_file_path.touch(exist_ok=True)
    
    
    def __init__(self) -> None:
        if len(self.get_list_of_dicts()) == 0:
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
    
    def save_file(self, data:list):
        with open(self.csv_file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title","author","genre","year","price"])
            writer.writerows(data)
    
    def get_list_of_dicts(self):
        with open(self.csv_file_path, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)
        

