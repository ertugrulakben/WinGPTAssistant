
# WinGPTAssistant

WinGPTAssistant is a GPT-4 powered assistant designed to boost productivity and prevent distractions in Windows. This assistant operates directly within the program you are using, without needing to open a browser or switch to another application. WinGPTAssistant provides seamless support across various programs including chat, email, text editing, WhatsApp, and more.

## Features
- Works across all applications (WhatsApp, email, text editors, etc.)
- Real-time weather and date information
- Google search and image search
- Play music on YouTube Music
- Clipboard integration for seamless operation

## Installation
### Prerequisites
1. **Python Installation**: Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
2. **Windows aText Installation**: Install Windows aText from the Microsoft Store. You can get it [here](https://apps.microsoft.com/detail/9n68hc1srr0k).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/username/WinGPTAssistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd WinGPTAssistant
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   Alternatively, you can install the packages manually:
   ```bash
   pip install openai pyperclip logging pyautogui requests webbrowser
   ```
4. Configure your API keys in gpt_request.py:
   ```python
   openai.api_key = "your-openai-api-key"
   weather_api_key = "your-weather-api-key"
   ```
5. Run the PowerShell script to initiate clipboard operations:
   ```powershell
   ./clipboard.ps1
   ```

## Usage
To create a new snippet and assign a shortcut (e.g., Shift+J), follow these steps:

1. Open aText and go to the "New Snippet" option.
2. Choose "PowerShell" as the script type.
3. Assign a shortcut (e.g., Shift+J).
4. Write something in a text editor and select it.
5. Press the assigned shortcut (e.g., Shift+J).
6. After a few seconds, the GPT-4 generated response will be pasted in place of the selected text.

# PowerShell Script (clipboard.ps1)
```powershell
# Copy selected text to clipboard
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("^c")
Start-Sleep -Milliseconds 300  # Increased wait time

# Get text from clipboard
$input_text = Get-Clipboard

# Run Python script and get the result
$output_text = & "C:/Users/$YOURNAME/AppData/Local/Programs/Python/Python312/python.exe" "C:/Users/$YOURNAME/WinGPTAssistant/gpt_request.py"

# Copying and pasting operations will be handled in the Python script
```

