def decision_tree_0(n_samples, gyro_std_x, gyro_std_y, acce_std_z, gyro_variance_z, gyro_kurt_x, gyro_kurt_y, acce_energy_z):
    if gyro_std_y <= 3.9:
        if acce_std_z <= 0.21:
            if gyro_variance_z <= 11.08:
                if n_samples <= 8.5:
                    return [2, 0, 8,]
                else:  # if n_samples > 8.5
                    return [  2, 104,   5,]
            else:  # if gyro_variance_z > 11.08
                return [21, 17, 19,]
        else:  # if acce_std_z > 0.21
            if gyro_std_x <= 4.07:
                if gyro_kurt_x <= -0.7:
                    if gyro_kurt_y <= -0.49:
                        return [235,   1,   2,]
                    else:  # if gyro_kurt_y > -0.49
                        return [0, 6, 1,]
                else:  # if gyro_kurt_x > -0.7
                    return [ 3, 27,  8,]
            else:  # if gyro_std_x > 4.07
                return [ 2, 41, 16,]
    else:  # if gyro_std_y > 3.9
        if gyro_std_x <= 3.35:
            return [ 2, 22,  1,]
        else:  # if gyro_std_x > 3.35
            if acce_energy_z <= 13.4:
                return [  1,   6, 141,]
            else:  # if acce_energy_z > 13.4
                return [ 0, 14, 12,]

def decision_tree_1(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z, gyro_skew_x, gyro_skew_y, gyro_skew_z, acce_skew_x, acce_skew_y, acce_skew_z, gyro_kurt_x, gyro_kurt_y, gyro_kurt_z, acce_kurt_x, acce_kurt_y, acce_kurt_z, gyro_max_x, gyro_max_y, gyro_max_z, acce_max_x, acce_max_y, acce_max_z, gyro_min_x, gyro_min_y, gyro_min_z, acce_min_x, acce_min_y, acce_min_z, gyro_range_x, gyro_range_y, gyro_range_z, acce_range_x, acce_range_y, acce_range_z, gyro_rms_x, gyro_rms_y, gyro_rms_z, acce_rms_x, acce_rms_y, acce_rms_z, gyro_energy_x, gyro_energy_y, gyro_energy_z, acce_energy_x, acce_energy_y, acce_energy_z, gyro_corr_xy, gyro_corr_xz, gyro_corr_yz, acce_corr_xy, acce_corr_xz, acce_corr_yz):
    if gyro_variance_y <= 15.2:
        if acce_min_z <= 0.64:
            if gyro_skew_y <= -1.01:
                return [ 0, 50,  1,]
            else:  # if gyro_skew_y > -1.01
                if gyro_mean_y <= 3.01:
                    if acce_corr_xz <= 0.32:
                        return [ 0,  9, 24,]
                    else:  # if acce_corr_xz > 0.32
                        return [ 0, 19,  2,]
                else:  # if gyro_mean_y > 3.01
                    return [239,   4,   0,]
        else:  # if acce_min_z > 0.64
            if acce_energy_z <= 10.76:
                if acce_range_x <= 0.28:
                    return [ 0, 15,  0,]
                else:  # if acce_range_x > 0.28
                    return [ 0,  3, 33,]
            else:  # if acce_energy_z > 10.76
                return [  6, 102,   8,]
    else:  # if gyro_variance_y > 15.2
        if acce_max_x <= 0.48:
            return [ 1, 10,  0,]
        else:  # if acce_max_x > 0.48
            if n_samples <= 11.5:
                return [  0,   9, 161,]
            else:  # if n_samples > 11.5
                return [ 0, 18,  5,]

