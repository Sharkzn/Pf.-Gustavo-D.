def move_left(grid):
    def compress(row):
        new_row = [num for num in row if num != 0] 
        return new_row + [0] * (4 - len(new_row))  
  
    def merge(row):
        new_row = []
        skip = False
        for i in range(4):
            if skip:
                skip = False
                continue
            if i < 3 and row[i] == row[i + 1] and row[i] != 0:
                new_row.append(row[i] * 2)  
                skip = True  
                new_row.append(row[i])
        new_row += [0] * (4 - len(new_row)) 
        return new_row

    new_grid = []
    for row in grid:
        compressed_row = compress(row)  
        merged_row = merge(compressed_row)  
        final_row = compress(merged_row)  
        new_grid.append(final_row)

    return new_grid

grid = [
    [2, 2, 0, 0],
    [4, 4, 4, 4],
    [0, 2, 2, 0],
    [2, 0, 0, 2]
]

new_grid = move_left(grid)
for row in new_grid:
    print(row)
