def read_txt_as_int(path):
    with open(path, 'r') as f:
        return [int(num.split('\n')[0]) for num in f.readlines()]

def read_txt_as_str(path):
    with open(path, 'r') as f:
        return [num.split('\n')[0] for num in f.readlines()]