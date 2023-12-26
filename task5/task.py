import numpy as np
import json


def flatten(range_r):
    res = []
    for i in range_r:
        if isinstance(i, int):
            res.append(i)
        else:
            for j in i:
                res.append(j)
    return res


def find_ind(range_r, x):
    for i, subrange in enumerate(range_r):
        if x in subrange:
            return i


def check_any_in(p1, p2):
    f = False
    for x in p1:
        f = f or (x in p2)
    return f


def f(x):
    if isinstance(x, int):
        return [x]
    return x


def parse_range(r):
    return [f(x) for x in json.loads(r)]


def _in_conflicts(value, conflicts):
    for cluster in conflicts:
        if value in cluster:
            return True, cluster
    return False, []

def calc_matrix(r):
    n = len(flatten(r))

    matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if find_ind(r, j + 1) >= find_ind(r, i + 1):
                matrix[i][j] = 1

    return matrix


def find_conflicts(m1, m2):
    y1 = np.array(m1)
    y2 = np.array(m2)
    y12 = np.multiply(y1, y2)
    y12t = np.multiply(y1.T, y2.T)
    conflicts = np.logical_or(y12, y12t).astype(np.int32)
    res = []
    for i in range(len(conflicts)):
        for j in range(i):
            if conflicts[i][j] == 0:
                res.append([j + 1, i + 1])

    united_conflicts = unite(res)
    return united_conflicts


def find_common_range(x, y, conflicts):
    result = []

    used = []
    for cl in x:
        for value in cl:
            if value in used:
                continue
            flag, cluster = _in_conflicts(value, conflicts)
            if flag:
                result.append(cluster.tolist())
                for a in cluster:
                    used.append(a)
            else:
                result.append(value)

    print(result)
    return result


def unite(c):
    n = len(c)
    for cnt in range(n):
        res = []
        to_skip = []
        for i, p1 in enumerate(c):
            if i in to_skip:
                continue
            merged = np.asarray(p1)
            for j, p2 in enumerate(c):
                if j <= i:
                    continue
                if check_any_in(p1, p2):
                    merged = np.append(merged, p2)
                    merged = np.unique(merged)
                    to_skip.append(j)
            merged.sort()
            res.append(merged)
        c = res

    return c


def task(x, y):
    x_p = parse_range(x)
    y_p = parse_range(y)
    m_x = calc_matrix(x_p)
    m_y = calc_matrix(y_p)
    conflict = find_conflicts(m_x, m_y)
    return find_common_range(x_p, y_p, conflict)


if __name__ == '__main__':
    x1 = "[[1,2],[3,4,5],6,7,9,[8,10]]"
    x2 = "[3,[1,4],2,6,[5,7,8],[9,10]]"
    task(x1, x2)