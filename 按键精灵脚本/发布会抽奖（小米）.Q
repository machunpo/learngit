[General]
SyntaxVersion=2
BeginHotkey=121
BeginHotkeyMod=0
PauseHotkey=0
PauseHotkeyMod=0
StopHotkey=123
StopHotkeyMod=0
RunOnce=1
EnableWindow=
MacroID=0334db77-a03f-4dd1-9465-8f55b00ea28c
Description=发布会抽奖
Enable=1
AutoRun=0
[Repeat]
Type=0
Number=1
[SetupUI]
Type=2
QUI=
[Relative]
SetupOCXFile=
[Comment]

[Script]
Dim strarry

Dim  n

n = 0

strarry = Array("新产品，超级六","威武","简直是完美的产品","大家好","开始了，精彩来了","真的很不错","完美")


Randomize





SayString strarry(n)

Delay 4000

KeyPress "Enter", 1


Delay 5000


Delay n*1000
