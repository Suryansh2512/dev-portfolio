# 🗂️ File Manager (Python)

A simple yet functional **File Manager** built with Python.  
It provides a graphical interface to manage your files and folders with ease — open, copy, move, rename, and delete, all in one place.  

---

## ✨ Features
- 📂 Browse and open files/folders  
- ✏️ Rename files or directories  
- 📋 Copy & Move files/folders to a new location  
- 🗑️ Delete files/folders (with confirmation prompt)  
- 🔍 View and navigate the current working directory  
- ⚡ Works on Windows, macOS, and Linux  

---

## 📦 Project Structure
file-manager/
│── file_manager.py # Main script with GUI + file operations
│── utils.py # Helper functions (if used)
│── requirements.txt # Dependencies (if any)
│── README.md # Documentation


---

## 🚀 Installation & Setup

### 1. Clone this repository
```bash
git clone https://github.com/Suryansh2512/dev-portfolio.git
cd dev-portfolio/python-projects/file-manager
```
### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the project
```bash
python file_manager.py
```

## 📸SCREENSHOT
<img width="1360" height="592" alt="image" src="https://github.com/user-attachments/assets/6b87e4b1-19e5-4ecc-a9e7-a7672b5b36e3" />

## ⚠️ Notes

Deleting is permanent — there’s no recycle bin.

Some operations (like modifying system files) may require administrator/root permissions.

Tested on Python 3.9+ (should work fine on 3.7+).

## 🛠️ Roadmap / Future Improvements

⬜ Multi-file selection

⬜ Drag & Drop support

⬜ Progress bar for large copy/move operations

⬜ File search & sorting

⬜ Improved GUI (dark mode, theming)

## 📜 License

Distributed under the MIT License.

