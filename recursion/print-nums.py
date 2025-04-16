def print_num(arr):
    for i in arr:
        if isinstance(i, int):
            print(i)
        elif isinstance(i, list):
            print_num(i)

print_num([
    1,
    2,
    3,
    [4,5,6],
    7,
    [8,
     [9, 10, 11, [12, 13, 14]
     ]
    ],
    [15, 16 ,17, 18, 19, 20]
])