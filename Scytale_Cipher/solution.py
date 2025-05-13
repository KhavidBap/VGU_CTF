text = "CR_Y0CPW0HSLE_UR4M{NN1DS0_!_3}"

def scytale(text, key):
    columns = len(text) // key
    grid = [''] * columns
    index = 0
    for row in range(key):
        for col in range(columns):
            grid[col] += text[index]
            index += 1
    return ''.join(grid)

for key in range(2, len(text)):
    if len(text) % key == 0:
        original = scytale(text, key)
        print(f"Key {key}: {original}")

# CYPHER{10_R0WS_4ND_3_C0LUMNS!}