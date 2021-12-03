
def encode(in_string, model):
    high = 1.0
    low = 0.0
    for c in in_string:
        print(low, high)
        low_range, high_range = model[c]
        spread = high - low
        high = low + spread * high_range
        low = low + spread * low_range
    return low + (high - low) / 2

def get_symbol(in_float, model):
    for c in model:
        low, high = model[c]
        if in_float >= low and in_float < high:
            return c

    return None

def decode(in_float, model, length):
    high = 1.0
    low = 0.0
    res = bytearray()
    for i in range(length):
        spread = high - low
        c = get_symbol((in_float - low) / spread, model)
        low_range, high_range = model[c]
        high = low + spread * high_range
        low = low + spread * low_range
        res.append(c)

    return res

def build_model():
    res = {}
    base = ord(b'a')
    for i in range(26):
        char = base + i
        res[char] = (0.01 * i, 0.01 * i + 0.01)
    return res

source = b'wxyz'
model = build_model()
print(decode(encode(source, model), model, len(source)))
