def decision_tree_0(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_variance_x <= 16.93:
        if gyro_std_x <= 3.5:
            if acce_std_y <= 1.76:
                if gyro_std_y <= 3.29:
                    if acce_mean_y <= 3.57:
                        return [ 1, 32,  0,]
                    else:  # if acce_mean_y > 3.57
                        return [0, 0, 4,]
                else:  # if gyro_std_y > 3.29
                    if gyro_mean_y <= 3.78:
                        if acce_std_x <= 1.85:
                            if acce_std_x <= 0.16:
                                return [0, 3, 0,]
                            else:  # if acce_std_x > 0.16
                                return [0, 0, 8,]
                        else:  # if acce_std_x > 1.85
                            return [0, 7, 0,]
                    else:  # if gyro_mean_y > 3.78
                        if gyro_variance_x <= 9.13:
                            return [2, 2, 2,]
                        else:  # if gyro_variance_x > 9.13
                            return [15,  0,  0,]
            else:  # if acce_std_y > 1.76
                if gyro_std_z <= 4.02:
                    return [ 4, 82,  1,]
                else:  # if gyro_std_z > 4.02
                    return [0, 0, 2,]
        else:  # if gyro_std_x > 3.5
            if gyro_std_y <= 4.0:
                if n_samples <= 14.5:
                    if acce_mean_z <= 0.87:
                        if gyro_mean_y <= 3.0:
                            return [0, 1, 5,]
                        else:  # if gyro_mean_y > 3.0
                            return [30,  0,  0,]
                    else:  # if acce_mean_z > 0.87
                        if acce_mean_y <= 2.99:
                            return [ 1, 51,  3,]
                        else:  # if acce_mean_y > 2.99
                            if gyro_variance_x <= 13.0:
                                return [4, 0, 0,]
                            else:  # if gyro_variance_x > 13.0
                                return [ 0, 10,  7,]
                else:  # if n_samples > 14.5
                    if gyro_mean_y <= 7.15:
                        return [260,   1,   0,]
                    else:  # if gyro_mean_y > 7.15
                        return [0, 2, 0,]
            else:  # if gyro_std_y > 4.0
                if acce_mean_x <= 2.6:
                    if gyro_std_y <= 4.43:
                        return [ 0,  1, 34,]
                    else:  # if gyro_std_y > 4.43
                        return [0, 4, 1,]
                else:  # if acce_mean_x > 2.6
                    return [ 0, 11,  0,]
    else:  # if gyro_variance_x > 16.93
        if gyro_std_y <= 3.78:
            if gyro_variance_x <= 18.73:
                if gyro_variance_z <= 6.6:
                    if gyro_variance_z <= 0.06:
                        return [0, 0, 4,]
                    else:  # if gyro_variance_z > 0.06
                        return [ 0, 16,  0,]
                else:  # if gyro_variance_z > 6.6
                    if gyro_variance_x <= 17.58:
                        if acce_mean_z <= 0.96:
                            return [7, 0, 0,]
                        else:  # if acce_mean_z > 0.96
                            return [0, 4, 1,]
                    else:  # if gyro_variance_x > 17.58
                        if gyro_mean_z <= 3.01:
                            return [0, 2, 0,]
                        else:  # if gyro_mean_z > 3.01
                            return [ 0,  3, 48,]
            else:  # if gyro_variance_x > 18.73
                if acce_mean_x <= 1.63:
                    if gyro_mean_y <= 2.35:
                        return [0, 2, 7,]
                    else:  # if gyro_mean_y > 2.35
                        return [0, 8, 0,]
                else:  # if acce_mean_x > 1.63
                    return [ 0, 22,  1,]
        else:  # if gyro_std_y > 3.78
            if acce_variance_x <= 0.02:
                return [0, 7, 0,]
            else:  # if acce_variance_x > 0.02
                if acce_variance_x <= 3.69:
                    if gyro_variance_y <= 19.79:
                        return [  0,  12, 158,]
                    else:  # if gyro_variance_y > 19.79
                        return [0, 3, 2,]
                else:  # if acce_variance_x > 3.69
                    return [0, 2, 0,]

def decision_tree_1(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if acce_mean_x <= 0.82:
        if gyro_mean_z <= 6.5:
            if gyro_mean_z <= 3.03:
                if acce_mean_z <= 0.88:
                    if gyro_std_y <= 3.35:
                        if gyro_variance_z <= 14.44:
                            return [0, 4, 0,]
                        else:  # if gyro_variance_z > 14.44
                            return [0, 0, 3,]
                    else:  # if gyro_std_y > 3.35
                        return [8, 0, 0,]
                else:  # if acce_mean_z > 0.88
                    return [ 0, 40,  0,]
            else:  # if gyro_mean_z > 3.03
                if acce_std_z <= 0.19:
                    return [0, 1, 3,]
                else:  # if acce_std_z > 0.19
                    return [205,   0,   1,]
        else:  # if gyro_mean_z > 6.5
            if gyro_variance_z <= 0.04:
                if acce_mean_y <= 2.24:
                    return [2, 3, 0,]
                else:  # if acce_mean_y > 2.24
                    return [0, 0, 5,]
            else:  # if gyro_variance_z > 0.04
                if gyro_std_y <= 4.14:
                    return [ 2, 59,  1,]
                else:  # if gyro_std_y > 4.14
                    if acce_variance_x <= 0.02:
                        return [0, 9, 0,]
                    else:  # if acce_variance_x > 0.02
                        return [ 0,  2, 10,]
    else:  # if acce_mean_x > 0.82
        if gyro_variance_x <= 17.05:
            if gyro_mean_y <= 6.22:
                if n_samples <= 14.5:
                    if gyro_variance_y <= 17.04:
                        if gyro_variance_z <= 0.06:
                            return [0, 1, 8,]
                        else:  # if gyro_variance_z > 0.06
                            if acce_variance_x <= 2.51:
                                if acce_variance_x <= 0.01:
                                    return [ 0, 13,  0,]
                                else:  # if acce_variance_x > 0.01
                                    if gyro_std_z <= 0.45:
                                        return [0, 3, 0,]
                                    else:  # if gyro_std_z > 0.45
                                        if acce_variance_x <= 1.9:
                                            return [ 0,  0, 11,]
                                        else:  # if acce_variance_x > 1.9
                                            return [0, 5, 3,]
                            else:  # if acce_variance_x > 2.51
                                return [ 0, 23,  1,]
                    else:  # if gyro_variance_y > 17.04
                        if acce_std_x <= 0.15:
                            return [0, 5, 0,]
                        else:  # if acce_std_x > 0.15
                            if n_samples <= 12.5:
                                if gyro_variance_x <= 3.32:
                                    return [0, 2, 0,]
                                else:  # if gyro_variance_x > 3.32
                                    return [ 0,  0, 47,]
                            else:  # if n_samples > 12.5
                                return [0, 3, 0,]
                else:  # if n_samples > 14.5
                    if acce_std_x <= 1.85:
                        return [80,  1,  0,]
                    else:  # if acce_std_x > 1.85
                        return [0, 2, 0,]
            else:  # if gyro_mean_y > 6.22
                return [ 0, 73,  5,]
        else:  # if gyro_variance_x > 17.05
            if acce_std_x <= 1.85:
                if acce_mean_x <= 2.67:
                    if gyro_std_y <= 3.22:
                        if acce_std_z <= 0.12:
                            return [0, 0, 6,]
                        else:  # if acce_std_z > 0.12
                            if acce_mean_z <= 0.89:
                                return [0, 0, 2,]
                            else:  # if acce_mean_z > 0.89
                                return [ 0, 14,  3,]
                    else:  # if gyro_std_y > 3.22
                        return [  5,   6, 177,]
                else:  # if acce_mean_x > 2.67
                    if gyro_std_y <= 1.21:
                        return [0, 0, 2,]
                    else:  # if gyro_std_y > 1.21
                        return [ 0, 16,  1,]
            else:  # if acce_std_x > 1.85
                if acce_mean_z <= 1.08:
                    return [ 0, 21,  0,]
                else:  # if acce_mean_z > 1.08
                    return [0, 0, 3,]

def decision_tree_2(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_mean_y <= 6.45:
        if gyro_mean_z <= 6.45:
            if gyro_mean_y <= 3.2:
                if gyro_mean_z <= 4.65:
                    if acce_mean_z <= 0.81:
                        if acce_mean_y <= 1.39:
                            if acce_mean_y <= 0.96:
                                return [3, 0, 0,]
                            else:  # if acce_mean_y > 0.96
                                return [0, 2, 0,]
                        else:  # if acce_mean_y > 1.39
                            return [ 0,  0, 10,]
                    else:  # if acce_mean_z > 0.81
                        if acce_mean_z <= 1.04:
                            return [ 2, 31,  0,]
                        else:  # if acce_mean_z > 1.04
                            if acce_mean_z <= 1.44:
                                return [0, 1, 7,]
                            else:  # if acce_mean_z > 1.44
                                return [0, 3, 0,]
                else:  # if gyro_mean_z > 4.65
                    return [ 0,  0, 22,]
            else:  # if gyro_mean_y > 3.2
                if gyro_std_z <= 3.98:
                    if gyro_variance_y <= 15.26:
                        return [302,   0,   0,]
                    else:  # if gyro_variance_y > 15.26
                        if gyro_mean_x <= 4.3:
                            if acce_variance_x <= 1.94:
                                if gyro_mean_z <= 3.61:
                                    return [0, 1, 2,]
                                else:  # if gyro_mean_z > 3.61
                                    return [2, 0, 0,]
                            else:  # if acce_variance_x > 1.94
                                return [ 0, 11,  0,]
                        else:  # if gyro_mean_x > 4.3
                            if gyro_std_x <= 2.2:
                                return [3, 0, 0,]
                            else:  # if gyro_std_x > 2.2
                                return [0, 0, 3,]
                else:  # if gyro_std_z > 3.98
                    return [ 0,  2, 35,]
        else:  # if gyro_mean_z > 6.45
            if gyro_variance_z <= 6.18:
                if gyro_std_z <= 0.45:
                    if gyro_variance_x <= 6.29:
                        return [0, 3, 0,]
                    else:  # if gyro_variance_x > 6.29
                        if gyro_mean_y <= 2.1:
                            if gyro_std_x <= 4.05:
                                return [0, 3, 0,]
                            else:  # if gyro_std_x > 4.05
                                return [0, 2, 6,]
                        else:  # if gyro_mean_y > 2.1
                            return [ 0,  1, 68,]
                else:  # if gyro_std_z > 0.45
                    if gyro_std_x <= 4.27:
                        if n_samples <= 8.5:
                            return [0, 0, 1,]
                        else:  # if n_samples > 8.5
                            return [ 0, 53,  0,]
                    else:  # if gyro_std_x > 4.27
                        if acce_std_x <= 1.79:
                            return [0, 0, 4,]
                        else:  # if acce_std_x > 1.79
                            return [0, 5, 0,]
            else:  # if gyro_variance_z > 6.18
                if acce_std_x <= 0.11:
                    return [1, 3, 0,]
                else:  # if acce_std_x > 0.11
                    return [  1,   2, 122,]
    else:  # if gyro_mean_y > 6.45
        if gyro_std_z <= 3.72:
            if acce_mean_y <= 2.51:
                if gyro_mean_y <= 8.77:
                    return [  1, 100,   1,]
                else:  # if gyro_mean_y > 8.77
                    return [1, 0, 0,]
            else:  # if acce_mean_y > 2.51
                if acce_std_y <= 1.87:
                    return [ 0, 41,  4,]
                else:  # if acce_std_y > 1.87
                    if gyro_variance_y <= 11.59:
                        return [0, 2, 0,]
                    else:  # if gyro_variance_y > 11.59
                        return [0, 0, 6,]
        else:  # if gyro_std_z > 3.72
            if gyro_std_x <= 3.84:
                return [0, 9, 0,]
            else:  # if gyro_std_x > 3.84
                if gyro_mean_y <= 6.76:
                    return [0, 2, 0,]
                else:  # if gyro_mean_y > 6.76
                    return [ 0,  2, 14,]

def decision_tree_3(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_std_x <= 4.03:
        if gyro_std_z <= 2.57:
            if acce_mean_z <= 1.09:
                if gyro_variance_z <= 0.07:
                    if acce_variance_z <= 0.05:
                        return [2, 0, 7,]
                    else:  # if acce_variance_z > 0.05
                        return [0, 2, 0,]
                else:  # if gyro_variance_z > 0.07
                    return [  0, 108,   3,]
            else:  # if acce_mean_z > 1.09
                if gyro_std_y <= 3.67:
                    return [0, 4, 0,]
                else:  # if gyro_std_y > 3.67
                    return [0, 0, 7,]
        else:  # if gyro_std_z > 2.57
            if gyro_mean_y <= 6.51:
                if gyro_mean_z <= 6.55:
                    if gyro_mean_x <= 2.91:
                        if acce_mean_y <= 3.34:
                            if acce_std_x <= 0.19:
                                return [2, 0, 3,]
                            else:  # if acce_std_x > 0.19
                                if gyro_mean_z <= 5.41:
                                    return [ 3, 17,  0,]
                                else:  # if gyro_mean_z > 5.41
                                    return [0, 0, 2,]
                        else:  # if acce_mean_y > 3.34
                            return [0, 0, 6,]
                    else:  # if gyro_mean_x > 2.91
                        if gyro_std_z <= 3.96:
                            if acce_mean_z <= 0.28:
                                return [0, 0, 2,]
                            else:  # if acce_mean_z > 0.28
                                return [240,   0,   0,]
                        else:  # if gyro_std_z > 3.96
                            if gyro_mean_z <= 4.86:
                                return [1, 5, 2,]
                            else:  # if gyro_mean_z > 4.86
                                return [ 0,  0, 14,]
                else:  # if gyro_mean_z > 6.55
                    return [ 0,  6, 30,]
            else:  # if gyro_mean_y > 6.51
                if n_samples <= 8.5:
                    return [0, 0, 6,]
                else:  # if n_samples > 8.5
                    return [ 0, 55,  2,]
    else:  # if gyro_std_x > 4.03
        if acce_mean_x <= 0.79:
            if n_samples <= 9.5:
                return [ 0,  0, 12,]
            else:  # if n_samples > 9.5
                if n_samples <= 15.5:
                    if gyro_mean_y <= 4.65:
                        if gyro_variance_z <= 6.32:
                            return [0, 6, 1,]
                        else:  # if gyro_variance_z > 6.32
                            if n_samples <= 10.5:
                                return [0, 0, 9,]
                            else:  # if n_samples > 10.5
                                return [0, 3, 1,]
                    else:  # if gyro_mean_y > 4.65
                        return [ 0, 41,  1,]
                else:  # if n_samples > 15.5
                    return [5, 0, 0,]
        else:  # if acce_mean_x > 0.79
            if acce_std_x <= 1.83:
                if n_samples <= 11.5:
                    if gyro_variance_y <= 11.2:
                        return [ 0,  8, 15,]
                    else:  # if gyro_variance_y > 11.2
                        if acce_variance_x <= 0.02:
                            return [0, 2, 0,]
                        else:  # if acce_variance_x > 0.02
                            if acce_variance_y <= 0.0:
                                return [0, 2, 0,]
                            else:  # if acce_variance_y > 0.0
                                return [  0,   2, 189,]
                else:  # if n_samples > 11.5
                    if acce_mean_z <= 0.93:
                        return [10,  0,  0,]
                    else:  # if acce_mean_z > 0.93
                        return [ 0, 23,  3,]
            else:  # if acce_std_x > 1.83
                if gyro_variance_z <= 15.37:
                    if acce_mean_x <= 1.75:
                        return [0, 1, 3,]
                    else:  # if acce_mean_x > 1.75
                        return [ 0, 25,  1,]
                else:  # if gyro_variance_z > 15.37
                    if gyro_std_x <= 4.21:
                        return [0, 2, 0,]
                    else:  # if gyro_std_x > 4.21
                        return [0, 0, 6,]

def decision_tree_4(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if n_samples <= 14.5:
        if gyro_variance_y <= 16.66:
            if gyro_mean_z <= 3.75:
                return [  2, 113,   3,]
            else:  # if gyro_mean_z > 3.75
                if gyro_std_z <= 2.58:
                    if acce_std_x <= 0.02:
                        return [5, 0, 0,]
                    else:  # if acce_std_x > 0.02
                        if n_samples <= 9.5:
                            return [0, 0, 6,]
                        else:  # if n_samples > 9.5
                            if n_samples <= 10.5:
                                if acce_mean_y <= 2.94:
                                    if acce_std_z <= 0.72:
                                        return [ 0, 16,  0,]
                                    else:  # if acce_std_z > 0.72
                                        return [0, 0, 1,]
                                else:  # if acce_mean_y > 2.94
                                    return [0, 0, 3,]
                            else:  # if n_samples > 10.5
                                return [ 0, 82,  1,]
                else:  # if gyro_std_z > 2.58
                    if gyro_std_z <= 3.53:
                        if gyro_mean_z <= 6.54:
                            return [37,  0,  0,]
                        else:  # if gyro_mean_z > 6.54
                            if gyro_std_y <= 2.51:
                                return [0, 7, 0,]
                            else:  # if gyro_std_y > 2.51
                                if acce_mean_y <= 1.68:
                                    return [0, 4, 0,]
                                else:  # if acce_mean_y > 1.68
                                    if acce_variance_x <= 3.65:
                                        return [ 0,  0, 26,]
                                    else:  # if acce_variance_x > 3.65
                                        return [0, 1, 0,]
                    else:  # if gyro_std_z > 3.53
                        if gyro_variance_x <= 13.66:
                            if acce_std_z <= 0.18:
                                return [0, 0, 1,]
                            else:  # if acce_std_z > 0.18
                                return [0, 8, 0,]
                        else:  # if gyro_variance_x > 13.66
                            if n_samples <= 12.5:
                                if acce_std_y <= 1.93:
                                    if acce_std_x <= 0.13:
                                        return [0, 3, 0,]
                                    else:  # if acce_std_x > 0.13
                                        if acce_mean_z <= 0.91:
                                            return [ 0,  0, 22,]
                                        else:  # if acce_mean_z > 0.91
                                            return [ 0,  6, 32,]
                                else:  # if acce_std_y > 1.93
                                    return [0, 2, 0,]
                            else:  # if n_samples > 12.5
                                if acce_variance_z <= 1.27:
                                    return [ 0, 13,  0,]
                                else:  # if acce_variance_z > 1.27
                                    return [0, 0, 1,]
        else:  # if gyro_variance_y > 16.66
            if n_samples <= 11.5:
                if gyro_mean_z <= 0.83:
                    return [2, 0, 0,]
                else:  # if gyro_mean_z > 0.83
                    if acce_variance_x <= 3.71:
                        return [  0,   1, 215,]
                    else:  # if acce_variance_x > 3.71
                        return [0, 1, 0,]
            else:  # if n_samples > 11.5
                if gyro_std_z <= 0.29:
                    return [0, 0, 2,]
                else:  # if gyro_std_z > 0.29
                    return [ 0, 31,  2,]
    else:  # if n_samples > 14.5
        if gyro_std_z <= 2.45:
            return [0, 6, 0,]
        else:  # if gyro_std_z > 2.45
            if gyro_std_x <= 4.16:
                if gyro_variance_y <= 9.64:
                    return [0, 2, 0,]
                else:  # if gyro_variance_y > 9.64
                    if acce_std_x <= 1.84:
                        if gyro_variance_z <= 17.22:
                            return [233,   1,   0,]
                        else:  # if gyro_variance_z > 17.22
                            return [0, 2, 0,]
                    else:  # if acce_std_x > 1.84
                        if acce_variance_x <= 3.49:
                            return [0, 1, 0,]
                        else:  # if acce_variance_x > 3.49
                            return [1, 0, 0,]
            else:  # if gyro_std_x > 4.16
                return [0, 5, 0,]

def decision_tree_5(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_std_y <= 3.94:
        if acce_variance_z <= 0.05:
            if gyro_std_y <= 3.42:
                if acce_variance_y <= 0.0:
                    if gyro_mean_y <= 7.79:
                        return [0, 0, 4,]
                    else:  # if gyro_mean_y > 7.79
                        return [2, 1, 0,]
                else:  # if acce_variance_y > 0.0
                    if n_samples <= 9.5:
                        return [0, 1, 7,]
                    else:  # if n_samples > 9.5
                        if gyro_std_y <= 0.21:
                            return [0, 0, 3,]
                        else:  # if gyro_std_y > 0.21
                            return [  3, 117,   3,]
            else:  # if gyro_std_y > 3.42
                if n_samples <= 16.5:
                    if gyro_variance_z <= 6.14:
                        if n_samples <= 10.0:
                            return [0, 0, 4,]
                        else:  # if n_samples > 10.0
                            return [ 0, 24,  0,]
                    else:  # if gyro_variance_z > 6.14
                        if n_samples <= 10.5:
                            return [ 0,  0, 23,]
                        else:  # if n_samples > 10.5
                            return [ 0, 14,  1,]
                else:  # if n_samples > 16.5
                    return [55,  0,  0,]
        else:  # if acce_variance_z > 0.05
            if gyro_std_y <= 3.12:
                if gyro_variance_x <= 13.45:
                    return [ 3, 23,  0,]
                else:  # if gyro_variance_x > 13.45
                    if gyro_mean_y <= 1.45:
                        return [ 0,  0, 19,]
                    else:  # if gyro_mean_y > 1.45
                        if gyro_variance_y <= 0.11:
                            return [0, 0, 3,]
                        else:  # if gyro_variance_y > 0.11
                            return [ 1, 19,  0,]
            else:  # if gyro_std_y > 3.12
                if gyro_variance_x <= 16.34:
                    if gyro_std_z <= 2.58:
                        return [0, 9, 1,]
                    else:  # if gyro_std_z > 2.58
                        if n_samples <= 11.5:
                            if acce_mean_x <= 0.78:
                                return [6, 0, 0,]
                            else:  # if acce_mean_x > 0.78
                                if acce_variance_y <= 3.09:
                                    return [0, 0, 5,]
                                else:  # if acce_variance_y > 3.09
                                    return [0, 5, 2,]
                        else:  # if n_samples > 11.5
                            return [221,   1,   0,]
                else:  # if gyro_variance_x > 16.34
                    if n_samples <= 9.5:
                        return [ 0,  0, 10,]
                    else:  # if n_samples > 9.5
                        if acce_mean_z <= 0.9:
                            if gyro_std_y <= 3.49:
                                return [0, 1, 7,]
                            else:  # if gyro_std_y > 3.49
                                return [4, 0, 0,]
                        else:  # if acce_mean_z > 0.9
                            return [ 0, 21,  1,]
    else:  # if gyro_std_y > 3.94
        if acce_variance_x <= 0.02:
            if acce_mean_y <= 3.08:
                return [ 0, 19,  0,]
            else:  # if acce_mean_y > 3.08
                return [2, 0, 1,]
        else:  # if acce_variance_x > 0.02
            if gyro_std_x <= 2.4:
                return [0, 7, 0,]
            else:  # if gyro_std_x > 2.4
                if acce_mean_x <= 2.78:
                    if gyro_std_y <= 4.48:
                        if acce_variance_x <= 3.51:
                            return [  1,   5, 209,]
                        else:  # if acce_variance_x > 3.51
                            if acce_mean_z <= 1.43:
                                return [0, 3, 0,]
                            else:  # if acce_mean_z > 1.43
                                return [0, 0, 4,]
                    else:  # if gyro_std_y > 4.48
                        return [0, 3, 0,]
                else:  # if acce_mean_x > 2.78
                    if gyro_variance_y <= 19.0:
                        return [ 0, 18,  0,]
                    else:  # if gyro_variance_y > 19.0
                        return [0, 0, 4,]

def decision_tree_6(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if acce_mean_z <= 0.97:
        if gyro_mean_y <= 3.16:
            if acce_variance_x <= 0.01:
                return [ 0, 11,  0,]
            else:  # if acce_variance_x > 0.01
                if gyro_variance_z <= 5.99:
                    if gyro_mean_z <= 8.83:
                        return [ 0, 10,  0,]
                    else:  # if gyro_mean_z > 8.83
                        return [0, 0, 4,]
                else:  # if gyro_variance_z > 5.99
                    return [ 1,  5, 27,]
        else:  # if gyro_mean_y > 3.16
            if gyro_variance_z <= 7.31:
                if n_samples <= 9.5:
                    return [3, 0, 1,]
                else:  # if n_samples > 9.5
                    return [ 0, 20,  2,]
            else:  # if gyro_variance_z > 7.31
                if gyro_mean_y <= 6.44:
                    if gyro_std_x <= 4.18:
                        if gyro_std_x <= 2.82:
                            return [1, 3, 0,]
                        else:  # if gyro_std_x > 2.82
                            if n_samples <= 11.5:
                                return [6, 0, 5,]
                            else:  # if n_samples > 11.5
                                return [233,   0,   0,]
                    else:  # if gyro_std_x > 4.18
                        return [0, 0, 6,]
                else:  # if gyro_mean_y > 6.44
                    return [ 0, 18,  0,]
    else:  # if acce_mean_z > 0.97
        if acce_std_x <= 0.06:
            return [ 1, 53,  2,]
        else:  # if acce_std_x > 0.06
            if acce_variance_x <= 3.43:
                if gyro_std_y <= 3.78:
                    if gyro_mean_y <= 6.63:
                        if acce_std_x <= 0.15:
                            if gyro_std_x <= 4.14:
                                return [26,  0,  0,]
                            else:  # if gyro_std_x > 4.14
                                return [0, 0, 3,]
                        else:  # if acce_std_x > 0.15
                            if gyro_variance_y <= 6.37:
                                return [ 0, 12,  0,]
                            else:  # if gyro_variance_y > 6.37
                                if acce_mean_z <= 1.01:
                                    if gyro_mean_y <= 3.52:
                                        return [0, 3, 7,]
                                    else:  # if gyro_mean_y > 3.52
                                        return [17,  0,  0,]
                                else:  # if acce_mean_z > 1.01
                                    if n_samples <= 10.5:
                                        return [ 0,  2, 19,]
                                    else:  # if n_samples > 10.5
                                        if gyro_std_y <= 3.24:
                                            return [4, 0, 1,]
                                        else:  # if gyro_std_y > 3.24
                                            return [ 1, 16,  0,]
                    else:  # if gyro_mean_y > 6.63
                        if acce_std_z <= 0.15:
                            if acce_mean_y <= 2.47:
                                return [ 0, 10,  1,]
                            else:  # if acce_mean_y > 2.47
                                if n_samples <= 11.5:
                                    return [ 0,  0, 16,]
                                else:  # if n_samples > 11.5
                                    return [0, 7, 0,]
                        else:  # if acce_std_z > 0.15
                            return [ 0, 50,  3,]
                else:  # if gyro_std_y > 3.78
                    if gyro_variance_z <= 0.14:
                        return [ 0,  0, 62,]
                    else:  # if gyro_variance_z > 0.14
                        if gyro_mean_z <= 3.41:
                            return [ 0, 16,  1,]
                        else:  # if gyro_mean_z > 3.41
                            if gyro_variance_z <= 6.24:
                                if gyro_std_z <= 0.51:
                                    return [0, 1, 7,]
                                else:  # if gyro_std_z > 0.51
                                    return [ 0, 14,  1,]
                            else:  # if gyro_variance_z > 6.24
                                return [  3,   6, 115,]
            else:  # if acce_variance_x > 3.43
                if gyro_variance_z <= 17.02:
                    if acce_mean_z <= 1.09:
                        return [ 0, 55,  0,]
                    else:  # if acce_mean_z > 1.09
                        return [1, 0, 2,]
                else:  # if gyro_variance_z > 17.02
                    return [0, 1, 5,]

def decision_tree_7(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_std_y <= 3.95:
        if gyro_std_z <= 2.7:
            if acce_mean_y <= 2.36:
                return [  0, 108,   4,]
            else:  # if acce_mean_y > 2.36
                if gyro_std_x <= 4.09:
                    return [ 0, 25,  3,]
                else:  # if gyro_std_x > 4.09
                    if gyro_mean_z <= 8.92:
                        if gyro_variance_z <= 6.14:
                            return [ 0, 14,  2,]
                        else:  # if gyro_variance_z > 6.14
                            return [0, 0, 6,]
                    else:  # if gyro_mean_z > 8.92
                        return [0, 0, 6,]
        else:  # if gyro_std_z > 2.7
            if acce_mean_z <= 0.97:
                if gyro_std_x <= 4.1:
                    if n_samples <= 12.5:
                        if n_samples <= 9.5:
                            return [0, 1, 7,]
                        else:  # if n_samples > 9.5
                            if gyro_std_z <= 3.25:
                                return [8, 1, 0,]
                            else:  # if gyro_std_z > 3.25
                                if acce_std_z <= 0.24:
                                    return [0, 2, 6,]
                                else:  # if acce_std_z > 0.24
                                    return [0, 7, 1,]
                    else:  # if n_samples > 12.5
                        return [244,   1,   0,]
                else:  # if gyro_std_x > 4.1
                    if gyro_mean_z <= 2.91:
                        if gyro_std_x <= 4.4:
                            return [ 0, 10,  0,]
                        else:  # if gyro_std_x > 4.4
                            return [0, 0, 2,]
                    else:  # if gyro_mean_z > 2.91
                        if gyro_variance_y <= 12.21:
                            return [0, 3, 5,]
                        else:  # if gyro_variance_y > 12.21
                            return [8, 1, 0,]
            else:  # if acce_mean_z > 0.97
                if acce_variance_x <= 3.26:
                    if gyro_variance_x <= 17.48:
                        if gyro_std_y <= 3.43:
                            if acce_mean_z <= 1.05:
                                if n_samples <= 8.0:
                                    return [0, 0, 3,]
                                else:  # if n_samples > 8.0
                                    return [ 0, 30,  0,]
                            else:  # if acce_mean_z > 1.05
                                if gyro_std_z <= 4.05:
                                    return [3, 0, 0,]
                                else:  # if gyro_std_z > 4.05
                                    return [0, 1, 7,]
                        else:  # if gyro_std_y > 3.43
                            if gyro_std_y <= 3.7:
                                return [26,  0,  1,]
                            else:  # if gyro_std_y > 3.7
                                if acce_mean_z <= 1.14:
                                    return [ 2, 16,  7,]
                                else:  # if acce_mean_z > 1.14
                                    return [4, 0, 0,]
                    else:  # if gyro_variance_x > 17.48
                        if acce_variance_x <= 0.01:
                            return [0, 5, 0,]
                        else:  # if acce_variance_x > 0.01
                            if acce_mean_z <= 0.97:
                                return [0, 2, 0,]
                            else:  # if acce_mean_z > 0.97
                                if gyro_mean_x <= 3.32:
                                    return [0, 3, 0,]
                                else:  # if gyro_mean_x > 3.32
                                    return [ 0,  1, 47,]
                else:  # if acce_variance_x > 3.26
                    if n_samples <= 15.5:
                        return [ 0, 24,  0,]
                    else:  # if n_samples > 15.5
                        return [3, 1, 0,]
    else:  # if gyro_std_y > 3.95
        if n_samples <= 11.5:
            if acce_mean_z <= 0.23:
                return [0, 2, 0,]
            else:  # if acce_mean_z > 0.23
                if acce_variance_x <= 0.02:
                    return [0, 7, 2,]
                else:  # if acce_variance_x > 0.02
                    if gyro_mean_z <= 3.12:
                        return [0, 8, 3,]
                    else:  # if gyro_mean_z > 3.12
                        return [  0,   2, 188,]
        else:  # if n_samples > 11.5
            return [ 0, 27,  0,]

def decision_tree_8(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_variance_y <= 15.53:
        if gyro_variance_z <= 6.6:
            if acce_mean_z <= 0.3:
                if acce_mean_z <= 0.18:
                    return [0, 2, 0,]
                else:  # if acce_mean_z > 0.18
                    return [0, 0, 6,]
            else:  # if acce_mean_z > 0.3
                if gyro_variance_z <= 0.05:
                    if acce_variance_z <= 0.03:
                        return [0, 0, 5,]
                    else:  # if acce_variance_z > 0.03
                        if gyro_variance_x <= 12.49:
                            return [0, 0, 1,]
                        else:  # if gyro_variance_x > 12.49
                            return [ 0, 16,  0,]
                else:  # if gyro_variance_z > 0.05
                    return [  0, 108,   0,]
        else:  # if gyro_variance_z > 6.6
            if gyro_std_x <= 4.18:
                if gyro_mean_y <= 6.34:
                    if gyro_std_z <= 3.99:
                        if gyro_mean_z <= 6.69:
                            if gyro_mean_y <= 2.63:
                                if n_samples <= 11.0:
                                    return [0, 1, 3,]
                                else:  # if n_samples > 11.0
                                    return [0, 4, 0,]
                            else:  # if gyro_mean_y > 2.63
                                return [298,   3,   0,]
                        else:  # if gyro_mean_z > 6.69
                            if acce_variance_x <= 1.59:
                                return [1, 0, 9,]
                            else:  # if acce_variance_x > 1.59
                                return [0, 5, 0,]
                    else:  # if gyro_std_z > 3.99
                        if gyro_std_z <= 4.29:
                            if gyro_mean_y <= 2.91:
                                return [0, 2, 9,]
                            else:  # if gyro_mean_y > 2.91
                                return [1, 2, 0,]
                        else:  # if gyro_std_z > 4.29
                            return [ 0, 16,  0,]
                else:  # if gyro_mean_y > 6.34
                    if gyro_std_x <= 3.73:
                        if n_samples <= 8.0:
                            return [0, 0, 1,]
                        else:  # if n_samples > 8.0
                            return [ 1, 53,  0,]
                    else:  # if gyro_std_x > 3.73
                        if n_samples <= 9.0:
                            return [0, 0, 7,]
                        else:  # if n_samples > 9.0
                            return [0, 8, 1,]
            else:  # if gyro_std_x > 4.18
                if acce_mean_y <= 2.0:
                    if gyro_std_y <= 2.84:
                        if acce_std_x <= 0.17:
                            return [0, 5, 0,]
                        else:  # if acce_std_x > 0.17
                            return [0, 2, 7,]
                    else:  # if gyro_std_y > 2.84
                        return [0, 7, 0,]
                else:  # if acce_mean_y > 2.0
                    return [ 0,  6, 38,]
    else:  # if gyro_variance_y > 15.53
        if acce_mean_z <= 1.07:
            if n_samples <= 11.5:
                if gyro_mean_z <= 2.7:
                    if acce_std_x <= 0.74:
                        return [0, 0, 2,]
                    else:  # if acce_std_x > 0.74
                        return [0, 7, 0,]
                else:  # if gyro_mean_z > 2.7
                    if gyro_std_x <= 3.6:
                        if acce_mean_x <= 0.43:
                            return [0, 5, 0,]
                        else:  # if acce_mean_x > 0.43
                            return [0, 1, 7,]
                    else:  # if gyro_std_x > 3.6
                        if acce_mean_y <= 1.29:
                            return [0, 1, 0,]
                        else:  # if acce_mean_y > 1.29
                            return [  0,   3, 136,]
            else:  # if n_samples > 11.5
                if gyro_variance_z <= 0.1:
                    return [0, 0, 2,]
                else:  # if gyro_variance_z > 0.1
                    if n_samples <= 18.0:
                        return [ 0, 32,  0,]
                    else:  # if n_samples > 18.0
                        return [1, 0, 0,]
        else:  # if acce_mean_z > 1.07
            return [ 0,  0, 75,]

def decision_tree_9(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_std_x <= 4.04:
        if acce_std_z <= 0.22:
            if gyro_std_z <= 3.3:
                if n_samples <= 9.5:
                    if gyro_mean_y <= 7.9:
                        return [ 0,  0, 18,]
                    else:  # if gyro_mean_y > 7.9
                        return [0, 2, 0,]
                else:  # if n_samples > 9.5
                    if n_samples <= 17.5:
                        if gyro_std_z <= 0.25:
                            return [0, 0, 2,]
                        else:  # if gyro_std_z > 0.25
                            return [  0, 111,   2,]
                    else:  # if n_samples > 17.5
                        return [3, 0, 0,]
            else:  # if gyro_std_z > 3.3
                if gyro_mean_x <= 2.29:
                    if n_samples <= 18.0:
                        if gyro_mean_y <= 5.72:
                            return [0, 2, 5,]
                        else:  # if gyro_mean_y > 5.72
                            return [ 0, 19,  0,]
                    else:  # if n_samples > 18.0
                        return [3, 0, 0,]
                else:  # if gyro_mean_x > 2.29
                    if acce_mean_z <= 0.99:
                        if gyro_std_y <= 3.95:
                            if gyro_mean_y <= 2.31:
                                return [0, 0, 4,]
                            else:  # if gyro_mean_y > 2.31
                                if gyro_variance_y <= 8.31:
                                    return [0, 2, 0,]
                                else:  # if gyro_variance_y > 8.31
                                    return [44,  1,  0,]
                        else:  # if gyro_std_y > 3.95
                            return [0, 0, 7,]
                    else:  # if acce_mean_z > 0.99
                        return [0, 4, 8,]
        else:  # if acce_std_z > 0.22
            if gyro_variance_y <= 9.04:
                if acce_variance_z <= 0.06:
                    return [0, 1, 4,]
                else:  # if acce_variance_z > 0.06
                    return [ 0, 21,  1,]
            else:  # if gyro_variance_y > 9.04
                if gyro_std_y <= 3.88:
                    if gyro_mean_z <= 6.59:
                        return [236,   5,   2,]
                    else:  # if gyro_mean_z > 6.59
                        if gyro_mean_z <= 6.75:
                            return [0, 0, 3,]
                        else:  # if gyro_mean_z > 6.75
                            return [2, 7, 0,]
                else:  # if gyro_std_y > 3.88
                    if acce_variance_y <= 2.45:
                        return [0, 0, 8,]
                    else:  # if acce_variance_y > 2.45
                        return [3, 9, 6,]
    else:  # if gyro_std_x > 4.04
        if gyro_variance_y <= 15.46:
            if n_samples <= 9.5:
                return [ 0,  0, 29,]
            else:  # if n_samples > 9.5
                if n_samples <= 17.5:
                    if n_samples <= 11.5:
                        if acce_mean_x <= 0.83:
                            if gyro_std_z <= 4.1:
                                return [ 0, 21,  2,]
                            else:  # if gyro_std_z > 4.1
                                return [0, 0, 3,]
                        else:  # if acce_mean_x > 0.83
                            if acce_mean_x <= 1.39:
                                return [ 0,  0, 15,]
                            else:  # if acce_mean_x > 1.39
                                return [ 0, 13,  3,]
                    else:  # if n_samples > 11.5
                        return [ 0, 72,  2,]
                else:  # if n_samples > 17.5
                    return [6, 0, 0,]
        else:  # if gyro_variance_y > 15.46
            if acce_mean_x <= 0.14:
                return [0, 6, 0,]
            else:  # if acce_mean_x > 0.14
                if gyro_mean_z <= 3.14:
                    return [0, 5, 0,]
                else:  # if gyro_mean_z > 3.14
                    if gyro_variance_x <= 17.1:
                        if acce_variance_y <= 3.49:
                            return [0, 7, 2,]
                        else:  # if acce_variance_y > 3.49
                            return [0, 0, 6,]
                    else:  # if gyro_variance_x > 17.1
                        return [  0,   7, 156,]

def decision_tree_10(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if n_samples <= 14.5:
        if gyro_std_y <= 4.13:
            if gyro_std_x <= 4.15:
                if acce_variance_z <= 0.08:
                    if gyro_mean_y <= 8.92:
                        if gyro_std_z <= 4.35:
                            if acce_mean_y <= 3.75:
                                return [  1, 153,   6,]
                            else:  # if acce_mean_y > 3.75
                                return [0, 0, 2,]
                        else:  # if gyro_std_z > 4.35
                            return [0, 0, 3,]
                    else:  # if gyro_mean_y > 8.92
                        return [2, 0, 1,]
                else:  # if acce_variance_z > 0.08
                    if acce_mean_x <= 0.79:
                        if gyro_variance_y <= 7.34:
                            return [0, 8, 0,]
                        else:  # if gyro_variance_y > 7.34
                            return [44,  0,  0,]
                    else:  # if acce_mean_x > 0.79
                        if acce_std_y <= 1.91:
                            if gyro_std_x <= 2.48:
                                return [0, 6, 1,]
                            else:  # if gyro_std_x > 2.48
                                if gyro_mean_z <= 5.16:
                                    return [0, 6, 1,]
                                else:  # if gyro_mean_z > 5.16
                                    return [ 0,  0, 10,]
                        else:  # if acce_std_y > 1.91
                            return [0, 9, 1,]
            else:  # if gyro_std_x > 4.15
                if gyro_mean_z <= 7.83:
                    if gyro_mean_z <= 4.8:
                        if acce_std_y <= 1.78:
                            return [ 0, 17,  0,]
                        else:  # if acce_std_y > 1.78
                            if acce_mean_x <= 0.95:
                                return [ 0,  1, 12,]
                            else:  # if acce_mean_x > 0.95
                                return [0, 6, 0,]
                    else:  # if gyro_mean_z > 4.8
                        if acce_mean_y <= 0.67:
                            return [0, 6, 0,]
                        else:  # if acce_mean_y > 0.67
                            if n_samples <= 12.5:
                                return [ 0,  2, 55,]
                            else:  # if n_samples > 12.5
                                return [0, 2, 0,]
                else:  # if gyro_mean_z > 7.83
                    if gyro_std_y <= 3.3:
                        return [ 0, 29,  2,]
                    else:  # if gyro_std_y > 3.3
                        if acce_std_x <= 1.86:
                            if acce_std_x <= 1.24:
                                if gyro_mean_z <= 8.27:
                                    return [0, 0, 2,]
                                else:  # if gyro_mean_z > 8.27
                                    return [0, 3, 0,]
                            else:  # if acce_std_x > 1.24
                                if n_samples <= 12.5:
                                    return [ 0,  0, 16,]
                                else:  # if n_samples > 12.5
                                    return [0, 1, 0,]
                        else:  # if acce_std_x > 1.86
                            return [0, 7, 0,]
        else:  # if gyro_std_y > 4.13
            if acce_variance_x <= 0.01:
                return [0, 9, 0,]
            else:  # if acce_variance_x > 0.01
                if n_samples <= 11.5:
                    if gyro_variance_y <= 20.17:
                        if acce_mean_y <= 3.93:
                            return [  0,   3, 181,]
                        else:  # if acce_mean_y > 3.93
                            return [0, 3, 1,]
                    else:  # if gyro_variance_y > 20.17
                        return [0, 1, 0,]
                else:  # if n_samples > 11.5
                    return [ 0, 17,  3,]
    else:  # if n_samples > 14.5
        if gyro_mean_y <= 6.78:
            if acce_variance_z <= 0.01:
                return [0, 2, 0,]
            else:  # if acce_variance_z > 0.01
                if gyro_variance_z <= 15.29:
                    return [251,   1,   0,]
                else:  # if gyro_variance_z > 15.29
                    if gyro_std_x <= 4.05:
                        return [3, 0, 0,]
                    else:  # if gyro_std_x > 4.05
                        return [0, 3, 0,]
        else:  # if gyro_mean_y > 6.78
            return [0, 7, 0,]

def decision_tree_11(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if n_samples <= 14.5:
        if gyro_mean_y <= 6.47:
            if acce_variance_x <= 0.02:
                if acce_std_x <= 0.07:
                    return [ 0, 37,  0,]
                else:  # if acce_std_x > 0.07
                    if acce_std_z <= 0.23:
                        if gyro_mean_z <= 3.03:
                            return [0, 0, 2,]
                        else:  # if gyro_mean_z > 3.03
                            return [0, 4, 0,]
                    else:  # if acce_std_z > 0.23
                        return [30,  0,  0,]
            else:  # if acce_variance_x > 0.02
                if gyro_variance_x <= 17.37:
                    if acce_std_x <= 1.85:
                        if acce_mean_x <= 0.88:
                            if acce_mean_z <= 0.9:
                                if gyro_mean_y <= 3.59:
                                    return [0, 4, 0,]
                                else:  # if gyro_mean_y > 3.59
                                    return [16,  0,  0,]
                            else:  # if acce_mean_z > 0.9
                                if n_samples <= 10.5:
                                    if gyro_mean_y <= 1.14:
                                        return [0, 2, 0,]
                                    else:  # if gyro_mean_y > 1.14
                                        return [ 0,  0, 12,]
                                else:  # if n_samples > 10.5
                                    if acce_variance_z <= 0.16:
                                        return [ 0, 14,  0,]
                                    else:  # if acce_variance_z > 0.16
                                        return [2, 0, 0,]
                        else:  # if acce_mean_x > 0.88
                            if acce_mean_y <= 2.01:
                                if gyro_mean_z <= 4.74:
                                    return [0, 6, 0,]
                                else:  # if gyro_mean_z > 4.74
                                    if gyro_std_y <= 3.83:
                                        return [0, 3, 1,]
                                    else:  # if gyro_std_y > 3.83
                                        return [0, 0, 8,]
                            else:  # if acce_mean_y > 2.01
                                if acce_mean_x <= 2.79:
                                    return [ 1,  4, 67,]
                                else:  # if acce_mean_x > 2.79
                                    if gyro_std_y <= 4.27:
                                        return [0, 5, 0,]
                                    else:  # if gyro_std_y > 4.27
                                        return [0, 0, 3,]
                    else:  # if acce_std_x > 1.85
                        return [ 0, 22,  0,]
                else:  # if gyro_variance_x > 17.37
                    if acce_mean_y <= 3.57:
                        if gyro_std_y <= 3.79:
                            if gyro_std_z <= 3.52:
                                return [ 0, 12,  4,]
                            else:  # if gyro_std_z > 3.52
                                if acce_mean_x <= 1.67:
                                    return [ 0,  0, 20,]
                                else:  # if acce_mean_x > 1.67
                                    return [0, 4, 0,]
                        else:  # if gyro_std_y > 3.79
                            return [  0,   6, 150,]
                    else:  # if acce_mean_y > 3.57
                        if gyro_mean_y <= 3.52:
                            return [0, 7, 0,]
                        else:  # if gyro_mean_y > 3.52
                            return [0, 1, 5,]
        else:  # if gyro_mean_y > 6.47
            if gyro_std_y <= 3.44:
                return [  1, 146,   6,]
            else:  # if gyro_std_y > 3.44
                if gyro_mean_y <= 6.74:
                    return [0, 7, 1,]
                else:  # if gyro_mean_y > 6.74
                    if n_samples <= 9.5:
                        return [ 0,  0, 16,]
                    else:  # if n_samples > 9.5
                        if gyro_variance_x <= 18.61:
                            return [ 0, 10,  0,]
                        else:  # if gyro_variance_x > 18.61
                            return [0, 0, 2,]
    else:  # if n_samples > 14.5
        if gyro_mean_x <= 1.97:
            return [0, 4, 0,]
        else:  # if gyro_mean_x > 1.97
            if gyro_variance_x <= 17.3:
                if acce_variance_y <= 3.69:
                    return [245,   1,   0,]
                else:  # if acce_variance_y > 3.69
                    return [0, 2, 0,]
            else:  # if gyro_variance_x > 17.3
                return [0, 7, 0,]

def decision_tree_12(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if n_samples <= 14.5:
        if gyro_variance_y <= 13.43:
            if acce_mean_z <= 0.87:
                if n_samples <= 12.5:
                    if gyro_variance_x <= 13.63:
                        if acce_variance_z <= 0.02:
                            return [ 0, 10,  0,]
                        else:  # if acce_variance_z > 0.02
                            if gyro_variance_z <= 12.47:
                                return [8, 0, 1,]
                            else:  # if gyro_variance_z > 12.47
                                if acce_mean_y <= 1.59:
                                    return [0, 2, 0,]
                                else:  # if acce_mean_y > 1.59
                                    return [0, 0, 4,]
                    else:  # if gyro_variance_x > 13.63
                        if acce_std_y <= 1.49:
                            return [0, 3, 1,]
                        else:  # if acce_std_y > 1.49
                            return [ 0,  0, 16,]
                else:  # if n_samples > 12.5
                    if acce_std_z <= 0.28:
                        return [0, 2, 0,]
                    else:  # if acce_std_z > 0.28
                        return [19,  0,  0,]
            else:  # if acce_mean_z > 0.87
                if n_samples <= 9.5:
                    if acce_mean_y <= 1.89:
                        return [0, 3, 1,]
                    else:  # if acce_mean_y > 1.89
                        return [ 0,  2, 19,]
                else:  # if n_samples > 9.5
                    if acce_variance_y <= 0.0:
                        return [0, 0, 2,]
                    else:  # if acce_variance_y > 0.0
                        if acce_std_z <= 0.35:
                            return [  0, 150,   5,]
                        else:  # if acce_std_z > 0.35
                            if acce_mean_z <= 1.11:
                                if gyro_std_y <= 3.18:
                                    return [0, 3, 1,]
                                else:  # if gyro_std_y > 3.18
                                    return [8, 0, 0,]
                            else:  # if acce_mean_z > 1.11
                                return [ 0, 18,  2,]
        else:  # if gyro_variance_y > 13.43
            if acce_mean_x <= 0.64:
                if gyro_std_x <= 0.11:
                    return [3, 0, 0,]
                else:  # if gyro_std_x > 0.11
                    if acce_std_y <= 1.75:
                        if gyro_variance_y <= 16.19:
                            return [1, 1, 0,]
                        else:  # if gyro_variance_y > 16.19
                            return [0, 0, 4,]
                    else:  # if acce_std_y > 1.75
                        return [ 1, 27,  0,]
            else:  # if acce_mean_x > 0.64
                if acce_std_x <= 1.87:
                    if gyro_mean_y <= 3.09:
                        if gyro_mean_z <= 4.4:
                            return [ 0, 11,  1,]
                        else:  # if gyro_mean_z > 4.4
                            if acce_mean_x <= 2.45:
                                if gyro_std_x <= 1.76:
                                    return [0, 1, 0,]
                                else:  # if gyro_std_x > 1.76
                                    return [ 0,  0, 34,]
                            else:  # if acce_mean_x > 2.45
                                return [0, 5, 0,]
                    else:  # if gyro_mean_y > 3.09
                        if acce_variance_x <= 0.02:
                            return [0, 1, 0,]
                        else:  # if acce_variance_x > 0.02
                            return [  0,  11, 207,]
                else:  # if acce_std_x > 1.87
                    return [ 0, 10,  1,]
    else:  # if n_samples > 14.5
        if acce_variance_y <= 0.01:
            return [0, 3, 0,]
        else:  # if acce_variance_y > 0.01
            if gyro_mean_x <= 6.7:
                if gyro_mean_z <= 7.4:
                    if gyro_variance_z <= 17.48:
                        return [285,   1,   0,]
                    else:  # if gyro_variance_z > 17.48
                        return [0, 2, 0,]
                else:  # if gyro_mean_z > 7.4
                    return [0, 3, 0,]
            else:  # if gyro_mean_x > 6.7
                if gyro_variance_x <= 12.18:
                    return [2, 0, 0,]
                else:  # if gyro_variance_x > 12.18
                    return [1, 4, 0,]

def decision_tree_13(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_variance_y <= 15.63:
        if gyro_std_y <= 3.36:
            if n_samples <= 9.5:
                if gyro_mean_x <= 2.33:
                    return [0, 3, 0,]
                else:  # if gyro_mean_x > 2.33
                    return [ 1,  3, 23,]
            else:  # if n_samples > 9.5
                if gyro_mean_y <= 6.33:
                    if gyro_std_y <= 3.13:
                        if n_samples <= 11.5:
                            if acce_std_x <= 0.66:
                                return [ 0,  5, 11,]
                            else:  # if acce_std_x > 0.66
                                return [0, 8, 0,]
                        else:  # if n_samples > 11.5
                            if gyro_std_z <= 4.36:
                                return [ 0, 31,  0,]
                            else:  # if gyro_std_z > 4.36
                                return [0, 1, 3,]
                    else:  # if gyro_std_y > 3.13
                        if acce_std_z <= 0.19:
                            return [0, 6, 1,]
                        else:  # if acce_std_z > 0.19
                            if gyro_mean_y <= 2.59:
                                return [0, 0, 2,]
                            else:  # if gyro_mean_y > 2.59
                                return [12,  0,  0,]
                else:  # if gyro_mean_y > 6.33
                    return [  0, 137,   0,]
        else:  # if gyro_std_y > 3.36
            if gyro_std_x <= 4.18:
                if n_samples <= 14.5:
                    if acce_std_z <= 0.3:
                        if gyro_variance_z <= 0.06:
                            return [0, 0, 5,]
                        else:  # if gyro_variance_z > 0.06
                            return [ 0, 43,  5,]
                    else:  # if acce_std_z > 0.3
                        if gyro_std_x <= 3.99:
                            if gyro_mean_y <= 3.24:
                                return [0, 2, 2,]
                            else:  # if gyro_mean_y > 3.24
                                return [30,  0,  0,]
                        else:  # if gyro_std_x > 3.99
                            if n_samples <= 11.0:
                                return [0, 0, 3,]
                            else:  # if n_samples > 11.0
                                return [0, 5, 0,]
                else:  # if n_samples > 14.5
                    if acce_mean_z <= 1.0:
                        return [228,   0,   0,]
                    else:  # if acce_mean_z > 1.0
                        if acce_mean_z <= 1.01:
                            return [0, 5, 0,]
                        else:  # if acce_mean_z > 1.01
                            return [17,  2,  0,]
            else:  # if gyro_std_x > 4.18
                if acce_variance_z <= 0.09:
                    if acce_variance_x <= 2.86:
                        if gyro_mean_y <= 7.23:
                            return [ 2,  0, 14,]
                        else:  # if gyro_mean_y > 7.23
                            return [0, 2, 0,]
                    else:  # if acce_variance_x > 2.86
                        return [ 0, 16,  1,]
                else:  # if acce_variance_z > 0.09
                    return [ 0,  4, 19,]
    else:  # if gyro_variance_y > 15.63
        if acce_std_x <= 0.13:
            if gyro_mean_z <= 5.56:
                return [1, 0, 1,]
            else:  # if gyro_mean_z > 5.56
                return [ 0, 18,  0,]
        else:  # if acce_std_x > 0.13
            if acce_std_z <= 0.05:
                if gyro_std_z <= 2.88:
                    return [0, 5, 1,]
                else:  # if gyro_std_z > 2.88
                    return [0, 0, 3,]
            else:  # if acce_std_z > 0.05
                if acce_mean_x <= 2.65:
                    if acce_mean_x <= 0.58:
                        return [0, 4, 0,]
                    else:  # if acce_mean_x > 0.58
                        if acce_variance_x <= 3.51:
                            return [  0,   3, 188,]
                        else:  # if acce_variance_x > 3.51
                            return [0, 4, 1,]
                else:  # if acce_mean_x > 2.65
                    if gyro_variance_y <= 18.59:
                        return [ 0, 13,  0,]
                    else:  # if gyro_variance_y > 18.59
                        return [0, 0, 6,]

def decision_tree_14(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_variance_y <= 15.63:
        if gyro_variance_y <= 11.35:
            if n_samples <= 9.5:
                if acce_mean_y <= 1.91:
                    return [2, 1, 0,]
                else:  # if acce_mean_y > 1.91
                    return [ 0,  0, 15,]
            else:  # if n_samples > 9.5
                if n_samples <= 14.5:
                    if acce_variance_z <= 0.13:
                        if acce_variance_y <= 0.0:
                            return [0, 0, 4,]
                        else:  # if acce_variance_y > 0.0
                            if gyro_mean_y <= 8.82:
                                return [  0, 144,   4,]
                            else:  # if gyro_mean_y > 8.82
                                return [0, 0, 4,]
                    else:  # if acce_variance_z > 0.13
                        if gyro_std_x <= 3.59:
                            if gyro_std_y <= 2.66:
                                return [0, 3, 0,]
                            else:  # if gyro_std_y > 2.66
                                return [7, 0, 0,]
                        else:  # if gyro_std_x > 3.59
                            if acce_std_x <= 0.13:
                                return [0, 7, 0,]
                            else:  # if acce_std_x > 0.13
                                return [0, 3, 8,]
                else:  # if n_samples > 14.5
                    if acce_std_x <= 1.86:
                        return [14,  0,  0,]
                    else:  # if acce_std_x > 1.86
                        return [0, 4, 0,]
        else:  # if gyro_variance_y > 11.35
            if gyro_std_z <= 2.66:
                if n_samples <= 10.5:
                    if acce_mean_y <= 2.2:
                        return [0, 4, 0,]
                    else:  # if acce_mean_y > 2.2
                        return [ 0,  0, 10,]
                else:  # if n_samples > 10.5
                    if gyro_std_z <= 2.54:
                        return [ 0, 33,  2,]
                    else:  # if gyro_std_z > 2.54
                        return [0, 0, 3,]
            else:  # if gyro_std_z > 2.66
                if gyro_std_z <= 3.82:
                    if gyro_mean_x <= 2.28:
                        return [ 2, 11,  0,]
                    else:  # if gyro_mean_x > 2.28
                        if gyro_mean_z <= 6.58:
                            return [273,   0,   1,]
                        else:  # if gyro_mean_z > 6.58
                            if n_samples <= 12.0:
                                return [ 0,  0, 11,]
                            else:  # if n_samples > 12.0
                                return [1, 9, 0,]
                else:  # if gyro_std_z > 3.82
                    if acce_variance_z <= 0.09:
                        return [ 1, 19,  5,]
                    else:  # if acce_variance_z > 0.09
                        if acce_variance_x <= 0.0:
                            return [0, 4, 0,]
                        else:  # if acce_variance_x > 0.0
                            if gyro_mean_z <= 5.19:
                                return [4, 0, 1,]
                            else:  # if gyro_mean_z > 5.19
                                return [0, 0, 9,]
    else:  # if gyro_variance_y > 15.63
        if acce_std_x <= 0.12:
            return [ 1, 17,  1,]
        else:  # if acce_std_x > 0.12
            if gyro_variance_y <= 16.66:
                if gyro_mean_y <= 2.95:
                    return [ 0,  0, 11,]
                else:  # if gyro_mean_y > 2.95
                    return [ 0, 10,  3,]
            else:  # if gyro_variance_y > 16.66
                if gyro_mean_z <= 3.21:
                    if gyro_mean_x <= 4.3:
                        return [0, 7, 1,]
                    else:  # if gyro_mean_x > 4.3
                        return [0, 0, 3,]
                else:  # if gyro_mean_z > 3.21
                    if gyro_std_y <= 4.46:
                        if acce_std_x <= 1.87:
                            return [  0,   1, 207,]
                        else:  # if acce_std_x > 1.87
                            return [0, 4, 2,]
                    else:  # if gyro_std_y > 4.46
                        if acce_mean_y <= 2.58:
                            return [0, 4, 0,]
                        else:  # if acce_mean_y > 2.58
                            return [0, 0, 5,]

def decision_tree_15(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if acce_mean_z <= 0.98:
        if gyro_std_x <= 4.04:
            if n_samples <= 13.5:
                if gyro_std_z <= 3.4:
                    if acce_mean_x <= 0.54:
                        if acce_variance_y <= 2.38:
                            return [10,  0,  0,]
                        else:  # if acce_variance_y > 2.38
                            if acce_mean_z <= 0.87:
                                return [6, 0, 0,]
                            else:  # if acce_mean_z > 0.87
                                return [ 0, 12,  0,]
                    else:  # if acce_mean_x > 0.54
                        return [ 3, 23,  3,]
                else:  # if gyro_std_z > 3.4
                    if gyro_variance_x <= 5.87:
                        return [0, 7, 0,]
                    else:  # if gyro_variance_x > 5.87
                        if n_samples <= 12.5:
                            return [ 0,  5, 25,]
                        else:  # if n_samples > 12.5
                            return [4, 0, 0,]
            else:  # if n_samples > 13.5
                return [221,   1,   0,]
        else:  # if gyro_std_x > 4.04
            if acce_mean_y <= 1.75:
                if acce_variance_x <= 0.32:
                    return [ 0, 21,  1,]
                else:  # if acce_variance_x > 0.32
                    return [7, 1, 0,]
            else:  # if acce_mean_y > 1.75
                if n_samples <= 11.5:
                    return [ 0,  8, 26,]
                else:  # if n_samples > 11.5
                    return [ 2, 11,  0,]
    else:  # if acce_mean_z > 0.98
        if gyro_mean_y <= 7.08:
            if gyro_variance_x <= 17.06:
                if n_samples <= 11.5:
                    if gyro_mean_y <= 5.81:
                        if gyro_variance_y <= 16.3:
                            if gyro_std_y <= 2.8:
                                return [0, 0, 6,]
                            else:  # if gyro_std_y > 2.8
                                return [ 1, 11,  3,]
                        else:  # if gyro_variance_y > 16.3
                            return [ 0,  1, 52,]
                    else:  # if gyro_mean_y > 5.81
                        return [ 0, 10,  3,]
                else:  # if n_samples > 11.5
                    if acce_variance_x <= 0.53:
                        if n_samples <= 16.5:
                            if gyro_variance_y <= 13.2:
                                return [5, 2, 0,]
                            else:  # if gyro_variance_y > 13.2
                                return [ 0, 13,  0,]
                        else:  # if n_samples > 16.5
                            return [21,  0,  0,]
                    else:  # if acce_variance_x > 0.53
                        if acce_variance_z <= 0.07:
                            return [ 0, 48,  0,]
                        else:  # if acce_variance_z > 0.07
                            return [9, 1, 0,]
            else:  # if gyro_variance_x > 17.06
                if acce_mean_z <= 1.07:
                    if gyro_mean_z <= 4.38:
                        if acce_mean_x <= 1.68:
                            return [0, 1, 5,]
                        else:  # if acce_mean_x > 1.68
                            return [ 0, 14,  0,]
                    else:  # if gyro_mean_z > 4.38
                        if gyro_variance_z <= 5.45:
                            if gyro_mean_z <= 8.47:
                                return [ 0, 17,  0,]
                            else:  # if gyro_mean_z > 8.47
                                if acce_variance_x <= 3.55:
                                    return [ 0,  0, 34,]
                                else:  # if acce_variance_x > 3.55
                                    return [0, 4, 0,]
                        else:  # if gyro_variance_z > 5.45
                            if n_samples <= 12.0:
                                return [ 0,  1, 74,]
                            else:  # if n_samples > 12.0
                                return [0, 3, 0,]
                else:  # if acce_mean_z > 1.07
                    if n_samples <= 12.5:
                        return [ 0,  2, 66,]
                    else:  # if n_samples > 12.5
                        return [0, 3, 0,]
        else:  # if gyro_mean_y > 7.08
            if gyro_variance_x <= 18.0:
                return [ 0, 74,  5,]
            else:  # if gyro_variance_x > 18.0
                return [0, 5, 9,]

def decision_tree_16(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_std_y <= 3.94:
        if gyro_mean_y <= 6.44:
            if acce_mean_z <= 0.97:
                if gyro_std_z <= 2.72:
                    if gyro_variance_x <= 15.07:
                        return [ 0, 17,  0,]
                    else:  # if gyro_variance_x > 15.07
                        if acce_mean_x <= 0.76:
                            return [0, 7, 0,]
                        else:  # if acce_mean_x > 0.76
                            return [0, 0, 8,]
                else:  # if gyro_std_z > 2.72
                    if acce_std_y <= 1.9:
                        if gyro_mean_y <= 2.85:
                            return [ 0,  2, 15,]
                        else:  # if gyro_mean_y > 2.85
                            return [218,   3,   0,]
                    else:  # if acce_std_y > 1.9
                        if acce_std_z <= 0.24:
                            return [1, 0, 8,]
                        else:  # if acce_std_z > 0.24
                            if acce_std_x <= 1.56:
                                return [0, 5, 1,]
                            else:  # if acce_std_x > 1.56
                                return [2, 0, 0,]
            else:  # if acce_mean_z > 0.97
                if n_samples <= 14.5:
                    if acce_variance_x <= 3.18:
                        if acce_std_x <= 0.13:
                            if gyro_variance_x <= 14.85:
                                return [10,  1,  0,]
                            else:  # if gyro_variance_x > 14.85
                                return [0, 7, 0,]
                        else:  # if acce_std_x > 0.13
                            if gyro_std_y <= 2.52:
                                return [ 0, 10,  0,]
                            else:  # if gyro_std_y > 2.52
                                if gyro_mean_y <= 1.98:
                                    return [ 0,  3, 15,]
                                else:  # if gyro_mean_y > 1.98
                                    if acce_mean_z <= 1.03:
                                        return [ 0, 16,  2,]
                                    else:  # if acce_mean_z > 1.03
                                        return [0, 1, 7,]
                    else:  # if acce_variance_x > 3.18
                        return [ 0, 39,  0,]
                else:  # if n_samples > 14.5
                    if acce_std_z <= 0.2:
                        return [1, 4, 0,]
                    else:  # if acce_std_z > 0.2
                        return [45,  0,  0,]
        else:  # if gyro_mean_y > 6.44
            if n_samples <= 9.5:
                return [ 0,  2, 17,]
            else:  # if n_samples > 9.5
                if gyro_std_z <= 3.79:
                    return [  1, 133,   4,]
                else:  # if gyro_std_z > 3.79
                    if gyro_variance_x <= 17.71:
                        return [ 0, 18,  1,]
                    else:  # if gyro_variance_x > 17.71
                        if gyro_mean_y <= 6.76:
                            return [0, 3, 0,]
                        else:  # if gyro_mean_y > 6.76
                            return [0, 0, 9,]
    else:  # if gyro_std_y > 3.94
        if acce_variance_z <= 0.0:
            if gyro_variance_x <= 18.11:
                if gyro_variance_z <= 11.84:
                    return [ 0, 13,  0,]
                else:  # if gyro_variance_z > 11.84
                    if gyro_variance_x <= 3.5:
                        return [0, 2, 0,]
                    else:  # if gyro_variance_x > 3.5
                        return [0, 0, 3,]
            else:  # if gyro_variance_x > 18.11
                return [0, 0, 2,]
        else:  # if acce_variance_z > 0.0
            if gyro_variance_x <= 10.92:
                if gyro_variance_y <= 17.07:
                    return [0, 8, 0,]
                else:  # if gyro_variance_y > 17.07
                    return [1, 1, 3,]
            else:  # if gyro_variance_x > 10.92
                if n_samples <= 12.5:
                    if acce_mean_x <= 2.85:
                        return [  0,   9, 207,]
                    else:  # if acce_mean_x > 2.85
                        return [0, 3, 0,]
                else:  # if n_samples > 12.5
                    if acce_std_x <= 0.89:
                        return [2, 0, 0,]
                    else:  # if acce_std_x > 0.89
                        return [ 0, 10,  0,]

def decision_tree_17(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_mean_z <= 6.5:
        if gyro_mean_x <= 2.91:
            if acce_mean_y <= 0.54:
                return [2, 0, 0,]
            else:  # if acce_mean_y > 0.54
                if acce_mean_z <= 0.95:
                    if n_samples <= 15.5:
                        if acce_std_y <= 1.55:
                            return [0, 0, 4,]
                        else:  # if acce_std_y > 1.55
                            if acce_std_z <= 0.74:
                                return [ 0, 12,  0,]
                            else:  # if acce_std_z > 0.74
                                return [0, 0, 2,]
                    else:  # if n_samples > 15.5
                        return [4, 0, 0,]
                else:  # if acce_mean_z > 0.95
                    return [ 0, 91,  3,]
        else:  # if gyro_mean_x > 2.91
            if gyro_std_z <= 3.9:
                if gyro_mean_z <= 2.49:
                    if n_samples <= 10.0:
                        if acce_variance_x <= 0.03:
                            return [1, 0, 0,]
                        else:  # if acce_variance_x > 0.03
                            return [0, 0, 6,]
                    else:  # if n_samples > 10.0
                        return [ 0, 12,  0,]
                else:  # if gyro_mean_z > 2.49
                    return [263,   0,   0,]
            else:  # if gyro_std_z > 3.9
                if n_samples <= 12.5:
                    if acce_mean_y <= 3.54:
                        if gyro_variance_x <= 6.51:
                            return [0, 4, 0,]
                        else:  # if gyro_variance_x > 6.51
                            return [ 0,  1, 70,]
                    else:  # if acce_mean_y > 3.54
                        return [0, 3, 1,]
                else:  # if n_samples > 12.5
                    if acce_mean_y <= 0.96:
                        return [4, 0, 0,]
                    else:  # if acce_mean_y > 0.96
                        if gyro_mean_x <= 3.33:
                            return [2, 0, 1,]
                        else:  # if gyro_mean_x > 3.33
                            return [ 0, 21,  0,]
    else:  # if gyro_mean_z > 6.5
        if acce_mean_x <= 0.89:
            if acce_variance_y <= 0.01:
                if n_samples <= 5.5:
                    return [1, 0, 0,]
                else:  # if n_samples > 5.5
                    return [0, 0, 7,]
            else:  # if acce_variance_y > 0.01
                if gyro_std_z <= 2.53:
                    if gyro_variance_z <= 0.08:
                        if gyro_variance_y <= 13.82:
                            return [ 0, 12,  0,]
                        else:  # if gyro_variance_y > 13.82
                            return [0, 0, 8,]
                    else:  # if gyro_variance_z > 0.08
                        return [ 0, 58,  0,]
                else:  # if gyro_std_z > 2.53
                    if acce_mean_y <= 1.96:
                        if acce_std_y <= 1.89:
                            return [0, 6, 0,]
                        else:  # if acce_std_y > 1.89
                            return [0, 0, 1,]
                    else:  # if acce_mean_y > 1.96
                        if gyro_variance_x <= 17.91:
                            if acce_variance_x <= 0.02:
                                return [0, 1, 2,]
                            else:  # if acce_variance_x > 0.02
                                return [3, 0, 0,]
                        else:  # if gyro_variance_x > 17.91
                            return [0, 0, 5,]
        else:  # if acce_mean_x > 0.89
            if gyro_mean_y <= 6.83:
                if n_samples <= 11.5:
                    return [  0,   8, 206,]
                else:  # if n_samples > 11.5
                    if n_samples <= 18.0:
                        return [ 0, 28,  0,]
                    else:  # if n_samples > 18.0
                        return [2, 0, 0,]
            else:  # if gyro_mean_y > 6.83
                if acce_mean_y <= 2.4:
                    return [ 0, 28,  0,]
                else:  # if acce_mean_y > 2.4
                    if acce_variance_z <= 0.02:
                        return [0, 0, 8,]
                    else:  # if acce_variance_z > 0.02
                        return [0, 9, 0,]

def decision_tree_18(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_variance_y <= 15.53:
        if gyro_mean_y <= 6.46:
            if gyro_std_x <= 4.19:
                if gyro_mean_y <= 3.0:
                    if n_samples <= 11.5:
                        if acce_mean_x <= 0.88:
                            if acce_variance_z <= 0.01:
                                return [0, 0, 2,]
                            else:  # if acce_variance_z > 0.01
                                return [ 0, 12,  1,]
                        else:  # if acce_mean_x > 0.88
                            if gyro_mean_x <= 2.17:
                                return [0, 4, 3,]
                            else:  # if gyro_mean_x > 2.17
                                return [ 0,  0, 20,]
                    else:  # if n_samples > 11.5
                        return [ 1, 29,  3,]
                else:  # if gyro_mean_y > 3.0
                    return [288,   2,   2,]
            else:  # if gyro_std_x > 4.19
                if acce_mean_x <= 2.26:
                    if acce_std_z <= 0.17:
                        return [ 0,  0, 17,]
                    else:  # if acce_std_z > 0.17
                        if acce_variance_z <= 0.12:
                            if acce_mean_z <= 1.04:
                                return [ 0, 18,  3,]
                            else:  # if acce_mean_z > 1.04
                                if acce_variance_y <= 2.92:
                                    return [0, 0, 9,]
                                else:  # if acce_variance_y > 2.92
                                    return [0, 2, 0,]
                        else:  # if acce_variance_z > 0.12
                            return [ 0,  0, 14,]
                else:  # if acce_mean_x > 2.26
                    return [ 0, 15,  0,]
        else:  # if gyro_mean_y > 6.46
            if gyro_std_z <= 3.93:
                if gyro_variance_y <= 11.83:
                    return [  2, 141,   2,]
                else:  # if gyro_variance_y > 11.83
                    if gyro_mean_x <= 4.39:
                        if gyro_mean_z <= 6.6:
                            return [ 0, 15,  0,]
                        else:  # if gyro_mean_z > 6.6
                            return [0, 0, 2,]
                    else:  # if gyro_mean_x > 4.39
                        if n_samples <= 12.5:
                            return [0, 0, 8,]
                        else:  # if n_samples > 12.5
                            return [0, 3, 0,]
            else:  # if gyro_std_z > 3.93
                if acce_std_z <= 0.17:
                    return [ 0,  0, 11,]
                else:  # if acce_std_z > 0.17
                    if acce_mean_y <= 0.95:
                        if gyro_variance_y <= 0.17:
                            return [0, 0, 4,]
                        else:  # if gyro_variance_y > 0.17
                            return [0, 2, 0,]
                    else:  # if acce_mean_y > 0.95
                        return [ 0, 12,  2,]
    else:  # if gyro_variance_y > 15.53
        if acce_variance_x <= 0.01:
            if gyro_variance_x <= 0.02:
                return [2, 0, 0,]
            else:  # if gyro_variance_x > 0.02
                return [ 0, 12,  0,]
        else:  # if acce_variance_x > 0.01
            if acce_mean_y <= 1.63:
                if gyro_mean_x <= 2.52:
                    return [0, 6, 0,]
                else:  # if gyro_mean_x > 2.52
                    if acce_std_x <= 1.7:
                        if acce_mean_x <= 2.06:
                            return [1, 0, 5,]
                        else:  # if acce_mean_x > 2.06
                            return [0, 4, 0,]
                    else:  # if acce_std_x > 1.7
                        return [ 0,  0, 12,]
            else:  # if acce_mean_y > 1.63
                if gyro_variance_y <= 19.53:
                    if acce_variance_x <= 3.38:
                        return [  0,  10, 166,]
                    else:  # if acce_variance_x > 3.38
                        return [0, 4, 6,]
                else:  # if gyro_variance_y > 19.53
                    if gyro_mean_z <= 7.66:
                        return [ 0,  0, 10,]
                    else:  # if gyro_mean_z > 7.66
                        if n_samples <= 12.0:
                            return [0, 0, 4,]
                        else:  # if n_samples > 12.0
                            return [0, 9, 0,]

def decision_tree_19(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if acce_mean_z <= 0.96:
        if n_samples <= 13.5:
            if gyro_variance_y <= 10.08:
                if acce_mean_x <= 0.85:
                    if acce_variance_y <= 0.01:
                        return [0, 0, 2,]
                    else:  # if acce_variance_y > 0.01
                        return [ 0, 35,  1,]
                else:  # if acce_mean_x > 0.85
                    if gyro_variance_x <= 16.09:
                        return [ 0, 15,  5,]
                    else:  # if gyro_variance_x > 16.09
                        return [0, 0, 9,]
            else:  # if gyro_variance_y > 10.08
                if acce_mean_z <= 0.75:
                    if n_samples <= 11.5:
                        return [ 0,  0, 22,]
                    else:  # if n_samples > 11.5
                        return [0, 4, 1,]
                else:  # if acce_mean_z > 0.75
                    if gyro_variance_x <= 15.92:
                        if gyro_std_x <= 3.3:
                            return [3, 4, 1,]
                        else:  # if gyro_std_x > 3.3
                            return [16,  0,  0,]
                    else:  # if gyro_variance_x > 15.92
                        return [0, 5, 1,]
        else:  # if n_samples > 13.5
            if gyro_mean_z <= 7.53:
                if gyro_variance_y <= 9.29:
                    return [1, 3, 0,]
                else:  # if gyro_variance_y > 9.29
                    return [228,   0,   0,]
            else:  # if gyro_mean_z > 7.53
                return [0, 3, 0,]
    else:  # if acce_mean_z > 0.96
        if gyro_variance_y <= 15.98:
            if gyro_mean_y <= 6.61:
                if gyro_std_z <= 2.54:
                    if gyro_mean_z <= 8.74:
                        return [ 0, 35,  1,]
                    else:  # if gyro_mean_z > 8.74
                        return [0, 0, 6,]
                else:  # if gyro_std_z > 2.54
                    if gyro_std_x <= 4.02:
                        if gyro_mean_x <= 6.78:
                            if gyro_mean_x <= 2.71:
                                return [0, 6, 0,]
                            else:  # if gyro_mean_x > 2.71
                                if gyro_variance_x <= 15.16:
                                    return [50,  0,  0,]
                                else:  # if gyro_variance_x > 15.16
                                    if gyro_mean_y <= 3.86:
                                        return [0, 3, 0,]
                                    else:  # if gyro_mean_y > 3.86
                                        return [7, 1, 0,]
                        else:  # if gyro_mean_x > 6.78
                            return [0, 0, 6,]
                    else:  # if gyro_std_x > 4.02
                        if n_samples <= 12.5:
                            return [ 0,  2, 19,]
                        else:  # if n_samples > 12.5
                            return [ 0, 24,  0,]
            else:  # if gyro_mean_y > 6.61
                if n_samples <= 8.5:
                    return [ 0,  0, 20,]
                else:  # if n_samples > 8.5
                    if gyro_variance_z <= 14.25:
                        return [  0, 106,   1,]
                    else:  # if gyro_variance_z > 14.25
                        if gyro_variance_x <= 17.16:
                            return [ 0, 15,  0,]
                        else:  # if gyro_variance_x > 17.16
                            return [0, 4, 6,]
        else:  # if gyro_variance_y > 15.98
            if gyro_variance_x <= 12.59:
                if gyro_variance_z <= 14.7:
                    return [ 0, 23,  2,]
                else:  # if gyro_variance_z > 14.7
                    return [0, 0, 2,]
            else:  # if gyro_variance_x > 12.59
                if acce_mean_x <= 2.78:
                    if acce_std_x <= 1.14:
                        if acce_std_y <= 1.78:
                            return [0, 0, 7,]
                        else:  # if acce_std_y > 1.78
                            return [0, 6, 1,]
                    else:  # if acce_std_x > 1.14
                        if acce_std_x <= 1.92:
                            return [  0,   6, 170,]
                        else:  # if acce_std_x > 1.92
                            return [0, 1, 0,]
                else:  # if acce_mean_x > 2.78
                    return [ 0, 11,  0,]

def decision_tree_20(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_mean_y <= 6.49:
        if gyro_std_x <= 4.04:
            if acce_variance_z <= 0.04:
                if gyro_std_x <= 3.37:
                    return [ 2, 36,  6,]
                else:  # if gyro_std_x > 3.37
                    if gyro_std_y <= 3.99:
                        if gyro_std_z <= 3.17:
                            if n_samples <= 9.5:
                                return [0, 0, 3,]
                            else:  # if n_samples > 9.5
                                return [ 0, 11,  1,]
                        else:  # if gyro_std_z > 3.17
                            return [16,  0,  0,]
                    else:  # if gyro_std_y > 3.99
                        if gyro_variance_y <= 19.66:
                            return [ 0,  3, 32,]
                        else:  # if gyro_variance_y > 19.66
                            return [0, 2, 0,]
            else:  # if acce_variance_z > 0.04
                if n_samples <= 12.5:
                    if acce_std_x <= 0.14:
                        if acce_variance_y <= 3.07:
                            if acce_std_z <= 0.29:
                                return [0, 2, 0,]
                            else:  # if acce_std_z > 0.29
                                return [9, 0, 0,]
                        else:  # if acce_variance_y > 3.07
                            return [0, 5, 0,]
                    else:  # if acce_std_x > 0.14
                        if gyro_mean_x <= 6.64:
                            if gyro_mean_z <= 7.53:
                                if acce_variance_y <= 0.73:
                                    return [1, 0, 3,]
                                else:  # if acce_variance_y > 0.73
                                    if acce_variance_z <= 0.16:
                                        return [ 0, 18,  0,]
                                    else:  # if acce_variance_z > 0.16
                                        return [1, 0, 2,]
                            else:  # if gyro_mean_z > 7.53
                                return [0, 0, 6,]
                        else:  # if gyro_mean_x > 6.64
                            return [ 0,  1, 15,]
                else:  # if n_samples > 12.5
                    return [263,   4,   0,]
        else:  # if gyro_std_x > 4.04
            if gyro_std_y <= 3.83:
                if gyro_mean_y <= 3.55:
                    if n_samples <= 11.5:
                        if acce_mean_x <= 2.49:
                            if acce_mean_x <= 0.69:
                                if acce_variance_z <= 0.03:
                                    return [0, 0, 5,]
                                else:  # if acce_variance_z > 0.03
                                    return [0, 7, 2,]
                            else:  # if acce_mean_x > 0.69
                                return [ 0,  0, 37,]
                        else:  # if acce_mean_x > 2.49
                            return [0, 5, 0,]
                    else:  # if n_samples > 11.5
                        return [ 0, 29,  0,]
                else:  # if gyro_mean_y > 3.55
                    if acce_variance_y <= 0.31:
                        return [0, 2, 0,]
                    else:  # if acce_variance_y > 0.31
                        return [13,  0,  0,]
            else:  # if gyro_std_y > 3.83
                if gyro_mean_z <= 3.37:
                    if acce_mean_x <= 0.95:
                        return [0, 0, 2,]
                    else:  # if acce_mean_x > 0.95
                        return [0, 8, 0,]
                else:  # if gyro_mean_z > 3.37
                    if n_samples <= 11.5:
                        return [  0,   4, 151,]
                    else:  # if n_samples > 11.5
                        if gyro_std_z <= 0.36:
                            return [0, 0, 3,]
                        else:  # if gyro_std_z > 0.36
                            return [ 0, 13,  0,]
    else:  # if gyro_mean_y > 6.49
        if gyro_std_z <= 3.77:
            if n_samples <= 9.5:
                return [0, 1, 8,]
            else:  # if n_samples > 9.5
                return [  2, 136,   1,]
        else:  # if gyro_std_z > 3.77
            if gyro_std_x <= 3.81:
                return [ 0, 11,  0,]
            else:  # if gyro_std_x > 3.81
                if gyro_mean_y <= 6.76:
                    return [0, 3, 0,]
                else:  # if gyro_mean_y > 6.76
                    return [ 0,  2, 13,]

def decision_tree_21(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_variance_y <= 15.53:
        if n_samples <= 14.5:
            if gyro_mean_z <= 2.29:
                return [ 0, 57,  0,]
            else:  # if gyro_mean_z > 2.29
                if gyro_mean_z <= 6.73:
                    if acce_mean_x <= 0.73:
                        if acce_variance_z <= 0.08:
                            if gyro_mean_y <= 2.47:
                                if acce_std_z <= 0.25:
                                    return [0, 0, 5,]
                                else:  # if acce_std_z > 0.25
                                    return [0, 2, 0,]
                            else:  # if gyro_mean_y > 2.47
                                return [1, 9, 0,]
                        else:  # if acce_variance_z > 0.08
                            return [36,  1,  0,]
                    else:  # if acce_mean_x > 0.73
                        if n_samples <= 12.5:
                            if gyro_variance_x <= 6.51:
                                return [0, 4, 0,]
                            else:  # if gyro_variance_x > 6.51
                                if acce_std_y <= 1.91:
                                    return [ 0,  4, 33,]
                                else:  # if acce_std_y > 1.91
                                    return [0, 4, 0,]
                        else:  # if n_samples > 12.5
                            return [ 0, 21,  1,]
                else:  # if gyro_mean_z > 6.73
                    if gyro_mean_x <= 5.24:
                        if gyro_std_x <= 4.44:
                            if n_samples <= 12.0:
                                if acce_variance_z <= 0.0:
                                    return [0, 2, 0,]
                                else:  # if acce_variance_z > 0.0
                                    if acce_mean_y <= 1.72:
                                        return [0, 2, 0,]
                                    else:  # if acce_mean_y > 1.72
                                        return [ 0,  0, 24,]
                            else:  # if n_samples > 12.0
                                return [0, 8, 0,]
                        else:  # if gyro_std_x > 4.44
                            return [ 0, 12,  1,]
                    else:  # if gyro_mean_x > 5.24
                        if acce_mean_y <= 3.07:
                            return [ 0, 91,  4,]
                        else:  # if acce_mean_y > 3.07
                            if gyro_variance_x <= 16.44:
                                if gyro_variance_x <= 13.66:
                                    return [0, 0, 5,]
                                else:  # if gyro_variance_x > 13.66
                                    return [0, 9, 0,]
                            else:  # if gyro_variance_x > 16.44
                                return [0, 0, 7,]
        else:  # if n_samples > 14.5
            if acce_variance_x <= 3.34:
                if gyro_mean_z <= 6.77:
                    return [265,   1,   0,]
                else:  # if gyro_mean_z > 6.77
                    return [0, 3, 0,]
            else:  # if acce_variance_x > 3.34
                return [1, 9, 0,]
    else:  # if gyro_variance_y > 15.53
        if acce_variance_z <= 0.0:
            if gyro_variance_x <= 12.01:
                return [ 0, 13,  0,]
            else:  # if gyro_variance_x > 12.01
                if gyro_std_y <= 4.37:
                    return [ 0,  0, 12,]
                else:  # if gyro_std_y > 4.37
                    return [0, 8, 1,]
        else:  # if acce_variance_z > 0.0
            if n_samples <= 11.5:
                if gyro_variance_x <= 7.58:
                    if acce_mean_y <= 2.53:
                        return [0, 6, 0,]
                    else:  # if acce_mean_y > 2.53
                        return [0, 0, 2,]
                else:  # if gyro_variance_x > 7.58
                    if acce_variance_x <= 0.01:
                        return [0, 2, 1,]
                    else:  # if acce_variance_x > 0.01
                        return [  0,   3, 201,]
            else:  # if n_samples > 11.5
                if acce_variance_z <= 0.01:
                    return [0, 0, 2,]
                else:  # if acce_variance_z > 0.01
                    if gyro_variance_y <= 16.24:
                        return [1, 0, 0,]
                    else:  # if gyro_variance_y > 16.24
                        if gyro_std_z <= 0.36:
                            return [0, 0, 1,]
                        else:  # if gyro_std_z > 0.36
                            return [ 0, 25,  0,]

def decision_tree_22(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if acce_mean_z <= 0.97:
        if gyro_variance_z <= 7.09:
            if acce_std_y <= 1.83:
                return [ 1, 35,  2,]
            else:  # if acce_std_y > 1.83
                if gyro_mean_x <= 4.58:
                    return [0, 1, 7,]
                else:  # if gyro_mean_x > 4.58
                    return [0, 6, 0,]
        else:  # if gyro_variance_z > 7.09
            if gyro_variance_z <= 14.95:
                if n_samples <= 12.5:
                    if acce_std_x <= 0.13:
                        if gyro_std_z <= 3.14:
                            return [4, 0, 0,]
                        else:  # if gyro_std_z > 3.14
                            if acce_variance_z <= 0.08:
                                return [ 0, 10,  0,]
                            else:  # if acce_variance_z > 0.08
                                return [3, 0, 0,]
                    else:  # if acce_std_x > 0.13
                        if acce_mean_y <= 1.37:
                            return [0, 6, 0,]
                        else:  # if acce_mean_y > 1.37
                            return [ 1,  0, 25,]
                else:  # if n_samples > 12.5
                    if gyro_variance_y <= 9.78:
                        return [0, 3, 0,]
                    else:  # if gyro_variance_y > 9.78
                        if gyro_std_x <= 2.66:
                            return [0, 2, 0,]
                        else:  # if gyro_std_x > 2.66
                            return [221,   0,   0,]
            else:  # if gyro_variance_z > 14.95
                if n_samples <= 15.0:
                    if acce_mean_x <= 1.18:
                        if acce_variance_z <= 0.07:
                            return [ 0,  0, 17,]
                        else:  # if acce_variance_z > 0.07
                            return [0, 6, 8,]
                    else:  # if acce_mean_x > 1.18
                        return [ 0, 11,  2,]
                else:  # if n_samples > 15.0
                    return [6, 0, 0,]
    else:  # if acce_mean_z > 0.97
        if n_samples <= 10.5:
            if gyro_variance_x <= 12.84:
                return [ 0, 17,  5,]
            else:  # if gyro_variance_x > 12.84
                if acce_mean_x <= 2.93:
                    if gyro_std_y <= 4.5:
                        return [  0,   8, 218,]
                    else:  # if gyro_std_y > 4.5
                        return [0, 4, 0,]
                else:  # if acce_mean_x > 2.93
                    return [0, 7, 0,]
        else:  # if n_samples > 10.5
            if acce_mean_z <= 1.14:
                if acce_variance_z <= 0.48:
                    if acce_variance_z <= 0.05:
                        if gyro_mean_z <= 8.9:
                            return [  1, 148,   6,]
                        else:  # if gyro_mean_z > 8.9
                            return [0, 0, 2,]
                    else:  # if acce_variance_z > 0.05
                        if gyro_mean_y <= 6.02:
                            if gyro_std_y <= 3.61:
                                if gyro_variance_y <= 5.76:
                                    return [0, 2, 2,]
                                else:  # if gyro_variance_y > 5.76
                                    return [10,  0,  0,]
                            else:  # if gyro_std_y > 3.61
                                if gyro_mean_z <= 8.68:
                                    return [0, 7, 3,]
                                else:  # if gyro_mean_z > 8.68
                                    return [0, 0, 4,]
                        else:  # if gyro_mean_y > 6.02
                            return [ 0, 30,  0,]
                else:  # if acce_variance_z > 0.48
                    if acce_std_x <= 0.13:
                        return [6, 1, 0,]
                    else:  # if acce_std_x > 0.13
                        return [0, 1, 8,]
            else:  # if acce_mean_z > 1.14
                if acce_std_z <= 1.57:
                    if gyro_mean_y <= 6.95:
                        return [23,  0,  0,]
                    else:  # if gyro_mean_y > 6.95
                        return [0, 2, 0,]
                else:  # if acce_std_z > 1.57
                    if acce_mean_y <= 1.68:
                        return [2, 0, 1,]
                    else:  # if acce_mean_y > 1.68
                        return [0, 5, 0,]

def decision_tree_23(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_std_y <= 3.94:
        if gyro_variance_y <= 11.35:
            if acce_variance_x <= 3.15:
                if gyro_mean_y <= 1.45:
                    if gyro_mean_y <= 1.16:
                        if acce_variance_y <= 2.81:
                            return [0, 3, 9,]
                        else:  # if acce_variance_y > 2.81
                            return [ 0, 15,  1,]
                    else:  # if gyro_mean_y > 1.16
                        return [ 0,  1, 23,]
                else:  # if gyro_mean_y > 1.45
                    if acce_std_x <= 1.74:
                        if acce_variance_z <= 0.14:
                            if gyro_variance_z <= 11.12:
                                return [ 0, 82,  0,]
                            else:  # if gyro_variance_z > 11.12
                                if gyro_std_y <= 0.37:
                                    return [0, 0, 3,]
                                else:  # if gyro_std_y > 0.37
                                    if n_samples <= 16.5:
                                        return [ 1, 29,  5,]
                                    else:  # if n_samples > 16.5
                                        return [4, 0, 0,]
                        else:  # if acce_variance_z > 0.14
                            if gyro_mean_x <= 6.25:
                                return [9, 0, 0,]
                            else:  # if gyro_mean_x > 6.25
                                return [0, 7, 0,]
                    else:  # if acce_std_x > 1.74
                        return [7, 0, 1,]
            else:  # if acce_variance_x > 3.15
                return [ 1, 56,  0,]
        else:  # if gyro_variance_y > 11.35
            if gyro_std_x <= 4.04:
                if gyro_mean_y <= 2.88:
                    return [ 0, 16, 10,]
                else:  # if gyro_mean_y > 2.88
                    if acce_std_x <= 0.06:
                        return [ 1, 11,  0,]
                    else:  # if acce_std_x > 0.06
                        if acce_std_z <= 0.07:
                            return [0, 7, 0,]
                        else:  # if acce_std_z > 0.07
                            if gyro_variance_y <= 15.26:
                                if gyro_std_z <= 2.58:
                                    return [0, 3, 0,]
                                else:  # if gyro_std_z > 2.58
                                    return [252,   2,   1,]
                            else:  # if gyro_variance_y > 15.26
                                return [0, 3, 0,]
            else:  # if gyro_std_x > 4.04
                if acce_mean_x <= 1.52:
                    if gyro_mean_y <= 2.66:
                        return [ 0,  0, 29,]
                    else:  # if gyro_mean_y > 2.66
                        if acce_std_x <= 1.27:
                            if n_samples <= 16.0:
                                return [0, 9, 0,]
                            else:  # if n_samples > 16.0
                                return [4, 0, 0,]
                        else:  # if acce_std_x > 1.27
                            if n_samples <= 12.5:
                                return [0, 0, 9,]
                            else:  # if n_samples > 12.5
                                return [1, 2, 0,]
                else:  # if acce_mean_x > 1.52
                    if acce_variance_y <= 3.48:
                        if acce_variance_x <= 3.3:
                            return [0, 2, 4,]
                        else:  # if acce_variance_x > 3.3
                            return [ 0, 19,  0,]
                    else:  # if acce_variance_y > 3.48
                        return [0, 3, 6,]
    else:  # if gyro_std_y > 3.94
        if acce_std_x <= 0.12:
            if acce_mean_y <= 3.22:
                return [ 0, 13,  0,]
            else:  # if acce_mean_y > 3.22
                return [2, 0, 0,]
        else:  # if acce_std_x > 0.12
            if acce_mean_x <= 2.78:
                if gyro_std_x <= 2.4:
                    return [0, 6, 0,]
                else:  # if gyro_std_x > 2.4
                    if acce_mean_x <= 0.53:
                        return [0, 7, 2,]
                    else:  # if acce_mean_x > 0.53
                        return [  1,  15, 190,]
            else:  # if acce_mean_x > 2.78
                if acce_std_x <= 0.89:
                    return [0, 0, 2,]
                else:  # if acce_std_x > 0.89
                    return [ 0, 11,  0,]

def decision_tree_24(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_std_y <= 3.95:
        if gyro_variance_y <= 10.61:
            if gyro_variance_z <= 13.6:
                if acce_std_z <= 0.37:
                    if n_samples <= 8.0:
                        return [1, 0, 6,]
                    else:  # if n_samples > 8.0
                        return [  4, 152,   5,]
                else:  # if acce_std_z > 0.37
                    if acce_mean_z <= 0.95:
                        if gyro_std_y <= 1.55:
                            return [0, 2, 0,]
                        else:  # if gyro_std_y > 1.55
                            return [0, 0, 5,]
                    else:  # if acce_mean_z > 0.95
                        return [5, 1, 0,]
            else:  # if gyro_variance_z > 13.6
                if gyro_mean_z <= 3.89:
                    if gyro_variance_z <= 15.57:
                        return [3, 0, 1,]
                    else:  # if gyro_variance_z > 15.57
                        return [ 0, 12,  0,]
                else:  # if gyro_mean_z > 3.89
                    if acce_variance_x <= 3.1:
                        if n_samples <= 12.5:
                            return [ 0,  3, 28,]
                        else:  # if n_samples > 12.5
                            return [0, 3, 0,]
                    else:  # if acce_variance_x > 3.1
                        if gyro_std_z <= 4.08:
                            return [1, 0, 2,]
                        else:  # if gyro_std_z > 4.08
                            return [0, 4, 0,]
        else:  # if gyro_variance_y > 10.61
            if gyro_std_z <= 2.57:
                if gyro_mean_z <= 8.71:
                    return [ 0, 37,  2,]
                else:  # if gyro_mean_z > 8.71
                    return [0, 0, 6,]
            else:  # if gyro_std_z > 2.57
                if gyro_variance_x <= 17.22:
                    if gyro_variance_z <= 15.13:
                        if gyro_mean_y <= 6.33:
                            if gyro_std_y <= 3.91:
                                if acce_mean_x <= 2.33:
                                    if acce_variance_y <= 3.68:
                                        return [290,   0,   0,]
                                    else:  # if acce_variance_y > 3.68
                                        if gyro_variance_y <= 12.24:
                                            return [0, 2, 0,]
                                        else:  # if gyro_variance_y > 12.24
                                            if gyro_mean_x <= 3.75:
                                                return [0, 0, 2,]
                                            else:  # if gyro_mean_x > 3.75
                                                return [2, 0, 0,]
                                else:  # if acce_mean_x > 2.33
                                    return [3, 6, 0,]
                            else:  # if gyro_std_y > 3.91
                                return [0, 6, 0,]
                        else:  # if gyro_mean_y > 6.33
                            return [ 0, 11,  1,]
                    else:  # if gyro_variance_z > 15.13
                        return [ 1, 11,  5,]
                else:  # if gyro_variance_x > 17.22
                    if acce_variance_x <= 3.29:
                        if acce_mean_y <= 1.92:
                            return [1, 3, 1,]
                        else:  # if acce_mean_y > 1.92
                            return [ 0,  3, 28,]
                    else:  # if acce_variance_x > 3.29
                        return [0, 7, 0,]
    else:  # if gyro_std_y > 3.95
        if acce_variance_x <= 0.01:
            if gyro_mean_z <= 5.56:
                return [1, 0, 1,]
            else:  # if gyro_mean_z > 5.56
                return [0, 7, 0,]
        else:  # if acce_variance_x > 0.01
            if n_samples <= 11.5:
                if acce_std_x <= 1.88:
                    if acce_mean_x <= 2.92:
                        return [  0,   1, 190,]
                    else:  # if acce_mean_x > 2.92
                        return [0, 5, 0,]
                else:  # if acce_std_x > 1.88
                    if gyro_variance_z <= 14.65:
                        return [0, 3, 0,]
                    else:  # if gyro_variance_z > 14.65
                        return [0, 0, 3,]
            else:  # if n_samples > 11.5
                if gyro_mean_z <= 8.75:
                    return [ 1, 18,  0,]
                else:  # if gyro_mean_z > 8.75
                    return [0, 0, 4,]

def decision_tree_25(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_std_y <= 3.94:
        if n_samples <= 14.5:
            if n_samples <= 9.5:
                if gyro_variance_y <= 7.19:
                    if gyro_mean_y <= 4.43:
                        return [0, 0, 2,]
                    else:  # if gyro_mean_y > 4.43
                        return [1, 5, 0,]
                else:  # if gyro_variance_y > 7.19
                    if gyro_std_x <= 2.67:
                        return [0, 1, 0,]
                    else:  # if gyro_std_x > 2.67
                        return [ 0,  1, 47,]
            else:  # if n_samples > 9.5
                if acce_std_z <= 0.28:
                    if acce_std_y <= 0.03:
                        return [0, 0, 2,]
                    else:  # if acce_std_y > 0.03
                        if gyro_std_y <= 0.2:
                            return [0, 1, 3,]
                        else:  # if gyro_std_y > 0.2
                            return [  0, 184,  10,]
                else:  # if acce_std_z > 0.28
                    if gyro_std_x <= 3.84:
                        if gyro_std_y <= 2.76:
                            return [0, 9, 1,]
                        else:  # if gyro_std_y > 2.76
                            if acce_mean_x <= 0.81:
                                return [39,  0,  0,]
                            else:  # if acce_mean_x > 0.81
                                return [1, 3, 4,]
                    else:  # if gyro_std_x > 3.84
                        if acce_mean_y <= 1.62:
                            if acce_std_z <= 1.73:
                                return [ 0, 21,  0,]
                            else:  # if acce_std_z > 1.73
                                return [0, 0, 1,]
                        else:  # if acce_mean_y > 1.62
                            if acce_std_x <= 0.6:
                                if gyro_std_y <= 2.49:
                                    return [0, 4, 0,]
                                else:  # if gyro_std_y > 2.49
                                    if acce_variance_x <= 0.01:
                                        return [1, 1, 0,]
                                    else:  # if acce_variance_x > 0.01
                                        return [ 0,  0, 21,]
                            else:  # if acce_std_x > 0.6
                                return [0, 8, 0,]
        else:  # if n_samples > 14.5
            if gyro_mean_z <= 6.5:
                if acce_variance_x <= 0.0:
                    return [0, 3, 0,]
                else:  # if acce_variance_x > 0.0
                    if gyro_mean_y <= 2.7:
                        return [0, 3, 0,]
                    else:  # if gyro_mean_y > 2.7
                        return [252,   1,   0,]
            else:  # if gyro_mean_z > 6.5
                if acce_mean_x <= 0.8:
                    return [2, 0, 0,]
                else:  # if acce_mean_x > 0.8
                    return [ 0, 10,  0,]
    else:  # if gyro_std_y > 3.94
        if acce_mean_x <= 2.64:
            if acce_variance_x <= 0.02:
                if acce_variance_y <= 1.47:
                    return [0, 0, 1,]
                else:  # if acce_variance_y > 1.47
                    return [ 0, 12,  0,]
            else:  # if acce_variance_x > 0.02
                if gyro_variance_y <= 19.43:
                    if acce_variance_x <= 3.67:
                        return [  0,   5, 190,]
                    else:  # if acce_variance_x > 3.67
                        return [0, 2, 0,]
                else:  # if gyro_variance_y > 19.43
                    if gyro_variance_z <= 7.78:
                        if gyro_std_x <= 3.69:
                            return [0, 0, 2,]
                        else:  # if gyro_std_x > 3.69
                            if gyro_std_z <= 0.3:
                                return [0, 0, 2,]
                            else:  # if gyro_std_z > 0.3
                                return [ 0, 11,  0,]
                    else:  # if gyro_variance_z > 7.78
                        if acce_variance_z <= 0.0:
                            return [0, 1, 0,]
                        else:  # if acce_variance_z > 0.0
                            return [0, 0, 9,]
        else:  # if acce_mean_x > 2.64
            if gyro_variance_y <= 18.65:
                return [ 0, 15,  0,]
            else:  # if gyro_variance_y > 18.65
                return [0, 0, 8,]

def decision_tree_26(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
    if gyro_mean_z <= 6.28:
        if gyro_mean_z <= 3.21:
            if gyro_variance_y <= 17.56:
                if gyro_mean_x <= 4.84:
                    if gyro_mean_y <= 0.44:
                        return [0, 0, 2,]
                    else:  # if gyro_mean_y > 0.44
                        return [  4, 103,   2,]
                else:  # if gyro_mean_x > 4.84
                    if n_samples <= 16.5:
                        if gyro_std_z <= 3.74:
                            return [0, 0, 2,]
                        else:  # if gyro_std_z > 3.74
                            return [0, 3, 0,]
                    else:  # if n_samples > 16.5
                        return [7, 0, 0,]
            else:  # if gyro_variance_y > 17.56
                return [0, 0, 8,]
        else:  # if gyro_mean_z > 3.21
            if gyro_std_y <= 3.94:
                if gyro_variance_z <= 15.98:
                    return [276,   1,   0,]
                else:  # if gyro_variance_z > 15.98
                    if acce_variance_z <= 0.02:
                        return [ 0,  1, 12,]
                    else:  # if acce_variance_z > 0.02
                        if acce_std_x <= 1.27:
                            if gyro_mean_x <= 3.18:
                                if gyro_std_z <= 4.42:
                                    return [0, 7, 1,]
                                else:  # if gyro_std_z > 4.42
                                    return [0, 0, 3,]
                            else:  # if gyro_mean_x > 3.18
                                return [ 0,  1, 11,]
                        else:  # if acce_std_x > 1.27
                            return [ 0, 26,  4,]
            else:  # if gyro_std_y > 3.94
                if n_samples <= 12.0:
                    return [ 0,  0, 35,]
                else:  # if n_samples > 12.0
                    return [1, 3, 0,]
    else:  # if gyro_mean_z > 6.28
        if gyro_std_y <= 3.38:
            if gyro_std_y <= 0.17:
                return [1, 0, 6,]
            else:  # if gyro_std_y > 0.17
                if acce_mean_y <= 2.81:
                    return [ 2, 92,  1,]
                else:  # if acce_mean_y > 2.81
                    if n_samples <= 11.5:
                        if acce_mean_z <= 1.06:
                            return [ 0,  0, 10,]
                        else:  # if acce_mean_z > 1.06
                            return [1, 1, 0,]
                    else:  # if n_samples > 11.5
                        return [0, 8, 0,]
        else:  # if gyro_std_y > 3.38
            if gyro_variance_x <= 12.4:
                if acce_mean_x <= 0.92:
                    if gyro_variance_z <= 7.02:
                        return [ 0, 21,  0,]
                    else:  # if gyro_variance_z > 7.02
                        return [1, 0, 0,]
                else:  # if acce_mean_x > 0.92
                    if n_samples <= 11.5:
                        return [0, 1, 8,]
                    else:  # if n_samples > 11.5
                        return [0, 5, 0,]
            else:  # if gyro_variance_x > 12.4
                if acce_std_x <= 0.09:
                    return [0, 8, 0,]
                else:  # if acce_std_x > 0.09
                    if acce_mean_y <= 1.74:
                        return [ 0, 12,  9,]
                    else:  # if acce_mean_y > 1.74
                        if acce_variance_x <= 3.51:
                            if acce_mean_x <= 0.91:
                                if gyro_variance_x <= 15.47:
                                    return [7, 0, 0,]
                                else:  # if gyro_variance_x > 15.47
                                    if acce_mean_y <= 2.19:
                                        return [0, 4, 0,]
                                    else:  # if acce_mean_y > 2.19
                                        if acce_variance_z <= 0.06:
                                            if acce_variance_x <= 2.31:
                                                return [ 0,  0, 19,]
                                            else:  # if acce_variance_x > 2.31
                                                return [0, 1, 0,]
                                        else:  # if acce_variance_z > 0.06
                                            return [0, 4, 3,]
                            else:  # if acce_mean_x > 0.91
                                return [  1,   5, 151,]
                        else:  # if acce_variance_x > 3.51
                            return [0, 5, 0,]

