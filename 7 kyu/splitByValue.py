def split_by_value(k, elements):
    return [n for n in elements if n < k] +  [n for n in elements if n >= k]