def decision_tree_2(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z, gyro_skew_x, gyro_skew_y, gyro_skew_z, acce_skew_x, acce_skew_y, acce_skew_z, gyro_kurt_x, gyro_kurt_y, gyro_kurt_z, acce_kurt_x, acce_kurt_y, acce_kurt_z, gyro_max_x, gyro_max_y, gyro_max_z, acce_max_x, acce_max_y, acce_max_z, gyro_min_x, gyro_min_y, gyro_min_z, acce_min_x, acce_min_y, acce_min_z, gyro_range_x, gyro_range_y, gyro_range_z, acce_range_x, acce_range_y, acce_range_z, gyro_rms_x, gyro_rms_y, gyro_rms_z, acce_rms_x, acce_rms_y, acce_rms_z, gyro_energy_x, gyro_energy_y, gyro_energy_z, acce_energy_x, acce_energy_y, acce_energy_z, gyro_corr_xy, gyro_corr_xz, gyro_corr_yz, acce_corr_xy, acce_corr_xz, acce_corr_yz):
    if gyro_kurt_y <= -1.11:
        if acce_min_z <= 0.68:
            if acce_min_x <= 0.66:
                return [245,   5,   8,]
            else:  # if acce_min_x > 0.66
                return [ 2,  4, 10,]
        else:  # if acce_min_z > 0.68
            if gyro_variance_x <= 13.1:
                return [ 3, 17,  4,]
            else:  # if gyro_variance_x > 13.1
                if acce_rms_x <= 1.32:
                    return [ 0, 11,  8,]
                else:  # if acce_rms_x > 1.32
                    if acce_energy_x <= 128.39:
                        return [  0,   4, 103,]
                    else:  # if acce_energy_x > 128.39
                        return [0, 6, 0,]
    else:  # if gyro_kurt_y > -1.11
        if acce_kurt_x <= -1.13:
            return [  0, 119,  19,]
        else:  # if acce_kurt_x > -1.13
            if gyro_variance_z <= 6.67:
                return [ 0, 48,  2,]
            else:  # if gyro_variance_z > 6.67
                if gyro_skew_z <= 0.28:
                    return [ 0,  9, 59,]
                else:  # if gyro_skew_z > 0.28
                    return [ 0, 23, 10,]

def decision_tree_3(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z, gyro_skew_x, gyro_skew_y, gyro_skew_z, acce_skew_x, acce_skew_y, acce_skew_z, gyro_kurt_x, gyro_kurt_y, gyro_kurt_z, acce_kurt_x, acce_kurt_y, acce_kurt_z, gyro_max_x, gyro_max_y, gyro_max_z, acce_max_x, acce_max_y, acce_max_z, gyro_min_x, gyro_min_y, gyro_min_z, acce_min_x, acce_min_y, acce_min_z, gyro_range_x, gyro_range_y, gyro_range_z, acce_range_x, acce_range_y, acce_range_z, gyro_rms_x, gyro_rms_y, gyro_rms_z, acce_rms_x, acce_rms_y, acce_rms_z, gyro_energy_x, gyro_energy_y, gyro_energy_z, acce_energy_x, acce_energy_y, acce_energy_z, gyro_corr_xy, gyro_corr_xz, gyro_corr_yz, acce_corr_xy, acce_corr_xz, acce_corr_yz):
    if gyro_std_x <= 4.04:
        if gyro_variance_z <= 7.23:
            if gyro_mean_z <= 8.72:
                return [ 1, 72,  4,]
            else:  # if gyro_mean_z > 8.72
                return [ 1,  5, 18,]
        else:  # if gyro_variance_z > 7.23
            if gyro_skew_y <= -0.87:
                return [ 1, 46,  7,]
            else:  # if gyro_skew_y > -0.87
                if gyro_rms_y <= 4.41:
                    return [ 0, 13,  9,]
                else:  # if gyro_rms_y > 4.41
                    if gyro_kurt_x <= -1.24:
                        return [207,   0,   0,]
                    else:  # if gyro_kurt_x > -1.24
                        return [17, 16, 29,]
    else:  # if gyro_std_x > 4.04
        if gyro_variance_y <= 16.68:
            if acce_energy_x <= 61.89:
                if acce_kurt_z <= -0.7:
                    return [ 4, 29,  7,]
                else:  # if acce_kurt_z > -0.7
                    return [ 0, 10, 45,]
            else:  # if acce_energy_x > 61.89
                return [ 3, 55,  2,]
        else:  # if gyro_variance_y > 16.68
            return [  0,  18, 100,]

