# Copy selected text to clipboard
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("^c")
Start-Sleep -Milliseconds 300  # Increased wait time

# Get text from clipboard
$input_text = Get-Clipboard

# Run Python script and get the result
$output_text = & "C:/Users/$YOURNAME/AppData/Local/Programs/Python/Python312/python.exe" "C:/Users/$YOURNAME/WinGPTAssistant/gpt_request.py"

# Copying and pasting operations will be handled in the Python script
