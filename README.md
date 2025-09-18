# 📚 Anniesland Library - Book Management Application  

## 🔹 Project Brief  

### 📖 Project Overview  
Anniesland Library requires a **Book Management Application** to replace its current manual system.  
You will develop a **console-based Python program** that allows staff to manage their collection of books efficiently.  

The program must support:  
- Adding books  
- Searching books  
- Sorting books  
- Exporting book data using **CSV files**  

---

## ⚡ Core Functionality  

### ➕ Add Book  
Users can add a book by entering:  
- Title  
- Author  
- Genre  
- Year (published)  
- Price  

📌 Each book is stored as a new row in **`books.csv`**  

---

### 🔍 Search for a Book by Title  
- Input: Book title (case-insensitive)  
- Output: Display full details if found  

---

### 📑 Sort Books by Title  
- Reads all books from **`books.csv`**  
- Sorts alphabetically by title  
- Displays sorted list  

---

### ⏳ Find Oldest & Newest Book  
- Identifies the **oldest** and **most recently published** book (based on Year)  

---

### 📤 Export Features  
- **Export Book Titles** → `titles.csv`  
- **Export Publication Years** → `years.csv`  

---

### 🧾 Count Titles by Author  
- Input: Author name  
- Output: Number of books written by that author  

---

## 🗂️ Data Storage Requirements  
- **Programming Language:** Python  
- **Interface:** Menu-driven console app  
- **Primary Data File:** `books.csv`  
- **Export Files:** `titles.csv`, `years.csv`  
- **Row Format:**  

```csv
Title,Author,Genre,Year,Price
```

---

## 📋 Project Requirements  

### 1️⃣ Requirement Specification  
- **Overview:** Console-based Book Management System for Anniesland Library  

#### ✅ Functional Requirements  
- Add book records  
- Search books by title  
- Sort books alphabetically  
- Find oldest and newest book  
- Export titles and years  
- Count titles by author  

#### ⚙️ Non-Functional Requirements  
- Efficient search and sorting operations  
- Robust error handling for invalid input  
- Clear and user-friendly menu system  
- Data persistence using CSV files  

📌 **Project Plan Includes:**  
- Tasks, Subtasks, Timescales, and Milestones  

---

### 2️⃣ Design  

- **User Interface Design:**  
  - Menu-driven console (wireframe/storyboard)  

- **Data Dictionary:**  
  - Fields: Title, Author, Genre, Year, Price  
  - Data types & descriptions defined  

- **Structure Chart:**  
  - Break system into smaller modules (Add, Search, Sort, Export, Count)  

- **Pseudocode:**  
  - Step-by-step logic for all key features  

---

### 3️⃣ Implementation Guidelines  

- Use **meaningful variable names**  
- Add **internal comments** for readability  
- Ensure **input validation** with error messages  

#### Constructs to Apply:  
- Sequencing (logical flow)  
- Selection (`if`, `elif`, `else`)  
- Iteration (`for`, `while`)  
- Functions (with parameters & return values)  
- File Handling (`open()`, `read()`, `write()`)  

---

## 🎯 Final Deliverables  
- Fully working **Python console application**  
- **CSV data files** (`books.csv`, `titles.csv`, `years.csv`)  
- Requirement Specification  
- Design Documentation (UI, Data Dictionary, Structure Chart, Pseudocode)  
- Implementation Code (with comments & validation)  

---