def decision_tree_4(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z, gyro_skew_x, gyro_skew_y, gyro_skew_z, acce_skew_x, acce_skew_y, acce_skew_z, gyro_kurt_x, gyro_kurt_y, gyro_kurt_z, acce_kurt_x, acce_kurt_y, acce_kurt_z, gyro_max_x, gyro_max_y, gyro_max_z, acce_max_x, acce_max_y, acce_max_z, gyro_min_x, gyro_min_y, gyro_min_z, acce_min_x, acce_min_y, acce_min_z, gyro_range_x, gyro_range_y, gyro_range_z, acce_range_x, acce_range_y, acce_range_z, gyro_rms_x, gyro_rms_y, gyro_rms_z, acce_rms_x, acce_rms_y, acce_rms_z, gyro_energy_x, gyro_energy_y, gyro_energy_z, acce_energy_x, acce_energy_y, acce_energy_z, gyro_corr_xy, gyro_corr_xz, gyro_corr_yz, acce_corr_xy, acce_corr_xz, acce_corr_yz):
    if n_samples <= 14.5:
        if n_samples <= 10.5:
            if gyro_mean_z <= 3.27:
                if gyro_skew_y <= 0.46:
                    return [ 2, 17,  0,]
                else:  # if gyro_skew_y > 0.46
                    return [0, 3, 9,]
            else:  # if gyro_mean_z > 3.27
                return [  1,  13, 181,]
        else:  # if n_samples > 10.5
            if gyro_kurt_x <= -1.5:
                if acce_rms_x <= 0.8:
                    if gyro_energy_z <= 704.9:
                        return [25,  0,  0,]
                    else:  # if gyro_energy_z > 704.9
                        return [0, 6, 1,]
                else:  # if acce_rms_x > 0.8
                    if gyro_range_y <= 9.02:
                        return [ 0, 25,  1,]
                    else:  # if gyro_range_y > 9.02
                        return [ 2, 34, 31,]
            else:  # if gyro_kurt_x > -1.5
                return [  5, 154,  12,]
    else:  # if n_samples > 14.5
        if gyro_mean_y <= 6.4:
            return [178,   4,   0,]
        else:  # if gyro_mean_y > 6.4
            return [ 1, 14,  0,]

def decision_tree_5(gyro_std_y, acce_skew_x, gyro_kurt_y, gyro_kurt_z,
                    acce_max_x, acce_rms_x, acce_energy_x, gyro_corr_xz):
    if gyro_std_y <= 3.93:
        if gyro_kurt_z <= -0.68:
            if acce_max_x <= 0.97:
                if gyro_std_y <= 2.81:
                    return [2, 9, 4,]
                else:  # if gyro_std_y > 2.81
                    return [155,   3,   1,]
            else:  # if acce_max_x > 0.97
                if gyro_corr_xz <= -0.19:
                    return [ 0, 34, 27,]
                else:  # if gyro_corr_xz > -0.19
                    if gyro_kurt_y <= -1.05:
                        return [75,  1,  1,]
                    else:  # if gyro_kurt_y > -1.05
                        if acce_rms_x <= 2.52:
                            return [ 0,  5, 25,]
                        else:  # if acce_rms_x > 2.52
                            return [ 0, 13,  1,]
        else:  # if gyro_kurt_z > -0.68
            return [  5, 142,  20,]
    else:  # if gyro_std_y > 3.93
        if acce_skew_x <= -0.9:
            return [ 0, 14,  0,]
        else:  # if acce_skew_x > -0.9
            if acce_energy_x <= 0.76:
                return [ 0, 10,  0,]
            else:  # if acce_energy_x > 0.76
                return [  0,  10, 162,]

