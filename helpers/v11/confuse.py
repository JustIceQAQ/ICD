def anti_confuse(value: str) -> str:
    s = ""
    key_char_code = ord(value[13])
    offset = (key_char_code - 48) % 70 % 14

    for i in range(len(value)):
        if i == 13:
            continue
        current_char_code = ord(value[i]) - offset
        s += chr(current_char_code)
    return s
