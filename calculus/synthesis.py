import numpy as np
import math


def sen(a):
    a = np.radians(a)
    return np.sin(a)


def cos(a):
    a = np.radians(a)
    return np.cos(a)


def arctan(a, b):
    return math.degrees(np.arctan2(a, b))


def sqrt(a):
    return np.sqrt(a)


def synthesis(theta_1, theta_2, theta_3, P1_x, P1_y, P2_x, P2_y, P3_x, P3_y, O2_x, O2_y, O4_x, O4_y):
    # Parte 1

    alpha_2 = theta_2 - theta_1
    alpha_3 = theta_3 - theta_1

    P2_1 = sqrt((P1_x - P2_x) ** 2 + (P1_y - P2_y) ** 2)
    P3_1 = sqrt((P1_x - P3_x) ** 2 + (P1_y - P3_y) ** 2)

    P21_x = P2_x - P1_x
    P21_y = P2_y - P1_y

    P31_x = P3_x - P1_x
    P31_y = P3_y - P1_y

    delta_2 = arctan(P2_y - P1_y, P2_x - P1_x)
    delta_3 = arctan(P3_y - P1_y, P3_x - P1_x)

    # Parte 2: Lado izquierdo

    R1_i = sqrt((O2_x - P1_x) ** 2 + (O2_y - P1_y) ** 2)
    R2_i = sqrt((O2_x - P2_x) ** 2 + (O2_y - P2_y) ** 2)
    R3_i = sqrt((O2_x - P3_x) ** 2 + (O2_y - P3_y) ** 2)

    dseta_1i = arctan(P1_y - O2_y, P1_x - O2_x)
    dseta_2i = arctan(P2_y - O2_y, P2_x - O2_x)
    dseta_3i = arctan(P3_y - O2_y, P3_x - O2_x)

    C1_i = R3_i * cos(alpha_2 + dseta_3i) - R2_i * cos(alpha_3 + dseta_2i)
    C2_i = R3_i * sen(alpha_2 + dseta_3i) - R2_i * sen(alpha_3 + dseta_2i)
    C3_i = R1_i * cos(alpha_3 + dseta_1i) - R3_i * cos(dseta_3i)
    C4_i = -R1_i * sen(alpha_3 + dseta_1i) + R3_i * sen(dseta_3i)
    C5_i = R1_i * cos(alpha_2 + dseta_1i) - R2_i * cos(dseta_2i)
    C6_i = -R1_i * sen(alpha_2 + dseta_1i) + R2_i * sen(dseta_2i)

    A1_i = -(C3_i ** 2) - (C4_i ** 2)
    A2_i = C3_i * C6_i - C4_i * C5_i
    A3_i = -C4_i * C6_i - C3_i * C5_i
    A4_i = C2_i * C3_i + C1_i * C4_i
    A5_i = C4_i * C5_i - C3_i * C6_i
    A6_i = C1_i * C3_i - C2_i * C4_i

    K1_i = A2_i * A4_i + A3_i * A6_i
    K2_i = A3_i * A4_i + A5_i * A6_i
    K3_i = (A1_i ** 2 - A2_i ** 2 - A3_i ** 2 - A4_i ** 2 - A6_i ** 2) / 2

    beta_3a = round(2 * arctan(K2_i + sqrt(K1_i ** 2 + K2_i ** 2 - K3_i ** 2), K1_i + K3_i), 3)
    beta_3b = round(2 * arctan(K2_i - sqrt(K1_i ** 2 + K2_i ** 2 - K3_i ** 2), K1_i + K3_i), 3)
    beta_2a = round(
        arctan(-(A3_i * sen(beta_3a) + A2_i * cos(beta_3a) + A4_i),
               -(A5_i * sen(beta_3a) + A3_i * cos(beta_3a) + A6_i)), 3)
    beta_2b = round(
        arctan(-(A3_i * sen(beta_3b) + A2_i * cos(beta_3b) + A4_i),
               -(A5_i * sen(beta_3b) + A3_i * cos(beta_3b) + A6_i)), 3)

    if beta_2a == alpha_2 or beta_3a == alpha_3:
        beta_2 = beta_2b
        beta_3 = beta_3b
    else:
        beta_2 = beta_2a
        beta_3 = beta_3a

    # Parte 2: Lado derecho

    R1_d = sqrt((O4_x - P1_x) ** 2 + (O4_y - P1_y) ** 2)
    R2_d = sqrt((O4_x - P2_x) ** 2 + (O4_y - P2_y) ** 2)
    R3_d = sqrt((O4_x - P3_x) ** 2 + (O4_y - P3_y) ** 2)

    dseta_1d = arctan(P1_y - O4_y, P1_x - O4_x)
    dseta_2d = arctan(P2_y - O4_y, P2_x - O4_x)
    dseta_3d = arctan(P3_y - O4_y, P3_x - O4_x)

    C1_d = R3_d * cos(alpha_2 + dseta_3d) - R2_d * cos(alpha_3 + dseta_2d)
    C2_d = R3_d * sen(alpha_2 + dseta_3d) - R2_d * sen(alpha_3 + dseta_2d)
    C3_d = R1_d * cos(alpha_3 + dseta_1d) - R3_d * cos(dseta_3d)
    C4_d = -R1_d * sen(alpha_3 + dseta_1d) + R3_d * sen(dseta_3d)
    C5_d = R1_d * cos(alpha_2 + dseta_1d) - R2_d * cos(dseta_2d)
    C6_d = -R1_d * sen(alpha_2 + dseta_1d) + R2_d * sen(dseta_2d)

    A1_d = -(C3_d ** 2) - (C4_d ** 2)
    A2_d = C3_d * C6_d - C4_d * C5_d
    A3_d = -C4_d * C6_d - C3_d * C5_d
    A4_d = C2_d * C3_d + C1_d * C4_d
    A5_d = C4_d * C5_d - C3_d * C6_d
    A6_d = C1_d * C3_d - C2_d * C4_d

    K1_d = A2_d * A4_d + A3_d * A6_d
    K2_d = A3_d * A4_d + A5_d * A6_d
    K3_d = (A1_d ** 2 - A2_d ** 2 - A3_d ** 2 - A4_d ** 2 - A6_d ** 2) / 2

    gamma_3a = round(2 * arctan(K2_d + sqrt(K1_d ** 2 + K2_d ** 2 - K3_d ** 2), K1_d + K3_d), 3)
    gamma_3b = round(2 * arctan(K2_d - sqrt(K1_d ** 2 + K2_d ** 2 - K3_d ** 2), K1_d + K3_d), 3)
    gamma_2a = round(arctan(-(A3_d * sen(gamma_3a) + A2_d * cos(gamma_3a) + A4_d),
                            -(A5_d * sen(gamma_3a) + A3_d * cos(gamma_3a) + A6_d)), 3)
    gamma_2b = round(arctan(-(A3_d * sen(gamma_3b) + A2_d * cos(gamma_3b) + A4_d),
                            -(A5_d * sen(gamma_3b) + A3_d * cos(gamma_3b) + A6_d)), 3)

    if gamma_2a == alpha_2 or gamma_3a == alpha_3:
        gamma_2 = gamma_2b
        gamma_3 = gamma_3b
    else:
        gamma_2 = gamma_2a
        gamma_3 = gamma_3a

    # Parte 3

    mtzi = np.zeros([4, 4])
    mtzi[0] = cos(beta_2) - 1, -sen(beta_2), cos(alpha_2) - 1, -sen(alpha_2)
    mtzi[1] = sen(beta_2), cos(beta_2) - 1, sen(alpha_2), cos(alpha_2) - 1
    mtzi[2] = cos(beta_3) - 1, -sen(beta_3), cos(alpha_3) - 1, -sen(alpha_3)
    mtzi[3] = sen(beta_3), cos(beta_3) - 1, sen(alpha_3), cos(alpha_3) - 1

    tii = np.zeros([4, 1])
    tii[0] = P2_1 * cos(delta_2)
    tii[1] = P2_1 * sen(delta_2)
    tii[2] = P3_1 * cos(delta_3)
    tii[3] = P3_1 * sen(delta_3)

    li = np.linalg.solve(mtzi, tii)
    W_x = li[0]
    W_y = li[1]
    Z_x = li[2]
    Z_y = li[3]

    mtzd = np.zeros([4, 4])
    mtzd[0] = cos(gamma_2) - 1, -sen(gamma_2), cos(alpha_2) - 1, -sen(alpha_2)
    mtzd[1] = sen(gamma_2), cos(gamma_2) - 1, sen(alpha_2), cos(alpha_2) - 1
    mtzd[2] = cos(gamma_3) - 1, -sen(gamma_3), cos(alpha_3) - 1, -sen(alpha_3)
    mtzd[3] = sen(gamma_3), cos(gamma_3) - 1, sen(alpha_3), cos(alpha_3) - 1

    tid = np.zeros([4, 1])
    tid[0] = P2_1 * cos(delta_2)
    tid[1] = P2_1 * sen(delta_2)
    tid[2] = P3_1 * cos(delta_3)
    tid[3] = P3_1 * sen(delta_3)

    ld = np.linalg.solve(mtzd, tid)
    U_x = ld[0]
    U_y = ld[1]
    S_x = ld[2]
    S_y = ld[3]

    W = sqrt(W_x ** 2 + W_y ** 2)
    Z = sqrt(Z_x ** 2 + Z_y ** 2)
    U = sqrt(U_x ** 2 + U_y ** 2)
    S = sqrt(S_x ** 2 + S_y ** 2)

    # redondeando
    W = round(W[0], 3)
    Z = round(Z[0], 3)
    U = round(U[0], 3)
    S = round(S[0], 3)

    theta = round(float(arctan(W_y, W_x)), 3)
    phi = round(float(arctan(Z_y, Z_x)), 3)
    sigma = round(arctan(U_y, U_x), 3)
    psi = round(arctan(S_y, S_x), 3)

    # Parte 4

    ax_1 = O2_x + W_x
    ay_1 = O2_y + W_y
    bx_1 = O4_x + U_x
    by_1 = O4_y + U_y

    l1 = sqrt((O4_x - O2_x) ** 2 + (O4_y - O2_y) ** 2)
    L1 = round(float(l1), 3)
    l2 = sqrt((ax_1 - O2_x) ** 2 + (ay_1 - O2_y) ** 2)
    L2 = round(float(l2), 3)
    l3 = sqrt((ax_1 - bx_1) ** 2 + (ay_1 - by_1) ** 2)
    L3 = round(float(l3), 3)
    l4 = sqrt((O4_x - bx_1) ** 2 + (O4_y - by_1) ** 2)
    L4 = round(float(l4), 3)

    # print('alpha2: ', alpha_2)
    # print('P21_x: ', P21_x)
    # print('P21_y: ', P21_y)
    # print('P31_x: ', P31_x)
    # print('P31_y: ', P31_y)
    # print('beta2: ', beta_2)
    # print('beta3: ', beta_3)
    # print('W: ', W)
    # print('theta: ', theta)
    # print('Z: ', Z)
    # print(' phi: ', phi)
    # print('gamma2: ', gamma_2)
    # print('gamma3: ', gamma_3)
    # print('U: ', U)
    # print('sigma: ', sigma)
    # print('S: ', S)
    # print('psi: ', psi)
    # print('L1: ', L1)
    # print('L2: ', L2)
    # print('L3: ', L3)
    # print('L4: ', L4)

    result = [str(alpha_2), str(alpha_3),
              str(P21_x), str(P21_y),
              str(P31_x), str(P31_y),
              str(beta_2), str(beta_3),
              str(W), str(theta), str(Z), str(phi),
              str(gamma_2), str(gamma_3),
              str(U), str(sigma), str(S), str(psi),
              str(L1), str(L2), str(L3), str(L4)]
    return result