def decision_tree_6(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z, gyro_skew_x, gyro_skew_y, gyro_skew_z, acce_skew_x, acce_skew_y, acce_skew_z, gyro_kurt_x, gyro_kurt_y, gyro_kurt_z, acce_kurt_x, acce_kurt_y, acce_kurt_z, gyro_max_x, gyro_max_y, gyro_max_z, acce_max_x, acce_max_y, acce_max_z, gyro_min_x, gyro_min_y, gyro_min_z, acce_min_x, acce_min_y, acce_min_z, gyro_range_x, gyro_range_y, gyro_range_z, acce_range_x, acce_range_y, acce_range_z, gyro_rms_x, gyro_rms_y, gyro_rms_z, acce_rms_x, acce_rms_y, acce_rms_z, gyro_energy_x, gyro_energy_y, gyro_energy_z, acce_energy_x, acce_energy_y, acce_energy_z, gyro_corr_xy, gyro_corr_xz, gyro_corr_yz, acce_corr_xy, acce_corr_xz, acce_corr_yz):
    if gyro_kurt_z <= -0.68:
        if gyro_std_y <= 3.83:
            if gyro_std_z <= 3.94:
                if gyro_rms_z <= 7.3:
                    return [246,   5,   0,]
                else:  # if gyro_rms_z > 7.3
                    return [ 2, 17, 11,]
            else:  # if gyro_std_z > 3.94
                return [ 1, 26, 25,]
        else:  # if gyro_std_y > 3.83
            if n_samples <= 11.5:
                return [ 1, 12, 69,]
            else:  # if n_samples > 11.5
                return [ 4, 19,  0,]
    else:  # if gyro_kurt_z > -0.68
        if gyro_skew_z <= 1.18:
            if gyro_skew_y <= -1.36:
                return [ 0, 52,  3,]
            else:  # if gyro_skew_y > -1.36
                if acce_variance_x <= 0.01:
                    return [ 0, 17,  0,]
                else:  # if acce_variance_x > 0.01
                    if gyro_rms_x <= 8.09:
                        return [ 3, 18, 97,]
                    else:  # if gyro_rms_x > 8.09
                        return [0, 9, 0,]
        else:  # if gyro_skew_z > 1.18
            return [ 0, 79,  3,]

def decision_tree_7(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z, gyro_skew_x, gyro_skew_y, gyro_skew_z, acce_skew_x, acce_skew_y, acce_skew_z, gyro_kurt_x, gyro_kurt_y, gyro_kurt_z, acce_kurt_x, acce_kurt_y, acce_kurt_z, gyro_max_x, gyro_max_y, gyro_max_z, acce_max_x, acce_max_y, acce_max_z, gyro_min_x, gyro_min_y, gyro_min_z, acce_min_x, acce_min_y, acce_min_z, gyro_range_x, gyro_range_y, gyro_range_z, acce_range_x, acce_range_y, acce_range_z, gyro_rms_x, gyro_rms_y, gyro_rms_z, acce_rms_x, acce_rms_y, acce_rms_z, gyro_energy_x, gyro_energy_y, gyro_energy_z, acce_energy_x, acce_energy_y, acce_energy_z, gyro_corr_xy, gyro_corr_xz, gyro_corr_yz, acce_corr_xy, acce_corr_xz, acce_corr_yz):
    if gyro_std_y <= 3.95:
        if n_samples <= 14.5:
            if acce_range_x <= 3.91:
                if acce_range_x <= 0.27:
                    return [ 2, 38,  0,]
                else:  # if acce_range_x > 0.27
                    if gyro_kurt_y <= -1.33:
                        return [27,  5,  1,]
                    else:  # if gyro_kurt_y > -1.33
                        if n_samples <= 9.5:
                            return [ 0,  3, 23,]
                        else:  # if n_samples > 9.5
                            return [ 2, 63, 27,]
            else:  # if acce_range_x > 3.91
                return [  1, 101,   7,]
        else:  # if n_samples > 14.5
            if gyro_mean_z <= 6.43:
                return [205,   1,   0,]
            else:  # if gyro_mean_z > 6.43
                return [ 1, 14,  0,]
    else:  # if gyro_std_y > 3.95
        if acce_min_z <= 0.96:
            if acce_variance_x <= 0.02:
                return [2, 5, 0,]
            else:  # if acce_variance_x > 0.02
                return [  0,  15, 159,]
        else:  # if acce_min_z > 0.96
            return [ 0, 15,  2,]

