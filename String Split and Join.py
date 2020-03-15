def swap_case(s):
    input_list = list(s)
    return "".join(i.lower() if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" else i.upper() for i in input_list)
