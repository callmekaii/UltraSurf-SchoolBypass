# UltraSurf-SchoolBypass

## About
This program is a tool designed to download and extract a specific Chrome extension. It is intended for educational purposes only, to explore how browser extensions function and how they might interact with network environments. It is **not** an automated installer but prepares the necessary files for manual installation of the extension in Chrome.

## Features

- Downloads a `.crx` file containing a Chrome extension.
- Extracts the contents of the `.crx` file into a designated folder.
- Includes a self-deletion mechanism to clean up the downloaded files and the extraction folder after the program exits.

## 🛠️ Installation and Usage

### Steps
1.  Download the compiled executable (`.exe`) and the accompanying batch file (`.bat`) from the `dist` folder provided. Ensure both files are in the same directory.
2.  Run the executable file (e.g., by double-clicking `UltrasurfDownloader.exe`).
3.  The program will download and extract the extension files into a new folder named `mjnbclmflcpookeapghfhapeffmpodij` in the same directory.
4.  Once the extraction is complete, open Google Chrome and navigate to `chrome://extensions/`.
5.  In the top right corner of the Chrome Extensions page, enable "Developer mode" by toggling the switch.
6.  Click on the "Load unpacked" button that appears.
7.  Navigate to the directory where you ran the executable and select the folder named `mjnbclmflcpookeapghfhapeffmpodij`.
8.  Click "Select Folder". The extension should now be loaded and active in your Chrome browser.
9.  **DON'T EXIT THE PROGRAM** when still using the extension as it self destructs and leave no traces of evidence for the school to find out lol. Only exit the program when done using the browser.

The program is designed to clean up the downloaded `.crx` file and the extracted folder (`mjnbclmflcpookeapghfhapeffmpodij`) automatically upon exit using the accompanying batch file.

**Disclaimer:** This program is provided for educational exploration. Using extensions to bypass network restrictions may violate the acceptable use policies of your school or network administrator. Use this program responsibly and at your own discretion.

## Language and Libraries Used
- **Python** (The original source language, compiled into an executable)
- **wget** - Used internally for downloading files.
- **zipfile** - Used internally for extracting zip archives.
- **os, subprocess, atexit, shutil** - Used internally for file system operations, running external processes, script cleanup, and directory management.
