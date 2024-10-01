class RandomForestOptimized:    
    def __init__(self):
            pass
    
    def score(self, n_samples, gyro_std_y, gyro_energy_y, gyro_kurt_y, gyro_variance_y, acce_min_z, gyro_kurt_z, gyro_rms_y, gyro_std_x, gyro_skew_y, gyro_kurt_x, gyro_skew_z, gyro_mean_z, gyro_rms_z, gyro_variance_z, acce_energy_x, gyro_mean_y, acce_range_x, acce_mean_z, acce_rms_x, acce_std_z, gyro_energy_x, acce_corr_xz, gyro_corr_xy, gyro_variance_x, acce_variance_x, acce_skew_x, acce_rms_y, acce_std_x, acce_max_x, acce_energy_z, gyro_std_z, gyro_energy_z, acce_variance_z, acce_min_x, acce_rms_z, acce_kurt_x, acce_mean_y, gyro_rms_x, acce_energy_y, acce_skew_z):
        self.n_samples = n_samples
        self.gyro_std_y = gyro_std_y
        self.gyro_energy_y = gyro_energy_y
        self.gyro_kurt_y = gyro_kurt_y
        self.gyro_variance_y = gyro_variance_y
        self.acce_min_z = acce_min_z
        self.gyro_kurt_z = gyro_kurt_z
        self.gyro_rms_y = gyro_rms_y
        self.gyro_std_x = gyro_std_x
        self.gyro_skew_y = gyro_skew_y
        self.gyro_kurt_x = gyro_kurt_x
        self.gyro_skew_z = gyro_skew_z
        self.gyro_mean_z = gyro_mean_z
        self.gyro_rms_z = gyro_rms_z
        self.gyro_variance_z = gyro_variance_z
        self.acce_energy_x = acce_energy_x
        self.gyro_mean_y = gyro_mean_y
        self.acce_range_x = acce_range_x
        self.acce_mean_z = acce_mean_z
        self.acce_rms_x = acce_rms_x
        self.acce_std_z = acce_std_z
        self.gyro_energy_x = gyro_energy_x
        self.acce_corr_xz = acce_corr_xz
        self.gyro_corr_xy = gyro_corr_xy
        self.gyro_variance_x = gyro_variance_x
        self.acce_variance_x = acce_variance_x
        self.acce_skew_x = acce_skew_x
        self.acce_rms_y = acce_rms_y
        self.acce_std_x = acce_std_x
        self.acce_max_x = acce_max_x
        self.acce_energy_z = acce_energy_z
        self.gyro_std_z = gyro_std_z
        self.gyro_energy_z = gyro_energy_z
        self.acce_variance_z = acce_variance_z
        self.acce_min_x = acce_min_x
        self.acce_rms_z = acce_rms_z
        self.acce_kurt_x = acce_kurt_x
        self.acce_mean_y = acce_mean_y
        self.gyro_rms_x = gyro_rms_x
        self.acce_energy_y = acce_energy_y
        self.acce_skew_z = acce_skew_z
    
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
        v10 = self.decision_tree_10()
        v11 = self.decision_tree_11()
        v12 = self.decision_tree_12()
        v13 = self.decision_tree_13()
        v14 = self.decision_tree_14()
        v15 = self.decision_tree_15()
        v16 = self.decision_tree_16()
        v17 = self.decision_tree_17()
        v18 = self.decision_tree_18()
        v19 = self.decision_tree_19()
        v20 = self.decision_tree_20()
        v21 = self.decision_tree_21()
    
        trees_values = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21]
    
        return [sum(col) / len(col) for col in zip(*trees_values)]

    def decision_tree_0(self):
        if self.n_samples <= 14.5:
            if self.gyro_variance_y <= 15.63:
                if self.acce_variance_z <= 0.08:
                    if self.acce_energy_z <= 10.09:
                        if self.gyro_variance_x <= 14.72:
                            return [ 0, 24,  2,]
                        else:  # if self.gyro_variance_x > 14.72
                            if self.acce_corr_xz <= -0.5:
                                return [2, 1, 0,]
                            else:  # if self.acce_corr_xz > -0.5
                                return [ 0,  1, 31,]
                    else:  # if self.acce_energy_z > 10.09
                        if self.gyro_std_y <= 0.19:
                            return [0, 0, 5,]
                        else:  # if self.gyro_std_y > 0.19
                            return [  0, 154,   6,]
                else:  # if self.acce_variance_z > 0.08
                    if self.gyro_kurt_y <= -1.37:
                        if self.acce_rms_x <= 0.84:
                            return [42,  0,  0,]
                        else:  # if self.acce_rms_x > 0.84
                            return [0, 2, 0,]
                    else:  # if self.gyro_kurt_y > -1.37
                        if self.acce_skew_z <= 0.85:
                            return [ 1, 32,  4,]
                        else:  # if self.acce_skew_z > 0.85
                            if self.acce_variance_x <= 0.02:
                                return [1, 5, 0,]
                            else:  # if self.acce_variance_x > 0.02
                                if self.acce_skew_x <= 2.06:
                                    return [ 0,  2, 36,]
                                else:  # if self.acce_skew_x > 2.06
                                    return [0, 2, 0,]
            else:  # if self.gyro_variance_y > 15.63
                if self.acce_variance_x <= 0.02:
                    return [ 0, 17,  0,]
                else:  # if self.acce_variance_x > 0.02
                    if self.gyro_skew_z <= -0.0:
                        if self.acce_std_x <= 1.87:
                            return [  0,   2, 168,]
                        else:  # if self.acce_std_x > 1.87
                            return [0, 3, 1,]
                    else:  # if self.gyro_skew_z > -0.0
                        if self.acce_min_z <= 0.94:
                            if self.acce_skew_z <= -0.06:
                                if self.acce_min_z <= 0.82:
                                    return [0, 8, 1,]
                                else:  # if self.acce_min_z > 0.82
                                    return [0, 0, 2,]
                            else:  # if self.acce_skew_z > -0.06
                                return [ 0,  4, 31,]
                        else:  # if self.acce_min_z > 0.94
                            return [ 0, 10,  0,]
        else:  # if self.n_samples > 14.5
            if self.gyro_mean_z <= 6.94:
                if self.gyro_kurt_y <= -0.9:
                    return [276,   0,   0,]
                else:  # if self.gyro_kurt_y > -0.9
                    return [0, 6, 0,]
            else:  # if self.gyro_mean_z > 6.94
                return [ 2, 15,  0,]

    def decision_tree_1(self):
        if self.gyro_kurt_y <= -1.1:
            if self.acce_max_x <= 0.99:
                if self.gyro_rms_x <= 7.11:
                    if self.acce_variance_x <= 0.0:
                        return [1, 6, 0,]
                    else:  # if self.acce_variance_x > 0.0
                        return [197,   5,   3,]
                else:  # if self.gyro_rms_x > 7.11
                    if self.gyro_std_z <= 0.1:
                        return [5, 0, 0,]
                    else:  # if self.gyro_std_z > 0.1
                        return [ 3, 14,  1,]
            else:  # if self.acce_max_x > 0.99
                if self.acce_mean_z <= 0.98:
                    if self.acce_std_x <= 0.52:
                        return [0, 3, 9,]
                    else:  # if self.acce_std_x > 0.52
                        if self.acce_std_z <= 0.13:
                            return [2, 0, 7,]
                        else:  # if self.acce_std_z > 0.13
                            if self.gyro_kurt_y <= -1.28:
                                return [79,  0,  1,]
                            else:  # if self.gyro_kurt_y > -1.28
                                return [1, 5, 0,]
                else:  # if self.acce_mean_z > 0.98
                    if self.gyro_variance_y <= 15.46:
                        if self.gyro_rms_z <= 5.45:
                            return [0, 7, 0,]
                        else:  # if self.gyro_rms_z > 5.45
                            return [11,  2,  1,]
                    else:  # if self.gyro_variance_y > 15.46
                        if self.gyro_skew_z <= 0.73:
                            if self.acce_rms_x <= 3.21:
                                if self.acce_min_z <= 0.97:
                                    return [  0,   4, 183,]
                                else:  # if self.acce_min_z > 0.97
                                    return [0, 6, 0,]
                            else:  # if self.acce_rms_x > 3.21
                                return [0, 3, 0,]
                        else:  # if self.gyro_skew_z > 0.73
                            return [0, 9, 0,]
        else:  # if self.gyro_kurt_y > -1.1
            if self.gyro_variance_x <= 13.31:
                return [  1, 119,   4,]
            else:  # if self.gyro_variance_x > 13.31
                if self.gyro_std_z <= 2.49:
                    if self.acce_energy_z <= 9.2:
                        return [0, 1, 7,]
                    else:  # if self.acce_energy_z > 9.2
                        return [ 0, 65,  4,]
                else:  # if self.gyro_std_z > 2.49
                    if self.acce_energy_z <= 11.53:
                        if self.acce_energy_y <= 39.19:
                            return [2, 9, 0,]
                        else:  # if self.acce_energy_y > 39.19
                            return [ 0,  1, 56,]
                    else:  # if self.acce_energy_z > 11.53
                        if self.acce_energy_x <= 13.49:
                            return [ 0,  2, 14,]
                        else:  # if self.acce_energy_x > 13.49
                            return [ 0, 43,  3,]

    def decision_tree_2(self):
        if self.gyro_energy_y <= 497.07:
            if self.gyro_std_y <= 4.08:
                if self.gyro_energy_y <= 324.71:
                    if self.acce_energy_x <= 61.72:
                        if self.acce_range_x <= 0.36:
                            return [ 3, 22,  0,]
                        else:  # if self.acce_range_x > 0.36
                            if self.acce_min_x <= 0.02:
                                if self.acce_rms_x <= 2.12:
                                    return [ 0, 19,  1,]
                                else:  # if self.acce_rms_x > 2.12
                                    return [0, 0, 4,]
                            else:  # if self.acce_min_x > 0.02
                                if self.acce_max_x <= 0.74:
                                    return [0, 5, 1,]
                                else:  # if self.acce_max_x > 0.74
                                    return [ 2,  3, 64,]
                    else:  # if self.acce_energy_x > 61.72
                        return [ 0, 47,  1,]
                else:  # if self.gyro_energy_y > 324.71
                    if self.gyro_mean_y <= 5.8:
                        return [40,  2,  0,]
                    else:  # if self.gyro_mean_y > 5.8
                        return [ 0,  0, 15,]
            else:  # if self.gyro_std_y > 4.08
                if self.acce_energy_x <= 108.54:
                    if self.acce_max_x <= 0.46:
                        return [3, 6, 1,]
                    else:  # if self.acce_max_x > 0.46
                        return [  0,   7, 184,]
                else:  # if self.acce_energy_x > 108.54
                    return [0, 7, 0,]
        else:  # if self.gyro_energy_y > 497.07
            if self.acce_mean_z <= 0.98:
                if self.gyro_rms_y <= 7.16:
                    if self.gyro_kurt_z <= 0.32:
                        return [231,   0,   0,]
                    else:  # if self.gyro_kurt_z > 0.32
                        return [0, 0, 2,]
                else:  # if self.gyro_rms_y > 7.16
                    return [ 0, 36,  1,]
            else:  # if self.acce_mean_z > 0.98
                if self.acce_rms_z <= 1.26:
                    if self.acce_energy_z <= 10.73:
                        if self.gyro_kurt_y <= 3.53:
                            return [ 0,  0, 12,]
                        else:  # if self.gyro_kurt_y > 3.53
                            return [0, 5, 1,]
                    else:  # if self.acce_energy_z > 10.73
                        if self.acce_energy_y <= 187.16:
                            return [  0, 116,  11,]
                        else:  # if self.acce_energy_y > 187.16
                            return [7, 2, 0,]
                else:  # if self.acce_rms_z > 1.26
                    if self.acce_variance_x <= 0.0:
                        return [0, 4, 0,]
                    else:  # if self.acce_variance_x > 0.0
                        if self.acce_rms_x <= 2.93:
                            return [30,  1,  0,]
                        else:  # if self.acce_rms_x > 2.93
                            return [0, 0, 3,]

    def decision_tree_3(self):
        if self.gyro_rms_z <= 7.24:
            if self.n_samples <= 14.5:
                if self.gyro_kurt_z <= -0.55:
                    if self.acce_corr_xz <= 0.29:
                        if self.acce_variance_x <= 0.03:
                            if self.acce_variance_z <= 0.07:
                                return [1, 8, 1,]
                            else:  # if self.acce_variance_z > 0.07
                                return [35,  1,  1,]
                        else:  # if self.acce_variance_x > 0.03
                            if self.gyro_kurt_x <= 7.05:
                                return [ 1,  2, 57,]
                            else:  # if self.gyro_kurt_x > 7.05
                                return [0, 2, 0,]
                    else:  # if self.acce_corr_xz > 0.29
                        if self.gyro_variance_y <= 18.91:
                            return [ 2, 41,  4,]
                        else:  # if self.gyro_variance_y > 18.91
                            return [0, 0, 4,]
                else:  # if self.gyro_kurt_z > -0.55
                    return [ 0, 75,  2,]
            else:  # if self.n_samples > 14.5
                if self.acce_min_z <= 0.74:
                    return [222,   0,   0,]
                else:  # if self.acce_min_z > 0.74
                    return [ 0, 12,  0,]
        else:  # if self.gyro_rms_z > 7.24
            if self.gyro_energy_z <= 802.38:
                if self.acce_variance_x <= 0.01:
                    return [ 1, 19,  1,]
                else:  # if self.acce_variance_x > 0.01
                    if self.gyro_energy_y <= 490.37:
                        if self.gyro_rms_x <= 7.93:
                            return [  0,   4, 217,]
                        else:  # if self.gyro_rms_x > 7.93
                            if self.gyro_std_z <= 2.69:
                                return [0, 7, 0,]
                            else:  # if self.gyro_std_z > 2.69
                                return [0, 1, 3,]
                    else:  # if self.gyro_energy_y > 490.37
                        if self.gyro_variance_x <= 15.42:
                            return [ 0, 14,  0,]
                        else:  # if self.gyro_variance_x > 15.42
                            if self.acce_energy_x <= 38.08:
                                return [ 0, 14,  6,]
                            else:  # if self.acce_energy_x > 38.08
                                return [ 0,  0, 13,]
            else:  # if self.gyro_energy_z > 802.38
                if self.acce_mean_y <= 2.35:
                    return [ 1, 79,  0,]
                else:  # if self.acce_mean_y > 2.35
                    if self.acce_corr_xz <= 0.01:
                        if self.acce_rms_z <= 0.96:
                            return [0, 2, 0,]
                        else:  # if self.acce_rms_z > 0.96
                            return [ 0,  0, 10,]
                    else:  # if self.acce_corr_xz > 0.01
                        if self.gyro_corr_xy <= -0.37:
                            return [0, 1, 3,]
                        else:  # if self.gyro_corr_xy > -0.37
                            return [ 0, 31,  1,]

    def decision_tree_4(self):
        if self.gyro_variance_y <= 15.67:
            if self.gyro_kurt_y <= -1.13:
                if self.n_samples <= 12.5:
                    if self.gyro_kurt_z <= -1.29:
                        if self.gyro_std_z <= 3.89:
                            return [15,  1,  0,]
                        else:  # if self.gyro_std_z > 3.89
                            return [0, 0, 3,]
                    else:  # if self.gyro_kurt_z > -1.29
                        return [ 1, 18,  0,]
                else:  # if self.n_samples > 12.5
                    if self.gyro_std_z <= 4.19:
                        return [261,   0,   0,]
                    else:  # if self.gyro_std_z > 4.19
                        return [0, 2, 0,]
            else:  # if self.gyro_kurt_y > -1.13
                if self.gyro_mean_y <= 6.83:
                    if self.acce_min_x <= 0.04:
                        return [ 2, 60,  5,]
                    else:  # if self.acce_min_x > 0.04
                        if self.acce_rms_z <= 1.08:
                            if self.acce_range_x <= 0.37:
                                return [ 0, 20,  0,]
                            else:  # if self.acce_range_x > 0.37
                                if self.acce_corr_xz <= 0.45:
                                    return [ 0,  1, 36,]
                                else:  # if self.acce_corr_xz > 0.45
                                    return [ 0, 24,  2,]
                        else:  # if self.acce_rms_z > 1.08
                            if self.gyro_rms_x <= 3.77:
                                return [0, 3, 0,]
                            else:  # if self.gyro_rms_x > 3.77
                                return [ 0,  0, 35,]
                else:  # if self.gyro_mean_y > 6.83
                    if self.gyro_energy_y <= 584.78:
                        return [0, 0, 8,]
                    else:  # if self.gyro_energy_y > 584.78
                        return [  0, 138,   6,]
        else:  # if self.gyro_variance_y > 15.67
            if self.acce_rms_x <= 0.3:
                if self.gyro_rms_z <= 6.8:
                    if self.acce_mean_y <= 3.81:
                        return [2, 0, 0,]
                    else:  # if self.acce_mean_y > 3.81
                        return [0, 0, 4,]
                else:  # if self.gyro_rms_z > 6.8
                    return [ 0, 12,  0,]
            else:  # if self.acce_rms_x > 0.3
                if self.acce_energy_z <= 13.78:
                    if self.gyro_std_x <= 3.24:
                        if self.acce_std_z <= 0.11:
                            return [0, 6, 3,]
                        else:  # if self.acce_std_z > 0.11
                            return [0, 0, 6,]
                    else:  # if self.gyro_std_x > 3.24
                        return [  0,   2, 200,]
                else:  # if self.acce_energy_z > 13.78
                    if self.acce_variance_z <= 0.07:
                        return [ 0, 17,  0,]
                    else:  # if self.acce_variance_z > 0.07
                        return [0, 0, 6,]

    def decision_tree_5(self):
        if self.gyro_std_y <= 3.95:
            if self.acce_rms_z <= 0.97:
                if self.gyro_rms_z <= 7.38:
                    if self.gyro_kurt_y <= -0.79:
                        if self.gyro_energy_x <= 204.81:
                            return [0, 1, 3,]
                        else:  # if self.gyro_energy_x > 204.81
                            return [226,   0,   0,]
                    else:  # if self.gyro_kurt_y > -0.79
                        if self.gyro_skew_y <= -0.15:
                            return [0, 8, 0,]
                        else:  # if self.gyro_skew_y > -0.15
                            return [ 0,  2, 11,]
                else:  # if self.gyro_rms_z > 7.38
                    return [ 2, 26,  4,]
            else:  # if self.acce_rms_z > 0.97
                if self.acce_std_z <= 0.36:
                    if self.gyro_skew_y <= -1.36:
                        if self.gyro_variance_z <= 15.5:
                            return [ 0, 99,  0,]
                        else:  # if self.gyro_variance_z > 15.5
                            return [0, 5, 5,]
                    else:  # if self.gyro_skew_y > -1.36
                        if self.n_samples <= 9.5:
                            return [ 0,  4, 33,]
                        else:  # if self.n_samples > 9.5
                            if self.acce_variance_z <= 0.05:
                                return [ 2, 60,  3,]
                            else:  # if self.acce_variance_z > 0.05
                                if self.acce_energy_z <= 17.25:
                                    return [ 3, 21,  6,]
                                else:  # if self.acce_energy_z > 17.25
                                    return [15,  0,  0,]
                else:  # if self.acce_std_z > 0.36
                    if self.acce_rms_x <= 0.85:
                        return [42,  0,  2,]
                    else:  # if self.acce_rms_x > 0.85
                        if self.acce_rms_x <= 0.93:
                            return [ 0, 14,  1,]
                        else:  # if self.acce_rms_x > 0.93
                            if self.acce_max_x <= 3.98:
                                return [ 0,  0, 15,]
                            else:  # if self.acce_max_x > 3.98
                                return [3, 3, 0,]
        else:  # if self.gyro_std_y > 3.95
            if self.n_samples <= 11.5:
                if self.acce_range_x <= 0.42:
                    return [2, 8, 1,]
                else:  # if self.acce_range_x > 0.42
                    if self.gyro_rms_x <= 4.16:
                        return [0, 6, 2,]
                    else:  # if self.gyro_rms_x > 4.16
                        if self.gyro_std_y <= 4.49:
                            if self.acce_corr_xz <= 0.79:
                                return [  0,   1, 221,]
                            else:  # if self.acce_corr_xz > 0.79
                                return [0, 3, 0,]
                        else:  # if self.gyro_std_y > 4.49
                            return [0, 3, 0,]
            else:  # if self.n_samples > 11.5
                return [ 2, 29,  2,]

    def decision_tree_6(self):
        if self.acce_mean_z <= 0.97:
            if self.gyro_energy_y <= 345.89:
                if self.n_samples <= 11.5:
                    if self.gyro_variance_z <= 6.06:
                        return [3, 8, 2,]
                    else:  # if self.gyro_variance_z > 6.06
                        return [ 1,  4, 35,]
                else:  # if self.n_samples > 11.5
                    return [ 2, 30,  3,]
            else:  # if self.gyro_energy_y > 345.89
                if self.gyro_rms_z <= 7.41:
                    if self.gyro_skew_z <= 1.2:
                        return [248,   2,   1,]
                    else:  # if self.gyro_skew_z > 1.2
                        return [ 0, 15,  0,]
                else:  # if self.gyro_rms_z > 7.41
                    return [ 0, 21,  4,]
        else:  # if self.acce_mean_z > 0.97
            if self.acce_energy_x <= 88.68:
                if self.gyro_kurt_y <= 0.18:
                    if self.acce_variance_x <= 0.03:
                        if self.gyro_mean_z <= 7.32:
                            if self.acce_rms_x <= 0.86:
                                return [24,  0,  2,]
                            else:  # if self.acce_rms_x > 0.86
                                return [0, 4, 0,]
                        else:  # if self.gyro_mean_z > 7.32
                            return [ 0, 11,  0,]
                    else:  # if self.acce_variance_x > 0.03
                        if self.gyro_energy_y <= 573.51:
                            if self.gyro_energy_z <= 727.42:
                                return [  1,   5, 165,]
                            else:  # if self.gyro_energy_z > 727.42
                                if self.gyro_corr_xy <= 0.21:
                                    return [ 0,  7, 29,]
                                else:  # if self.gyro_corr_xy > 0.21
                                    return [0, 8, 1,]
                        else:  # if self.gyro_energy_y > 573.51
                            return [ 1, 17, 11,]
                else:  # if self.gyro_kurt_y > 0.18
                    if self.gyro_kurt_z <= -0.55:
                        if self.gyro_skew_z <= 0.04:
                            return [ 0,  3, 17,]
                        else:  # if self.gyro_skew_z > 0.04
                            return [0, 9, 0,]
                    else:  # if self.gyro_kurt_z > -0.55
                        if self.acce_min_x <= 0.06:
                            return [ 0, 57,  0,]
                        else:  # if self.acce_min_x > 0.06
                            if self.gyro_kurt_x <= -1.66:
                                return [ 0,  0, 10,]
                            else:  # if self.gyro_kurt_x > -1.66
                                return [ 0, 11,  1,]
            else:  # if self.acce_energy_x > 88.68
                if self.acce_energy_y <= 185.1:
                    return [ 5, 92,  7,]
                else:  # if self.acce_energy_y > 185.1
                    if self.gyro_energy_x <= 660.54:
                        return [ 0, 11,  0,]
                    else:  # if self.gyro_energy_x > 660.54
                        return [11,  0,  0,]

    def decision_tree_7(self):
        if self.n_samples <= 14.5:
            if self.gyro_std_y <= 3.95:
                if self.acce_min_z <= 0.22:
                    if self.acce_rms_x <= 0.84:
                        return [30,  0,  0,]
                    else:  # if self.acce_rms_x > 0.84
                        if self.acce_range_x <= 0.32:
                            return [ 0, 10,  0,]
                        else:  # if self.acce_range_x > 0.32
                            if self.gyro_energy_y <= 607.19:
                                if self.acce_mean_y <= 3.7:
                                    return [ 0,  0, 34,]
                                else:  # if self.acce_mean_y > 3.7
                                    return [2, 0, 0,]
                            else:  # if self.gyro_energy_y > 607.19
                                return [0, 6, 1,]
                else:  # if self.acce_min_z > 0.22
                    if self.gyro_energy_y <= 573.51:
                        if self.acce_rms_x <= 2.84:
                            if self.n_samples <= 9.5:
                                return [ 0,  1, 57,]
                            else:  # if self.n_samples > 9.5
                                if self.gyro_skew_z <= -0.27:
                                    if self.gyro_skew_z <= -2.68:
                                        return [ 0, 17,  0,]
                                    else:  # if self.gyro_skew_z > -2.68
                                        if self.acce_min_z <= 0.29:
                                            return [3, 0, 0,]
                                        else:  # if self.acce_min_z > 0.29
                                            return [ 0,  4, 11,]
                                else:  # if self.gyro_skew_z > -0.27
                                    return [ 0, 32,  2,]
                        else:  # if self.acce_rms_x > 2.84
                            return [ 0, 31,  1,]
                    else:  # if self.gyro_energy_y > 573.51
                        return [  1, 142,   9,]
            else:  # if self.gyro_std_y > 3.95
                if self.acce_range_x <= 0.38:
                    return [ 0, 13,  1,]
                else:  # if self.acce_range_x > 0.38
                    if self.acce_energy_x <= 113.92:
                        if self.gyro_kurt_z <= 7.03:
                            if self.acce_variance_z <= 0.0:
                                return [0, 4, 2,]
                            else:  # if self.acce_variance_z > 0.0
                                if self.acce_corr_xz <= 0.77:
                                    return [  0,   3, 181,]
                                else:  # if self.acce_corr_xz > 0.77
                                    return [0, 2, 0,]
                        else:  # if self.gyro_kurt_z > 7.03
                            return [0, 3, 0,]
                    else:  # if self.acce_energy_x > 113.92
                        return [ 0, 12,  0,]
        else:  # if self.n_samples > 14.5
            if self.gyro_mean_y <= 6.78:
                if self.gyro_kurt_y <= -0.89:
                    return [261,   1,   0,]
                else:  # if self.gyro_kurt_y > -0.89
                    return [1, 6, 0,]
            else:  # if self.gyro_mean_y > 6.78
                return [ 0, 15,  0,]

    def decision_tree_8(self):
        if self.gyro_kurt_y <= -1.12:
            if self.acce_min_z <= 0.68:
                if self.gyro_variance_x <= 17.58:
                    if self.gyro_variance_y <= 15.33:
                        if self.gyro_rms_x <= 7.27:
                            return [284,   1,   4,]
                        else:  # if self.gyro_rms_x > 7.27
                            if self.acce_std_z <= 0.26:
                                return [5, 0, 0,]
                            else:  # if self.acce_std_z > 0.26
                                return [0, 5, 0,]
                    else:  # if self.gyro_variance_y > 15.33
                        if self.acce_min_z <= 0.06:
                            return [0, 0, 7,]
                        else:  # if self.acce_min_z > 0.06
                            return [3, 8, 3,]
                else:  # if self.gyro_variance_x > 17.58
                    if self.acce_energy_y <= 61.35:
                        return [ 0,  0, 11,]
                    else:  # if self.acce_energy_y > 61.35
                        return [0, 6, 1,]
            else:  # if self.acce_min_z > 0.68
                if self.gyro_energy_x <= 647.21:
                    if self.gyro_mean_z <= 3.35:
                        return [2, 9, 3,]
                    else:  # if self.gyro_mean_z > 3.35
                        if self.acce_min_z <= 0.98:
                            return [  0,   6, 191,]
                        else:  # if self.acce_min_z > 0.98
                            return [0, 3, 0,]
                else:  # if self.gyro_energy_x > 647.21
                    return [ 2, 20,  7,]
        else:  # if self.gyro_kurt_y > -1.12
            if self.acce_std_z <= 1.03:
                if self.acce_energy_z <= 11.47:
                    if self.gyro_std_y <= 2.57:
                        return [ 0, 35,  0,]
                    else:  # if self.gyro_std_y > 2.57
                        if self.gyro_kurt_x <= -0.22:
                            if self.acce_mean_y <= 2.5:
                                if self.acce_variance_z <= 0.01:
                                    return [ 0, 10,  0,]
                                else:  # if self.acce_variance_z > 0.01
                                    if self.acce_rms_x <= 0.54:
                                        return [0, 4, 0,]
                                    else:  # if self.acce_rms_x > 0.54
                                        if self.acce_energy_x <= 60.39:
                                            return [ 1,  1, 17,]
                                        else:  # if self.acce_energy_x > 60.39
                                            return [1, 3, 0,]
                            else:  # if self.acce_mean_y > 2.5
                                return [ 0,  1, 33,]
                        else:  # if self.gyro_kurt_x > -0.22
                            return [ 0, 20,  2,]
                else:  # if self.acce_energy_z > 11.47
                    return [  0, 151,   5,]
            else:  # if self.acce_std_z > 1.03
                if self.gyro_mean_y <= 2.39:
                    return [ 0,  0, 23,]
                else:  # if self.gyro_mean_y > 2.39
                    return [2, 6, 3,]

    def decision_tree_9(self):
        if self.n_samples <= 14.5:
            if self.gyro_energy_y <= 575.17:
                if self.gyro_variance_y <= 15.63:
                    if self.n_samples <= 9.5:
                        if self.acce_variance_z <= 0.0:
                            return [0, 3, 0,]
                        else:  # if self.acce_variance_z > 0.0
                            return [ 0,  1, 43,]
                    else:  # if self.n_samples > 9.5
                        if self.acce_min_z <= 0.3:
                            if self.gyro_rms_y <= 4.56:
                                if self.gyro_rms_z <= 5.75:
                                    return [0, 5, 1,]
                                else:  # if self.gyro_rms_z > 5.75
                                    if self.gyro_energy_z <= 818.86:
                                        return [ 0,  1, 24,]
                                    else:  # if self.gyro_energy_z > 818.86
                                        return [0, 3, 0,]
                            else:  # if self.gyro_rms_y > 4.56
                                if self.n_samples <= 10.5:
                                    return [0, 2, 1,]
                                else:  # if self.n_samples > 10.5
                                    return [45,  0,  1,]
                        else:  # if self.acce_min_z > 0.3
                            return [ 0, 91,  9,]
                else:  # if self.gyro_variance_y > 15.63
                    if self.gyro_energy_x <= 644.25:
                        if self.acce_energy_x <= 109.0:
                            if self.acce_kurt_x <= 4.99:
                                if self.acce_variance_x <= 0.01:
                                    return [0, 3, 2,]
                                else:  # if self.acce_variance_x > 0.01
                                    if self.acce_range_x <= 3.98:
                                        return [  0,   0, 187,]
                                    else:  # if self.acce_range_x > 3.98
                                        return [0, 3, 4,]
                            else:  # if self.acce_kurt_x > 4.99
                                return [0, 2, 0,]
                        else:  # if self.acce_energy_x > 109.0
                            return [ 0, 11,  1,]
                    else:  # if self.gyro_energy_x > 644.25
                        return [ 0, 15,  6,]
            else:  # if self.gyro_energy_y > 575.17
                if self.gyro_mean_y <= 5.78:
                    return [4, 0, 0,]
                else:  # if self.gyro_mean_y > 5.78
                    if self.acce_min_z <= 0.0:
                        return [0, 0, 4,]
                    else:  # if self.acce_min_z > 0.0
                        return [  1, 154,   5,]
        else:  # if self.n_samples > 14.5
            if self.gyro_kurt_z <= -0.91:
                if self.gyro_skew_y <= 0.97:
                    return [235,   1,   0,]
                else:  # if self.gyro_skew_y > 0.97
                    return [0, 3, 0,]
            else:  # if self.gyro_kurt_z > -0.91
                if self.acce_variance_x <= 2.34:
                    return [11,  1,  0,]
                else:  # if self.acce_variance_x > 2.34
                    return [ 2, 14,  0,]

    def decision_tree_10(self):
        if self.gyro_kurt_z <= -0.7:
            if self.n_samples <= 13.5:
                if self.acce_max_x <= 1.1:
                    if self.gyro_mean_z <= 6.43:
                        if self.gyro_skew_y <= 0.53:
                            return [23,  1,  1,]
                        else:  # if self.gyro_skew_y > 0.53
                            return [0, 8, 3,]
                    else:  # if self.gyro_mean_z > 6.43
                        return [ 2, 23,  2,]
                else:  # if self.acce_max_x > 1.1
                    if self.n_samples <= 11.5:
                        if self.acce_range_x <= 3.95:
                            return [  2,   8, 113,]
                        else:  # if self.acce_range_x > 3.95
                            if self.gyro_skew_z <= 0.03:
                                return [ 0,  2, 13,]
                            else:  # if self.gyro_skew_z > 0.03
                                return [ 0, 10,  1,]
                    else:  # if self.n_samples > 11.5
                        return [ 0, 28,  3,]
            else:  # if self.n_samples > 13.5
                if self.gyro_variance_z <= 16.96:
                    return [271,   5,   0,]
                else:  # if self.gyro_variance_z > 16.96
                    return [0, 7, 0,]
        else:  # if self.gyro_kurt_z > -0.7
            if self.gyro_std_z <= 2.49:
                if self.n_samples <= 9.5:
                    return [ 0,  0, 14,]
                else:  # if self.n_samples > 9.5
                    if self.gyro_rms_z <= 8.73:
                        return [  0, 130,   1,]
                    else:  # if self.gyro_rms_z > 8.73
                        if self.acce_variance_x <= 2.75:
                            return [0, 5, 0,]
                        else:  # if self.acce_variance_x > 2.75
                            return [ 0,  0, 15,]
            else:  # if self.gyro_std_z > 2.49
                if self.n_samples <= 9.5:
                    if self.gyro_rms_z <= 4.3:
                        return [0, 2, 0,]
                    else:  # if self.gyro_rms_z > 4.3
                        return [ 0,  1, 97,]
                else:  # if self.n_samples > 9.5
                    if self.gyro_rms_z <= 7.99:
                        if self.acce_rms_z <= 1.43:
                            if self.gyro_skew_y <= 2.73:
                                return [ 1, 61,  2,]
                            else:  # if self.gyro_skew_y > 2.73
                                return [0, 1, 3,]
                        else:  # if self.acce_rms_z > 1.43
                            return [3, 0, 0,]
                    else:  # if self.gyro_rms_z > 7.99
                        if self.acce_rms_y <= 2.55:
                            return [ 0, 11,  0,]
                        else:  # if self.acce_rms_y > 2.55
                            if self.n_samples <= 11.5:
                                return [ 0,  0, 24,]
                            else:  # if self.n_samples > 11.5
                                return [0, 2, 0,]

    def decision_tree_11(self):
        if self.n_samples <= 14.5:
            if self.gyro_rms_y <= 7.19:
                if self.acce_rms_x <= 0.93:
                    if self.gyro_kurt_z <= -0.78:
                        if self.acce_std_x <= 0.07:
                            return [ 0, 17,  1,]
                        else:  # if self.acce_std_x > 0.07
                            if self.gyro_variance_x <= 16.16:
                                if self.acce_rms_z <= 0.76:
                                    return [0, 0, 3,]
                                else:  # if self.acce_rms_z > 0.76
                                    return [46,  0,  0,]
                            else:  # if self.gyro_variance_x > 16.16
                                return [0, 1, 7,]
                    else:  # if self.gyro_kurt_z > -0.78
                        return [ 0, 19,  5,]
                else:  # if self.acce_rms_x > 0.93
                    if self.acce_corr_xz <= 0.38:
                        if self.acce_range_x <= 3.97:
                            if self.acce_range_x <= 0.42:
                                return [0, 4, 0,]
                            else:  # if self.acce_range_x > 0.42
                                return [  2,   5, 198,]
                        else:  # if self.acce_range_x > 3.97
                            if self.n_samples <= 11.5:
                                return [0, 3, 8,]
                            else:  # if self.n_samples > 11.5
                                return [ 0, 11,  0,]
                    else:  # if self.acce_corr_xz > 0.38
                        if self.gyro_std_y <= 4.1:
                            if self.acce_energy_x <= 12.3:
                                return [0, 0, 4,]
                            else:  # if self.acce_energy_x > 12.3
                                return [ 1, 52,  2,]
                        else:  # if self.gyro_std_y > 4.1
                            if self.acce_variance_z <= 0.07:
                                return [ 0, 10,  8,]
                            else:  # if self.acce_variance_z > 0.07
                                return [ 0,  0, 16,]
            else:  # if self.gyro_rms_y > 7.19
                if self.gyro_kurt_y <= -0.12:
                    if self.acce_rms_y <= 2.79:
                        if self.gyro_std_z <= 3.7:
                            return [ 1, 25,  1,]
                        else:  # if self.gyro_std_z > 3.7
                            return [0, 0, 5,]
                    else:  # if self.acce_rms_y > 2.79
                        if self.gyro_rms_x <= 4.98:
                            return [0, 4, 1,]
                        else:  # if self.gyro_rms_x > 4.98
                            return [ 0,  1, 29,]
                else:  # if self.gyro_kurt_y > -0.12
                    return [  0, 139,   7,]
        else:  # if self.n_samples > 14.5
            if self.gyro_skew_z <= -1.33:
                return [1, 7, 0,]
            else:  # if self.gyro_skew_z > -1.33
                if self.acce_min_z <= 0.77:
                    return [245,   0,   0,]
                else:  # if self.acce_min_z > 0.77
                    return [ 0, 10,  0,]

    def decision_tree_12(self):
        if self.gyro_variance_x <= 16.32:
            if self.n_samples <= 14.5:
                if self.gyro_energy_y <= 567.31:
                    if self.acce_range_x <= 0.56:
                        if self.gyro_energy_z <= 698.32:
                            if self.acce_corr_xz <= 0.16:
                                return [34,  0,  0,]
                            else:  # if self.acce_corr_xz > 0.16
                                return [0, 3, 1,]
                        else:  # if self.gyro_energy_z > 698.32
                            return [ 0, 11,  0,]
                    else:  # if self.acce_range_x > 0.56
                        if self.gyro_mean_z <= 2.72:
                            return [ 0, 17,  0,]
                        else:  # if self.gyro_mean_z > 2.72
                            if self.acce_corr_xz <= 0.36:
                                return [ 1,  7, 73,]
                            else:  # if self.acce_corr_xz > 0.36
                                if self.gyro_rms_y <= 4.61:
                                    return [ 0, 17,  0,]
                                else:  # if self.gyro_rms_y > 4.61
                                    return [ 1,  9, 12,]
                else:  # if self.gyro_energy_y > 567.31
                    return [ 4, 94,  2,]
            else:  # if self.n_samples > 14.5
                return [270,   2,   0,]
        else:  # if self.gyro_variance_x > 16.32
            if self.gyro_variance_y <= 14.7:
                if self.gyro_kurt_y <= -1.26:
                    if self.gyro_std_x <= 4.27:
                        return [18,  0,  0,]
                    else:  # if self.gyro_std_x > 4.27
                        return [0, 5, 0,]
                else:  # if self.gyro_kurt_y > -1.26
                    if self.gyro_energy_z <= 802.38:
                        if self.gyro_rms_y <= 4.33:
                            if self.acce_rms_x <= 2.77:
                                return [ 0,  5, 33,]
                            else:  # if self.acce_rms_x > 2.77
                                return [0, 5, 0,]
                        else:  # if self.gyro_rms_y > 4.33
                            if self.gyro_mean_z <= 4.83:
                                return [ 0, 18,  0,]
                            else:  # if self.gyro_mean_z > 4.83
                                if self.acce_rms_x <= 1.77:
                                    return [ 0, 11,  0,]
                                else:  # if self.acce_rms_x > 1.77
                                    return [ 0,  5, 20,]
                    else:  # if self.gyro_energy_z > 802.38
                        return [ 0, 43,  0,]
            else:  # if self.gyro_variance_y > 14.7
                if self.acce_rms_x <= 3.23:
                    if self.n_samples <= 12.5:
                        return [  0,   5, 153,]
                    else:  # if self.n_samples > 12.5
                        return [0, 5, 1,]
                else:  # if self.acce_rms_x > 3.23
                    if self.acce_min_x <= 1.51:
                        return [ 0, 10,  0,]
                    else:  # if self.acce_min_x > 1.51
                        return [0, 0, 4,]

    def decision_tree_13(self):
        if self.gyro_rms_y <= 7.18:
            if self.n_samples <= 11.5:
                if self.acce_skew_x <= -0.79:
                    if self.gyro_energy_y <= 437.28:
                        return [ 0, 11,  0,]
                    else:  # if self.gyro_energy_y > 437.28
                        return [0, 0, 3,]
                else:  # if self.acce_skew_x > -0.79
                    if self.gyro_variance_x <= 12.34:
                        if self.acce_min_x <= 0.06:
                            return [ 0, 10,  2,]
                        else:  # if self.acce_min_x > 0.06
                            return [2, 1, 7,]
                    else:  # if self.gyro_variance_x > 12.34
                        if self.acce_variance_z <= 0.0:
                            return [0, 3, 0,]
                        else:  # if self.acce_variance_z > 0.0
                            if self.gyro_variance_y <= 6.23:
                                return [0, 5, 1,]
                            else:  # if self.gyro_variance_y > 6.23
                                if self.acce_max_x <= 4.0:
                                    return [  0,   1, 220,]
                                else:  # if self.acce_max_x > 4.0
                                    return [2, 0, 0,]
            else:  # if self.n_samples > 11.5
                if self.gyro_skew_y <= 0.69:
                    if self.gyro_mean_z <= 6.58:
                        if self.gyro_std_x <= 4.22:
                            if self.gyro_mean_y <= 2.02:
                                return [0, 2, 0,]
                            else:  # if self.gyro_mean_y > 2.02
                                return [285,   1,   0,]
                        else:  # if self.gyro_std_x > 4.22
                            return [0, 5, 0,]
                    else:  # if self.gyro_mean_z > 6.58
                        return [ 1, 14,  2,]
                else:  # if self.gyro_skew_y > 0.69
                    if self.acce_min_x <= 0.68:
                        return [ 0, 61,  1,]
                    else:  # if self.acce_min_x > 0.68
                        return [ 0, 12,  7,]
        else:  # if self.gyro_rms_y > 7.18
            if self.gyro_skew_y <= -1.36:
                return [  0, 147,   6,]
            else:  # if self.gyro_skew_y > -1.36
                if self.gyro_energy_z <= 724.5:
                    if self.acce_rms_y <= 2.88:
                        if self.acce_max_x <= 3.97:
                            if self.acce_rms_y <= 2.59:
                                return [1, 0, 7,]
                            else:  # if self.acce_rms_y > 2.59
                                return [0, 5, 1,]
                        else:  # if self.acce_max_x > 3.97
                            return [ 0, 18,  1,]
                    else:  # if self.acce_rms_y > 2.88
                        if self.gyro_mean_y <= 7.88:
                            return [ 0,  0, 30,]
                        else:  # if self.gyro_mean_y > 7.88
                            return [0, 5, 0,]
                else:  # if self.gyro_energy_z > 724.5
                    return [ 0, 19,  0,]

    def decision_tree_14(self):
        if self.n_samples <= 14.5:
            if self.gyro_kurt_z <= 6.15:
                if self.gyro_mean_y <= 6.45:
                    if self.acce_rms_x <= 0.9:
                        if self.acce_std_z <= 0.29:
                            if self.acce_range_x <= 0.38:
                                return [ 2, 19,  2,]
                            else:  # if self.acce_range_x > 0.38
                                if self.acce_rms_y <= 2.51:
                                    return [0, 3, 0,]
                                else:  # if self.acce_rms_y > 2.51
                                    return [ 0,  0, 18,]
                        else:  # if self.acce_std_z > 0.29
                            if self.gyro_energy_x <= 641.69:
                                if self.gyro_mean_z <= 3.69:
                                    return [0, 3, 0,]
                                else:  # if self.gyro_mean_z > 3.69
                                    return [37,  0,  2,]
                            else:  # if self.gyro_energy_x > 641.69
                                return [0, 6, 0,]
                    else:  # if self.acce_rms_x > 0.9
                        if self.gyro_rms_y <= 5.11:
                            if self.acce_energy_x <= 77.2:
                                if self.acce_kurt_x <= 2.86:
                                    if self.acce_min_x <= 0.01:
                                        return [0, 4, 0,]
                                    else:  # if self.acce_min_x > 0.01
                                        return [ 0,  7, 57,]
                                else:  # if self.acce_kurt_x > 2.86
                                    return [ 0, 11,  0,]
                            else:  # if self.acce_energy_x > 77.2
                                return [ 0, 39,  1,]
                        else:  # if self.gyro_rms_y > 5.11
                            if self.gyro_variance_x <= 6.19:
                                return [0, 6, 0,]
                            else:  # if self.gyro_variance_x > 6.19
                                if self.n_samples <= 11.5:
                                    return [  0,   3, 195,]
                                else:  # if self.n_samples > 11.5
                                    if self.acce_std_x <= 1.49:
                                        return [0, 1, 6,]
                                    else:  # if self.acce_std_x > 1.49
                                        return [ 0, 10,  0,]
                else:  # if self.gyro_mean_y > 6.45
                    if self.n_samples <= 9.5:
                        return [ 2,  2, 16,]
                    else:  # if self.n_samples > 9.5
                        if self.gyro_variance_x <= 16.95:
                            return [ 0, 78,  0,]
                        else:  # if self.gyro_variance_x > 16.95
                            return [ 0, 26, 12,]
            else:  # if self.gyro_kurt_z > 6.15
                return [ 0, 62,  0,]
        else:  # if self.n_samples > 14.5
            if self.gyro_skew_z <= -1.4:
                return [1, 4, 0,]
            else:  # if self.gyro_skew_z > -1.4
                if self.gyro_kurt_y <= -0.94:
                    return [261,   0,   0,]
                else:  # if self.gyro_kurt_y > -0.94
                    return [0, 3, 0,]

    def decision_tree_15(self):
        if self.acce_rms_z <= 0.98:
            if self.gyro_std_z <= 2.69:
                if self.n_samples <= 9.5:
                    return [3, 0, 3,]
                else:  # if self.n_samples > 9.5
                    return [ 0, 45,  3,]
            else:  # if self.gyro_std_z > 2.69
                if self.acce_energy_z <= 6.62:
                    if self.gyro_corr_xy <= 0.33:
                        if self.acce_std_x <= 0.12:
                            return [0, 6, 0,]
                        else:  # if self.acce_std_x > 0.12
                            return [ 3,  0, 23,]
                    else:  # if self.gyro_corr_xy > 0.33
                        return [0, 6, 0,]
                else:  # if self.acce_energy_z > 6.62
                    if self.gyro_energy_x <= 249.64:
                        return [3, 8, 2,]
                    else:  # if self.gyro_energy_x > 249.64
                        if self.gyro_std_y <= 4.12:
                            if self.gyro_variance_y <= 7.45:
                                return [0, 3, 2,]
                            else:  # if self.gyro_variance_y > 7.45
                                return [207,   0,   0,]
                        else:  # if self.gyro_std_y > 4.12
                            return [0, 0, 4,]
        else:  # if self.acce_rms_z > 0.98
            if self.gyro_std_y <= 4.08:
                if self.gyro_kurt_x <= -1.36:
                    if self.gyro_std_x <= 4.07:
                        return [70,  5,  0,]
                    else:  # if self.gyro_std_x > 4.07
                        if self.acce_variance_x <= 3.3:
                            if self.acce_energy_x <= 74.59:
                                if self.acce_kurt_x <= 0.47:
                                    if self.gyro_kurt_z <= 6.34:
                                        return [ 0,  6, 70,]
                                    else:  # if self.gyro_kurt_z > 6.34
                                        return [0, 4, 0,]
                                else:  # if self.acce_kurt_x > 0.47
                                    return [0, 8, 0,]
                            else:  # if self.acce_energy_x > 74.59
                                return [ 0, 16,  0,]
                        else:  # if self.acce_variance_x > 3.3
                            return [ 0, 29,  2,]
                else:  # if self.gyro_kurt_x > -1.36
                    if self.gyro_energy_y <= 84.09:
                        return [ 0,  3, 11,]
                    else:  # if self.gyro_energy_y > 84.09
                        if self.acce_energy_z <= 9.29:
                            return [0, 0, 7,]
                        else:  # if self.acce_energy_z > 9.29
                            return [  5, 129,   5,]
            else:  # if self.gyro_std_y > 4.08
                if self.acce_std_x <= 0.1:
                    return [ 0, 15,  1,]
                else:  # if self.acce_std_x > 0.1
                    if self.n_samples <= 12.5:
                        return [  0,   5, 177,]
                    else:  # if self.n_samples > 12.5
                        return [0, 9, 1,]

    def decision_tree_16(self):
        if self.gyro_mean_y <= 6.44:
            if self.acce_min_z <= 0.7:
                if self.gyro_kurt_z <= -0.71:
                    if self.gyro_variance_y <= 9.74:
                        if self.gyro_kurt_y <= 3.49:
                            return [2, 9, 0,]
                        else:  # if self.gyro_kurt_y > 3.49
                            return [0, 3, 9,]
                    else:  # if self.gyro_variance_y > 9.74
                        if self.gyro_energy_y <= 343.03:
                            if self.acce_rms_x <= 1.03:
                                if self.acce_rms_x <= 0.76:
                                    return [3, 2, 0,]
                                else:  # if self.acce_rms_x > 0.76
                                    return [ 0,  0, 15,]
                            else:  # if self.acce_rms_x > 1.03
                                return [0, 7, 1,]
                        else:  # if self.gyro_energy_y > 343.03
                            if self.gyro_std_y <= 3.91:
                                return [271,   0,   0,]
                            else:  # if self.gyro_std_y > 3.91
                                return [1, 3, 2,]
                else:  # if self.gyro_kurt_z > -0.71
                    if self.gyro_energy_x <= 492.77:
                        if self.acce_min_x <= 0.22:
                            return [ 0, 13,  1,]
                        else:  # if self.acce_min_x > 0.22
                            if self.gyro_kurt_y <= 5.56:
                                return [ 0,  0, 22,]
                            else:  # if self.gyro_kurt_y > 5.56
                                return [0, 3, 0,]
                    else:  # if self.gyro_energy_x > 492.77
                        return [ 2, 18,  1,]
            else:  # if self.acce_min_z > 0.7
                if self.gyro_skew_z <= -0.01:
                    if self.gyro_skew_y <= 0.77:
                        if self.acce_std_x <= 0.08:
                            return [0, 5, 0,]
                        else:  # if self.acce_std_x > 0.08
                            return [  0,   7, 172,]
                    else:  # if self.gyro_skew_y > 0.77
                        if self.gyro_std_z <= 3.61:
                            return [ 0, 25,  7,]
                        else:  # if self.gyro_std_z > 3.61
                            return [0, 1, 9,]
                else:  # if self.gyro_skew_z > -0.01
                    if self.acce_corr_xz <= -0.25:
                        return [ 1,  1, 17,]
                    else:  # if self.acce_corr_xz > -0.25
                        if self.acce_mean_z <= 1.07:
                            if self.acce_energy_y <= 38.24:
                                return [0, 0, 4,]
                            else:  # if self.acce_energy_y > 38.24
                                return [ 1, 53,  4,]
                        else:  # if self.acce_mean_z > 1.07
                            return [0, 0, 7,]
        else:  # if self.gyro_mean_y > 6.44
            if self.n_samples <= 9.5:
                return [ 0,  2, 16,]
            else:  # if self.n_samples > 9.5
                return [  2, 163,  14,]

    def decision_tree_17(self):
        if self.gyro_energy_y <= 490.32:
            if self.n_samples <= 11.5:
                if self.acce_max_x <= 0.8:
                    if self.acce_min_x <= 0.22:
                        if self.acce_variance_x <= 0.02:
                            return [0, 0, 6,]
                        else:  # if self.acce_variance_x > 0.02
                            return [ 0, 12,  2,]
                    else:  # if self.acce_min_x > 0.22
                        return [9, 0, 0,]
                else:  # if self.acce_max_x > 0.8
                    if self.acce_energy_x <= 97.13:
                        if self.acce_skew_x <= 2.61:
                            return [  0,   3, 278,]
                        else:  # if self.acce_skew_x > 2.61
                            return [0, 2, 0,]
                    else:  # if self.acce_energy_x > 97.13
                        return [0, 8, 2,]
            else:  # if self.n_samples > 11.5
                if self.gyro_skew_y <= 0.56:
                    if self.gyro_std_z <= 2.56:
                        if self.gyro_rms_z <= 8.77:
                            return [0, 3, 0,]
                        else:  # if self.gyro_rms_z > 8.77
                            return [0, 0, 2,]
                    else:  # if self.gyro_std_z > 2.56
                        return [29,  0,  0,]
                else:  # if self.gyro_skew_y > 0.56
                    return [ 2, 81,  2,]
        else:  # if self.gyro_energy_y > 490.32
            if self.gyro_skew_y <= -0.83:
                if self.gyro_kurt_x <= -1.5:
                    if self.gyro_skew_y <= -1.37:
                        return [ 0, 45,  3,]
                    else:  # if self.gyro_skew_y > -1.37
                        if self.acce_corr_xz <= 0.43:
                            return [ 1,  0, 11,]
                        else:  # if self.acce_corr_xz > 0.43
                            return [0, 2, 0,]
                else:  # if self.gyro_kurt_x > -1.5
                    return [  0, 112,   2,]
            else:  # if self.gyro_skew_y > -0.83
                if self.gyro_variance_y <= 16.49:
                    if self.gyro_kurt_y <= -1.19:
                        if self.gyro_rms_y <= 7.84:
                            return [242,   0,   0,]
                        else:  # if self.gyro_rms_y > 7.84
                            return [0, 2, 0,]
                    else:  # if self.gyro_kurt_y > -1.19
                        if self.gyro_kurt_z <= -0.6:
                            return [1, 0, 2,]
                        else:  # if self.gyro_kurt_z > -0.6
                            return [0, 3, 0,]
                else:  # if self.gyro_variance_y > 16.49
                    if self.acce_std_x <= 0.16:
                        return [ 0, 12,  0,]
                    else:  # if self.acce_std_x > 0.16
                        if self.gyro_mean_y <= 4.78:
                            return [0, 4, 0,]
                        else:  # if self.gyro_mean_y > 4.78
                            return [ 0,  2, 14,]

    def decision_tree_18(self):
        if self.n_samples <= 14.5:
            if self.acce_variance_x <= 0.02:
                if self.gyro_mean_y <= 6.08:
                    if self.gyro_rms_z <= 7.33:
                        if self.acce_variance_x <= 0.01:
                            return [2, 3, 3,]
                        else:  # if self.acce_variance_x > 0.01
                            return [36,  0,  0,]
                    else:  # if self.gyro_rms_z > 7.33
                        return [ 0, 30,  1,]
                else:  # if self.gyro_mean_y > 6.08
                    return [ 1, 48,  0,]
            else:  # if self.acce_variance_x > 0.02
                if self.gyro_std_y <= 3.78:
                    if self.acce_energy_x <= 47.81:
                        if self.gyro_energy_y <= 558.12:
                            if self.acce_rms_x <= 0.49:
                                return [ 3, 13,  2,]
                            else:  # if self.acce_rms_x > 0.49
                                if self.acce_range_x <= 3.88:
                                    if self.gyro_kurt_y <= -0.82:
                                        return [2, 1, 0,]
                                    else:  # if self.gyro_kurt_y > -0.82
                                        return [ 0,  2, 51,]
                                else:  # if self.acce_range_x > 3.88
                                    if self.gyro_rms_y <= 3.92:
                                        return [ 0, 14,  3,]
                                    else:  # if self.gyro_rms_y > 3.92
                                        return [1, 0, 8,]
                        else:  # if self.gyro_energy_y > 558.12
                            return [ 2, 33,  4,]
                    else:  # if self.acce_energy_x > 47.81
                        return [  0, 111,   9,]
                else:  # if self.gyro_std_y > 3.78
                    if self.acce_range_x <= 3.97:
                        if self.n_samples <= 11.5:
                            if self.acce_energy_x <= 113.85:
                                return [  0,   5, 212,]
                            else:  # if self.acce_energy_x > 113.85
                                return [0, 3, 0,]
                        else:  # if self.n_samples > 11.5
                            if self.acce_kurt_x <= 0.54:
                                return [0, 9, 0,]
                            else:  # if self.acce_kurt_x > 0.54
                                return [0, 0, 4,]
                    else:  # if self.acce_range_x > 3.97
                        if self.gyro_energy_z <= 815.37:
                            if self.gyro_std_y <= 4.06:
                                return [0, 4, 0,]
                            else:  # if self.gyro_std_y > 4.06
                                return [0, 2, 9,]
                        else:  # if self.gyro_energy_z > 815.37
                            return [ 0, 10,  0,]
        else:  # if self.n_samples > 14.5
            if self.gyro_rms_y <= 7.4:
                if self.acce_min_z <= 0.77:
                    return [248,   1,   0,]
                else:  # if self.acce_min_z > 0.77
                    return [0, 5, 0,]
            else:  # if self.gyro_rms_y > 7.4
                return [0, 4, 0,]

    def decision_tree_19(self):
        if self.gyro_energy_y <= 504.76:
            if self.acce_min_z <= 0.81:
                if self.acce_range_x <= 3.78:
                    if self.gyro_energy_y <= 344.65:
                        if self.acce_max_x <= 1.03:
                            return [ 5, 24,  9,]
                        else:  # if self.acce_max_x > 1.03
                            return [ 0,  3, 41,]
                    else:  # if self.gyro_energy_y > 344.65
                        if self.acce_energy_x <= 9.19:
                            return [35,  0,  0,]
                        else:  # if self.acce_energy_x > 9.19
                            return [0, 1, 6,]
                else:  # if self.acce_range_x > 3.78
                    if self.acce_variance_z <= 0.14:
                        if self.acce_mean_z <= 0.91:
                            return [5, 1, 0,]
                        else:  # if self.acce_mean_z > 0.91
                            if self.acce_skew_z <= 1.92:
                                return [ 2, 58,  4,]
                            else:  # if self.acce_skew_z > 1.92
                                return [0, 0, 4,]
                    else:  # if self.acce_variance_z > 0.14
                        return [6, 0, 2,]
            else:  # if self.acce_min_z > 0.81
                if self.gyro_std_x <= 3.62:
                    if self.gyro_kurt_y <= -1.59:
                        if self.gyro_energy_y <= 491.4:
                            return [ 0,  0, 11,]
                        else:  # if self.gyro_energy_y > 491.4
                            return [0, 3, 0,]
                    else:  # if self.gyro_kurt_y > -1.59
                        if self.acce_mean_y <= 2.79:
                            return [ 0, 22,  0,]
                        else:  # if self.acce_mean_y > 2.79
                            return [0, 1, 4,]
                else:  # if self.gyro_std_x > 3.62
                    if self.n_samples <= 11.5:
                        return [  0,   1, 173,]
                    else:  # if self.n_samples > 11.5
                        if self.acce_skew_z <= -0.91:
                            return [0, 0, 3,]
                        else:  # if self.acce_skew_z > -0.91
                            return [ 0, 16,  0,]
        else:  # if self.gyro_energy_y > 504.76
            if self.gyro_kurt_y <= -0.98:
                if self.gyro_std_x <= 4.18:
                    if self.gyro_variance_z <= 6.31:
                        return [0, 8, 3,]
                    else:  # if self.gyro_variance_z > 6.31
                        if self.gyro_std_y <= 1.72:
                            return [0, 4, 3,]
                        else:  # if self.gyro_std_y > 1.72
                            return [251,   2,   1,]
                else:  # if self.gyro_std_x > 4.18
                    return [ 1, 12,  3,]
            else:  # if self.gyro_kurt_y > -0.98
                if self.n_samples <= 8.5:
                    return [0, 0, 4,]
                else:  # if self.n_samples > 8.5
                    return [  0, 155,  12,]

    def decision_tree_20(self):
        if self.gyro_kurt_y <= -0.98:
            if self.acce_mean_z <= 0.97:
                if self.acce_energy_z <= 7.07:
                    return [ 1,  2, 17,]
                else:  # if self.acce_energy_z > 7.07
                    if self.gyro_rms_x <= 7.68:
                        if self.gyro_std_y <= 1.82:
                            return [0, 3, 0,]
                        else:  # if self.gyro_std_y > 1.82
                            return [247,   2,   1,]
                    else:  # if self.gyro_rms_x > 7.68
                        return [2, 2, 3,]
            else:  # if self.acce_mean_z > 0.97
                if self.gyro_energy_x <= 503.2:
                    if self.gyro_mean_z <= 3.38:
                        return [ 0, 15,  3,]
                    else:  # if self.gyro_mean_z > 3.38
                        if self.gyro_std_y <= 3.69:
                            if self.gyro_std_y <= 1.5:
                                return [0, 0, 3,]
                            else:  # if self.gyro_std_y > 1.5
                                return [8, 0, 0,]
                        else:  # if self.gyro_std_y > 3.69
                            return [  0,   4, 153,]
                else:  # if self.gyro_energy_x > 503.2
                    if self.gyro_rms_z <= 7.17:
                        if self.gyro_energy_z <= 471.94:
                            return [0, 1, 2,]
                        else:  # if self.gyro_energy_z > 471.94
                            if self.gyro_variance_z <= 17.32:
                                return [44,  0,  0,]
                            else:  # if self.gyro_variance_z > 17.32
                                return [0, 3, 0,]
                    else:  # if self.gyro_rms_z > 7.17
                        if self.acce_rms_y <= 3.0:
                            return [ 0, 28,  1,]
                        else:  # if self.acce_rms_y > 3.0
                            if self.acce_range_x <= 3.98:
                                return [ 0,  5, 17,]
                            else:  # if self.acce_range_x > 3.98
                                return [0, 6, 0,]
        else:  # if self.gyro_kurt_y > -0.98
            if self.acce_rms_z <= 1.13:
                if self.acce_energy_z <= 9.12:
                    if self.acce_skew_x <= -0.32:
                        return [ 0, 12,  0,]
                    else:  # if self.acce_skew_x > -0.32
                        if self.n_samples <= 13.5:
                            if self.acce_range_x <= 0.39:
                                return [0, 2, 0,]
                            else:  # if self.acce_range_x > 0.39
                                return [ 0,  1, 39,]
                        else:  # if self.n_samples > 13.5
                            return [3, 0, 0,]
                else:  # if self.acce_energy_z > 9.12
                    return [  0, 206,  17,]
            else:  # if self.acce_rms_z > 1.13
                if self.acce_std_x <= 0.11:
                    return [0, 8, 0,]
                else:  # if self.acce_std_x > 0.11
                    return [ 2,  2, 34,]

    def decision_tree_21(self):
        if self.gyro_rms_z <= 7.24:
            if self.gyro_energy_x <= 333.42:
                if self.gyro_rms_x <= 5.52:
                    if self.gyro_kurt_z <= -0.82:
                        if self.gyro_energy_y <= 286.6:
                            return [ 0, 19,  2,]
                        else:  # if self.gyro_energy_y > 286.6
                            return [6, 3, 4,]
                    else:  # if self.gyro_kurt_z > -0.82
                        return [ 0, 60,  2,]
                else:  # if self.gyro_rms_x > 5.52
                    return [ 0,  0, 17,]
            else:  # if self.gyro_energy_x > 333.42
                if self.gyro_std_x <= 4.2:
                    if self.gyro_variance_x <= 7.67:
                        return [0, 3, 1,]
                    else:  # if self.gyro_variance_x > 7.67
                        if self.gyro_std_z <= 4.05:
                            return [294,   0,   0,]
                        else:  # if self.gyro_std_z > 4.05
                            if self.acce_rms_z <= 1.04:
                                return [0, 4, 0,]
                            else:  # if self.acce_rms_z > 1.04
                                return [0, 0, 3,]
                else:  # if self.gyro_std_x > 4.2
                    if self.acce_energy_x <= 91.19:
                        if self.n_samples <= 12.5:
                            return [ 0,  0, 18,]
                        else:  # if self.n_samples > 12.5
                            return [0, 4, 0,]
                    else:  # if self.acce_energy_x > 91.19
                        return [ 0, 18,  1,]
        else:  # if self.gyro_rms_z > 7.24
            if self.gyro_energy_y <= 569.68:
                if self.acce_range_x <= 0.36:
                    if self.n_samples <= 8.5:
                        return [0, 0, 2,]
                    else:  # if self.n_samples > 8.5
                        return [ 0, 30,  0,]
                else:  # if self.acce_range_x > 0.36
                    if self.acce_std_x <= 1.85:
                        if self.acce_energy_y <= 161.92:
                            if self.gyro_kurt_z <= 4.21:
                                if self.acce_energy_y <= 3.18:
                                    return [0, 3, 0,]
                                else:  # if self.acce_energy_y > 3.18
                                    if self.acce_energy_x <= 118.01:
                                        return [  0,   5, 224,]
                                    else:  # if self.acce_energy_x > 118.01
                                        return [0, 2, 0,]
                            else:  # if self.gyro_kurt_z > 4.21
                                if self.gyro_rms_z <= 8.23:
                                    return [ 0, 13,  0,]
                                else:  # if self.gyro_rms_z > 8.23
                                    return [ 0,  0, 18,]
                        else:  # if self.acce_energy_y > 161.92
                            return [0, 7, 0,]
                    else:  # if self.acce_std_x > 1.85
                        return [ 0, 22,  0,]
            else:  # if self.gyro_energy_y > 569.68
                return [  5, 103,   6,]

