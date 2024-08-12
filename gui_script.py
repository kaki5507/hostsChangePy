import tkinter as tk
from tkinter import messagebox
import os

# hosts 파일 경로
HOSTS_FILE_PATH = r'C:\Windows\System32\drivers\etc\hosts'  # Windows의 경우

def update_hosts_file(line_numbers):
    try:
        # hosts 파일을 UTF-8 인코딩으로 읽기
        with open(HOSTS_FILE_PATH, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line_num in line_numbers:
            index = line_num - 1
            if lines[index].strip().startswith("#"):
                lines[index] = lines[index].replace("#", "", 1).lstrip()
        
        # hosts 파일을 UTF-8 인코딩으로 쓰기
        with open(HOSTS_FILE_PATH, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        
        messagebox.showinfo("Success", "Selected lines updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def run_task_A():
    update_hosts_file([67, 68])

def run_task_B():
    update_hosts_file([69])

# GUI 생성
def create_gui():
    root = tk.Tk()
    root.title("Hosts File Modifier")

    tk.Label(root, text="Choose an action:").pack(pady=10)

    tk.Button(root, text="Run Task A (Lines 67, 68)", command=run_task_A).pack(pady=5)
    tk.Button(root, text="Run Task B (Line 69)", command=run_task_B).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
