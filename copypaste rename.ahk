CapsLock::
toggle := !toggle
goto, % toggle ? "copy" : "paste"
return

copy:
send {F2}
sleep, 20
send ^c
return

paste:
send {F2}
sleep, 20
send ^v
return

F1::
toggle := false
return