def decision_tree_8(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z, gyro_skew_x, gyro_skew_y, gyro_skew_z, acce_skew_x, acce_skew_y, acce_skew_z, gyro_kurt_x, gyro_kurt_y, gyro_kurt_z, acce_kurt_x, acce_kurt_y, acce_kurt_z, gyro_max_x, gyro_max_y, gyro_max_z, acce_max_x, acce_max_y, acce_max_z, gyro_min_x, gyro_min_y, gyro_min_z, acce_min_x, acce_min_y, acce_min_z, gyro_range_x, gyro_range_y, gyro_range_z, acce_range_x, acce_range_y, acce_range_z, gyro_rms_x, gyro_rms_y, gyro_rms_z, acce_rms_x, acce_rms_y, acce_rms_z, gyro_energy_x, gyro_energy_y, gyro_energy_z, acce_energy_x, acce_energy_y, acce_energy_z, gyro_corr_xy, gyro_corr_xz, gyro_corr_yz, acce_corr_xy, acce_corr_xz, acce_corr_yz):
    if gyro_std_x <= 4.09:
        if n_samples <= 14.5:
            if gyro_rms_y <= 7.11:
                if n_samples <= 11.5:
                    if gyro_kurt_x <= -1.61:
                        return [8, 0, 0,]
                    else:  # if gyro_kurt_x > -1.61
                        return [ 1, 19, 57,]
                else:  # if n_samples > 11.5
                    if gyro_rms_x <= 7.07:
                        if gyro_mean_x <= 3.11:
                            return [0, 7, 1,]
                        else:  # if gyro_mean_x > 3.11
                            return [26,  0,  0,]
                    else:  # if gyro_rms_x > 7.07
                        return [ 2, 30,  0,]
            else:  # if gyro_rms_y > 7.11
                return [ 0, 90, 12,]
        else:  # if n_samples > 14.5
            return [175,   6,   0,]
    else:  # if gyro_std_x > 4.09
        if gyro_std_y <= 3.84:
            if acce_min_x <= 0.17:
                return [ 4, 69, 28,]
            else:  # if acce_min_x > 0.17
                return [ 0,  3, 18,]
        else:  # if gyro_std_y > 3.84
            return [  1,  13, 149,]

def decision_tree_9(n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z, gyro_skew_x, gyro_skew_y, gyro_skew_z, acce_skew_x, acce_skew_y, acce_skew_z, gyro_kurt_x, gyro_kurt_y, gyro_kurt_z, acce_kurt_x, acce_kurt_y, acce_kurt_z, gyro_max_x, gyro_max_y, gyro_max_z, acce_max_x, acce_max_y, acce_max_z, gyro_min_x, gyro_min_y, gyro_min_z, acce_min_x, acce_min_y, acce_min_z, gyro_range_x, gyro_range_y, gyro_range_z, acce_range_x, acce_range_y, acce_range_z, gyro_rms_x, gyro_rms_y, gyro_rms_z, acce_rms_x, acce_rms_y, acce_rms_z, gyro_energy_x, gyro_energy_y, gyro_energy_z, acce_energy_x, acce_energy_y, acce_energy_z, gyro_corr_xy, gyro_corr_xz, gyro_corr_yz, acce_corr_xy, acce_corr_xz, acce_corr_yz):
    if gyro_variance_y <= 15.32:
        if acce_min_z <= 0.55:
            if gyro_energy_y <= 283.49:
                return [ 3, 27, 28,]
            else:  # if gyro_energy_y > 283.49
                if gyro_std_x <= 4.17:
                    if gyro_rms_y <= 7.3:
                        return [195,   1,   0,]
                    else:  # if gyro_rms_y > 7.3
                        return [ 0, 19,  0,]
                else:  # if gyro_std_x > 4.17
                    return [ 0, 20,  2,]
        else:  # if acce_min_z > 0.55
            if gyro_kurt_z <= -0.45:
                if acce_min_z <= 0.69:
                    return [27, 19,  2,]
                else:  # if acce_min_z > 0.69
                    return [ 1, 24, 24,]
            else:  # if gyro_kurt_z > -0.45
                return [  0, 102,  17,]
    else:  # if gyro_variance_y > 15.32
        if acce_rms_x <= 0.26:
            return [ 0, 16,  0,]
        else:  # if acce_rms_x > 0.26
            if acce_skew_x <= -0.87:
                return [ 0, 14,  1,]
            else:  # if acce_skew_x > -0.87
                return [  1,  14, 162,]

