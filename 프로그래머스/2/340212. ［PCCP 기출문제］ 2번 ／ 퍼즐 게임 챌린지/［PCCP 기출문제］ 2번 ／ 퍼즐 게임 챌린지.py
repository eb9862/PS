def find_time_to_solve(diffs: list, times: list, limit: int, level: int) -> int:
    l = len(diffs)
    t = 0
    time_prev = 0
    for i in range(l):
        time_cur = times[i]
        diff = diffs[i]
        if diff <= level:
            t += time_cur
        else:
            total = (time_prev + time_cur) * (diff - level) + time_cur
            t += total
        time_prev = time_cur
    return t

def solution(diffs, times, limit):
    answer = 0

    level = 1
    level_max = limit // 2
    while level <= level_max:
        m = (level + level_max) // 2
        t = find_time_to_solve(diffs, times, limit, m)
        if t > limit :
            level = m + 1
        else:
            answer = m
            level_max = m - 1
    return answer