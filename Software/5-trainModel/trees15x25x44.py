class RandomForestOptimized:    
    def __init__(self):
            pass
    
    def score(self, n_samples, gyro_std_y, acce_min_z, gyro_kurt_y, gyro_variance_y, gyro_std_x, gyro_kurt_z, gyro_skew_y, gyro_energy_y, gyro_skew_z, gyro_kurt_x, gyro_mean_z, gyro_mean_y, gyro_variance_z, acce_energy_x, acce_range_x, gyro_rms_y, acce_std_z, acce_corr_xz, acce_rms_x, gyro_rms_z, acce_max_x, acce_skew_x, acce_energy_z, gyro_std_z, gyro_energy_x, acce_variance_z, gyro_energy_z, acce_variance_x, acce_std_x, gyro_rms_x, acce_mean_z, acce_min_x, acce_rms_z, gyro_range_y, acce_skew_z, acce_rms_y, gyro_corr_xz, acce_kurt_x, gyro_max_z, gyro_variance_x, gyro_min_x, acce_max_z, gyro_corr_xy):
        self.n_samples = n_samples
        self.gyro_std_y = gyro_std_y
        self.acce_min_z = acce_min_z
        self.gyro_kurt_y = gyro_kurt_y
        self.gyro_variance_y = gyro_variance_y
        self.gyro_std_x = gyro_std_x
        self.gyro_kurt_z = gyro_kurt_z
        self.gyro_skew_y = gyro_skew_y
        self.gyro_energy_y = gyro_energy_y
        self.gyro_skew_z = gyro_skew_z
        self.gyro_kurt_x = gyro_kurt_x
        self.gyro_mean_z = gyro_mean_z
        self.gyro_mean_y = gyro_mean_y
        self.gyro_variance_z = gyro_variance_z
        self.acce_energy_x = acce_energy_x
        self.acce_range_x = acce_range_x
        self.gyro_rms_y = gyro_rms_y
        self.acce_std_z = acce_std_z
        self.acce_corr_xz = acce_corr_xz
        self.acce_rms_x = acce_rms_x
        self.gyro_rms_z = gyro_rms_z
        self.acce_max_x = acce_max_x
        self.acce_skew_x = acce_skew_x
        self.acce_energy_z = acce_energy_z
        self.gyro_std_z = gyro_std_z
        self.gyro_energy_x = gyro_energy_x
        self.acce_variance_z = acce_variance_z
        self.gyro_energy_z = gyro_energy_z
        self.acce_variance_x = acce_variance_x
        self.acce_std_x = acce_std_x
        self.gyro_rms_x = gyro_rms_x
        self.acce_mean_z = acce_mean_z
        self.acce_min_x = acce_min_x
        self.acce_rms_z = acce_rms_z
        self.gyro_range_y = gyro_range_y
        self.acce_skew_z = acce_skew_z
        self.acce_rms_y = acce_rms_y
        self.gyro_corr_xz = gyro_corr_xz
        self.acce_kurt_x = acce_kurt_x
        self.gyro_max_z = gyro_max_z
        self.gyro_variance_x = gyro_variance_x
        self.gyro_min_x = gyro_min_x
        self.acce_max_z = acce_max_z
        self.gyro_corr_xy = gyro_corr_xy
    
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
    
        trees_values = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14]
    
        return [sum(col) / len(col) for col in zip(*trees_values)]

    def decision_tree_0(self):
        if self.gyro_std_x <= 4.11:
            if self.gyro_std_y <= 3.37:
                if self.acce_std_z <= 0.34:
                    if self.gyro_kurt_z <= -1.63:
                        if self.acce_min_z <= 0.55:
                            return [6, 0, 0,]
                        else:  # if self.acce_min_z > 0.55
                            return [0, 3, 2,]
                    else:  # if self.gyro_kurt_z > -1.63
                        return [  3, 114,   4,]
                else:  # if self.acce_std_z > 0.34
                    if self.gyro_kurt_y <= -0.2:
                        if self.gyro_kurt_x <= -0.03:
                            return [10,  0,  0,]
                        else:  # if self.gyro_kurt_x > -0.03
                            return [0, 3, 0,]
                    else:  # if self.gyro_kurt_y > -0.2
                        if self.gyro_mean_y <= 1.38:
                            return [0, 1, 7,]
                        else:  # if self.gyro_mean_y > 1.38
                            return [0, 7, 0,]
            else:  # if self.gyro_std_y > 3.37
                if self.gyro_std_y <= 3.9:
                    if self.acce_min_z <= 0.7:
                        if self.acce_std_x <= 0.06:
                            return [1, 7, 0,]
                        else:  # if self.acce_std_x > 0.06
                            if self.n_samples <= 11.5:
                                return [2, 4, 2,]
                            else:  # if self.n_samples > 11.5
                                return [289,   3,   0,]
                    else:  # if self.acce_min_z > 0.7
                        if self.acce_variance_z <= 0.07:
                            if self.n_samples <= 18.5:
                                return [ 0, 23,  1,]
                            else:  # if self.n_samples > 18.5
                                return [3, 0, 0,]
                        else:  # if self.acce_variance_z > 0.07
                            return [0, 0, 3,]
                else:  # if self.gyro_std_y > 3.9
                    if self.acce_range_x <= 0.36:
                        return [ 0, 19,  0,]
                    else:  # if self.acce_range_x > 0.36
                        if self.gyro_variance_y <= 17.32:
                            if self.acce_energy_x <= 20.72:
                                return [5, 1, 3,]
                            else:  # if self.acce_energy_x > 20.72
                                return [ 0, 14,  1,]
                        else:  # if self.gyro_variance_y > 17.32
                            if self.gyro_variance_y <= 19.35:
                                return [ 0,  0, 39,]
                            else:  # if self.gyro_variance_y > 19.35
                                return [0, 9, 5,]
        else:  # if self.gyro_std_x > 4.11
            if self.acce_energy_x <= 91.09:
                if self.gyro_energy_y <= 575.32:
                    if self.gyro_energy_x <= 573.32:
                        return [  0,  10, 205,]
                    else:  # if self.gyro_energy_x > 573.32
                        return [0, 9, 3,]
                else:  # if self.gyro_energy_y > 575.32
                    if self.gyro_rms_y <= 7.03:
                        return [5, 0, 0,]
                    else:  # if self.gyro_rms_y > 7.03
                        if self.gyro_energy_x <= 329.29:
                            return [0, 0, 4,]
                        else:  # if self.gyro_energy_x > 329.29
                            return [ 0, 21,  3,]
            else:  # if self.acce_energy_x > 91.09
                if self.gyro_std_y <= 4.21:
                    return [ 0, 38,  0,]
                else:  # if self.gyro_std_y > 4.21
                    return [0, 2, 5,]

    def decision_tree_1(self):
        if self.acce_min_z <= 0.62:
            if self.gyro_rms_z <= 7.24:
                if self.gyro_variance_z <= 14.95:
                    if self.gyro_energy_z <= 253.18:
                        if self.gyro_kurt_x <= -1.24:
                            return [1, 3, 4,]
                        else:  # if self.gyro_kurt_x > -1.24
                            return [ 0, 19,  0,]
                    else:  # if self.gyro_energy_z > 253.18
                        return [277,   0,   0,]
                else:  # if self.gyro_variance_z > 14.95
                    if self.acce_mean_z <= 0.92:
                        if self.acce_energy_x <= 24.31:
                            return [ 1,  0, 18,]
                        else:  # if self.acce_energy_x > 24.31
                            return [0, 2, 0,]
                    else:  # if self.acce_mean_z > 0.92
                        if self.acce_max_z <= 3.93:
                            return [ 0, 12,  0,]
                        else:  # if self.acce_max_z > 3.93
                            if self.acce_rms_y <= 0.99:
                                return [3, 0, 0,]
                            else:  # if self.acce_rms_y > 0.99
                                return [0, 1, 7,]
            else:  # if self.gyro_rms_z > 7.24
                if self.acce_min_x <= 0.41:
                    if self.acce_variance_z <= 0.14:
                        return [ 1, 36,  0,]
                    else:  # if self.acce_variance_z > 0.14
                        return [1, 0, 3,]
                else:  # if self.acce_min_x > 0.41
                    if self.gyro_energy_x <= 480.21:
                        if self.acce_energy_x <= 3.64:
                            return [2, 0, 0,]
                        else:  # if self.acce_energy_x > 3.64
                            return [ 0,  0, 17,]
                    else:  # if self.gyro_energy_x > 480.21
                        if self.gyro_std_z <= 3.92:
                            return [ 0, 21,  1,]
                        else:  # if self.gyro_std_z > 3.92
                            return [0, 0, 2,]
        else:  # if self.acce_min_z > 0.62
            if self.gyro_rms_y <= 7.81:
                if self.acce_energy_z <= 12.4:
                    if self.acce_rms_y <= 3.0:
                        if self.acce_kurt_x <= -0.68:
                            if self.gyro_energy_x <= 117.58:
                                return [0, 6, 0,]
                            else:  # if self.gyro_energy_x > 117.58
                                if self.acce_max_x <= 2.08:
                                    return [0, 2, 0,]
                                else:  # if self.acce_max_x > 2.08
                                    return [ 0,  0, 42,]
                        else:  # if self.acce_kurt_x > -0.68
                            return [ 0, 18,  5,]
                    else:  # if self.acce_rms_y > 3.0
                        if self.gyro_std_x <= 1.5:
                            return [3, 1, 0,]
                        else:  # if self.gyro_std_x > 1.5
                            return [  0,   5, 154,]
                else:  # if self.acce_energy_z > 12.4
                    if self.acce_std_z <= 0.26:
                        if self.gyro_max_z <= 8.84:
                            return [4, 1, 0,]
                        else:  # if self.gyro_max_z > 8.84
                            return [ 9, 68,  2,]
                    else:  # if self.acce_std_z > 0.26
                        return [ 0,  0, 20,]
            else:  # if self.gyro_rms_y > 7.81
                if self.gyro_energy_y <= 597.92:
                    return [ 0,  0, 12,]
                else:  # if self.gyro_energy_y > 597.92
                    return [  0, 109,   6,]

    def decision_tree_2(self):
        if self.gyro_std_y <= 3.94:
            if self.n_samples <= 14.5:
                if self.acce_corr_xz <= 0.12:
                    if self.gyro_kurt_y <= -1.14:
                        if self.gyro_variance_y <= 4.26:
                            return [0, 9, 0,]
                        else:  # if self.gyro_variance_y > 4.26
                            return [37,  1,  0,]
                    else:  # if self.gyro_kurt_y > -1.14
                        if self.gyro_energy_y <= 582.17:
                            if self.acce_corr_xz <= -0.63:
                                if self.acce_rms_x <= 1.78:
                                    return [ 0, 17,  0,]
                                else:  # if self.acce_rms_x > 1.78
                                    return [0, 0, 2,]
                            else:  # if self.acce_corr_xz > -0.63
                                if self.gyro_skew_y <= 3.0:
                                    return [ 0,  2, 65,]
                                else:  # if self.gyro_skew_y > 3.0
                                    return [0, 5, 0,]
                        else:  # if self.gyro_energy_y > 582.17
                            if self.acce_variance_x <= 2.35:
                                return [ 0, 52,  1,]
                            else:  # if self.acce_variance_x > 2.35
                                return [0, 0, 4,]
                else:  # if self.acce_corr_xz > 0.12
                    if self.acce_min_z <= 0.12:
                        if self.acce_variance_z <= 0.68:
                            return [ 0,  0, 12,]
                        else:  # if self.acce_variance_z > 0.68
                            return [0, 9, 0,]
                    else:  # if self.acce_min_z > 0.12
                        if self.acce_corr_xz <= 0.43:
                            if self.n_samples <= 10.5:
                                if self.gyro_kurt_y <= 4.93:
                                    if self.gyro_range_y <= 8.95:
                                        return [0, 2, 0,]
                                    else:  # if self.gyro_range_y > 8.95
                                        return [ 0,  0, 11,]
                                else:  # if self.gyro_kurt_y > 4.93
                                    return [0, 4, 0,]
                            else:  # if self.n_samples > 10.5
                                return [ 1, 42,  0,]
                        else:  # if self.acce_corr_xz > 0.43
                            return [ 1, 87,  0,]
            else:  # if self.n_samples > 14.5
                if self.gyro_variance_x <= 17.7:
                    return [271,   2,   0,]
                else:  # if self.gyro_variance_x > 17.7
                    return [0, 7, 0,]
        else:  # if self.gyro_std_y > 3.94
            if self.n_samples <= 11.5:
                if self.gyro_rms_z <= 4.26:
                    if self.acce_energy_x <= 31.23:
                        return [3, 0, 0,]
                    else:  # if self.acce_energy_x > 31.23
                        return [0, 2, 0,]
                else:  # if self.gyro_rms_z > 4.26
                    if self.n_samples <= 9.5:
                        return [  0,   0, 134,]
                    else:  # if self.n_samples > 9.5
                        if self.acce_max_x <= 0.38:
                            return [0, 5, 0,]
                        else:  # if self.acce_max_x > 0.38
                            if self.acce_skew_z <= -0.28:
                                return [0, 4, 1,]
                            else:  # if self.acce_skew_z > -0.28
                                return [ 0,  4, 69,]
            else:  # if self.n_samples > 11.5
                if self.gyro_kurt_z <= -1.83:
                    return [3, 0, 0,]
                else:  # if self.gyro_kurt_z > -1.83
                    return [ 0, 28,  2,]

    def decision_tree_3(self):
        if self.acce_min_z <= 0.69:
            if self.n_samples <= 14.5:
                if self.acce_min_z <= 0.22:
                    if self.gyro_energy_y <= 344.83:
                        if self.acce_variance_x <= 0.01:
                            return [0, 6, 0,]
                        else:  # if self.acce_variance_x > 0.01
                            if self.gyro_mean_z <= 0.86:
                                return [0, 2, 0,]
                            else:  # if self.gyro_mean_z > 0.86
                                return [ 0,  0, 39,]
                    else:  # if self.gyro_energy_y > 344.83
                        if self.gyro_rms_y <= 6.91:
                            if self.acce_rms_z <= 2.25:
                                return [33,  1,  0,]
                            else:  # if self.acce_rms_z > 2.25
                                return [0, 0, 2,]
                        else:  # if self.gyro_rms_y > 6.91
                            if self.gyro_kurt_x <= -1.75:
                                return [0, 0, 2,]
                            else:  # if self.gyro_kurt_x > -1.75
                                return [ 0, 13,  1,]
                else:  # if self.acce_min_z > 0.22
                    if self.gyro_std_z <= 3.8:
                        return [  6, 101,   2,]
                    else:  # if self.gyro_std_z > 3.8
                        if self.acce_rms_z <= 0.98:
                            return [ 0,  2, 16,]
                        else:  # if self.acce_rms_z > 0.98
                            return [ 0, 17,  0,]
            else:  # if self.n_samples > 14.5
                if self.gyro_mean_y <= 6.78:
                    return [222,   0,   0,]
                else:  # if self.gyro_mean_y > 6.78
                    return [0, 5, 0,]
        else:  # if self.acce_min_z > 0.69
            if self.acce_energy_z <= 12.36:
                if self.gyro_skew_y <= -1.42:
                    if self.gyro_mean_z <= 3.79:
                        return [ 0, 14,  0,]
                    else:  # if self.gyro_mean_z > 3.79
                        if self.gyro_energy_x <= 598.87:
                            return [ 0,  1, 10,]
                        else:  # if self.gyro_energy_x > 598.87
                            return [0, 3, 0,]
                else:  # if self.gyro_skew_y > -1.42
                    if self.acce_range_x <= 0.18:
                        return [1, 9, 1,]
                    else:  # if self.acce_range_x > 0.18
                        if self.acce_rms_y <= 2.49:
                            if self.gyro_variance_x <= 16.77:
                                return [0, 8, 0,]
                            else:  # if self.gyro_variance_x > 16.77
                                return [0, 0, 6,]
                        else:  # if self.acce_rms_y > 2.49
                            if self.gyro_skew_z <= 1.37:
                                if self.acce_range_x <= 3.98:
                                    return [  0,   1, 213,]
                                else:  # if self.acce_range_x > 3.98
                                    return [0, 2, 1,]
                            else:  # if self.gyro_skew_z > 1.37
                                return [0, 3, 0,]
            else:  # if self.acce_energy_z > 12.36
                if self.acce_rms_z <= 1.1:
                    if self.acce_skew_x <= 3.17:
                        return [  1, 122,   2,]
                    else:  # if self.acce_skew_x > 3.17
                        return [0, 0, 2,]
                else:  # if self.acce_rms_z > 1.1
                    if self.acce_energy_z <= 14.69:
                        return [ 0,  1, 26,]
                    else:  # if self.acce_energy_z > 14.69
                        return [0, 2, 0,]

    def decision_tree_4(self):
        if self.gyro_skew_y <= -1.15:
            if self.gyro_skew_y <= -1.36:
                if self.gyro_energy_y <= 498.22:
                    return [0, 0, 2,]
                else:  # if self.gyro_energy_y > 498.22
                    return [  0, 143,   4,]
            else:  # if self.gyro_skew_y > -1.36
                if self.gyro_energy_z <= 359.22:
                    return [ 0, 10,  0,]
                else:  # if self.gyro_energy_z > 359.22
                    return [0, 3, 7,]
        else:  # if self.gyro_skew_y > -1.15
            if self.gyro_std_y <= 3.96:
                if self.gyro_mean_y <= 3.05:
                    if self.acce_corr_xz <= 0.38:
                        if self.acce_skew_x <= 0.17:
                            if self.acce_mean_z <= 1.07:
                                if self.gyro_std_x <= 4.31:
                                    return [ 0, 18,  0,]
                                else:  # if self.gyro_std_x > 4.31
                                    return [0, 4, 4,]
                            else:  # if self.acce_mean_z > 1.07
                                return [0, 0, 4,]
                        else:  # if self.acce_skew_x > 0.17
                            if self.acce_rms_z <= 1.02:
                                if self.acce_skew_z <= 0.64:
                                    return [1, 8, 3,]
                                else:  # if self.acce_skew_z > 0.64
                                    return [ 2,  0, 18,]
                            else:  # if self.acce_rms_z > 1.02
                                return [ 0,  0, 36,]
                    else:  # if self.acce_corr_xz > 0.38
                        return [ 0, 61,  3,]
                else:  # if self.gyro_mean_y > 3.05
                    if self.gyro_kurt_y <= -1.19:
                        if self.gyro_kurt_z <= 0.1:
                            if self.acce_min_x <= 0.0:
                                return [0, 3, 0,]
                            else:  # if self.acce_min_x > 0.0
                                if self.gyro_corr_xz <= -0.26:
                                    return [1, 2, 2,]
                                else:  # if self.gyro_corr_xz > -0.26
                                    return [271,   2,   0,]
                        else:  # if self.gyro_kurt_z > 0.1
                            return [0, 4, 0,]
                    else:  # if self.gyro_kurt_y > -1.19
                        if self.acce_mean_z <= 1.14:
                            if self.acce_rms_x <= 1.35:
                                return [0, 5, 0,]
                            else:  # if self.acce_rms_x > 1.35
                                if self.acce_variance_x <= 3.18:
                                    return [ 0,  1, 12,]
                                else:  # if self.acce_variance_x > 3.18
                                    return [0, 3, 0,]
                        else:  # if self.acce_mean_z > 1.14
                            return [4, 0, 0,]
            else:  # if self.gyro_std_y > 3.96
                if self.acce_variance_x <= 0.01:
                    if self.acce_kurt_x <= -1.9:
                        return [2, 0, 4,]
                    else:  # if self.acce_kurt_x > -1.9
                        return [ 0, 14,  0,]
                else:  # if self.acce_variance_x > 0.01
                    if self.acce_energy_z <= 13.78:
                        if self.gyro_rms_z <= 4.39:
                            return [0, 4, 0,]
                        else:  # if self.gyro_rms_z > 4.39
                            return [  0,   2, 209,]
                    else:  # if self.acce_energy_z > 13.78
                        if self.acce_max_z <= 1.92:
                            return [ 0, 16,  0,]
                        else:  # if self.acce_max_z > 1.92
                            return [0, 1, 6,]

    def decision_tree_5(self):
        if self.gyro_variance_y <= 15.6:
            if self.gyro_mean_y <= 6.44:
                if self.gyro_kurt_y <= -1.12:
                    if self.gyro_rms_y <= 2.72:
                        return [0, 5, 3,]
                    else:  # if self.gyro_rms_y > 2.72
                        if self.n_samples <= 10.5:
                            return [0, 4, 0,]
                        else:  # if self.n_samples > 10.5
                            return [290,   0,   0,]
                else:  # if self.gyro_kurt_y > -1.12
                    if self.gyro_variance_z <= 6.55:
                        if self.gyro_energy_x <= 477.14:
                            if self.gyro_variance_z <= 0.07:
                                return [0, 0, 9,]
                            else:  # if self.gyro_variance_z > 0.07
                                return [0, 3, 0,]
                        else:  # if self.gyro_energy_x > 477.14
                            return [ 0, 44,  1,]
                    else:  # if self.gyro_variance_z > 6.55
                        if self.acce_energy_x <= 74.95:
                            if self.acce_skew_z <= 0.81:
                                if self.gyro_energy_x <= 392.04:
                                    if self.gyro_variance_x <= 16.68:
                                        return [0, 4, 0,]
                                    else:  # if self.gyro_variance_x > 16.68
                                        return [0, 0, 9,]
                                else:  # if self.gyro_energy_x > 392.04
                                    return [1, 9, 0,]
                            else:  # if self.acce_skew_z > 0.81
                                return [ 0,  0, 35,]
                        else:  # if self.acce_energy_x > 74.95
                            return [ 0, 24,  0,]
            else:  # if self.gyro_mean_y > 6.44
                if self.acce_energy_z <= 10.02:
                    if self.acce_energy_x <= 19.23:
                        return [ 2, 11,  0,]
                    else:  # if self.acce_energy_x > 19.23
                        if self.gyro_energy_y <= 685.28:
                            return [ 0,  0, 16,]
                        else:  # if self.gyro_energy_y > 685.28
                            return [0, 6, 0,]
                else:  # if self.acce_energy_z > 10.02
                    if self.gyro_variance_z <= 15.39:
                        return [  0, 125,   1,]
                    else:  # if self.gyro_variance_z > 15.39
                        if self.gyro_std_z <= 4.09:
                            return [0, 0, 7,]
                        else:  # if self.gyro_std_z > 4.09
                            return [0, 8, 2,]
        else:  # if self.gyro_variance_y > 15.6
            if self.gyro_energy_y <= 492.52:
                if self.acce_energy_x <= 92.85:
                    if self.n_samples <= 12.0:
                        if self.gyro_variance_y <= 20.21:
                            return [  2,   1, 210,]
                        else:  # if self.gyro_variance_y > 20.21
                            return [0, 3, 0,]
                    else:  # if self.n_samples > 12.0
                        return [0, 3, 1,]
                else:  # if self.acce_energy_x > 92.85
                    return [ 0, 12,  2,]
            else:  # if self.gyro_energy_y > 492.52
                if self.gyro_std_z <= 3.29:
                    if self.gyro_max_z <= 9.14:
                        return [ 0, 29,  1,]
                    else:  # if self.gyro_max_z > 9.14
                        return [0, 0, 3,]
                else:  # if self.gyro_std_z > 3.29
                    if self.acce_rms_y <= 2.49:
                        return [2, 2, 0,]
                    else:  # if self.acce_rms_y > 2.49
                        return [0, 0, 9,]

    def decision_tree_6(self):
        if self.gyro_variance_y <= 15.64:
            if self.acce_mean_z <= 0.98:
                if self.gyro_variance_y <= 10.89:
                    if self.gyro_kurt_z <= -1.65:
                        if self.gyro_variance_z <= 16.62:
                            return [7, 0, 0,]
                        else:  # if self.gyro_variance_z > 16.62
                            return [0, 4, 3,]
                    else:  # if self.gyro_kurt_z > -1.65
                        return [ 2, 49,  9,]
                else:  # if self.gyro_variance_y > 10.89
                    if self.gyro_rms_z <= 7.17:
                        if self.gyro_kurt_x <= 3.65:
                            if self.gyro_energy_y <= 337.4:
                                return [1, 3, 3,]
                            else:  # if self.gyro_energy_y > 337.4
                                return [245,   1,   0,]
                        else:  # if self.gyro_kurt_x > 3.65
                            return [0, 8, 0,]
                    else:  # if self.gyro_rms_z > 7.17
                        if self.acce_max_x <= 1.02:
                            if self.gyro_kurt_z <= -0.24:
                                return [3, 0, 1,]
                            else:  # if self.gyro_kurt_z > -0.24
                                return [0, 6, 0,]
                        else:  # if self.acce_max_x > 1.02
                            if self.n_samples <= 12.5:
                                return [ 0,  0, 20,]
                            else:  # if self.n_samples > 12.5
                                return [0, 4, 0,]
            else:  # if self.acce_mean_z > 0.98
                if self.n_samples <= 9.5:
                    return [ 0,  4, 45,]
                else:  # if self.n_samples > 9.5
                    if self.acce_max_z <= 3.84:
                        if self.gyro_kurt_y <= -1.53:
                            return [10,  0,  0,]
                        else:  # if self.gyro_kurt_y > -1.53
                            if self.acce_corr_xz <= -0.08:
                                if self.gyro_mean_z <= 5.54:
                                    return [ 0, 11,  0,]
                                else:  # if self.gyro_mean_z > 5.54
                                    if self.acce_max_x <= 0.44:
                                        return [0, 9, 0,]
                                    else:  # if self.acce_max_x > 0.44
                                        return [ 0,  1, 11,]
                            else:  # if self.acce_corr_xz > -0.08
                                return [  1, 159,   1,]
                    else:  # if self.acce_max_z > 3.84
                        if self.gyro_kurt_y <= -0.56:
                            if self.gyro_std_y <= 1.69:
                                return [0, 2, 0,]
                            else:  # if self.gyro_std_y > 1.69
                                return [26,  0,  0,]
                        else:  # if self.gyro_kurt_y > -0.56
                            if self.acce_corr_xz <= 0.13:
                                return [0, 0, 6,]
                            else:  # if self.acce_corr_xz > 0.13
                                return [ 0, 11,  0,]
        else:  # if self.gyro_variance_y > 15.64
            if self.gyro_energy_x <= 486.94:
                if self.gyro_mean_z <= 2.58:
                    return [0, 6, 0,]
                else:  # if self.gyro_mean_z > 2.58
                    return [  0,   2, 155,]
            else:  # if self.gyro_energy_x > 486.94
                if self.n_samples <= 11.5:
                    if self.acce_range_x <= 0.39:
                        return [0, 6, 0,]
                    else:  # if self.acce_range_x > 0.39
                        return [ 0,  1, 30,]
                else:  # if self.n_samples > 11.5
                    return [ 1, 28,  4,]

    def decision_tree_7(self):
        if self.n_samples <= 14.5:
            if self.n_samples <= 10.5:
                if self.acce_energy_x <= 2.31:
                    return [ 0, 24,  6,]
                else:  # if self.acce_energy_x > 2.31
                    if self.gyro_rms_z <= 4.97:
                        if self.acce_max_z <= 1.1:
                            return [0, 0, 3,]
                        else:  # if self.acce_max_z > 1.1
                            return [ 0, 11,  2,]
                    else:  # if self.gyro_rms_z > 4.97
                        if self.acce_energy_x <= 88.9:
                            if self.acce_skew_x <= 2.46:
                                return [  0,   4, 227,]
                            else:  # if self.acce_skew_x > 2.46
                                return [0, 3, 1,]
                        else:  # if self.acce_energy_x > 88.9
                            if self.gyro_energy_y <= 495.13:
                                return [0, 4, 7,]
                            else:  # if self.gyro_energy_y > 495.13
                                return [0, 6, 0,]
            else:  # if self.n_samples > 10.5
                if self.gyro_kurt_y <= -0.8:
                    if self.gyro_variance_y <= 14.05:
                        if self.acce_rms_z <= 1.01:
                            return [33,  0,  0,]
                        else:  # if self.acce_rms_z > 1.01
                            if self.acce_skew_z <= 1.69:
                                return [1, 7, 0,]
                            else:  # if self.acce_skew_z > 1.69
                                if self.gyro_corr_xz <= 0.64:
                                    return [0, 0, 5,]
                                else:  # if self.gyro_corr_xz > 0.64
                                    return [2, 0, 0,]
                    else:  # if self.gyro_variance_y > 14.05
                        if self.acce_corr_xz <= -0.01:
                            if self.acce_corr_xz <= -0.38:
                                return [0, 4, 2,]
                            else:  # if self.acce_corr_xz > -0.38
                                if self.acce_max_x <= 0.7:
                                    return [0, 2, 0,]
                                else:  # if self.acce_max_x > 0.7
                                    return [ 0,  0, 15,]
                        else:  # if self.acce_corr_xz > -0.01
                            if self.acce_rms_x <= 2.67:
                                if self.gyro_max_z <= 9.09:
                                    return [0, 9, 0,]
                                else:  # if self.gyro_max_z > 9.09
                                    if self.gyro_energy_z <= 912.26:
                                        return [0, 1, 9,]
                                    else:  # if self.gyro_energy_z > 912.26
                                        return [0, 3, 0,]
                            else:  # if self.acce_rms_x > 2.67
                                return [ 0, 17,  0,]
                else:  # if self.gyro_kurt_y > -0.8
                    if self.acce_min_z <= 0.22:
                        if self.acce_energy_x <= 10.61:
                            return [ 0,  1, 13,]
                        else:  # if self.acce_energy_x > 10.61
                            return [ 0, 14,  3,]
                    else:  # if self.acce_min_z > 0.22
                        if self.gyro_max_z <= 9.17:
                            return [  0, 170,   3,]
                        else:  # if self.gyro_max_z > 9.17
                            return [0, 0, 3,]
        else:  # if self.n_samples > 14.5
            if self.gyro_rms_z <= 7.95:
                if self.gyro_variance_z <= 17.33:
                    return [262,   1,   0,]
                else:  # if self.gyro_variance_z > 17.33
                    return [0, 5, 0,]
            else:  # if self.gyro_rms_z > 7.95
                return [ 0, 16,  0,]

    def decision_tree_8(self):
        if self.gyro_variance_y <= 15.63:
            if self.gyro_kurt_y <= -1.28:
                if self.gyro_std_y <= 1.77:
                    return [0, 5, 1,]
                else:  # if self.gyro_std_y > 1.77
                    if self.gyro_corr_xy <= -0.38:
                        return [2, 0, 3,]
                    else:  # if self.gyro_corr_xy > -0.38
                        if self.gyro_energy_x <= 247.18:
                            return [1, 3, 0,]
                        else:  # if self.gyro_energy_x > 247.18
                            return [285,   0,   0,]
            else:  # if self.gyro_kurt_y > -1.28
                if self.acce_std_z <= 1.03:
                    if self.gyro_mean_y <= 7.0:
                        if self.n_samples <= 9.5:
                            if self.acce_corr_xz <= 0.4:
                                return [ 0,  0, 23,]
                            else:  # if self.acce_corr_xz > 0.4
                                return [0, 3, 0,]
                        else:  # if self.n_samples > 9.5
                            if self.gyro_energy_y <= 167.75:
                                if self.gyro_std_y <= 3.35:
                                    return [ 0, 39,  6,]
                                else:  # if self.gyro_std_y > 3.35
                                    return [ 0,  0, 18,]
                            else:  # if self.gyro_energy_y > 167.75
                                if self.acce_max_z <= 1.09:
                                    if self.gyro_skew_z <= -0.99:
                                        return [0, 5, 0,]
                                    else:  # if self.gyro_skew_z > -0.99
                                        if self.gyro_kurt_z <= -0.14:
                                            return [5, 0, 2,]
                                        else:  # if self.gyro_kurt_z > -0.14
                                            return [0, 3, 0,]
                                else:  # if self.acce_max_z > 1.09
                                    return [ 2, 64,  0,]
                    else:  # if self.gyro_mean_y > 7.0
                        if self.gyro_kurt_z <= -1.79:
                            return [0, 0, 3,]
                        else:  # if self.gyro_kurt_z > -1.79
                            return [  0, 115,   6,]
                else:  # if self.acce_std_z > 1.03
                    if self.acce_std_x <= 0.07:
                        return [0, 5, 0,]
                    else:  # if self.acce_std_x > 0.07
                        if self.gyro_std_x <= 3.77:
                            return [3, 2, 1,]
                        else:  # if self.gyro_std_x > 3.77
                            return [ 0,  0, 26,]
        else:  # if self.gyro_variance_y > 15.63
            if self.n_samples <= 11.5:
                if self.gyro_rms_x <= 8.0:
                    if self.acce_max_x <= 0.48:
                        return [0, 4, 0,]
                    else:  # if self.acce_max_x > 0.48
                        if self.acce_skew_x <= -1.18:
                            return [0, 4, 0,]
                        else:  # if self.acce_skew_x > -1.18
                            if self.gyro_variance_x <= 5.87:
                                return [0, 2, 0,]
                            else:  # if self.gyro_variance_x > 5.87
                                return [  0,   3, 211,]
                else:  # if self.gyro_rms_x > 8.0
                    if self.gyro_skew_y <= 0.39:
                        return [0, 1, 4,]
                    else:  # if self.gyro_skew_y > 0.39
                        return [0, 4, 0,]
            else:  # if self.n_samples > 11.5
                if self.gyro_mean_z <= 8.73:
                    return [ 2, 27,  2,]
                else:  # if self.gyro_mean_z > 8.73
                    return [0, 0, 4,]

    def decision_tree_9(self):
        if self.n_samples <= 14.5:
            if self.gyro_mean_z <= 3.24:
                if self.acce_min_z <= 0.02:
                    if self.gyro_corr_xz <= 0.01:
                        return [0, 0, 6,]
                    else:  # if self.gyro_corr_xz > 0.01
                        return [0, 2, 0,]
                else:  # if self.acce_min_z > 0.02
                    return [  0, 127,   5,]
            else:  # if self.gyro_mean_z > 3.24
                if self.gyro_energy_z <= 721.72:
                    if self.acce_variance_x <= 0.02:
                        if self.gyro_mean_z <= 6.41:
                            if self.acce_variance_x <= 0.01:
                                if self.gyro_max_z <= 9.05:
                                    return [0, 0, 4,]
                                else:  # if self.gyro_max_z > 9.05
                                    return [0, 5, 0,]
                            else:  # if self.acce_variance_x > 0.01
                                if self.gyro_kurt_y <= -0.65:
                                    return [46,  0,  0,]
                                else:  # if self.gyro_kurt_y > -0.65
                                    return [0, 1, 1,]
                        else:  # if self.gyro_mean_z > 6.41
                            if self.gyro_range_y <= 8.87:
                                return [0, 0, 3,]
                            else:  # if self.gyro_range_y > 8.87
                                return [ 0, 15,  2,]
                    else:  # if self.acce_variance_x > 0.02
                        if self.gyro_std_y <= 3.66:
                            if self.acce_min_x <= 0.02:
                                if self.acce_std_z <= 0.29:
                                    return [ 0, 20,  0,]
                                else:  # if self.acce_std_z > 0.29
                                    if self.acce_max_x <= 3.99:
                                        return [0, 0, 5,]
                                    else:  # if self.acce_max_x > 3.99
                                        return [2, 2, 0,]
                            else:  # if self.acce_min_x > 0.02
                                return [ 2, 11, 42,]
                        else:  # if self.gyro_std_y > 3.66
                            if self.gyro_std_y <= 4.49:
                                return [  0,   9, 189,]
                            else:  # if self.gyro_std_y > 4.49
                                return [0, 2, 0,]
                else:  # if self.gyro_energy_z > 721.72
                    if self.gyro_kurt_y <= -1.17:
                        if self.gyro_variance_z <= 0.17:
                            return [ 0,  0, 17,]
                        else:  # if self.gyro_variance_z > 0.17
                            if self.gyro_max_z <= 9.13:
                                return [ 0, 19,  0,]
                            else:  # if self.gyro_max_z > 9.13
                                return [0, 1, 6,]
                    else:  # if self.gyro_kurt_y > -1.17
                        if self.acce_skew_z <= 1.92:
                            return [ 0, 70,  2,]
                        else:  # if self.acce_skew_z > 1.92
                            if self.acce_energy_z <= 15.52:
                                return [ 0, 10,  3,]
                            else:  # if self.acce_energy_z > 15.52
                                return [0, 0, 3,]
        else:  # if self.n_samples > 14.5
            if self.gyro_skew_y <= -1.02:
                return [0, 9, 0,]
            else:  # if self.gyro_skew_y > -1.02
                if self.n_samples <= 15.5:
                    if self.acce_rms_y <= 3.35:
                        return [23,  0,  0,]
                    else:  # if self.acce_rms_y > 3.35
                        return [0, 9, 0,]
                else:  # if self.n_samples > 15.5
                    return [225,   1,   0,]

    def decision_tree_10(self):
        if self.gyro_rms_z <= 7.18:
            if self.gyro_kurt_z <= -0.7:
                if self.gyro_std_z <= 3.88:
                    return [285,   1,   0,]
                else:  # if self.gyro_std_z > 3.88
                    if self.n_samples <= 11.5:
                        if self.acce_std_z <= 0.26:
                            return [ 0,  1, 39,]
                        else:  # if self.acce_std_z > 0.26
                            if self.acce_min_z <= 0.03:
                                return [0, 0, 7,]
                            else:  # if self.acce_min_z > 0.03
                                return [ 0, 13,  3,]
                    else:  # if self.n_samples > 11.5
                        if self.gyro_energy_z <= 632.04:
                            return [ 1, 24,  2,]
                        else:  # if self.gyro_energy_z > 632.04
                            return [7, 0, 0,]
            else:  # if self.gyro_kurt_z > -0.7
                if self.acce_energy_z <= 1.31:
                    return [0, 1, 3,]
                else:  # if self.acce_energy_z > 1.31
                    return [ 1, 87,  2,]
        else:  # if self.gyro_rms_z > 7.18
            if self.gyro_skew_z <= -2.49:
                if self.gyro_mean_z <= 7.98:
                    return [ 0, 58,  1,]
                else:  # if self.gyro_mean_z > 7.98
                    if self.acce_min_z <= 0.84:
                        if self.gyro_skew_z <= -2.81:
                            return [ 0, 29,  0,]
                        else:  # if self.gyro_skew_z > -2.81
                            return [0, 0, 5,]
                    else:  # if self.acce_min_z > 0.84
                        return [0, 0, 9,]
            else:  # if self.gyro_skew_z > -2.49
                if self.gyro_energy_y <= 571.94:
                    if self.acce_rms_x <= 0.89:
                        if self.acce_rms_y <= 3.36:
                            return [ 2, 16,  0,]
                        else:  # if self.acce_rms_y > 3.36
                            if self.acce_min_z <= 0.37:
                                return [0, 3, 0,]
                            else:  # if self.acce_min_z > 0.37
                                return [0, 0, 7,]
                    else:  # if self.acce_rms_x > 0.89
                        if self.gyro_energy_x <= 487.42:
                            if self.acce_skew_x <= 2.73:
                                return [  0,   1, 176,]
                            else:  # if self.acce_skew_x > 2.73
                                return [0, 2, 0,]
                        else:  # if self.gyro_energy_x > 487.42
                            if self.acce_range_x <= 3.92:
                                return [ 0,  1, 22,]
                            else:  # if self.acce_range_x > 3.92
                                if self.gyro_std_z <= 0.19:
                                    return [0, 0, 4,]
                                else:  # if self.gyro_std_z > 0.19
                                    return [ 0, 19,  2,]
                else:  # if self.gyro_energy_y > 571.94
                    if self.acce_rms_y <= 2.85:
                        if self.n_samples <= 18.0:
                            return [ 0, 40,  2,]
                        else:  # if self.n_samples > 18.0
                            return [2, 0, 0,]
                    else:  # if self.acce_rms_y > 2.85
                        if self.acce_range_x <= 3.94:
                            if self.gyro_std_z <= 3.34:
                                return [4, 1, 0,]
                            else:  # if self.gyro_std_z > 3.34
                                return [0, 0, 8,]
                        else:  # if self.acce_range_x > 3.94
                            return [0, 8, 0,]

    def decision_tree_11(self):
        if self.gyro_variance_y <= 15.52:
            if self.gyro_kurt_z <= -0.68:
                if self.gyro_kurt_y <= -0.98:
                    if self.gyro_skew_z <= 0.82:
                        if self.gyro_max_z <= 9.17:
                            if self.gyro_corr_xy <= -0.52:
                                return [0, 0, 1,]
                            else:  # if self.gyro_corr_xy > -0.52
                                return [280,   0,   0,]
                        else:  # if self.gyro_max_z > 9.17
                            return [0, 2, 0,]
                    else:  # if self.gyro_skew_z > 0.82
                        if self.gyro_variance_z <= 12.89:
                            return [7, 0, 0,]
                        else:  # if self.gyro_variance_z > 12.89
                            return [0, 5, 0,]
                else:  # if self.gyro_kurt_y > -0.98
                    if self.acce_corr_xz <= 0.1:
                        if self.acce_corr_xz <= -0.57:
                            return [ 0, 16,  0,]
                        else:  # if self.acce_corr_xz > -0.57
                            if self.acce_range_x <= 0.42:
                                return [0, 2, 0,]
                            else:  # if self.acce_range_x > 0.42
                                return [ 0,  0, 28,]
                    else:  # if self.acce_corr_xz > 0.1
                        if self.acce_max_z <= 1.15:
                            if self.n_samples <= 11.5:
                                return [0, 0, 6,]
                            else:  # if self.n_samples > 11.5
                                return [2, 1, 0,]
                        else:  # if self.acce_max_z > 1.15
                            return [ 0, 55,  1,]
            else:  # if self.gyro_kurt_z > -0.68
                if self.n_samples <= 9.5:
                    if self.gyro_range_y <= 4.55:
                        return [0, 1, 0,]
                    else:  # if self.gyro_range_y > 4.55
                        return [ 0,  0, 35,]
                else:  # if self.n_samples > 9.5
                    if self.acce_min_z <= 0.07:
                        if self.gyro_rms_x <= 7.77:
                            if self.acce_std_z <= 0.76:
                                return [ 0,  0, 10,]
                            else:  # if self.acce_std_z > 0.76
                                return [5, 0, 1,]
                        else:  # if self.gyro_rms_x > 7.77
                            return [0, 5, 0,]
                    else:  # if self.acce_min_z > 0.07
                        return [  1, 168,   4,]
        else:  # if self.gyro_variance_y > 15.52
            if self.n_samples <= 11.5:
                if self.gyro_std_x <= 3.33:
                    if self.gyro_rms_y <= 6.09:
                        return [0, 0, 1,]
                    else:  # if self.gyro_rms_y > 6.09
                        return [0, 9, 0,]
                else:  # if self.gyro_std_x > 3.33
                    if self.acce_range_x <= 0.36:
                        if self.acce_kurt_x <= -1.44:
                            return [0, 0, 1,]
                        else:  # if self.acce_kurt_x > -1.44
                            return [0, 5, 0,]
                    else:  # if self.acce_range_x > 0.36
                        if self.acce_energy_x <= 113.85:
                            return [  0,   0, 205,]
                        else:  # if self.acce_energy_x > 113.85
                            return [0, 1, 0,]
            else:  # if self.n_samples > 11.5
                if self.gyro_mean_z <= 8.75:
                    return [ 1, 38,  0,]
                else:  # if self.gyro_mean_z > 8.75
                    return [0, 0, 2,]

    def decision_tree_12(self):
        if self.n_samples <= 14.5:
            if self.gyro_skew_y <= -1.15:
                if self.gyro_energy_y <= 584.78:
                    if self.gyro_rms_y <= 7.65:
                        return [0, 8, 0,]
                    else:  # if self.gyro_rms_y > 7.65
                        return [ 0,  0, 12,]
                else:  # if self.gyro_energy_y > 584.78
                    if self.acce_variance_x <= 3.81:
                        return [  0, 113,   2,]
                    else:  # if self.acce_variance_x > 3.81
                        return [0, 0, 3,]
            else:  # if self.gyro_skew_y > -1.15
                if self.gyro_std_y <= 4.13:
                    if self.gyro_kurt_y <= -1.5:
                        if self.acce_std_x <= 0.16:
                            if self.gyro_range_y <= 4.56:
                                return [0, 2, 0,]
                            else:  # if self.gyro_range_y > 4.56
                                return [31,  0,  0,]
                        else:  # if self.acce_std_x > 0.16
                            if self.acce_min_x <= 0.33:
                                return [ 0, 14,  0,]
                            else:  # if self.acce_min_x > 0.33
                                return [0, 0, 3,]
                    else:  # if self.gyro_kurt_y > -1.5
                        if self.acce_min_x <= 0.05:
                            if self.gyro_energy_x <= 449.2:
                                if self.gyro_rms_z <= 6.5:
                                    return [ 0, 17,  1,]
                                else:  # if self.gyro_rms_z > 6.5
                                    return [ 0,  1, 16,]
                            else:  # if self.gyro_energy_x > 449.2
                                return [ 1, 45,  4,]
                        else:  # if self.acce_min_x > 0.05
                            if self.acce_max_x <= 1.04:
                                if self.acce_min_x <= 0.16:
                                    return [3, 2, 5,]
                                else:  # if self.acce_min_x > 0.16
                                    return [ 1, 17,  1,]
                            else:  # if self.acce_max_x > 1.04
                                if self.gyro_skew_z <= 0.0:
                                    if self.n_samples <= 12.5:
                                        return [ 1,  0, 56,]
                                    else:  # if self.n_samples > 12.5
                                        return [0, 2, 0,]
                                else:  # if self.gyro_skew_z > 0.0
                                    if self.acce_max_x <= 2.65:
                                        return [0, 0, 8,]
                                    else:  # if self.acce_max_x > 2.65
                                        return [ 0, 11,  1,]
                else:  # if self.gyro_std_y > 4.13
                    if self.gyro_energy_x <= 676.93:
                        if self.gyro_energy_y <= 567.24:
                            if self.n_samples <= 12.5:
                                if self.gyro_std_x <= 1.45:
                                    return [3, 1, 0,]
                                else:  # if self.gyro_std_x > 1.45
                                    return [  0,   3, 184,]
                            else:  # if self.n_samples > 12.5
                                return [0, 5, 0,]
                        else:  # if self.gyro_energy_y > 567.24
                            return [0, 7, 1,]
                    else:  # if self.gyro_energy_x > 676.93
                        return [ 0, 13,  2,]
        else:  # if self.n_samples > 14.5
            if self.gyro_std_x <= 4.21:
                if self.gyro_variance_z <= 17.33:
                    return [288,   1,   0,]
                else:  # if self.gyro_variance_z > 17.33
                    return [0, 2, 0,]
            else:  # if self.gyro_std_x > 4.21
                return [0, 8, 0,]

    def decision_tree_13(self):
        if self.gyro_std_y <= 3.95:
            if self.acce_min_z <= 0.62:
                if self.n_samples <= 14.5:
                    if self.acce_min_x <= 0.08:
                        if self.acce_rms_x <= 3.25:
                            return [ 1, 64,  2,]
                        else:  # if self.acce_rms_x > 3.25
                            return [0, 0, 2,]
                    else:  # if self.acce_min_x > 0.08
                        if self.gyro_mean_y <= 3.13:
                            if self.acce_std_x <= 0.1:
                                return [ 0, 17,  0,]
                            else:  # if self.acce_std_x > 0.1
                                if self.acce_std_x <= 0.91:
                                    return [ 0,  1, 37,]
                                else:  # if self.acce_std_x > 0.91
                                    return [0, 4, 0,]
                        else:  # if self.gyro_mean_y > 3.13
                            if self.acce_max_x <= 0.89:
                                if self.acce_std_x <= 0.2:
                                    return [34,  0,  0,]
                                else:  # if self.acce_std_x > 0.2
                                    return [0, 3, 0,]
                            else:  # if self.acce_max_x > 0.89
                                if self.acce_range_x <= 3.85:
                                    return [ 0, 17,  0,]
                                else:  # if self.acce_range_x > 3.85
                                    return [2, 0, 0,]
                else:  # if self.n_samples > 14.5
                    if self.gyro_rms_z <= 7.52:
                        return [236,   0,   0,]
                    else:  # if self.gyro_rms_z > 7.52
                        return [0, 5, 0,]
            else:  # if self.acce_min_z > 0.62
                if self.gyro_energy_z <= 280.67:
                    return [ 0, 74,  1,]
                else:  # if self.gyro_energy_z > 280.67
                    if self.acce_rms_z <= 0.97:
                        if self.gyro_rms_z <= 7.43:
                            if self.acce_kurt_x <= 3.6:
                                return [17,  0,  0,]
                            else:  # if self.acce_kurt_x > 3.6
                                return [0, 0, 2,]
                        else:  # if self.gyro_rms_z > 7.43
                            if self.acce_std_x <= 0.11:
                                return [0, 8, 0,]
                            else:  # if self.acce_std_x > 0.11
                                return [0, 1, 4,]
                    else:  # if self.acce_rms_z > 0.97
                        if self.gyro_energy_x <= 493.41:
                            if self.acce_energy_x <= 68.82:
                                return [ 0,  6, 44,]
                            else:  # if self.acce_energy_x > 68.82
                                if self.acce_mean_z <= 0.99:
                                    return [0, 0, 3,]
                                else:  # if self.acce_mean_z > 0.99
                                    return [ 0, 21,  0,]
                        else:  # if self.gyro_energy_x > 493.41
                            return [ 0, 63,  4,]
        else:  # if self.gyro_std_y > 3.95
            if self.gyro_std_x <= 3.49:
                return [ 1, 15,  3,]
            else:  # if self.gyro_std_x > 3.49
                if self.acce_corr_xz <= 0.46:
                    if self.acce_rms_x <= 0.52:
                        return [0, 2, 0,]
                    else:  # if self.acce_rms_x > 0.52
                        return [  0,   6, 174,]
                else:  # if self.acce_corr_xz > 0.46
                    if self.acce_energy_z <= 14.0:
                        return [ 0,  4, 12,]
                    else:  # if self.acce_energy_z > 14.0
                        return [0, 9, 0,]

    def decision_tree_14(self):
        if self.gyro_rms_z <= 7.18:
            if self.gyro_rms_x <= 4.58:
                if self.gyro_kurt_y <= -1.63:
                    if self.gyro_kurt_y <= -1.91:
                        return [0, 2, 3,]
                    else:  # if self.gyro_kurt_y > -1.91
                        return [13,  0,  0,]
                else:  # if self.gyro_kurt_y > -1.63
                    if self.n_samples <= 8.5:
                        return [0, 0, 4,]
                    else:  # if self.n_samples > 8.5
                        return [ 2, 85,  6,]
            else:  # if self.gyro_rms_x > 4.58
                if self.acce_mean_z <= 0.98:
                    if self.acce_min_x <= 0.6:
                        if self.gyro_energy_y <= 323.42:
                            return [1, 4, 3,]
                        else:  # if self.gyro_energy_y > 323.42
                            return [240,   0,   0,]
                    else:  # if self.acce_min_x > 0.6
                        if self.gyro_rms_y <= 6.81:
                            return [0, 0, 9,]
                        else:  # if self.gyro_rms_y > 6.81
                            return [0, 3, 0,]
                else:  # if self.acce_mean_z > 0.98
                    if self.gyro_std_x <= 4.03:
                        if self.acce_max_x <= 3.99:
                            return [40,  0,  4,]
                        else:  # if self.acce_max_x > 3.99
                            return [0, 5, 2,]
                    else:  # if self.gyro_std_x > 4.03
                        if self.acce_corr_xz <= 0.14:
                            return [ 0,  0, 18,]
                        else:  # if self.acce_corr_xz > 0.14
                            if self.acce_energy_z <= 11.39:
                                return [0, 0, 3,]
                            else:  # if self.acce_energy_z > 11.39
                                return [ 0, 37,  0,]
        else:  # if self.gyro_rms_z > 7.18
            if self.gyro_std_y <= 3.43:
                if self.gyro_variance_z <= 7.4:
                    return [ 2, 80,  1,]
                else:  # if self.gyro_variance_z > 7.4
                    if self.n_samples <= 11.5:
                        return [ 0,  5, 23,]
                    else:  # if self.n_samples > 11.5
                        return [1, 9, 0,]
            else:  # if self.gyro_std_y > 3.43
                if self.acce_max_x <= 0.45:
                    return [ 0, 16,  0,]
                else:  # if self.acce_max_x > 0.45
                    if self.gyro_skew_z <= -2.86:
                        return [ 0, 16,  0,]
                    else:  # if self.gyro_skew_z > -2.86
                        if self.acce_energy_x <= 107.97:
                            if self.acce_variance_x <= 3.51:
                                if self.acce_kurt_x <= 5.69:
                                    if self.n_samples <= 12.5:
                                        if self.acce_variance_x <= 0.01:
                                            return [0, 2, 0,]
                                        else:  # if self.acce_variance_x > 0.01
                                            return [  0,   1, 229,]
                                    else:  # if self.n_samples > 12.5
                                        return [4, 3, 0,]
                                else:  # if self.acce_kurt_x > 5.69
                                    if self.acce_skew_z <= -0.54:
                                        return [0, 0, 4,]
                                    else:  # if self.acce_skew_z > -0.54
                                        return [0, 5, 0,]
                            else:  # if self.acce_variance_x > 3.51
                                return [0, 5, 0,]
                        else:  # if self.acce_energy_x > 107.97
                            return [0, 9, 0,]

