class RandomForestOptimized:    
    def __init__(self):
            pass
    
    def score(self, n_samples, gyro_std_y, acce_min_z, gyro_std_x, gyro_variance_y, gyro_kurt_z, gyro_kurt_y, gyro_skew_y, gyro_variance_z, gyro_kurt_x, gyro_mean_y, gyro_rms_y, acce_energy_x, gyro_energy_y, acce_std_z, acce_max_x, gyro_mean_z, acce_skew_x, acce_rms_x, acce_range_x, gyro_std_z, gyro_rms_z, acce_energy_z, gyro_rms_x, gyro_skew_z, acce_min_x, acce_corr_xz, acce_mean_z, acce_variance_x, gyro_corr_xz, acce_kurt_x):
        self.n_samples = n_samples
        self.gyro_std_y = gyro_std_y
        self.acce_min_z = acce_min_z
        self.gyro_std_x = gyro_std_x
        self.gyro_variance_y = gyro_variance_y
        self.gyro_kurt_z = gyro_kurt_z
        self.gyro_kurt_y = gyro_kurt_y
        self.gyro_skew_y = gyro_skew_y
        self.gyro_variance_z = gyro_variance_z
        self.gyro_kurt_x = gyro_kurt_x
        self.gyro_mean_y = gyro_mean_y
        self.gyro_rms_y = gyro_rms_y
        self.acce_energy_x = acce_energy_x
        self.gyro_energy_y = gyro_energy_y
        self.acce_std_z = acce_std_z
        self.acce_max_x = acce_max_x
        self.gyro_mean_z = gyro_mean_z
        self.acce_skew_x = acce_skew_x
        self.acce_rms_x = acce_rms_x
        self.acce_range_x = acce_range_x
        self.gyro_std_z = gyro_std_z
        self.gyro_rms_z = gyro_rms_z
        self.acce_energy_z = acce_energy_z
        self.gyro_rms_x = gyro_rms_x
        self.gyro_skew_z = gyro_skew_z
        self.acce_min_x = acce_min_x
        self.acce_corr_xz = acce_corr_xz
        self.acce_mean_z = acce_mean_z
        self.acce_variance_x = acce_variance_x
        self.gyro_corr_xz = gyro_corr_xz
        self.acce_kurt_x = acce_kurt_x
    
        v0 = self.decision_tree_0()
        v1 = self.decision_tree_1()
        v2 = self.decision_tree_2()
        v3 = self.decision_tree_3()
        v4 = self.decision_tree_4()
        v5 = self.decision_tree_5()
        v6 = self.decision_tree_6()
        v7 = self.decision_tree_7()
        v8 = self.decision_tree_8()
        v9 = self.decision_tree_9()
    
        trees_values = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9]
    
        return [sum(col) / len(col) for col in zip(*trees_values)]

    def decision_tree_0(self):
        if self.gyro_mean_z <= 6.5:
            if self.gyro_rms_y <= 7.17:
                if self.gyro_std_y <= 4.0:
                    if self.gyro_kurt_y <= -1.12:
                        if self.n_samples <= 10.5:
                            return [2, 8, 1,]
                        else:  # if self.n_samples > 10.5
                            return [315,   3,   0,]
                    else:  # if self.gyro_kurt_y > -1.12
                        if self.gyro_skew_z <= 0.08:
                            return [ 0,  1, 19,]
                        else:  # if self.gyro_skew_z > 0.08
                            return [ 1, 27,  4,]
                else:  # if self.gyro_std_y > 4.0
                    return [ 0, 12, 33,]
            else:  # if self.gyro_rms_y > 7.17
                if self.gyro_kurt_z <= -1.04:
                    if self.gyro_kurt_x <= -1.43:
                        return [ 0,  3, 23,]
                    else:  # if self.gyro_kurt_x > -1.43
                        return [ 0, 17,  3,]
                else:  # if self.gyro_kurt_z > -1.04
                    return [ 0, 68,  1,]
        else:  # if self.gyro_mean_z > 6.5
            if self.acce_energy_z <= 12.22:
                if self.gyro_variance_y <= 11.66:
                    if self.acce_min_z <= 0.81:
                        return [ 0, 33,  4,]
                    else:  # if self.acce_min_z > 0.81
                        if self.gyro_skew_z <= -2.25:
                            return [0, 6, 0,]
                        else:  # if self.gyro_skew_z > -2.25
                            return [ 0,  0, 15,]
                else:  # if self.gyro_variance_y > 11.66
                    if self.acce_range_x <= 0.33:
                        return [0, 9, 0,]
                    else:  # if self.acce_range_x > 0.33
                        return [  0,   7, 145,]
            else:  # if self.acce_energy_z > 12.22
                if self.gyro_rms_z <= 8.77:
                    if self.gyro_std_y <= 3.97:
                        if self.acce_std_z <= 0.71:
                            return [ 1, 66,  0,]
                        else:  # if self.acce_std_z > 0.71
                            return [5, 1, 4,]
                    else:  # if self.gyro_std_y > 3.97
                        if self.acce_kurt_x <= -0.77:
                            if self.gyro_mean_z <= 8.18:
                                return [ 0,  0, 15,]
                            else:  # if self.gyro_mean_z > 8.18
                                return [0, 6, 0,]
                        else:  # if self.acce_kurt_x > -0.77
                            return [ 0, 15,  0,]
                else:  # if self.gyro_rms_z > 8.77
                    if self.gyro_skew_y <= -1.0:
                        return [0, 5, 0,]
                    else:  # if self.gyro_skew_y > -1.0
                        return [ 0,  1, 20,]

    def decision_tree_1(self):
        if self.gyro_variance_y <= 15.5:
            if self.gyro_kurt_y <= -1.31:
                if self.gyro_rms_y <= 7.8:
                    if self.gyro_energy_y <= 339.69:
                        return [1, 4, 2,]
                    else:  # if self.gyro_energy_y > 339.69
                        return [281,   1,   0,]
                else:  # if self.gyro_rms_y > 7.8
                    return [2, 8, 0,]
            else:  # if self.gyro_kurt_y > -1.31
                if self.gyro_std_z <= 2.54:
                    return [  0, 131,  11,]
                else:  # if self.gyro_std_z > 2.54
                    if self.acce_mean_z <= 0.58:
                        if self.gyro_mean_y <= 2.58:
                            return [ 0,  0, 16,]
                        else:  # if self.gyro_mean_y > 2.58
                            return [2, 0, 0,]
                    else:  # if self.acce_mean_z > 0.58
                        if self.acce_corr_xz <= 0.18:
                            if self.gyro_rms_x <= 4.32:
                                return [ 0, 29,  0,]
                            else:  # if self.gyro_rms_x > 4.32
                                if self.acce_range_x <= 3.97:
                                    if self.acce_variance_x <= 0.02:
                                        return [6, 4, 2,]
                                    else:  # if self.acce_variance_x > 0.02
                                        return [ 0,  7, 53,]
                                else:  # if self.acce_range_x > 3.97
                                    if self.acce_energy_z <= 39.16:
                                        return [0, 8, 0,]
                                    else:  # if self.acce_energy_z > 39.16
                                        return [3, 0, 0,]
                        else:  # if self.acce_corr_xz > 0.18
                            if self.acce_energy_z <= 9.6:
                                if self.gyro_energy_y <= 603.65:
                                    return [0, 0, 7,]
                                else:  # if self.gyro_energy_y > 603.65
                                    return [0, 6, 0,]
                            else:  # if self.acce_energy_z > 9.6
                                if self.n_samples <= 17.5:
                                    return [ 1, 66,  0,]
                                else:  # if self.n_samples > 17.5
                                    return [3, 0, 0,]
        else:  # if self.gyro_variance_y > 15.5
            if self.n_samples <= 11.5:
                if self.acce_min_z <= 0.96:
                    if self.acce_variance_x <= 0.02:
                        return [3, 3, 0,]
                    else:  # if self.acce_variance_x > 0.02
                        if self.acce_skew_x <= -1.11:
                            return [0, 2, 0,]
                        else:  # if self.acce_skew_x > -1.11
                            return [  0,   1, 198,]
                else:  # if self.acce_min_z > 0.96
                    return [0, 8, 1,]
            else:  # if self.n_samples > 11.5
                return [ 0, 26,  3,]

    def decision_tree_2(self):
        if self.gyro_variance_z <= 6.43:
            if self.gyro_rms_z <= 8.65:
                if self.gyro_kurt_z <= -1.87:
                    return [3, 0, 0,]
                else:  # if self.gyro_kurt_z > -1.87
                    if self.acce_min_z <= 0.08:
                        return [0, 0, 2,]
                    else:  # if self.acce_min_z > 0.08
                        return [  0, 147,   9,]
            else:  # if self.gyro_rms_z > 8.65
                if self.gyro_std_y <= 3.45:
                    return [ 1, 17,  3,]
                else:  # if self.gyro_std_y > 3.45
                    return [ 0,  1, 64,]
        else:  # if self.gyro_variance_z > 6.43
            if self.acce_max_x <= 0.97:
                if self.acce_max_x <= 0.51:
                    if self.gyro_rms_y <= 6.41:
                        return [0, 0, 2,]
                    else:  # if self.gyro_rms_y > 6.41
                        return [ 0, 15,  0,]
                else:  # if self.acce_max_x > 0.51
                    if self.gyro_std_y <= 2.8:
                        if self.gyro_rms_x <= 7.25:
                            return [0, 5, 0,]
                        else:  # if self.gyro_rms_x > 7.25
                            return [0, 1, 6,]
                    else:  # if self.gyro_std_y > 2.8
                        if self.gyro_kurt_y <= -0.88:
                            if self.acce_min_z <= 0.68:
                                return [211,   1,   0,]
                            else:  # if self.acce_min_z > 0.68
                                return [0, 0, 5,]
                        else:  # if self.gyro_kurt_y > -0.88
                            return [0, 6, 0,]
            else:  # if self.acce_max_x > 0.97
                if self.gyro_energy_y <= 579.21:
                    if self.acce_corr_xz <= 0.59:
                        if self.gyro_skew_z <= 0.0:
                            return [  4,   1, 173,]
                        else:  # if self.gyro_skew_z > 0.0
                            if self.n_samples <= 14.5:
                                if self.acce_corr_xz <= 0.29:
                                    if self.gyro_rms_x <= 1.73:
                                        return [0, 4, 0,]
                                    else:  # if self.gyro_rms_x > 1.73
                                        return [ 0,  1, 27,]
                                else:  # if self.acce_corr_xz > 0.29
                                    return [ 0, 11,  0,]
                            else:  # if self.n_samples > 14.5
                                return [11,  0,  0,]
                    else:  # if self.acce_corr_xz > 0.59
                        return [ 3, 30,  4,]
                else:  # if self.gyro_energy_y > 579.21
                    if self.gyro_kurt_y <= -1.11:
                        return [83,  1,  0,]
                    else:  # if self.gyro_kurt_y > -1.11
                        return [ 0, 41,  6,]

    def decision_tree_3(self):
        if self.gyro_skew_y <= -1.37:
            if self.n_samples <= 8.5:
                return [0, 0, 5,]
            else:  # if self.n_samples > 8.5
                return [  0, 141,   6,]
        else:  # if self.gyro_skew_y > -1.37
            if self.acce_min_z <= 0.69:
                if self.n_samples <= 13.5:
                    if self.acce_variance_x <= 0.02:
                        if self.gyro_skew_y <= 0.45:
                            if self.acce_energy_z <= 6.29:
                                return [1, 4, 0,]
                            else:  # if self.acce_energy_z > 6.29
                                return [22,  0,  0,]
                        else:  # if self.gyro_skew_y > 0.45
                            return [ 0, 15,  1,]
                    else:  # if self.acce_variance_x > 0.02
                        if self.acce_mean_z <= 0.85:
                            if self.acce_energy_x <= 35.4:
                                return [ 1,  0, 37,]
                            else:  # if self.acce_energy_x > 35.4
                                return [0, 3, 0,]
                        else:  # if self.acce_mean_z > 0.85
                            if self.gyro_variance_z <= 14.16:
                                if self.acce_min_x <= 0.32:
                                    return [ 4, 33,  0,]
                                else:  # if self.acce_min_x > 0.32
                                    return [0, 0, 5,]
                            else:  # if self.gyro_variance_z > 14.16
                                return [ 0,  8, 18,]
                else:  # if self.n_samples > 13.5
                    if self.gyro_skew_y <= 0.93:
                        if self.gyro_std_z <= 2.5:
                            return [0, 2, 0,]
                        else:  # if self.gyro_std_z > 2.5
                            return [233,   1,   0,]
                    else:  # if self.gyro_skew_y > 0.93
                        return [0, 3, 0,]
            else:  # if self.acce_min_z > 0.69
                if self.gyro_skew_z <= 0.07:
                    if self.gyro_kurt_z <= 5.42:
                        if self.acce_variance_x <= 0.0:
                            return [ 1, 15,  1,]
                        else:  # if self.acce_variance_x > 0.0
                            if self.acce_variance_x <= 3.4:
                                return [  0,   7, 221,]
                            else:  # if self.acce_variance_x > 3.4
                                return [ 0, 11,  4,]
                    else:  # if self.gyro_kurt_z > 5.42
                        return [ 0, 16,  2,]
                else:  # if self.gyro_skew_z > 0.07
                    if self.acce_corr_xz <= 0.42:
                        if self.acce_energy_z <= 10.48:
                            return [ 0,  2, 16,]
                        else:  # if self.acce_energy_z > 10.48
                            return [ 1, 19,  6,]
                    else:  # if self.acce_corr_xz > 0.42
                        return [ 0, 33,  1,]

    def decision_tree_4(self):
        if self.n_samples <= 14.5:
            if self.gyro_skew_y <= -1.15:
                return [  0, 144,  13,]
            else:  # if self.gyro_skew_y > -1.15
                if self.gyro_variance_y <= 15.67:
                    if self.gyro_kurt_y <= -1.35:
                        if self.gyro_variance_z <= 12.82:
                            if self.acce_energy_x <= 11.47:
                                return [40,  2,  0,]
                            else:  # if self.acce_energy_x > 11.47
                                return [2, 4, 0,]
                        else:  # if self.gyro_variance_z > 12.82
                            return [0, 6, 2,]
                    else:  # if self.gyro_kurt_y > -1.35
                        if self.acce_min_z <= 0.3:
                            if self.acce_range_x <= 0.44:
                                return [1, 5, 0,]
                            else:  # if self.acce_range_x > 0.44
                                return [ 0,  1, 38,]
                        else:  # if self.acce_min_z > 0.3
                            if self.acce_corr_xz <= 0.38:
                                if self.acce_energy_x <= 85.24:
                                    if self.gyro_kurt_x <= -1.47:
                                        if self.n_samples <= 10.5:
                                            return [ 0,  0, 24,]
                                        else:  # if self.n_samples > 10.5
                                            if self.acce_min_z <= 0.83:
                                                return [0, 5, 0,]
                                            else:  # if self.acce_min_z > 0.83
                                                return [0, 0, 4,]
                                    else:  # if self.gyro_kurt_x > -1.47
                                        if self.acce_rms_x <= 1.77:
                                            return [ 0, 17,  5,]
                                        else:  # if self.acce_rms_x > 1.77
                                            return [0, 0, 6,]
                                else:  # if self.acce_energy_x > 85.24
                                    return [ 0, 13,  1,]
                            else:  # if self.acce_corr_xz > 0.38
                                return [ 0, 50,  2,]
                else:  # if self.gyro_variance_y > 15.67
                    if self.n_samples <= 11.5:
                        if self.gyro_std_x <= 2.75:
                            return [2, 4, 4,]
                        else:  # if self.gyro_std_x > 2.75
                            return [  0,   5, 210,]
                    else:  # if self.n_samples > 11.5
                        if self.gyro_mean_z <= 8.73:
                            return [ 0, 26,  2,]
                        else:  # if self.gyro_mean_z > 8.73
                            return [0, 0, 3,]
        else:  # if self.n_samples > 14.5
            if self.gyro_kurt_y <= -1.02:
                if self.gyro_rms_x <= 8.37:
                    return [234,   0,   0,]
                else:  # if self.gyro_rms_x > 8.37
                    return [0, 2, 0,]
            else:  # if self.gyro_kurt_y > -1.02
                return [ 2, 20,  0,]

    def decision_tree_5(self):
        if self.acce_max_x <= 0.97:
            if self.gyro_skew_y <= -0.81:
                return [ 1, 49,  0,]
            else:  # if self.gyro_skew_y > -0.81
                if self.n_samples <= 12.5:
                    if self.acce_corr_xz <= -0.57:
                        if self.gyro_std_z <= 2.74:
                            return [ 2, 15,  0,]
                        else:  # if self.gyro_std_z > 2.74
                            return [5, 1, 0,]
                    else:  # if self.acce_corr_xz > -0.57
                        if self.gyro_energy_y <= 335.12:
                            return [ 2,  0, 19,]
                        else:  # if self.gyro_energy_y > 335.12
                            if self.acce_min_x <= 0.29:
                                return [0, 5, 0,]
                            else:  # if self.acce_min_x > 0.29
                                return [7, 0, 0,]
                else:  # if self.n_samples > 12.5
                    if self.gyro_std_z <= 2.57:
                        return [0, 5, 0,]
                    else:  # if self.gyro_std_z > 2.57
                        if self.acce_min_x <= 0.77:
                            return [187,   0,   0,]
                        else:  # if self.acce_min_x > 0.77
                            return [0, 3, 0,]
        else:  # if self.acce_max_x > 0.97
            if self.gyro_variance_y <= 14.48:
                if self.n_samples <= 16.5:
                    if self.acce_corr_xz <= 0.25:
                        if self.gyro_energy_y <= 622.5:
                            if self.acce_range_x <= 0.46:
                                return [0, 4, 0,]
                            else:  # if self.acce_range_x > 0.46
                                return [ 2,  2, 45,]
                        else:  # if self.gyro_energy_y > 622.5
                            return [ 0, 34,  6,]
                    else:  # if self.acce_corr_xz > 0.25
                        return [  5, 125,   6,]
                else:  # if self.n_samples > 16.5
                    if self.acce_skew_x <= -0.9:
                        return [0, 3, 0,]
                    else:  # if self.acce_skew_x > -0.9
                        return [82,  0,  0,]
            else:  # if self.gyro_variance_y > 14.48
                if self.acce_skew_x <= -0.91:
                    return [ 0, 13,  0,]
                else:  # if self.acce_skew_x > -0.91
                    if self.gyro_std_x <= 3.47:
                        return [ 0, 12,  3,]
                    else:  # if self.gyro_std_x > 3.47
                        if self.acce_kurt_x <= 4.93:
                            if self.gyro_skew_z <= -2.95:
                                return [0, 7, 0,]
                            else:  # if self.gyro_skew_z > -2.95
                                return [  2,   9, 229,]
                        else:  # if self.acce_kurt_x > 4.93
                            return [2, 6, 1,]

    def decision_tree_6(self):
        if self.n_samples <= 14.5:
            if self.gyro_std_x <= 4.13:
                if self.acce_min_z <= 0.3:
                    if self.acce_max_x <= 0.88:
                        return [30,  0,  0,]
                    else:  # if self.acce_max_x > 0.88
                        if self.acce_max_x <= 1.14:
                            return [ 2, 21,  0,]
                        else:  # if self.acce_max_x > 1.14
                            return [ 1,  9, 11,]
                else:  # if self.acce_min_z > 0.3
                    if self.gyro_skew_y <= -0.57:
                        if self.gyro_std_z <= 3.95:
                            return [ 0, 93,  3,]
                        else:  # if self.gyro_std_z > 3.95
                            return [0, 2, 5,]
                    else:  # if self.gyro_skew_y > -0.57
                        if self.n_samples <= 11.5:
                            if self.acce_kurt_x <= -0.23:
                                if self.acce_variance_x <= 0.03:
                                    return [3, 6, 1,]
                                else:  # if self.acce_variance_x > 0.03
                                    return [ 0,  5, 55,]
                            else:  # if self.acce_kurt_x > -0.23
                                if self.gyro_kurt_y <= -1.64:
                                    return [ 0,  1, 12,]
                                else:  # if self.gyro_kurt_y > -1.64
                                    return [ 0, 15,  0,]
                        else:  # if self.n_samples > 11.5
                            return [ 0, 55,  2,]
            else:  # if self.gyro_std_x > 4.13
                if self.acce_energy_x <= 92.75:
                    if self.gyro_skew_y <= -1.38:
                        return [ 0, 26,  6,]
                    else:  # if self.gyro_skew_y > -1.38
                        if self.n_samples <= 11.5:
                            if self.acce_kurt_x <= 4.76:
                                return [  0,   2, 179,]
                            else:  # if self.acce_kurt_x > 4.76
                                return [0, 8, 0,]
                        else:  # if self.n_samples > 11.5
                            if self.acce_corr_xz <= -0.01:
                                return [ 0,  1, 11,]
                            else:  # if self.acce_corr_xz > -0.01
                                return [ 0, 18,  0,]
                else:  # if self.acce_energy_x > 92.75
                    if self.gyro_kurt_z <= -1.99:
                        return [0, 0, 3,]
                    else:  # if self.gyro_kurt_z > -1.99
                        return [ 0, 34,  0,]
        else:  # if self.n_samples > 14.5
            if self.gyro_skew_z <= -1.33:
                return [ 2, 12,  0,]
            else:  # if self.gyro_skew_z > -1.33
                if self.gyro_corr_xz <= -0.45:
                    return [0, 3, 0,]
                else:  # if self.gyro_corr_xz > -0.45
                    return [258,   4,   0,]

    def decision_tree_7(self):
        if self.gyro_kurt_y <= -0.97:
            if self.acce_rms_x <= 0.9:
                if self.acce_max_x <= 0.54:
                    return [ 0, 13,  1,]
                else:  # if self.acce_max_x > 0.54
                    if self.gyro_variance_y <= 4.85:
                        return [0, 5, 2,]
                    else:  # if self.gyro_variance_y > 4.85
                        if self.gyro_energy_y <= 268.47:
                            return [0, 0, 2,]
                        else:  # if self.gyro_energy_y > 268.47
                            return [204,   1,   0,]
            else:  # if self.acce_rms_x > 0.9
                if self.n_samples <= 15.5:
                    if self.n_samples <= 11.5:
                        if self.acce_variance_x <= 3.53:
                            if self.gyro_variance_y <= 15.52:
                                if self.acce_min_x <= 0.04:
                                    return [0, 9, 0,]
                                else:  # if self.acce_min_x > 0.04
                                    return [0, 0, 9,]
                            else:  # if self.gyro_variance_y > 15.52
                                return [  0,   4, 175,]
                        else:  # if self.acce_variance_x > 3.53
                            return [0, 4, 2,]
                    else:  # if self.n_samples > 11.5
                        if self.acce_corr_xz <= 0.03:
                            return [0, 1, 4,]
                        else:  # if self.acce_corr_xz > 0.03
                            return [ 2, 22,  0,]
                else:  # if self.n_samples > 15.5
                    return [90,  0,  0,]
        else:  # if self.gyro_kurt_y > -0.97
            if self.gyro_skew_y <= -1.36:
                if self.gyro_energy_y <= 513.57:
                    return [0, 0, 7,]
                else:  # if self.gyro_energy_y > 513.57
                    if self.gyro_kurt_z <= -1.83:
                        return [0, 0, 3,]
                    else:  # if self.gyro_kurt_z > -1.83
                        return [  0, 151,   4,]
            else:  # if self.gyro_skew_y > -1.36
                if self.acce_energy_x <= 78.13:
                    if self.gyro_kurt_x <= -1.48:
                        if self.acce_max_x <= 1.06:
                            return [ 0, 13,  4,]
                        else:  # if self.acce_max_x > 1.06
                            if self.n_samples <= 11.5:
                                return [ 0,  1, 66,]
                            else:  # if self.n_samples > 11.5
                                return [1, 5, 2,]
                    else:  # if self.gyro_kurt_x > -1.48
                        if self.acce_min_z <= 0.13:
                            return [ 0,  0, 10,]
                        else:  # if self.acce_min_z > 0.13
                            return [ 0, 38,  7,]
                else:  # if self.acce_energy_x > 78.13
                    return [ 1, 35,  1,]

    def decision_tree_8(self):
        if self.acce_min_z <= 0.68:
            if self.gyro_kurt_y <= -1.28:
                if self.gyro_energy_y <= 336.83:
                    return [ 1,  6, 16,]
                else:  # if self.gyro_energy_y > 336.83
                    if self.gyro_std_z <= 2.57:
                        if self.gyro_std_z <= 0.36:
                            return [0, 0, 4,]
                        else:  # if self.gyro_std_z > 0.36
                            return [0, 6, 0,]
                    else:  # if self.gyro_std_z > 2.57
                        return [287,   3,   4,]
            else:  # if self.gyro_kurt_y > -1.28
                if self.acce_min_x <= 0.22:
                    if self.acce_energy_x <= 137.23:
                        return [ 2, 80,  1,]
                    else:  # if self.acce_energy_x > 137.23
                        return [3, 0, 0,]
                else:  # if self.acce_min_x > 0.22
                    if self.acce_skew_x <= 0.17:
                        return [ 1, 16,  0,]
                    else:  # if self.acce_skew_x > 0.17
                        if self.gyro_std_z <= 2.41:
                            return [0, 7, 2,]
                        else:  # if self.gyro_std_z > 2.41
                            if self.acce_variance_x <= 0.01:
                                return [0, 2, 0,]
                            else:  # if self.acce_variance_x > 0.01
                                if self.acce_corr_xz <= -0.81:
                                    return [2, 0, 0,]
                                else:  # if self.acce_corr_xz > -0.81
                                    return [ 0,  0, 37,]
        else:  # if self.acce_min_z > 0.68
            if self.acce_energy_z <= 12.25:
                if self.gyro_rms_z <= 4.27:
                    return [ 0, 16,  0,]
                else:  # if self.gyro_rms_z > 4.27
                    if self.acce_range_x <= 0.36:
                        return [ 0, 17,  1,]
                    else:  # if self.acce_range_x > 0.36
                        return [  0,   9, 210,]
            else:  # if self.acce_energy_z > 12.25
                if self.gyro_mean_z <= 8.77:
                    if self.gyro_kurt_x <= -1.67:
                        if self.gyro_variance_y <= 18.91:
                            if self.gyro_std_x <= 4.21:
                                return [2, 0, 1,]
                            else:  # if self.gyro_std_x > 4.21
                                return [ 0, 33,  2,]
                        else:  # if self.gyro_variance_y > 18.91
                            return [ 0,  2, 11,]
                    else:  # if self.gyro_kurt_x > -1.67
                        if self.gyro_variance_z <= 19.58:
                            return [ 2, 91,  1,]
                        else:  # if self.gyro_variance_z > 19.58
                            return [0, 0, 2,]
                else:  # if self.gyro_mean_z > 8.77
                    return [ 0,  1, 18,]

    def decision_tree_9(self):
        if self.gyro_variance_y <= 15.63:
            if self.gyro_kurt_y <= -1.24:
                if self.gyro_std_y <= 1.77:
                    return [0, 7, 1,]
                else:  # if self.gyro_std_y > 1.77
                    if self.gyro_corr_xz <= -0.3:
                        return [0, 2, 0,]
                    else:  # if self.gyro_corr_xz > -0.3
                        return [292,   0,   1,]
            else:  # if self.gyro_kurt_y > -1.24
                if self.gyro_energy_y <= 167.98:
                    if self.gyro_rms_y <= 3.72:
                        if self.gyro_std_z <= 3.61:
                            if self.gyro_variance_z <= 0.04:
                                return [0, 0, 4,]
                            else:  # if self.gyro_variance_z > 0.04
                                return [ 0, 46,  6,]
                        else:  # if self.gyro_std_z > 3.61
                            if self.gyro_energy_y <= 87.7:
                                return [ 0,  1, 17,]
                            else:  # if self.gyro_energy_y > 87.7
                                return [0, 7, 0,]
                    else:  # if self.gyro_rms_y > 3.72
                        return [ 0,  4, 31,]
                else:  # if self.gyro_energy_y > 167.98
                    if self.acce_energy_z <= 10.02:
                        if self.acce_variance_x <= 0.07:
                            return [ 2, 26,  3,]
                        else:  # if self.acce_variance_x > 0.07
                            if self.acce_energy_z <= 5.39:
                                return [1, 3, 0,]
                            else:  # if self.acce_energy_z > 5.39
                                return [ 0,  0, 13,]
                    else:  # if self.acce_energy_z > 10.02
                        if self.n_samples <= 19.0:
                            return [  0, 176,  11,]
                        else:  # if self.n_samples > 19.0
                            return [3, 0, 0,]
        else:  # if self.gyro_variance_y > 15.63
            if self.acce_min_z <= 0.95:
                if self.gyro_rms_z <= 5.18:
                    if self.acce_mean_z <= 0.98:
                        return [0, 0, 4,]
                    else:  # if self.acce_mean_z > 0.98
                        return [0, 9, 0,]
                else:  # if self.gyro_rms_z > 5.18
                    if self.acce_kurt_x <= 5.49:
                        if self.acce_variance_x <= 0.02:
                            return [0, 5, 2,]
                        else:  # if self.acce_variance_x > 0.02
                            if self.n_samples <= 12.0:
                                return [  0,   1, 189,]
                            else:  # if self.n_samples > 12.0
                                return [0, 6, 0,]
                    else:  # if self.acce_kurt_x > 5.49
                        return [0, 5, 1,]
            else:  # if self.acce_min_z > 0.95
                return [ 0, 15,  5,]

