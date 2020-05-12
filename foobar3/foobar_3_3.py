from fractions import Fraction as Fr
import numpy as np
# from sympy import *


def transpose(mat):
    tmat = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == 0:
                tmat.append([])
            tmat[j].append(mat[i][j])
    return tmat


def copy_mat(mat):
    cmat = []
    for i in range(len(mat)):
        cmat.append([])
        for j in range(len(mat[i])):
            cmat[i].append(
                Fr(mat[i][j].numerator, mat[i][j].denominator))
    return cmat


def gauss_elmination(m, values):
    mat = copy_mat(m)
    for i in range(len(mat)):
        index = -1
        for j in range(i, len(mat)):
            if mat[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gauss elimination failed!')
        mat[i], mat[index] = mat[index], mat[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(mat)):
            if mat[j][i].numerator == 0:
                continue
            ratio = -mat[j][i]/mat[i][i]
            for k in range(i, len(mat)):
                mat[j][k] += ratio * mat[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        index = len(mat) - 1 - i
        end = len(mat) - 1
        while end > index:
            values[index] -= mat[index][end] * res[end]
            end -= 1
        res[index] = values[index]/mat[index][index]
    return res


def inverse(mat):
    tmat = transpose(mat)
    mat_inv = []
    for i in range(len(tmat)):
        values = [Fr(int(i == j), 1) for j in range(len(mat))]
        mat_inv.append(gauss_elmination(tmat, values))
    return mat_inv


def computeGCD(x, y):

    while(y):
        x, y = y, x % y

    return x


def get_standard_matrix(m):
    for ind_row, val_row in enumerate(m):
        s = sum(m[ind_row])
        # print(s)
        if(s == 0):
            m[ind_row][ind_row] = 1
        else:
            for ind_col, col_val in enumerate(val_row):
                m[ind_row][ind_col] = Fr(col_val, s)

    # print(m)


def lcm(x, y):
    return (x*y/computeGCD(x, y))


def solution(m):
    # Your code here
    Q = []
    R = []
    result = []
    transition_states = []
    non_transition_states = []
    for row_ind, row in enumerate(m):
        if(sum(row) == 0):
            transition_states.append(row_ind)
        else:
            non_transition_states.append(row_ind)
    get_standard_matrix(m)
    # print("alag----------------------->")
    if(len(transition_states) == 1):
        return [1, 1]
    # Q and R calculation
    for i in non_transition_states:
        temp = []
        for j in non_transition_states:
            temp.append(m[i][j])
        Q.append(temp)

    for i in non_transition_states:
        temp = []
        for j in transition_states:
            temp.append(m[i][j])
        R.append(temp)
    # print("R is the ")
    # print(R)
    # print("Q is the ")
    # print(Q)
    # calculating I-Q
    result = []
    for i in range(len(Q)):
        for j in range(len(Q)):
            if i == j:
                Q[i][j] = Fr(1, 1)-Q[i][j]
            else:
                Q[i][j] = -Q[i][j]

    # print(Q)
    # I took help for inversing the matrix
    F = inverse(Q)
    # print(F)
    # print(R)

    # finding the F*R
    FR = np.dot(F, R)
    FR = FR[0]
    den = 1
    for i in FR:
        den = lcm(den, i.denominator)
    result = list(map(lambda x: int(x.numerator*den/x.denominator), FR))
    result.append(int(den))
    return result


print(solution([
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]))
