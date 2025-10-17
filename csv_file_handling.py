from pathlib import Path
import csv

class CSVFileHandling():
    # Class-level attribute: Windows-style path (use forward slash for cross-platform)
    csv_file_path = Path("files\\books.csv")
    csv_file_path.touch(exist_ok=True)
    
    
    def __init__(self) -> None:
        # Initialize headers only if file is empty (prevents overwriting data)
        if len(self.get_list_of_dicts()) == 0:
            self._initialize_file()
    
    def _initialize_file(self):
        # newline="" prevents extra blank rows in CSV on Windows
        with open(self.csv_file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title","author","genre","year","price"])
    
    def load_file(self):
        with open(self.csv_file_path, "r") as f:
            reader = csv.reader(f)
            # Skip header row before converting to list
            next(reader)
            return list(reader)
    
    def save_file(self, data:list):
        # Always rewrite entire file including headers
        with open(self.csv_file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title","author","genre","year","price"])
            writer.writerows(data)
    
    def get_list_of_dicts(self):
        # DictReader automatically maps CSV columns to dictionary keys
        with open(self.csv_file_path, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)