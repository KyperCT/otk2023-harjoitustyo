def check_score(grid, score):
    clears = []
    for row in range(0, grid.rows):
        if grid.check_row(row):
            clears.append(row)
    if clears:
        for row in clears:
            grid.shift_down_over(row)
        return score + ((2 ** len(clears)) * 100)
    return score
