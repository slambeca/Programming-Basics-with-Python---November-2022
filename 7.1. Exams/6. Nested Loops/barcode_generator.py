start_range = str(input())
end_range = str(input())

st_1 = int(start_range[0])
st_2 = int(start_range[1])
st_3 = int(start_range[2])
st_4 = int(start_range[3])

end_1 = int(end_range[0])
end_2 = int(end_range[1])
end_3 = int(end_range[2])
end_4 = int(end_range[3])

for a in range(st_1, end_1 + 1):
    for b in range(st_2, end_2 + 1):
        for c in range(st_3, end_3 + 1):
            for d in range(st_4, end_4 + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f"{a}{b}{c}{d}", end=" ")