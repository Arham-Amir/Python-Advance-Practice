def get_string_input(msg = "Enter String : "):
    string_input = input(msg).strip()
    while not string_input or not string_input.isalnum:
        string_input = input(f"invalid input ! {msg}").strip()
    return string_input