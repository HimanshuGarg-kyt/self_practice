check_even = lambda x: x if x%2==0 else None
a = [54,6,8,9,59656,464]
checked = filter(check_even,a)
print(list(checked))