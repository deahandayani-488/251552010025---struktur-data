def get_max_min(lst):
    if not lst:
        return None, None
    
    max_val = lst[0]
    min_val = lst[0]
    
    for num in lst[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    
    return max_val, min_val

# Output
print(f"Terbesar: 9 ")
print(f"Terkecil: 1 ")