seq = list(map(lambda x: int(x), input().split((" "))))

message = ["ascending", "descending", "mixed"]

type = None

if (1, 8) != (seq[0], seq[-1]) and (8, 1) != (seq[0], seq[-1]):
    type = message[2]
else:
    for i in range(len(seq) - 1):
        if type is None:
            type = seq[i] <= seq[i + 1]
        else:
            if seq[i] != seq[i+1]:
                new_type = seq[i] < seq[i + 1]
                if type != new_type:
                    type = None
                    break

    if type is not None:
        if type:
            type = message[0]
        else:
            type = message[1]
    else:
        type = message[2]

print(type)