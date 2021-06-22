import keyboard

print("key code(x10) code(x16)")

while True:
    key = keyboard.read_event()
    print(key.name, end=" \t")
    print(key.scan_code, end=" \t")
    print(hex(key.scan_code))
