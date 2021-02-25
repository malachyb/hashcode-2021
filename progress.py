def progress(intersections, all_pos):
    reds = []
    for i, pos in enumerate(all_pos[0]):
        if pos[1] is not None and intersections[int(pos[1])] != pos[0]:
            reds.append(i)
    for i, row in enumerate(all_pos):
        if i == 0:
            continue
        for red in reds:
            all_pos[i][red] = all_pos[i-1][red]
    all_pos.pop(0)
    return all_pos
