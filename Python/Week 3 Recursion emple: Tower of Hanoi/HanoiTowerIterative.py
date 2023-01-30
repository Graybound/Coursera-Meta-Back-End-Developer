def hanoi_iterative(n, source, target, auxiliary):
    state = {source: list(range(n, 0, -1)), auxiliary: [], target: []}
    moves = []
    while n > 0:
        if not state[source]:
            continue
        disk = state[source].pop()
        state[target].append(disk)
        moves.append((source, target))
        if n > 1:
            if not state[source]:
                continue
            disk = state[source].pop()
            state[auxiliary].append(disk)
            moves.append((source, auxiliary))
            disk = state[target].pop()
            state[auxiliary].append(disk)
            moves.append((target, auxiliary))
        n -= 1
    print(state)
    return moves


print(hanoi_iterative(10, 'A', 'C', 'B'))
