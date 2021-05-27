# to run powershell-scripts with a doubleclick -> create shortcut with:
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -command "& 'C:\path\to\prog.ps1'

#do a thing, minimize all windows, wait, do something else 
& "C:\path\to\file.exe"
echo "i did a thing"

Start-Sleep -Seconds 5

# minimize all windows
$shell = New-Object -ComObject "Shell.Application"
$shell.minimizeall()


& "C:\path\to\something\else.exe"
