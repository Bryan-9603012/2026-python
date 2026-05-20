"""
UVA 11332 - 鏡子可見性 (Mirror Visibility)
從原點 (0,0) 判斷哪些鏡子（線段）可見。
鏡子不會通過原點。
演算法：計算每個鏡子的角度區間，依距離排序後檢查覆蓋情況。
"""

import sys
import math


def normalize_angle(a):
    """將角度正規化到 [0, 2π)"""
    a = a % (2 * math.pi)
    if a < 0:
        a += 2 * math.pi
    return a


def get_angular_intervals(sx, sy, ex, ey):
    """計算線段從原點看的角度區間（可能因繞界而分成兩個）"""
    a1 = normalize_angle(math.atan2(sy, sx))
    a2 = normalize_angle(math.atan2(ey, ex))

    lo = min(a1, a2)
    hi = max(a1, a2)

    if hi - lo > math.pi:
        # 繞界：分成兩個區間
        return [(hi, 2 * math.pi), (0, lo)]
    else:
        return [(lo, hi)]


def min_distance(sx, sy, ex, ey):
    """計算線段到原點的最小距離"""
    # 端點到原點的距離
    d1 = math.sqrt(sx * sx + sy * sy)
    d2 = math.sqrt(ex * ex + ey * ey)
    return min(d1, d2)


def merge_intervals(intervals):
    """合併重疊的區間"""
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def is_fully_covered(new_intervals, covered):
    """檢查新區間是否完全被已覆蓋區間覆蓋"""
    for ns, ne in new_intervals:
        # 檢查 [ns, ne] 是否完全被 covered 覆蓋
        current = ns
        fully = False
        for cs, ce in covered:
            if cs > current:
                break
            if cs <= current <= ce:
                current = max(current, ce)
                if current >= ne:
                    fully = True
                    break
        if not fully:
            return False
    return True


def solve():
    input_data = sys.stdin.read().split()
    idx = 0

    def next_int():
        nonlocal idx
        val = int(input_data[idx])
        idx += 1
        return val

    results = []

    while idx < len(input_data):
        n = next_int()
        if n == 0:
            break

        mirrors = []
        for i in range(n):
            sx = next_int()
            sy = next_int()
            ex = next_int()
            ey = next_int()
            intervals = get_angular_intervals(sx, sy, ex, ey)
            dist = min_distance(sx, sy, ex, ey)
            mirrors.append({
                'idx': i,
                'intervals': intervals,
                'dist': dist
            })

        # 依距離排序（近的優先）
        mirrors.sort(key=lambda m: (m['dist'], m['idx']))

        visible = [False] * n
        covered = []  # 已覆蓋的角度區間（合併後）

        for m in mirrors:
            if not is_fully_covered(m['intervals'], covered):
                visible[m['idx']] = True
                # 將此鏡子的區間加入 covered
                all_intervals = covered + m['intervals']
                covered = merge_intervals(all_intervals)

        results.append(''.join('1' if v else '0' for v in visible))

    print('\n'.join(results))


if __name__ == "__main__":
    solve()
