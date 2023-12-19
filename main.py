import os
import tkinter as tk
from tkinter import filedialog
from Yara.MalwareSig import *

RULE_FILE_LOC = 'Yara/rules'

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_var.set(folder_path)

def scan_folder():
    folder_to_scan = folder_var.get()
    if folder_to_scan:
        yara_scanner = YaraScanner(RULE_FILE_LOC, folder_to_scan)
        yara_rule_dict = yara_scanner.make_dict()
        hit_files = set(yara_scanner.scan_files(yara_rule_dict))
        scanned_files = []
        for _, _, files in os.walk(folder_to_scan):
            scanned_files += files
        scanned_files = set(scanned_files)
        safe_files = scanned_files - hit_files
        
        with open('report.txt', 'w') as report_file:
            report_file.write('List of files that are safe:\n\n')
            for file in safe_files:
                report_file.write(file + '\n')
            report_file.write('\n' + '-' * 20 + '\n\n')
            report_file.write('List of files that are not safe:\n\n')
            for file in hit_files:
                report_file.write(file + '\n')

root = tk.Tk()
root.title("Folder Selection")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

folder_var = tk.StringVar()

selected_folder_label = tk.Label(frame, text="Selected Folder:")
selected_folder_label.grid(row=0, column=0, sticky="w")

folder_entry = tk.Entry(frame, textvariable=folder_var, state='readonly', width=40)
folder_entry.grid(row=0, column=1, padx=10)

select_button = tk.Button(frame, text="Select Folder", command=select_folder)
select_button.grid(row=0, column=2, padx=10)

scan_button = tk.Button(frame, text="Scan", command=scan_folder)
scan_button.grid(row=1, columnspan=3, pady=10)

root.mainloop()
