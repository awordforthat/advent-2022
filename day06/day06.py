with open("input.txt") as f:
    input = f.readlines()[0]

packet_width = 14  # 4 for a, 14 for b
index = 0
token = ""
while index < len(input) - packet_width:
    token = input[index : index + packet_width]
    if len(set(token)) == len(token):
        break
    index += 1
print(token, index + packet_width)
