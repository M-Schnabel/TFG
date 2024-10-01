class RandomForestOptimized:    
    def __init__(self):
            pass
    
    def score(self, n_samples, gyro_std_y, acce_min_z, gyro_kurt_y, gyro_variance_y, gyro_std_x, gyro_rms_y, gyro_energy_y, gyro_kurt_z, gyro_skew_y, gyro_kurt_x, gyro_skew_z, gyro_mean_z, gyro_variance_z, gyro_mean_y, acce_range_x, acce_energy_x, acce_std_z, acce_rms_x, acce_corr_xz, gyro_energy_x, acce_skew_x, acce_max_x, acce_variance_x, gyro_rms_z, acce_energy_z, acce_energy_y, acce_variance_z, gyro_energy_z, gyro_std_z, acce_mean_z, acce_std_x, gyro_range_y, acce_min_x, gyro_rms_x, acce_rms_z, gyro_variance_x, acce_rms_y, acce_skew_z, acce_mean_y, gyro_min_x, acce_kurt_x, acce_corr_yz, acce_kurt_z, gyro_max_z, acce_max_z, acce_skew_y, gyro_mean_x, gyro_corr_xz, acce_std_y, gyro_min_z, gyro_corr_xy, acce_mean_x, acce_min_y, gyro_min_y):
        self.n_samples = n_samples
        self.gyro_std_y = gyro_std_y
        self.acce_min_z = acce_min_z
        self.gyro_kurt_y = gyro_kurt_y
        self.gyro_variance_y = gyro_variance_y
        self.gyro_std_x = gyro_std_x
        self.gyro_rms_y = gyro_rms_y
        self.gyro_energy_y = gyro_energy_y
        self.gyro_kurt_z = gyro_kurt_z
        self.gyro_skew_y = gyro_skew_y
        self.gyro_kurt_x = gyro_kurt_x
        self.gyro_skew_z = gyro_skew_z
        self.gyro_mean_z = gyro_mean_z
        self.gyro_variance_z = gyro_variance_z
        self.gyro_mean_y = gyro_mean_y
        self.acce_range_x = acce_range_x
        self.acce_energy_x = acce_energy_x
        self.acce_std_z = acce_std_z
        self.acce_rms_x = acce_rms_x
        self.acce_corr_xz = acce_corr_xz
        self.gyro_energy_x = gyro_energy_x
        self.acce_skew_x = acce_skew_x
        self.acce_max_x = acce_max_x
        self.acce_variance_x = acce_variance_x
        self.gyro_rms_z = gyro_rms_z
        self.acce_energy_z = acce_energy_z
        self.acce_energy_y = acce_energy_y
        self.acce_variance_z = acce_variance_z
        self.gyro_energy_z = gyro_energy_z
        self.gyro_std_z = gyro_std_z
        self.acce_mean_z = acce_mean_z
        self.acce_std_x = acce_std_x
        self.gyro_range_y = gyro_range_y
        self.acce_min_x = acce_min_x
        self.gyro_rms_x = gyro_rms_x
        self.acce_rms_z = acce_rms_z
        self.gyro_variance_x = gyro_variance_x
        self.acce_rms_y = acce_rms_y
        self.acce_skew_z = acce_skew_z
        self.acce_mean_y = acce_mean_y
        self.gyro_min_x = gyro_min_x
        self.acce_kurt_x = acce_kurt_x
        self.acce_corr_yz = acce_corr_yz
        self.acce_kurt_z = acce_kurt_z
        self.gyro_max_z = gyro_max_z
        self.acce_max_z = acce_max_z
        self.acce_skew_y = acce_skew_y
        self.gyro_mean_x = gyro_mean_x
        self.gyro_corr_xz = gyro_corr_xz
        self.acce_std_y = acce_std_y
        self.gyro_min_z = gyro_min_z
        self.gyro_corr_xy = gyro_corr_xy
        self.acce_mean_x = acce_mean_x
        self.acce_min_y = acce_min_y
        self.gyro_min_y = gyro_min_y
    
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
    
        trees_values = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16]
    
        return [sum(col) / len(col) for col in zip(*trees_values)]

    def decision_tree_0(self):
        if self.gyro_kurt_z <= -0.98:
            if self.gyro_std_y <= 3.93:
                if self.gyro_std_z <= 3.92:
                    if self.acce_min_z <= 0.68:
                        if self.gyro_energy_z <= 245.45:
                            return [0, 3, 0,]
                        else:  # if self.gyro_energy_z > 245.45
                            if self.gyro_min_z <= 4.32:
                                return [294,   0,   0,]
                            else:  # if self.gyro_min_z > 4.32
                                return [0, 4, 0,]
                    else:  # if self.acce_min_z > 0.68
                        if self.acce_mean_z <= 0.98:
                            if self.gyro_min_z <= 4.5:
                                return [4, 0, 0,]
                            else:  # if self.gyro_min_z > 4.5
                                return [0, 0, 4,]
                        else:  # if self.acce_mean_z > 0.98
                            return [ 0, 24,  1,]
                else:  # if self.gyro_std_z > 3.92
                    if self.acce_corr_xz <= 0.17:
                        if self.acce_min_x <= 2.31:
                            return [ 1,  2, 27,]
                        else:  # if self.acce_min_x > 2.31
                            return [0, 2, 0,]
                    else:  # if self.acce_corr_xz > 0.17
                        if self.acce_rms_z <= 0.68:
                            return [0, 0, 2,]
                        else:  # if self.acce_rms_z > 0.68
                            if self.acce_rms_x <= 0.85:
                                return [2, 0, 0,]
                            else:  # if self.acce_rms_x > 0.85
                                return [ 0, 34,  4,]
            else:  # if self.gyro_std_y > 3.93
                if self.gyro_std_x <= 4.14:
                    if self.gyro_min_z <= 8.21:
                        if self.acce_rms_z <= 0.81:
                            return [4, 0, 0,]
                        else:  # if self.acce_rms_z > 0.81
                            if self.gyro_energy_y <= 366.15:
                                if self.acce_max_x <= 1.01:
                                    return [0, 5, 0,]
                                else:  # if self.acce_max_x > 1.01
                                    return [0, 0, 5,]
                            else:  # if self.gyro_energy_y > 366.15
                                return [ 0, 18,  1,]
                    else:  # if self.gyro_min_z > 8.21
                        if self.gyro_kurt_y <= -1.68:
                            return [0, 0, 7,]
                        else:  # if self.gyro_kurt_y > -1.68
                            return [0, 2, 0,]
                else:  # if self.gyro_std_x > 4.14
                    if self.gyro_mean_z <= 3.14:
                        return [0, 3, 0,]
                    else:  # if self.gyro_mean_z > 3.14
                        if self.acce_range_x <= 3.97:
                            return [ 0,  0, 65,]
                        else:  # if self.acce_range_x > 3.97
                            if self.gyro_corr_xz <= -0.16:
                                return [0, 3, 0,]
                            else:  # if self.gyro_corr_xz > -0.16
                                return [0, 0, 2,]
        else:  # if self.gyro_kurt_z > -0.98
            if self.gyro_mean_y <= 6.46:
                if self.gyro_variance_x <= 15.99:
                    if self.gyro_variance_y <= 17.32:
                        if self.acce_std_z <= 0.25:
                            if self.n_samples <= 8.5:
                                return [0, 0, 2,]
                            else:  # if self.n_samples > 8.5
                                return [ 0, 37,  0,]
                        else:  # if self.acce_std_z > 0.25
                            if self.acce_min_z <= 0.35:
                                return [16,  0,  0,]
                            else:  # if self.acce_min_z > 0.35
                                if self.gyro_corr_xy <= -0.11:
                                    return [0, 0, 2,]
                                else:  # if self.gyro_corr_xy > -0.11
                                    return [1, 7, 0,]
                    else:  # if self.gyro_variance_y > 17.32
                        if self.acce_rms_x <= 1.27:
                            return [0, 4, 0,]
                        else:  # if self.acce_rms_x > 1.27
                            return [ 0,  0, 18,]
                else:  # if self.gyro_variance_x > 15.99
                    if self.acce_mean_x <= 0.14:
                        return [0, 4, 0,]
                    else:  # if self.acce_mean_x > 0.14
                        if self.acce_energy_x <= 90.35:
                            if self.gyro_min_y <= 0.0:
                                return [0, 1, 0,]
                            else:  # if self.gyro_min_y > 0.0
                                if self.acce_corr_xz <= -0.89:
                                    if self.gyro_corr_xy <= -0.1:
                                        return [0, 2, 0,]
                                    else:  # if self.gyro_corr_xy > -0.1
                                        return [0, 0, 2,]
                                else:  # if self.acce_corr_xz > -0.89
                                    return [  0,   0, 125,]
                        else:  # if self.acce_energy_x > 90.35
                            if self.gyro_std_y <= 4.24:
                                return [ 0, 12,  0,]
                            else:  # if self.gyro_std_y > 4.24
                                return [0, 0, 2,]
            else:  # if self.gyro_mean_y > 6.46
                if self.acce_max_x <= 3.93:
                    if self.acce_rms_x <= 1.3:
                        return [ 0, 49,  1,]
                    else:  # if self.acce_rms_x > 1.3
                        return [ 0,  0, 16,]
                else:  # if self.acce_max_x > 3.93
                    if self.acce_min_x <= 0.13:
                        return [ 2, 72,  0,]
                    else:  # if self.acce_min_x > 0.13
                        return [0, 0, 1,]

    def decision_tree_1(self):
        if self.gyro_skew_y <= -1.36:
            if self.gyro_corr_xy <= 1.0:
                if self.acce_energy_z <= 10.76:
                    if self.acce_std_x <= 0.83:
                        return [ 0, 33,  0,]
                    else:  # if self.acce_std_x > 0.83
                        if self.acce_mean_y <= 2.15:
                            return [0, 2, 0,]
                        else:  # if self.acce_mean_y > 2.15
                            return [0, 0, 7,]
                else:  # if self.acce_energy_z > 10.76
                    return [  0, 118,   0,]
            else:  # if self.gyro_corr_xy > 1.0
                return [0, 0, 2,]
        else:  # if self.gyro_skew_y > -1.36
            if self.gyro_variance_y <= 15.5:
                if self.gyro_energy_y <= 339.69:
                    if self.gyro_energy_x <= 573.45:
                        if self.gyro_energy_y <= 168.69:
                            if self.gyro_rms_y <= 2.75:
                                if self.gyro_min_z <= 0.02:
                                    if self.acce_std_z <= 0.3:
                                        return [0, 0, 2,]
                                    else:  # if self.acce_std_z > 0.3
                                        return [0, 1, 0,]
                                else:  # if self.gyro_min_z > 0.02
                                    return [ 0, 14,  0,]
                            else:  # if self.gyro_rms_y > 2.75
                                if self.acce_skew_z <= 0.94:
                                    if self.acce_mean_x <= 1.84:
                                        if self.acce_kurt_z <= -1.29:
                                            if self.gyro_kurt_x <= -1.84:
                                                return [2, 0, 0,]
                                            else:  # if self.gyro_kurt_x > -1.84
                                                return [0, 2, 0,]
                                        else:  # if self.acce_kurt_z > -1.29
                                            if self.gyro_variance_x <= 19.69:
                                                return [ 0,  0, 15,]
                                            else:  # if self.gyro_variance_x > 19.69
                                                return [0, 2, 0,]
                                    else:  # if self.acce_mean_x > 1.84
                                        return [0, 7, 0,]
                                else:  # if self.acce_skew_z > 0.94
                                    return [ 0,  2, 36,]
                        else:  # if self.gyro_energy_y > 168.69
                            if self.acce_rms_z <= 0.96:
                                if self.acce_energy_x <= 2.54:
                                    return [0, 1, 0,]
                                else:  # if self.acce_energy_x > 2.54
                                    return [5, 0, 0,]
                            else:  # if self.acce_rms_z > 0.96
                                return [ 0, 21,  0,]
                    else:  # if self.gyro_energy_x > 573.45
                        if self.acce_rms_z <= 1.43:
                            if self.gyro_std_z <= 3.65:
                                return [ 0, 36,  0,]
                            else:  # if self.gyro_std_z > 3.65
                                return [0, 0, 3,]
                        else:  # if self.acce_rms_z > 1.43
                            if self.acce_skew_y <= 0.38:
                                return [0, 0, 4,]
                            else:  # if self.acce_skew_y > 0.38
                                return [0, 2, 0,]
                else:  # if self.gyro_energy_y > 339.69
                    if self.gyro_rms_y <= 7.37:
                        if self.acce_rms_y <= 0.42:
                            return [0, 1, 0,]
                        else:  # if self.acce_rms_y > 0.42
                            if self.gyro_rms_z <= 8.07:
                                return [292,   1,   0,]
                            else:  # if self.gyro_rms_z > 8.07
                                return [0, 1, 0,]
                    else:  # if self.gyro_rms_y > 7.37
                        if self.gyro_rms_y <= 8.26:
                            if self.n_samples <= 10.5:
                                return [ 0,  0, 19,]
                            else:  # if self.n_samples > 10.5
                                return [0, 7, 0,]
                        else:  # if self.gyro_rms_y > 8.26
                            if self.gyro_variance_z <= 13.06:
                                return [ 0, 12,  0,]
                            else:  # if self.gyro_variance_z > 13.06
                                if self.gyro_energy_y <= 1008.81:
                                    return [0, 0, 3,]
                                else:  # if self.gyro_energy_y > 1008.81
                                    return [0, 1, 0,]
            else:  # if self.gyro_variance_y > 15.5
                if self.acce_min_z <= 0.96:
                    if self.acce_skew_x <= -0.83:
                        return [ 0, 10,  0,]
                    else:  # if self.acce_skew_x > -0.83
                        if self.acce_rms_x <= 0.33:
                            if self.gyro_kurt_z <= -1.87:
                                return [3, 0, 0,]
                            else:  # if self.gyro_kurt_z > -1.87
                                return [0, 5, 0,]
                        else:  # if self.acce_rms_x > 0.33
                            if self.n_samples <= 12.5:
                                if self.acce_energy_x <= 118.01:
                                    return [  0,   0, 195,]
                                else:  # if self.acce_energy_x > 118.01
                                    return [0, 1, 0,]
                            else:  # if self.n_samples > 12.5
                                if self.acce_min_y <= 0.04:
                                    return [0, 4, 0,]
                                else:  # if self.acce_min_y > 0.04
                                    return [0, 0, 1,]
                else:  # if self.acce_min_z > 0.96
                    if self.gyro_std_x <= 4.27:
                        if self.n_samples <= 8.5:
                            return [0, 0, 3,]
                        else:  # if self.n_samples > 8.5
                            return [ 0, 20,  0,]
                    else:  # if self.gyro_std_x > 4.27
                        return [0, 0, 3,]

    def decision_tree_2(self):
        if self.gyro_kurt_y <= -1.32:
            if self.acce_variance_x <= 0.05:
                if self.gyro_rms_z <= 7.48:
                    if self.gyro_rms_y <= 2.79:
                        return [0, 2, 0,]
                    else:  # if self.gyro_rms_y > 2.79
                        if self.acce_max_x <= 1.0:
                            if self.acce_std_y <= 0.03:
                                return [0, 0, 1,]
                            else:  # if self.acce_std_y > 0.03
                                if self.gyro_kurt_z <= 0.46:
                                    return [206,   0,   0,]
                                else:  # if self.gyro_kurt_z > 0.46
                                    return [0, 1, 0,]
                        else:  # if self.acce_max_x > 1.0
                            return [0, 1, 8,]
                else:  # if self.gyro_rms_z > 7.48
                    if self.acce_mean_y <= 2.51:
                        return [ 1, 18,  1,]
                    else:  # if self.acce_mean_y > 2.51
                        return [0, 0, 3,]
            else:  # if self.acce_variance_x > 0.05
                if self.n_samples <= 15.5:
                    if self.n_samples <= 11.5:
                        if self.gyro_energy_y <= 567.81:
                            if self.acce_skew_x <= 2.52:
                                if self.gyro_std_x <= 1.42:
                                    return [0, 4, 0,]
                                else:  # if self.gyro_std_x > 1.42
                                    if self.acce_energy_x <= 112.37:
                                        return [  0,   0, 180,]
                                    else:  # if self.acce_energy_x > 112.37
                                        return [0, 1, 0,]
                            else:  # if self.acce_skew_x > 2.52
                                return [1, 1, 0,]
                        else:  # if self.gyro_energy_y > 567.81
                            return [0, 2, 0,]
                    else:  # if self.n_samples > 11.5
                        if self.acce_rms_z <= 1.01:
                            return [0, 1, 2,]
                        else:  # if self.acce_rms_z > 1.01
                            return [ 0, 16,  0,]
                else:  # if self.n_samples > 15.5
                    return [98,  0,  0,]
        else:  # if self.gyro_kurt_y > -1.32
            if self.gyro_energy_x <= 573.45:
                if self.acce_skew_x <= 0.18:
                    if self.gyro_kurt_x <= -1.58:
                        if self.gyro_rms_x <= 6.9:
                            if self.acce_variance_x <= 0.03:
                                if self.acce_energy_x <= 8.19:
                                    return [3, 0, 0,]
                                else:  # if self.acce_energy_x > 8.19
                                    return [0, 2, 0,]
                            else:  # if self.acce_variance_x > 0.03
                                if self.gyro_energy_x <= 319.98:
                                    return [0, 0, 2,]
                                else:  # if self.gyro_energy_x > 319.98
                                    return [ 0, 18,  0,]
                        else:  # if self.gyro_rms_x > 6.9
                            return [0, 0, 5,]
                    else:  # if self.gyro_kurt_x > -1.58
                        return [ 0, 52,  0,]
                else:  # if self.acce_skew_x > 0.18
                    if self.acce_kurt_z <= -0.18:
                        if self.gyro_variance_y <= 12.61:
                            if self.gyro_corr_xy <= -0.31:
                                if self.gyro_mean_y <= 4.28:
                                    return [0, 0, 6,]
                                else:  # if self.gyro_mean_y > 4.28
                                    return [0, 3, 0,]
                            else:  # if self.gyro_corr_xy > -0.31
                                if self.acce_energy_z <= 4.12:
                                    return [2, 1, 0,]
                                else:  # if self.acce_energy_z > 4.12
                                    if self.gyro_kurt_y <= -1.28:
                                        return [1, 0, 0,]
                                    else:  # if self.gyro_kurt_y > -1.28
                                        if self.acce_max_z <= 3.94:
                                            return [ 0, 45,  0,]
                                        else:  # if self.acce_max_z > 3.94
                                            return [0, 0, 1,]
                        else:  # if self.gyro_variance_y > 12.61
                            if self.gyro_skew_z <= -0.0:
                                return [ 0,  0, 12,]
                            else:  # if self.gyro_skew_z > -0.0
                                return [0, 4, 1,]
                    else:  # if self.acce_kurt_z > -0.18
                        if self.gyro_energy_y <= 602.9:
                            if self.acce_corr_yz <= 0.64:
                                if self.gyro_std_x <= 0.12:
                                    return [0, 1, 0,]
                                else:  # if self.gyro_std_x > 0.12
                                    return [ 0,  2, 70,]
                            else:  # if self.acce_corr_yz > 0.64
                                return [0, 2, 0,]
                        else:  # if self.gyro_energy_y > 602.9
                            if self.acce_energy_z <= 11.81:
                                return [0, 1, 4,]
                            else:  # if self.acce_energy_z > 11.81
                                if self.gyro_mean_y <= 6.91:
                                    return [0, 0, 1,]
                                else:  # if self.gyro_mean_y > 6.91
                                    return [ 0, 10,  0,]
            else:  # if self.gyro_energy_x > 573.45
                if self.gyro_energy_z <= 662.96:
                    if self.acce_mean_z <= 0.96:
                        return [2, 1, 4,]
                    else:  # if self.acce_mean_z > 0.96
                        return [0, 7, 0,]
                else:  # if self.gyro_energy_z > 662.96
                    if self.n_samples <= 18.5:
                        return [ 0, 86,  0,]
                    else:  # if self.n_samples > 18.5
                        return [2, 0, 0,]

    def decision_tree_3(self):
        if self.gyro_energy_y <= 502.39:
            if self.acce_corr_xz <= 0.47:
                if self.acce_rms_x <= 0.88:
                    if self.acce_std_z <= 0.29:
                        if self.gyro_kurt_x <= 0.21:
                            if self.acce_variance_x <= 0.01:
                                return [1, 9, 1,]
                            else:  # if self.acce_variance_x > 0.01
                                return [ 0,  0, 14,]
                        else:  # if self.gyro_kurt_x > 0.21
                            return [ 0, 19,  0,]
                    else:  # if self.acce_std_z > 0.29
                        if self.gyro_variance_y <= 8.27:
                            if self.acce_skew_z <= 1.31:
                                return [0, 3, 0,]
                            else:  # if self.acce_skew_z > 1.31
                                return [0, 0, 5,]
                        else:  # if self.gyro_variance_y > 8.27
                            if self.gyro_variance_z <= 12.69:
                                return [26,  0,  0,]
                            else:  # if self.gyro_variance_z > 12.69
                                if self.acce_max_z <= 2.96:
                                    return [0, 0, 5,]
                                else:  # if self.acce_max_z > 2.96
                                    return [0, 2, 0,]
                else:  # if self.acce_rms_x > 0.88
                    if self.gyro_mean_y <= 2.19:
                        if self.acce_min_z <= 0.3:
                            return [ 0,  0, 28,]
                        else:  # if self.acce_min_z > 0.3
                            if self.acce_variance_z <= 0.08:
                                if self.gyro_corr_xy <= -0.47:
                                    if self.gyro_rms_y <= 3.81:
                                        return [0, 0, 3,]
                                    else:  # if self.gyro_rms_y > 3.81
                                        return [0, 2, 0,]
                                else:  # if self.gyro_corr_xy > -0.47
                                    return [ 0, 24,  1,]
                            else:  # if self.acce_variance_z > 0.08
                                return [0, 0, 4,]
                    else:  # if self.gyro_mean_y > 2.19
                        if self.gyro_std_y <= 3.61:
                            if self.gyro_mean_y <= 6.36:
                                return [11,  0,  0,]
                            else:  # if self.gyro_mean_y > 6.36
                                return [0, 0, 2,]
                        else:  # if self.gyro_std_y > 3.61
                            if self.acce_kurt_x <= 8.42:
                                if self.acce_energy_x <= 116.81:
                                    return [  0,   3, 208,]
                                else:  # if self.acce_energy_x > 116.81
                                    return [0, 4, 0,]
                            else:  # if self.acce_kurt_x > 8.42
                                return [0, 3, 0,]
            else:  # if self.acce_corr_xz > 0.47
                if self.acce_mean_x <= 2.09:
                    if self.gyro_rms_y <= 5.09:
                        if self.acce_skew_z <= -0.07:
                            return [0, 0, 3,]
                        else:  # if self.acce_skew_z > -0.07
                            if self.gyro_kurt_y <= -1.43:
                                return [2, 1, 0,]
                            else:  # if self.gyro_kurt_y > -1.43
                                return [ 0, 17,  0,]
                    else:  # if self.gyro_rms_y > 5.09
                        if self.gyro_variance_z <= 5.89:
                            if self.gyro_kurt_z <= 2.39:
                                return [1, 0, 1,]
                            else:  # if self.gyro_kurt_z > 2.39
                                return [0, 5, 0,]
                        else:  # if self.gyro_variance_z > 5.89
                            return [ 0,  0, 16,]
                else:  # if self.acce_mean_x > 2.09
                    return [ 0, 42,  0,]
        else:  # if self.gyro_energy_y > 502.39
            if self.gyro_mean_y <= 6.36:
                if self.acce_std_z <= 0.12:
                    if self.acce_skew_x <= 1.63:
                        if self.acce_rms_x <= 2.29:
                            return [0, 9, 0,]
                        else:  # if self.acce_rms_x > 2.29
                            return [0, 0, 2,]
                    else:  # if self.acce_skew_x > 1.63
                        return [0, 0, 3,]
                else:  # if self.acce_std_z > 0.12
                    if self.gyro_kurt_z <= -0.01:
                        if self.gyro_variance_z <= 3.85:
                            return [0, 0, 3,]
                        else:  # if self.gyro_variance_z > 3.85
                            return [221,   0,   0,]
                    else:  # if self.gyro_kurt_z > -0.01
                        return [0, 6, 1,]
            else:  # if self.gyro_mean_y > 6.36
                if self.n_samples <= 9.5:
                    if self.gyro_variance_y <= 8.17:
                        return [0, 5, 0,]
                    else:  # if self.gyro_variance_y > 8.17
                        return [0, 0, 8,]
                else:  # if self.n_samples > 9.5
                    if self.gyro_min_y <= 8.31:
                        if self.gyro_variance_z <= 14.39:
                            return [  1, 146,   4,]
                        else:  # if self.gyro_variance_z > 14.39
                            if self.acce_corr_xz <= 0.15:
                                if self.acce_range_x <= 2.23:
                                    return [0, 2, 0,]
                                else:  # if self.acce_range_x > 2.23
                                    return [0, 0, 6,]
                            else:  # if self.acce_corr_xz > 0.15
                                return [0, 9, 0,]
                    else:  # if self.gyro_min_y > 8.31
                        if self.gyro_kurt_x <= 0.49:
                            return [0, 0, 5,]
                        else:  # if self.gyro_kurt_x > 0.49
                            return [0, 2, 0,]

    def decision_tree_4(self):
        if self.gyro_skew_y <= -1.15:
            if self.gyro_variance_y <= 11.83:
                if self.n_samples <= 8.0:
                    return [0, 0, 3,]
                else:  # if self.n_samples > 8.0
                    return [  0, 139,   3,]
            else:  # if self.gyro_variance_y > 11.83
                if self.gyro_kurt_x <= -1.4:
                    if self.gyro_corr_xz <= -0.45:
                        return [0, 3, 0,]
                    else:  # if self.gyro_corr_xz > -0.45
                        if self.acce_min_y <= 0.0:
                            return [0, 2, 0,]
                        else:  # if self.acce_min_y > 0.0
                            return [0, 0, 7,]
                else:  # if self.gyro_kurt_x > -1.4
                    return [ 0, 12,  0,]
        else:  # if self.gyro_skew_y > -1.15
            if self.acce_mean_z <= 0.97:
                if self.gyro_kurt_y <= -1.19:
                    if self.gyro_variance_y <= 15.26:
                        if self.gyro_variance_y <= 4.14:
                            if self.gyro_std_y <= 0.13:
                                return [5, 0, 0,]
                            else:  # if self.gyro_std_y > 0.13
                                if self.gyro_std_y <= 0.31:
                                    return [0, 0, 2,]
                                else:  # if self.gyro_std_y > 0.31
                                    return [0, 4, 0,]
                        else:  # if self.gyro_variance_y > 4.14
                            return [216,   0,   0,]
                    else:  # if self.gyro_variance_y > 15.26
                        if self.gyro_variance_x <= 11.38:
                            if self.n_samples <= 10.5:
                                return [2, 0, 1,]
                            else:  # if self.n_samples > 10.5
                                return [0, 4, 0,]
                        else:  # if self.gyro_variance_x > 11.38
                            return [ 0,  0, 17,]
                else:  # if self.gyro_kurt_y > -1.19
                    if self.acce_max_z <= 1.63:
                        if self.acce_min_z <= 0.3:
                            return [ 0,  1, 10,]
                        else:  # if self.acce_min_z > 0.3
                            if self.acce_rms_y <= 3.73:
                                if self.gyro_min_x <= 0.06:
                                    return [ 0, 20,  0,]
                                else:  # if self.gyro_min_x > 0.06
                                    if self.acce_corr_yz <= 0.25:
                                        return [0, 4, 0,]
                                    else:  # if self.acce_corr_yz > 0.25
                                        return [2, 0, 2,]
                            else:  # if self.acce_rms_y > 3.73
                                return [0, 0, 2,]
                    else:  # if self.acce_max_z > 1.63
                        return [ 0,  0, 22,]
            else:  # if self.acce_mean_z > 0.97
                if self.gyro_mean_z <= 5.97:
                    if self.acce_min_z <= 0.58:
                        if self.gyro_rms_x <= 5.04:
                            return [0, 7, 0,]
                        else:  # if self.gyro_rms_x > 5.04
                            if self.gyro_variance_x <= 16.86:
                                if self.gyro_kurt_x <= 0.21:
                                    return [48,  0,  0,]
                                else:  # if self.gyro_kurt_x > 0.21
                                    if self.acce_rms_x <= 1.8:
                                        return [0, 0, 2,]
                                    else:  # if self.acce_rms_x > 1.8
                                        return [0, 2, 0,]
                            else:  # if self.gyro_variance_x > 16.86
                                if self.acce_corr_xz <= 0.19:
                                    return [0, 0, 8,]
                                else:  # if self.acce_corr_xz > 0.19
                                    return [0, 2, 0,]
                    else:  # if self.acce_min_z > 0.58
                        if self.acce_skew_x <= -0.0:
                            return [ 0, 31,  2,]
                        else:  # if self.acce_skew_x > -0.0
                            if self.gyro_variance_y <= 14.71:
                                return [0, 4, 1,]
                            else:  # if self.gyro_variance_y > 14.71
                                return [ 0,  0, 21,]
                else:  # if self.gyro_mean_z > 5.97
                    if self.gyro_energy_x <= 633.87:
                        if self.acce_variance_x <= 0.01:
                            return [ 0, 11,  0,]
                        else:  # if self.acce_variance_x > 0.01
                            if self.gyro_kurt_y <= -1.42:
                                return [  1,   4, 164,]
                            else:  # if self.gyro_kurt_y > -1.42
                                if self.gyro_std_x <= 4.37:
                                    if self.n_samples <= 12.0:
                                        if self.acce_max_x <= 4.0:
                                            return [ 0,  0, 37,]
                                        else:  # if self.acce_max_x > 4.0
                                            return [0, 2, 0,]
                                    else:  # if self.n_samples > 12.0
                                        return [0, 4, 0,]
                                else:  # if self.gyro_std_x > 4.37
                                    if self.gyro_mean_z <= 7.98:
                                        return [0, 0, 3,]
                                    else:  # if self.gyro_mean_z > 7.98
                                        return [ 0, 10,  0,]
                    else:  # if self.gyro_energy_x > 633.87
                        if self.acce_min_z <= 0.59:
                            return [7, 0, 0,]
                        else:  # if self.acce_min_z > 0.59
                            if self.gyro_rms_z <= 8.23:
                                return [ 0, 29,  0,]
                            else:  # if self.gyro_rms_z > 8.23
                                if self.gyro_kurt_z <= -0.45:
                                    return [0, 9, 0,]
                                else:  # if self.gyro_kurt_z > -0.45
                                    return [0, 0, 7,]

    def decision_tree_5(self):
        if self.acce_mean_z <= 0.96:
            if self.gyro_kurt_y <= -1.06:
                if self.gyro_corr_xz <= -0.22:
                    if self.gyro_variance_x <= 10.32:
                        return [2, 1, 0,]
                    else:  # if self.gyro_variance_x > 10.32
                        if self.gyro_corr_xz <= -0.58:
                            return [0, 1, 0,]
                        else:  # if self.gyro_corr_xz > -0.58
                            return [ 0,  0, 14,]
                else:  # if self.gyro_corr_xz > -0.22
                    if self.acce_variance_z <= 0.0:
                        return [0, 7, 1,]
                    else:  # if self.acce_variance_z > 0.0
                        if self.gyro_std_x <= 4.2:
                            if self.gyro_skew_z <= -1.09:
                                if self.acce_corr_xz <= -0.45:
                                    return [0, 3, 0,]
                                else:  # if self.acce_corr_xz > -0.45
                                    return [0, 0, 2,]
                            else:  # if self.gyro_skew_z > -1.09
                                if self.gyro_variance_y <= 17.11:
                                    return [244,   0,   0,]
                                else:  # if self.gyro_variance_y > 17.11
                                    return [0, 0, 2,]
                        else:  # if self.gyro_std_x > 4.2
                            return [0, 0, 4,]
            else:  # if self.gyro_kurt_y > -1.06
                if self.gyro_std_z <= 3.37:
                    if self.acce_rms_z <= 0.99:
                        if self.gyro_kurt_x <= -1.96:
                            return [0, 0, 1,]
                        else:  # if self.gyro_kurt_x > -1.96
                            return [ 0, 33,  1,]
                    else:  # if self.acce_rms_z > 0.99
                        return [0, 1, 3,]
                else:  # if self.gyro_std_z > 3.37
                    if self.acce_max_x <= 0.8:
                        return [0, 3, 0,]
                    else:  # if self.acce_max_x > 0.8
                        if self.gyro_corr_xy <= 0.32:
                            return [ 1,  0, 20,]
                        else:  # if self.gyro_corr_xy > 0.32
                            return [0, 1, 0,]
        else:  # if self.acce_mean_z > 0.96
            if self.gyro_std_y <= 3.95:
                if self.acce_rms_z <= 1.13:
                    if self.acce_rms_y <= 3.07:
                        if self.gyro_std_z <= 3.35:
                            return [ 0, 98,  1,]
                        else:  # if self.gyro_std_z > 3.35
                            if self.gyro_energy_x <= 652.12:
                                if self.n_samples <= 9.0:
                                    return [0, 0, 4,]
                                else:  # if self.n_samples > 9.0
                                    return [ 0, 20,  0,]
                            else:  # if self.gyro_energy_x > 652.12
                                return [7, 0, 0,]
                    else:  # if self.acce_rms_y > 3.07
                        if self.acce_corr_xz <= 0.2:
                            if self.gyro_skew_z <= -0.4:
                                return [ 0,  0, 25,]
                            else:  # if self.gyro_skew_z > -0.4
                                return [ 0, 12,  2,]
                        else:  # if self.acce_corr_xz > 0.2
                            if self.gyro_mean_x <= 4.74:
                                return [ 1, 39,  0,]
                            else:  # if self.gyro_mean_x > 4.74
                                if self.gyro_energy_y <= 404.65:
                                    if self.acce_mean_z <= 0.97:
                                        return [0, 0, 2,]
                                    else:  # if self.acce_mean_z > 0.97
                                        return [ 0, 14,  0,]
                                else:  # if self.gyro_energy_y > 404.65
                                    if self.acce_energy_y <= 157.26:
                                        if self.gyro_mean_z <= 7.51:
                                            return [0, 0, 2,]
                                        else:  # if self.gyro_mean_z > 7.51
                                            return [0, 3, 0,]
                                    else:  # if self.acce_energy_y > 157.26
                                        return [9, 0, 0,]
                else:  # if self.acce_rms_z > 1.13
                    if self.acce_rms_z <= 2.2:
                        if self.acce_mean_x <= 0.85:
                            return [33,  0,  0,]
                        else:  # if self.acce_mean_x > 0.85
                            if self.acce_corr_xz <= 0.49:
                                return [ 0,  0, 16,]
                            else:  # if self.acce_corr_xz > 0.49
                                return [0, 2, 0,]
                    else:  # if self.acce_rms_z > 2.2
                        if self.acce_kurt_x <= -1.75:
                            return [0, 0, 1,]
                        else:  # if self.acce_kurt_x > -1.75
                            return [ 0, 14,  0,]
            else:  # if self.gyro_std_y > 3.95
                if self.gyro_std_x <= 3.47:
                    if self.acce_rms_y <= 3.93:
                        return [ 0, 16,  0,]
                    else:  # if self.acce_rms_y > 3.93
                        return [0, 0, 1,]
                else:  # if self.gyro_std_x > 3.47
                    if self.n_samples <= 11.5:
                        if self.acce_mean_y <= 1.29:
                            if self.acce_rms_y <= 2.04:
                                return [0, 0, 7,]
                            else:  # if self.acce_rms_y > 2.04
                                return [0, 5, 0,]
                        else:  # if self.acce_mean_y > 1.29
                            return [  0,   3, 198,]
                    else:  # if self.n_samples > 11.5
                        if self.acce_skew_z <= -0.55:
                            return [0, 0, 2,]
                        else:  # if self.acce_skew_z > -0.55
                            return [ 0, 17,  0,]

    def decision_tree_6(self):
        if self.gyro_mean_y <= 6.43:
            if self.gyro_energy_y <= 499.97:
                if self.n_samples <= 11.5:
                    if self.gyro_std_x <= 3.58:
                        if self.acce_skew_x <= 0.31:
                            if self.gyro_range_y <= 8.93:
                                return [4, 0, 0,]
                            else:  # if self.gyro_range_y > 8.93
                                return [ 0, 13,  1,]
                        else:  # if self.acce_skew_x > 0.31
                            if self.gyro_max_z <= 8.99:
                                return [0, 4, 0,]
                            else:  # if self.gyro_max_z > 8.99
                                if self.acce_energy_x <= 5.55:
                                    return [1, 0, 0,]
                                else:  # if self.acce_energy_x > 5.55
                                    return [ 0,  0, 18,]
                    else:  # if self.gyro_std_x > 3.58
                        if self.gyro_std_y <= 2.49:
                            return [0, 7, 2,]
                        else:  # if self.gyro_std_y > 2.49
                            if self.acce_mean_x <= 0.88:
                                if self.acce_skew_x <= 2.52:
                                    if self.acce_rms_y <= 3.04:
                                        if self.n_samples <= 9.5:
                                            return [0, 0, 4,]
                                        else:  # if self.n_samples > 9.5
                                            return [0, 5, 0,]
                                    else:  # if self.acce_rms_y > 3.04
                                        return [ 0,  0, 27,]
                                else:  # if self.acce_skew_x > 2.52
                                    return [1, 5, 0,]
                            else:  # if self.acce_mean_x > 0.88
                                if self.acce_mean_x <= 2.77:
                                    return [  0,   1, 175,]
                                else:  # if self.acce_mean_x > 2.77
                                    if self.acce_variance_x <= 1.2:
                                        return [0, 0, 3,]
                                    else:  # if self.acce_variance_x > 1.2
                                        return [0, 3, 0,]
                else:  # if self.n_samples > 11.5
                    if self.acce_skew_z <= -0.5:
                        if self.gyro_min_y <= 0.01:
                            if self.gyro_mean_x <= 5.8:
                                return [0, 2, 0,]
                            else:  # if self.gyro_mean_x > 5.8
                                return [0, 0, 2,]
                        else:  # if self.gyro_min_y > 0.01
                            return [17,  0,  0,]
                    else:  # if self.acce_skew_z > -0.5
                        if self.gyro_energy_y <= 353.76:
                            if self.gyro_max_z <= 9.15:
                                return [ 2, 76,  0,]
                            else:  # if self.gyro_max_z > 9.15
                                if self.gyro_rms_z <= 6.38:
                                    if self.gyro_kurt_x <= -0.99:
                                        return [ 0, 13,  0,]
                                    else:  # if self.gyro_kurt_x > -0.99
                                        return [0, 0, 1,]
                                else:  # if self.gyro_rms_z > 6.38
                                    return [0, 1, 5,]
                        else:  # if self.gyro_energy_y > 353.76
                            if self.gyro_rms_z <= 7.25:
                                if self.acce_energy_y <= 174.56:
                                    return [20,  0,  0,]
                                else:  # if self.acce_energy_y > 174.56
                                    return [1, 3, 0,]
                            else:  # if self.gyro_rms_z > 7.25
                                return [ 0, 12,  0,]
            else:  # if self.gyro_energy_y > 499.97
                if self.acce_min_z <= 0.79:
                    if self.gyro_rms_z <= 7.73:
                        return [245,   0,   0,]
                    else:  # if self.gyro_rms_z > 7.73
                        return [0, 6, 0,]
                else:  # if self.acce_min_z > 0.79
                    if self.acce_mean_y <= 2.31:
                        return [0, 9, 1,]
                    else:  # if self.acce_mean_y > 2.31
                        if self.acce_energy_y <= 148.57:
                            return [ 0,  0, 10,]
                        else:  # if self.acce_energy_y > 148.57
                            return [0, 1, 0,]
        else:  # if self.gyro_mean_y > 6.43
            if self.gyro_variance_y <= 12.93:
                if self.n_samples <= 8.5:
                    if self.gyro_variance_x <= 7.47:
                        return [3, 0, 0,]
                    else:  # if self.gyro_variance_x > 7.47
                        return [0, 0, 8,]
                else:  # if self.n_samples > 8.5
                    if self.gyro_min_y <= 8.31:
                        if self.n_samples <= 18.5:
                            if self.acce_std_z <= 1.73:
                                return [  0, 138,   4,]
                            else:  # if self.acce_std_z > 1.73
                                return [0, 1, 2,]
                        else:  # if self.n_samples > 18.5
                            return [2, 0, 0,]
                    else:  # if self.gyro_min_y > 8.31
                        if self.gyro_kurt_x <= 0.49:
                            return [0, 0, 3,]
                        else:  # if self.gyro_kurt_x > 0.49
                            return [0, 3, 0,]
            else:  # if self.gyro_variance_y > 12.93
                if self.acce_skew_y <= -0.0:
                    if self.acce_energy_z <= 14.79:
                        if self.gyro_mean_x <= 2.47:
                            return [0, 2, 0,]
                        else:  # if self.gyro_mean_x > 2.47
                            return [ 0,  0, 22,]
                    else:  # if self.acce_energy_z > 14.79
                        return [0, 2, 0,]
                else:  # if self.acce_skew_y > -0.0
                    return [0, 8, 0,]

    def decision_tree_7(self):
        if self.n_samples <= 14.5:
            if self.gyro_variance_y <= 15.6:
                if self.acce_energy_z <= 10.3:
                    if self.acce_range_x <= 0.65:
                        if self.gyro_kurt_y <= -1.22:
                            if self.gyro_std_z <= 3.72:
                                return [25,  0,  0,]
                            else:  # if self.gyro_std_z > 3.72
                                return [0, 0, 1,]
                        else:  # if self.gyro_kurt_y > -1.22
                            if self.gyro_variance_y <= 7.03:
                                if self.gyro_kurt_x <= 6.06:
                                    return [ 0, 27,  1,]
                                else:  # if self.gyro_kurt_x > 6.06
                                    return [0, 0, 1,]
                            else:  # if self.gyro_variance_y > 7.03
                                if self.acce_energy_y <= 75.5:
                                    return [0, 5, 0,]
                                else:  # if self.acce_energy_y > 75.5
                                    if self.acce_std_x <= 0.09:
                                        return [0, 4, 0,]
                                    else:  # if self.acce_std_x > 0.09
                                        return [0, 0, 7,]
                    else:  # if self.acce_range_x > 0.65
                        if self.acce_rms_y <= 2.77:
                            if self.gyro_range_y <= 8.99:
                                if self.acce_max_x <= 3.99:
                                    return [ 0, 13,  0,]
                                else:  # if self.acce_max_x > 3.99
                                    return [0, 0, 3,]
                            else:  # if self.gyro_range_y > 8.99
                                if self.gyro_max_z <= 9.0:
                                    return [0, 1, 0,]
                                else:  # if self.gyro_max_z > 9.0
                                    return [0, 0, 5,]
                        else:  # if self.acce_rms_y > 2.77
                            return [ 0,  2, 58,]
                else:  # if self.acce_energy_z > 10.3
                    if self.acce_corr_xz <= 0.02:
                        if self.gyro_variance_z <= 6.35:
                            return [ 0, 32,  0,]
                        else:  # if self.gyro_variance_z > 6.35
                            if self.gyro_mean_z <= 2.55:
                                return [ 0, 10,  0,]
                            else:  # if self.gyro_mean_z > 2.55
                                if self.gyro_kurt_y <= -1.24:
                                    if self.gyro_min_z <= 0.04:
                                        return [0, 2, 0,]
                                    else:  # if self.gyro_min_z > 0.04
                                        return [9, 0, 0,]
                                else:  # if self.gyro_kurt_y > -1.24
                                    if self.acce_max_x <= 0.45:
                                        return [0, 2, 0,]
                                    else:  # if self.acce_max_x > 0.45
                                        return [ 0,  0, 33,]
                    else:  # if self.acce_corr_xz > 0.02
                        if self.gyro_rms_z <= 8.78:
                            if self.gyro_min_x <= 0.12:
                                return [  0, 136,   1,]
                            else:  # if self.gyro_min_x > 0.12
                                if self.gyro_corr_xz <= 0.21:
                                    if self.gyro_energy_x <= 752.86:
                                        return [0, 0, 2,]
                                    else:  # if self.gyro_energy_x > 752.86
                                        return [0, 4, 0,]
                                else:  # if self.gyro_corr_xz > 0.21
                                    return [2, 0, 0,]
                        else:  # if self.gyro_rms_z > 8.78
                            if self.gyro_std_y <= 3.04:
                                return [0, 5, 0,]
                            else:  # if self.gyro_std_y > 3.04
                                return [0, 0, 3,]
            else:  # if self.gyro_variance_y > 15.6
                if self.acce_variance_x <= 0.02:
                    if self.acce_range_x <= 0.06:
                        return [0, 0, 1,]
                    else:  # if self.acce_range_x > 0.06
                        return [ 0, 13,  0,]
                else:  # if self.acce_variance_x > 0.02
                    if self.acce_energy_x <= 113.92:
                        if self.gyro_energy_x <= 680.93:
                            if self.gyro_mean_z <= 2.1:
                                return [0, 2, 0,]
                            else:  # if self.gyro_mean_z > 2.1
                                if self.acce_energy_y <= 158.94:
                                    if self.gyro_energy_y <= 682.86:
                                        if self.acce_variance_z <= 0.0:
                                            return [0, 1, 0,]
                                        else:  # if self.acce_variance_z > 0.0
                                            return [  0,   2, 182,]
                                    else:  # if self.gyro_energy_y > 682.86
                                        return [0, 1, 0,]
                                else:  # if self.acce_energy_y > 158.94
                                    return [0, 1, 0,]
                        else:  # if self.gyro_energy_x > 680.93
                            return [0, 5, 1,]
                    else:  # if self.acce_energy_x > 113.92
                        return [ 0, 12,  0,]
        else:  # if self.n_samples > 14.5
            if self.gyro_skew_z <= -1.3:
                if self.acce_rms_y <= 0.95:
                    return [1, 0, 0,]
                else:  # if self.acce_rms_y > 0.95
                    return [ 0, 12,  0,]
            else:  # if self.gyro_skew_z > -1.3
                if self.gyro_rms_y <= 4.57:
                    if self.gyro_variance_z <= 15.13:
                        return [2, 0, 0,]
                    else:  # if self.gyro_variance_z > 15.13
                        return [0, 6, 0,]
                else:  # if self.gyro_rms_y > 4.57
                    if self.gyro_std_z <= 1.58:
                        return [0, 4, 0,]
                    else:  # if self.gyro_std_z > 1.58
                        return [259,   0,   0,]

    def decision_tree_8(self):
        if self.n_samples <= 14.5:
            if self.gyro_energy_x <= 575.62:
                if self.gyro_skew_z <= 0.15:
                    if self.gyro_skew_y <= -1.23:
                        if self.acce_max_z <= 1.1:
                            return [0, 0, 6,]
                        else:  # if self.acce_max_z > 1.1
                            if self.gyro_energy_z <= 629.21:
                                if self.acce_corr_yz <= -0.14:
                                    return [0, 6, 0,]
                                else:  # if self.acce_corr_yz > -0.14
                                    if self.acce_std_z <= 0.19:
                                        return [0, 0, 6,]
                                    else:  # if self.acce_std_z > 0.19
                                        return [0, 2, 0,]
                            else:  # if self.gyro_energy_z > 629.21
                                return [ 0, 22,  0,]
                    else:  # if self.gyro_skew_y > -1.23
                        if self.acce_std_x <= 0.15:
                            if self.gyro_mean_z <= 6.35:
                                if self.acce_corr_xz <= 0.31:
                                    return [33,  0,  0,]
                                else:  # if self.acce_corr_xz > 0.31
                                    return [0, 0, 1,]
                            else:  # if self.gyro_mean_z > 6.35
                                if self.acce_skew_z <= 1.92:
                                    return [0, 7, 1,]
                                else:  # if self.acce_skew_z > 1.92
                                    return [0, 0, 3,]
                        else:  # if self.acce_std_x > 0.15
                            if self.gyro_energy_x <= 487.76:
                                if self.acce_skew_x <= 2.7:
                                    if self.acce_energy_x <= 2.14:
                                        return [0, 1, 0,]
                                    else:  # if self.acce_energy_x > 2.14
                                        return [  0,   0, 217,]
                                else:  # if self.acce_skew_x > 2.7
                                    return [1, 0, 0,]
                            else:  # if self.gyro_energy_x > 487.76
                                if self.gyro_variance_y <= 12.41:
                                    if self.acce_skew_x <= 0.29:
                                        return [0, 5, 1,]
                                    else:  # if self.acce_skew_x > 0.29
                                        return [8, 0, 0,]
                                else:  # if self.gyro_variance_y > 12.41
                                    if self.gyro_mean_y <= 5.75:
                                        if self.acce_std_x <= 1.89:
                                            return [ 0,  0, 25,]
                                        else:  # if self.acce_std_x > 1.89
                                            return [0, 1, 0,]
                                    else:  # if self.gyro_mean_y > 5.75
                                        return [0, 6, 2,]
                else:  # if self.gyro_skew_z > 0.15
                    if self.gyro_rms_x <= 5.15:
                        if self.acce_energy_z <= 8.66:
                            if self.gyro_rms_x <= 3.55:
                                return [0, 6, 0,]
                            else:  # if self.gyro_rms_x > 3.55
                                return [1, 0, 6,]
                        else:  # if self.acce_energy_z > 8.66
                            return [ 1, 72,  0,]
                    else:  # if self.gyro_rms_x > 5.15
                        if self.acce_kurt_x <= -0.24:
                            if self.acce_energy_x <= 92.14:
                                if self.gyro_std_y <= 2.51:
                                    return [0, 2, 0,]
                                else:  # if self.gyro_std_y > 2.51
                                    return [ 0,  0, 21,]
                            else:  # if self.acce_energy_x > 92.14
                                if self.acce_std_z <= 1.05:
                                    return [0, 9, 0,]
                                else:  # if self.acce_std_z > 1.05
                                    return [0, 0, 2,]
                        else:  # if self.acce_kurt_x > -0.24
                            return [ 0, 18,  1,]
            else:  # if self.gyro_energy_x > 575.62
                if self.gyro_rms_z <= 7.12:
                    if self.gyro_mean_z <= 3.19:
                        if self.acce_mean_x <= 0.95:
                            return [0, 0, 1,]
                        else:  # if self.acce_mean_x > 0.95
                            return [0, 9, 0,]
                    else:  # if self.gyro_mean_z > 3.19
                        if self.gyro_min_y <= 0.1:
                            if self.gyro_kurt_x <= -1.37:
                                return [0, 2, 0,]
                            else:  # if self.gyro_kurt_x > -1.37
                                return [1, 0, 8,]
                        else:  # if self.gyro_min_y > 0.1
                            if self.gyro_range_y <= 4.53:
                                return [0, 1, 0,]
                            else:  # if self.gyro_range_y > 4.53
                                return [10,  0,  0,]
                else:  # if self.gyro_rms_z > 7.12
                    if self.gyro_rms_z <= 8.99:
                        if self.acce_max_z <= 3.95:
                            return [  0, 106,   5,]
                        else:  # if self.acce_max_z > 3.95
                            return [0, 0, 1,]
                    else:  # if self.gyro_rms_z > 8.99
                        if self.acce_skew_y <= 0.15:
                            return [0, 0, 3,]
                        else:  # if self.acce_skew_y > 0.15
                            return [0, 2, 0,]
        else:  # if self.n_samples > 14.5
            if self.acce_min_z <= 0.69:
                if self.gyro_corr_xz <= -0.46:
                    return [0, 4, 0,]
                else:  # if self.gyro_corr_xz > -0.46
                    return [241,   0,   0,]
            else:  # if self.acce_min_z > 0.69
                if self.n_samples <= 19.5:
                    return [0, 8, 0,]
                else:  # if self.n_samples > 19.5
                    return [4, 0, 0,]

    def decision_tree_9(self):
        if self.acce_mean_z <= 0.96:
            if self.gyro_kurt_y <= -1.24:
                if self.acce_mean_z <= 0.56:
                    if self.gyro_variance_y <= 19.43:
                        if self.gyro_energy_z <= 815.43:
                            return [0, 0, 9,]
                        else:  # if self.gyro_energy_z > 815.43
                            return [1, 0, 0,]
                    else:  # if self.gyro_variance_y > 19.43
                        return [0, 2, 0,]
                else:  # if self.acce_mean_z > 0.56
                    if self.gyro_rms_z <= 7.52:
                        if self.gyro_energy_y <= 210.96:
                            return [0, 0, 2,]
                        else:  # if self.gyro_energy_y > 210.96
                            if self.acce_mean_x <= 2.92:
                                return [239,   0,   0,]
                            else:  # if self.acce_mean_x > 2.92
                                return [0, 0, 1,]
                    else:  # if self.gyro_rms_z > 7.52
                        return [0, 1, 3,]
            else:  # if self.gyro_kurt_y > -1.24
                if self.acce_min_x <= 0.51:
                    if self.acce_skew_z <= -0.62:
                        return [2, 1, 0,]
                    else:  # if self.acce_skew_z > -0.62
                        if self.acce_rms_y <= 0.97:
                            return [1, 0, 0,]
                        else:  # if self.acce_rms_y > 0.97
                            return [ 1, 37,  2,]
                else:  # if self.acce_min_x > 0.51
                    if self.acce_range_x <= 0.47:
                        return [ 0, 24,  0,]
                    else:  # if self.acce_range_x > 0.47
                        return [ 0,  0, 27,]
        else:  # if self.acce_mean_z > 0.96
            if self.acce_corr_xz <= 0.21:
                if self.gyro_mean_y <= 7.09:
                    if self.acce_energy_x <= 9.4:
                        if self.acce_variance_z <= 0.07:
                            if self.acce_max_x <= 0.46:
                                return [ 0, 13,  0,]
                            else:  # if self.acce_max_x > 0.46
                                return [0, 1, 3,]
                        else:  # if self.acce_variance_z > 0.07
                            if self.acce_kurt_z <= -0.84:
                                return [0, 0, 1,]
                            else:  # if self.acce_kurt_z > -0.84
                                return [15,  0,  0,]
                    else:  # if self.acce_energy_x > 9.4
                        if self.acce_rms_x <= 3.48:
                            if self.acce_skew_z <= 2.5:
                                if self.n_samples <= 11.5:
                                    if self.acce_range_x <= 3.98:
                                        return [  0,   0, 171,]
                                    else:  # if self.acce_range_x > 3.98
                                        if self.gyro_std_z <= 0.39:
                                            return [0, 0, 3,]
                                        else:  # if self.gyro_std_z > 0.39
                                            return [0, 4, 0,]
                                else:  # if self.n_samples > 11.5
                                    if self.acce_min_x <= 0.03:
                                        return [1, 7, 0,]
                                    else:  # if self.acce_min_x > 0.03
                                        if self.gyro_energy_z <= 667.25:
                                            return [0, 0, 4,]
                                        else:  # if self.gyro_energy_z > 667.25
                                            return [3, 0, 1,]
                            else:  # if self.acce_skew_z > 2.5
                                return [0, 2, 0,]
                        else:  # if self.acce_rms_x > 3.48
                            return [0, 9, 0,]
                else:  # if self.gyro_mean_y > 7.09
                    if self.gyro_min_z <= 0.01:
                        if self.gyro_std_z <= 3.48:
                            return [0, 4, 0,]
                        else:  # if self.gyro_std_z > 3.48
                            return [0, 0, 7,]
                    else:  # if self.gyro_min_z > 0.01
                        return [ 0, 43,  2,]
            else:  # if self.acce_corr_xz > 0.21
                if self.gyro_kurt_y <= -1.11:
                    if self.acce_energy_z <= 15.99:
                        if self.acce_max_z <= 1.55:
                            if self.acce_energy_z <= 6.35:
                                return [0, 0, 2,]
                            else:  # if self.acce_energy_z > 6.35
                                return [ 0, 24,  0,]
                        else:  # if self.acce_max_z > 1.55
                            if self.acce_variance_x <= 1.63:
                                return [0, 4, 0,]
                            else:  # if self.acce_variance_x > 1.63
                                if self.acce_skew_y <= -2.99:
                                    return [0, 1, 0,]
                                else:  # if self.acce_skew_y > -2.99
                                    return [ 0,  0, 41,]
                    else:  # if self.acce_energy_z > 15.99
                        if self.gyro_std_z <= 3.97:
                            return [35,  0,  0,]
                        else:  # if self.gyro_std_z > 3.97
                            return [0, 2, 0,]
                else:  # if self.gyro_kurt_y > -1.11
                    if self.acce_max_x <= 0.72:
                        if self.acce_corr_yz <= 0.07:
                            return [0, 6, 0,]
                        else:  # if self.acce_corr_yz > 0.07
                            return [0, 0, 5,]
                    else:  # if self.acce_max_x > 0.72
                        if self.n_samples <= 9.5:
                            if self.acce_energy_y <= 120.64:
                                return [0, 4, 0,]
                            else:  # if self.acce_energy_y > 120.64
                                return [0, 0, 3,]
                        else:  # if self.n_samples > 9.5
                            return [  0, 124,   1,]

    def decision_tree_10(self):
        if self.gyro_mean_z <= 6.5:
            if self.gyro_mean_z <= 3.18:
                if self.acce_max_z <= 0.85:
                    if self.acce_corr_yz <= 0.14:
                        if self.acce_max_z <= 0.6:
                            return [0, 2, 0,]
                        else:  # if self.acce_max_z > 0.6
                            return [2, 0, 0,]
                    else:  # if self.acce_corr_yz > 0.14
                        return [0, 0, 3,]
                else:  # if self.acce_max_z > 0.85
                    if self.acce_mean_y <= 3.22:
                        if self.gyro_variance_y <= 17.62:
                            if self.gyro_energy_z <= 356.02:
                                return [ 2, 94,  0,]
                            else:  # if self.gyro_energy_z > 356.02
                                return [2, 0, 0,]
                        else:  # if self.gyro_variance_y > 17.62
                            return [0, 0, 2,]
                    else:  # if self.acce_mean_y > 3.22
                        if self.acce_rms_x <= 1.27:
                            return [0, 0, 3,]
                        else:  # if self.acce_rms_x > 1.27
                            return [0, 3, 0,]
            else:  # if self.gyro_mean_z > 3.18
                if self.gyro_std_x <= 4.19:
                    if self.n_samples <= 12.5:
                        if self.acce_mean_y <= 1.99:
                            if self.gyro_mean_y <= 6.41:
                                if self.acce_skew_y <= 0.2:
                                    return [0, 3, 0,]
                                else:  # if self.acce_skew_y > 0.2
                                    return [3, 0, 1,]
                            else:  # if self.gyro_mean_y > 6.41
                                return [0, 9, 0,]
                        else:  # if self.acce_mean_y > 1.99
                            if self.gyro_variance_z <= 13.27:
                                return [7, 0, 0,]
                            else:  # if self.gyro_variance_z > 13.27
                                if self.gyro_rms_x <= 4.15:
                                    return [0, 3, 0,]
                                else:  # if self.gyro_rms_x > 4.15
                                    if self.acce_std_y <= 1.94:
                                        return [ 0,  0, 25,]
                                    else:  # if self.acce_std_y > 1.94
                                        return [0, 1, 0,]
                    else:  # if self.n_samples > 12.5
                        if self.gyro_kurt_y <= -0.65:
                            if self.gyro_std_z <= 4.19:
                                return [280,   0,   0,]
                            else:  # if self.gyro_std_z > 4.19
                                return [0, 3, 0,]
                        else:  # if self.gyro_kurt_y > -0.65
                            return [0, 8, 0,]
                else:  # if self.gyro_std_x > 4.19
                    if self.acce_energy_x <= 95.28:
                        return [ 0,  2, 54,]
                    else:  # if self.acce_energy_x > 95.28
                        if self.acce_rms_x <= 3.25:
                            return [0, 5, 0,]
                        else:  # if self.acce_rms_x > 3.25
                            return [0, 0, 1,]
        else:  # if self.gyro_mean_z > 6.5
            if self.acce_rms_y <= 3.04:
                if self.gyro_energy_y <= 487.43:
                    if self.gyro_kurt_z <= 4.2:
                        if self.acce_variance_x <= 0.01:
                            if self.gyro_min_z <= 8.54:
                                return [ 0, 10,  0,]
                            else:  # if self.gyro_min_z > 8.54
                                return [2, 0, 0,]
                        else:  # if self.acce_variance_x > 0.01
                            if self.acce_range_x <= 3.98:
                                if self.gyro_std_y <= 4.47:
                                    return [ 0,  0, 48,]
                                else:  # if self.gyro_std_y > 4.47
                                    return [0, 1, 0,]
                            else:  # if self.acce_range_x > 3.98
                                return [0, 4, 0,]
                    else:  # if self.gyro_kurt_z > 4.2
                        return [ 0, 31,  2,]
                else:  # if self.gyro_energy_y > 487.43
                    if self.n_samples <= 19.0:
                        if self.gyro_corr_xz <= -0.12:
                            return [ 0, 68,  0,]
                        else:  # if self.gyro_corr_xz > -0.12
                            if self.gyro_max_z <= 9.14:
                                return [ 0, 26,  0,]
                            else:  # if self.gyro_max_z > 9.14
                                if self.acce_mean_y <= 1.05:
                                    return [0, 3, 0,]
                                else:  # if self.acce_mean_y > 1.05
                                    return [0, 0, 8,]
                    else:  # if self.n_samples > 19.0
                        return [2, 0, 0,]
            else:  # if self.acce_rms_y > 3.04
                if self.gyro_energy_z <= 802.38:
                    if self.acce_std_x <= 0.09:
                        return [0, 3, 0,]
                    else:  # if self.acce_std_x > 0.09
                        return [  0,   0, 134,]
                else:  # if self.gyro_energy_z > 802.38
                    if self.n_samples <= 11.5:
                        if self.acce_min_z <= 0.67:
                            if self.acce_kurt_z <= 1.65:
                                return [0, 3, 0,]
                            else:  # if self.acce_kurt_z > 1.65
                                return [0, 0, 1,]
                        else:  # if self.acce_min_z > 0.67
                            return [ 0,  0, 10,]
                    else:  # if self.n_samples > 11.5
                        if self.acce_energy_x <= 9.39:
                            return [2, 1, 0,]
                        else:  # if self.acce_energy_x > 9.39
                            return [ 0, 22,  0,]

    def decision_tree_11(self):
        if self.n_samples <= 14.5:
            if self.n_samples <= 10.5:
                if self.acce_rms_x <= 0.54:
                    if self.gyro_mean_y <= 4.59:
                        if self.acce_skew_x <= 0.19:
                            if self.gyro_rms_y <= 5.67:
                                return [0, 4, 0,]
                            else:  # if self.gyro_rms_y > 5.67
                                return [0, 0, 1,]
                        else:  # if self.acce_skew_x > 0.19
                            return [0, 0, 6,]
                    else:  # if self.gyro_mean_y > 4.59
                        if self.acce_variance_x <= 0.0:
                            return [1, 0, 0,]
                        else:  # if self.acce_variance_x > 0.0
                            return [ 0, 16,  0,]
                else:  # if self.acce_rms_x > 0.54
                    if self.gyro_range_y <= 8.8:
                        if self.acce_skew_z <= 0.81:
                            return [ 0, 10,  0,]
                        else:  # if self.acce_skew_z > 0.81
                            return [0, 0, 3,]
                    else:  # if self.gyro_range_y > 8.8
                        if self.gyro_std_x <= 3.53:
                            if self.acce_rms_y <= 2.82:
                                return [0, 8, 0,]
                            else:  # if self.acce_rms_y > 2.82
                                if self.gyro_variance_z <= 16.13:
                                    return [0, 0, 2,]
                                else:  # if self.gyro_variance_z > 16.13
                                    return [0, 1, 0,]
                        else:  # if self.gyro_std_x > 3.53
                            if self.acce_skew_x <= -1.18:
                                return [0, 3, 0,]
                            else:  # if self.acce_skew_x > -1.18
                                return [  0,   2, 233,]
            else:  # if self.n_samples > 10.5
                if self.acce_variance_z <= 0.08:
                    if self.gyro_kurt_y <= -1.66:
                        if self.gyro_variance_y <= 19.32:
                            if self.gyro_min_x <= 0.05:
                                return [ 0,  1, 15,]
                            else:  # if self.gyro_min_x > 0.05
                                return [0, 4, 0,]
                        else:  # if self.gyro_variance_y > 19.32
                            if self.acce_rms_y <= 3.55:
                                return [ 0, 16,  0,]
                            else:  # if self.acce_rms_y > 3.55
                                return [0, 0, 1,]
                    else:  # if self.gyro_kurt_y > -1.66
                        if self.acce_min_x <= 0.1:
                            if self.gyro_variance_y <= 0.05:
                                return [0, 0, 1,]
                            else:  # if self.gyro_variance_y > 0.05
                                return [  0, 157,   1,]
                        else:  # if self.acce_min_x > 0.1
                            if self.acce_energy_y <= 108.34:
                                return [ 0, 20,  0,]
                            else:  # if self.acce_energy_y > 108.34
                                if self.gyro_max_z <= 9.13:
                                    return [1, 7, 0,]
                                else:  # if self.gyro_max_z > 9.13
                                    if self.gyro_variance_x <= 7.28:
                                        return [0, 1, 0,]
                                    else:  # if self.gyro_variance_x > 7.28
                                        return [0, 0, 9,]
                else:  # if self.acce_variance_z > 0.08
                    if self.acce_max_x <= 0.9:
                        if self.gyro_kurt_y <= -1.07:
                            return [43,  0,  0,]
                        else:  # if self.gyro_kurt_y > -1.07
                            return [ 0, 10,  0,]
                    else:  # if self.acce_max_x > 0.9
                        if self.gyro_corr_xy <= -0.52:
                            if self.gyro_energy_y <= 660.22:
                                return [ 0,  0, 10,]
                            else:  # if self.gyro_energy_y > 660.22
                                return [0, 1, 0,]
                        else:  # if self.gyro_corr_xy > -0.52
                            if self.acce_energy_x <= 10.64:
                                if self.acce_rms_x <= 0.9:
                                    if self.gyro_variance_x <= 12.56:
                                        return [2, 0, 0,]
                                    else:  # if self.gyro_variance_x > 12.56
                                        return [0, 2, 0,]
                                else:  # if self.acce_rms_x > 0.9
                                    return [ 0,  0, 10,]
                            else:  # if self.acce_energy_x > 10.64
                                if self.gyro_std_y <= 3.98:
                                    if self.acce_corr_xz <= 0.04:
                                        return [2, 0, 1,]
                                    else:  # if self.acce_corr_xz > 0.04
                                        if self.acce_energy_z <= 12.17:
                                            return [1, 0, 0,]
                                        else:  # if self.acce_energy_z > 12.17
                                            return [ 0, 28,  0,]
                                else:  # if self.gyro_std_y > 3.98
                                    return [0, 0, 2,]
        else:  # if self.n_samples > 14.5
            if self.gyro_std_z <= 2.46:
                return [0, 8, 0,]
            else:  # if self.gyro_std_z > 2.46
                if self.gyro_mean_z <= 6.77:
                    if self.gyro_std_z <= 4.14:
                        if self.gyro_rms_y <= 7.69:
                            return [245,   0,   0,]
                        else:  # if self.gyro_rms_y > 7.69
                            return [0, 2, 0,]
                    else:  # if self.gyro_std_z > 4.14
                        return [0, 3, 0,]
                else:  # if self.gyro_mean_z > 6.77
                    if self.acce_rms_y <= 1.93:
                        return [1, 0, 0,]
                    else:  # if self.acce_rms_y > 1.93
                        return [0, 4, 0,]

    def decision_tree_12(self):
        if self.gyro_mean_z <= 6.52:
            if self.gyro_variance_z <= 15.13:
                if self.gyro_kurt_x <= -1.31:
                    if self.gyro_variance_x <= 17.7:
                        if self.gyro_skew_y <= -1.14:
                            return [0, 2, 0,]
                        else:  # if self.gyro_skew_y > -1.14
                            return [291,   0,   0,]
                    else:  # if self.gyro_variance_x > 17.7
                        if self.acce_corr_yz <= 0.06:
                            return [0, 6, 0,]
                        else:  # if self.acce_corr_yz > 0.06
                            return [0, 1, 3,]
                else:  # if self.gyro_kurt_x > -1.31
                    if self.acce_energy_z <= 14.39:
                        if self.gyro_rms_z <= 4.41:
                            return [ 0, 57,  0,]
                        else:  # if self.gyro_rms_z > 4.41
                            if self.acce_min_x <= 0.18:
                                return [0, 4, 0,]
                            else:  # if self.acce_min_x > 0.18
                                return [5, 0, 0,]
                    else:  # if self.acce_energy_z > 14.39
                        if self.gyro_rms_z <= 4.63:
                            return [0, 7, 0,]
                        else:  # if self.gyro_rms_z > 4.63
                            return [27,  0,  0,]
            else:  # if self.gyro_variance_z > 15.13
                if self.gyro_skew_z <= 0.4:
                    if self.gyro_energy_z <= 576.27:
                        if self.acce_corr_xz <= 0.39:
                            if self.gyro_variance_x <= 13.19:
                                if self.acce_skew_z <= 0.64:
                                    return [1, 3, 0,]
                                else:  # if self.acce_skew_z > 0.64
                                    return [0, 0, 4,]
                            else:  # if self.gyro_variance_x > 13.19
                                return [ 0,  4, 69,]
                        else:  # if self.acce_corr_xz > 0.39
                            if self.acce_mean_x <= 1.55:
                                return [0, 1, 9,]
                            else:  # if self.acce_mean_x > 1.55
                                return [ 0, 10,  0,]
                    else:  # if self.gyro_energy_z > 576.27
                        if self.acce_corr_xz <= -0.67:
                            return [3, 0, 0,]
                        else:  # if self.acce_corr_xz > -0.67
                            if self.gyro_std_x <= 4.43:
                                return [ 0, 10,  0,]
                            else:  # if self.gyro_std_x > 4.43
                                return [0, 0, 1,]
                else:  # if self.gyro_skew_z > 0.4
                    if self.acce_max_x <= 4.0:
                        if self.acce_range_x <= 3.86:
                            if self.acce_min_z <= 0.74:
                                return [0, 5, 1,]
                            else:  # if self.acce_min_z > 0.74
                                return [0, 0, 3,]
                        else:  # if self.acce_range_x > 3.86
                            return [ 0, 26,  0,]
                    else:  # if self.acce_max_x > 4.0
                        return [0, 0, 2,]
        else:  # if self.gyro_mean_z > 6.52
            if self.gyro_energy_y <= 567.24:
                if self.gyro_skew_z <= -0.3:
                    if self.gyro_skew_y <= 1.15:
                        if self.gyro_kurt_z <= 6.26:
                            if self.acce_energy_z <= 14.2:
                                if self.gyro_std_y <= 3.4:
                                    return [0, 3, 1,]
                                else:  # if self.gyro_std_y > 3.4
                                    if self.acce_corr_xz <= 0.77:
                                        return [  0,   0, 158,]
                                    else:  # if self.acce_corr_xz > 0.77
                                        return [0, 1, 0,]
                            else:  # if self.acce_energy_z > 14.2
                                return [1, 1, 0,]
                        else:  # if self.gyro_kurt_z > 6.26
                            return [0, 4, 0,]
                    else:  # if self.gyro_skew_y > 1.15
                        if self.acce_variance_x <= 3.39:
                            if self.acce_skew_x <= 1.14:
                                if self.acce_corr_xz <= -0.63:
                                    return [0, 2, 0,]
                                else:  # if self.acce_corr_xz > -0.63
                                    return [ 0,  0, 17,]
                            else:  # if self.acce_skew_x > 1.14
                                if self.acce_corr_xz <= -0.12:
                                    return [0, 0, 1,]
                                else:  # if self.acce_corr_xz > -0.12
                                    return [ 0, 10,  0,]
                        else:  # if self.acce_variance_x > 3.39
                            return [0, 8, 0,]
                else:  # if self.gyro_skew_z > -0.3
                    if self.gyro_mean_z <= 8.73:
                        if self.gyro_rms_x <= 6.36:
                            return [0, 2, 3,]
                        else:  # if self.gyro_rms_x > 6.36
                            if self.acce_min_y <= 0.0:
                                return [0, 0, 1,]
                            else:  # if self.acce_min_y > 0.0
                                return [ 0, 24,  0,]
                    else:  # if self.gyro_mean_z > 8.73
                        if self.acce_energy_x <= 2.32:
                            return [0, 3, 0,]
                        else:  # if self.acce_energy_x > 2.32
                            return [ 0,  1, 21,]
            else:  # if self.gyro_energy_y > 567.24
                if self.acce_variance_z <= 0.01:
                    if self.gyro_max_z <= 9.12:
                        return [ 0, 14,  0,]
                    else:  # if self.gyro_max_z > 9.12
                        return [0, 0, 5,]
                else:  # if self.acce_variance_z > 0.01
                    return [ 0, 63,  0,]

    def decision_tree_13(self):
        if self.acce_min_z <= 0.69:
            if self.gyro_skew_y <= -0.8:
                if self.gyro_variance_y <= 0.01:
                    return [0, 0, 2,]
                else:  # if self.gyro_variance_y > 0.01
                    if self.acce_std_x <= 1.96:
                        return [ 1, 84,  0,]
                    else:  # if self.acce_std_x > 1.96
                        return [0, 0, 1,]
            else:  # if self.gyro_skew_y > -0.8
                if self.gyro_skew_y <= 0.5:
                    if self.gyro_variance_y <= 4.18:
                        if self.gyro_mean_y <= 8.75:
                            return [ 0, 13,  0,]
                        else:  # if self.gyro_mean_y > 8.75
                            return [1, 0, 2,]
                    else:  # if self.gyro_variance_y > 4.18
                        if self.acce_variance_z <= 2.42:
                            if self.acce_range_x <= 0.22:
                                return [0, 2, 0,]
                            else:  # if self.acce_range_x > 0.22
                                if self.gyro_corr_xy <= -0.42:
                                    return [0, 0, 3,]
                                else:  # if self.gyro_corr_xy > -0.42
                                    if self.acce_rms_x <= 3.2:
                                        return [279,   0,   0,]
                                    else:  # if self.acce_rms_x > 3.2
                                        return [0, 2, 1,]
                        else:  # if self.acce_variance_z > 2.42
                            return [0, 0, 4,]
                else:  # if self.gyro_skew_y > 0.5
                    if self.acce_kurt_z <= -0.64:
                        if self.gyro_kurt_y <= -1.4:
                            return [1, 0, 3,]
                        else:  # if self.gyro_kurt_y > -1.4
                            if self.gyro_variance_y <= 14.12:
                                if self.acce_energy_x <= 9.36:
                                    if self.gyro_range_y <= 9.05:
                                        return [1, 3, 0,]
                                    else:  # if self.gyro_range_y > 9.05
                                        return [0, 0, 3,]
                                else:  # if self.acce_energy_x > 9.36
                                    if self.gyro_rms_x <= 8.59:
                                        return [ 0, 31,  0,]
                                    else:  # if self.gyro_rms_x > 8.59
                                        return [0, 0, 1,]
                            else:  # if self.gyro_variance_y > 14.12
                                return [0, 0, 2,]
                    else:  # if self.acce_kurt_z > -0.64
                        if self.gyro_corr_xz <= 0.55:
                            if self.acce_range_x <= 3.87:
                                if self.acce_energy_x <= 65.8:
                                    if self.gyro_energy_z <= 914.0:
                                        return [ 0,  0, 39,]
                                    else:  # if self.gyro_energy_z > 914.0
                                        return [0, 1, 0,]
                                else:  # if self.acce_energy_x > 65.8
                                    return [0, 1, 0,]
                            else:  # if self.acce_range_x > 3.87
                                if self.acce_min_z <= 0.49:
                                    return [0, 3, 0,]
                                else:  # if self.acce_min_z > 0.49
                                    return [2, 0, 0,]
                        else:  # if self.gyro_corr_xz > 0.55
                            return [0, 5, 0,]
        else:  # if self.acce_min_z > 0.69
            if self.gyro_std_y <= 3.6:
                if self.acce_energy_z <= 10.76:
                    if self.gyro_variance_y <= 6.74:
                        return [0, 5, 0,]
                    else:  # if self.gyro_variance_y > 6.74
                        if self.acce_rms_x <= 3.24:
                            return [ 0,  0, 22,]
                        else:  # if self.acce_rms_x > 3.24
                            return [0, 1, 0,]
                else:  # if self.acce_energy_z > 10.76
                    return [  1, 111,   2,]
            else:  # if self.gyro_std_y > 3.6
                if self.acce_energy_z <= 12.24:
                    if self.acce_range_x <= 0.51:
                        if self.acce_range_x <= 0.07:
                            return [1, 0, 1,]
                        else:  # if self.acce_range_x > 0.07
                            return [0, 5, 0,]
                    else:  # if self.acce_range_x > 0.51
                        if self.acce_energy_x <= 92.5:
                            if self.acce_variance_z <= 0.0:
                                if self.gyro_kurt_y <= -1.83:
                                    return [0, 3, 0,]
                                else:  # if self.gyro_kurt_y > -1.83
                                    return [0, 0, 3,]
                            else:  # if self.acce_variance_z > 0.0
                                return [  0,   0, 169,]
                        else:  # if self.acce_energy_x > 92.5
                            if self.gyro_std_z <= 3.48:
                                return [0, 5, 0,]
                            else:  # if self.gyro_std_z > 3.48
                                return [0, 0, 3,]
                else:  # if self.acce_energy_z > 12.24
                    if self.acce_variance_z <= 0.08:
                        if self.acce_mean_z <= 0.97:
                            return [4, 0, 0,]
                        else:  # if self.acce_mean_z > 0.97
                            if self.acce_skew_y <= -1.44:
                                if self.gyro_variance_x <= 17.83:
                                    return [0, 0, 4,]
                                else:  # if self.gyro_variance_x > 17.83
                                    return [0, 1, 0,]
                            else:  # if self.acce_skew_y > -1.44
                                if self.gyro_kurt_x <= -1.98:
                                    return [0, 0, 1,]
                                else:  # if self.gyro_kurt_x > -1.98
                                    return [ 0, 44,  1,]
                    else:  # if self.acce_variance_z > 0.08
                        return [ 0,  0, 21,]

    def decision_tree_14(self):
        if self.gyro_energy_x <= 576.66:
            if self.gyro_std_x <= 4.01:
                if self.n_samples <= 14.5:
                    if self.gyro_mean_z <= 4.62:
                        if self.acce_energy_x <= 9.44:
                            if self.gyro_mean_z <= 3.41:
                                if self.gyro_mean_x <= 2.23:
                                    return [ 0, 23,  1,]
                                else:  # if self.gyro_mean_x > 2.23
                                    return [1, 0, 2,]
                            else:  # if self.gyro_mean_z > 3.41
                                if self.gyro_rms_y <= 4.63:
                                    return [0, 0, 2,]
                                else:  # if self.gyro_rms_y > 4.63
                                    return [8, 0, 0,]
                        else:  # if self.acce_energy_x > 9.44
                            if self.n_samples <= 8.5:
                                return [0, 0, 3,]
                            else:  # if self.n_samples > 8.5
                                return [ 0, 65,  0,]
                    else:  # if self.gyro_mean_z > 4.62
                        if self.n_samples <= 10.5:
                            if self.gyro_energy_y <= 541.83:
                                if self.acce_energy_y <= 23.56:
                                    return [2, 0, 0,]
                                else:  # if self.acce_energy_y > 23.56
                                    if self.acce_corr_yz <= -0.47:
                                        return [0, 2, 1,]
                                    else:  # if self.acce_corr_yz > -0.47
                                        return [ 0,  1, 56,]
                            else:  # if self.gyro_energy_y > 541.83
                                return [0, 4, 0,]
                        else:  # if self.n_samples > 10.5
                            if self.gyro_mean_z <= 6.45:
                                return [25,  0,  1,]
                            else:  # if self.gyro_mean_z > 6.45
                                if self.gyro_energy_z <= 829.91:
                                    return [0, 0, 2,]
                                else:  # if self.gyro_energy_z > 829.91
                                    return [0, 4, 0,]
                else:  # if self.n_samples > 14.5
                    if self.gyro_skew_y <= 1.15:
                        return [63,  0,  0,]
                    else:  # if self.gyro_skew_y > 1.15
                        return [0, 1, 0,]
            else:  # if self.gyro_std_x > 4.01
                if self.gyro_skew_y <= -1.37:
                    if self.acce_std_y <= 0.61:
                        return [0, 0, 2,]
                    else:  # if self.acce_std_y > 0.61
                        if self.gyro_energy_x <= 322.24:
                            return [0, 0, 2,]
                        else:  # if self.gyro_energy_x > 322.24
                            return [ 0, 30,  2,]
                else:  # if self.gyro_skew_y > -1.37
                    if self.acce_variance_x <= 3.36:
                        if self.gyro_rms_z <= 6.19:
                            if self.acce_energy_x <= 10.72:
                                if self.gyro_mean_z <= 2.1:
                                    return [0, 2, 0,]
                                else:  # if self.gyro_mean_z > 2.1
                                    return [0, 0, 6,]
                            else:  # if self.acce_energy_x > 10.72
                                return [ 0, 14,  1,]
                        else:  # if self.gyro_rms_z > 6.19
                            if self.acce_kurt_x <= 5.66:
                                if self.acce_max_x <= 0.22:
                                    return [0, 3, 1,]
                                else:  # if self.acce_max_x > 0.22
                                    if self.gyro_energy_z <= 822.96:
                                        if self.gyro_std_x <= 4.01:
                                            return [0, 1, 0,]
                                        else:  # if self.gyro_std_x > 4.01
                                            return [  0,   2, 190,]
                                    else:  # if self.gyro_energy_z > 822.96
                                        if self.acce_rms_y <= 3.06:
                                            return [0, 4, 0,]
                                        else:  # if self.acce_rms_y > 3.06
                                            return [0, 1, 6,]
                            else:  # if self.acce_kurt_x > 5.66
                                return [0, 4, 0,]
                    else:  # if self.acce_variance_x > 3.36
                        if self.acce_energy_x <= 83.03:
                            return [0, 0, 9,]
                        else:  # if self.acce_energy_x > 83.03
                            if self.acce_mean_x <= 2.49:
                                return [ 0, 16,  0,]
                            else:  # if self.acce_mean_x > 2.49
                                return [0, 1, 2,]
        else:  # if self.gyro_energy_x > 576.66
            if self.gyro_rms_z <= 7.25:
                if self.gyro_variance_x <= 17.81:
                    if self.gyro_corr_xy <= -0.42:
                        return [0, 0, 6,]
                    else:  # if self.gyro_corr_xy > -0.42
                        if self.gyro_kurt_y <= -0.32:
                            if self.n_samples <= 12.0:
                                return [0, 0, 2,]
                            else:  # if self.n_samples > 12.0
                                return [201,   0,   0,]
                        else:  # if self.gyro_kurt_y > -0.32
                            return [0, 3, 0,]
                else:  # if self.gyro_variance_x > 17.81
                    return [0, 7, 0,]
            else:  # if self.gyro_rms_z > 7.25
                if self.acce_skew_z <= -1.35:
                    return [0, 0, 4,]
                else:  # if self.acce_skew_z > -1.35
                    if self.n_samples <= 18.0:
                        if self.n_samples <= 9.5:
                            return [0, 0, 2,]
                        else:  # if self.n_samples > 9.5
                            return [ 0, 99,  6,]
                    else:  # if self.n_samples > 18.0
                        return [3, 0, 0,]

    def decision_tree_15(self):
        if self.acce_max_x <= 0.95:
            if self.acce_min_x <= 0.17:
                if self.acce_max_x <= 0.53:
                    if self.acce_mean_y <= 2.81:
                        return [ 0, 43,  0,]
                    else:  # if self.acce_mean_y > 2.81
                        return [ 0,  1, 11,]
                else:  # if self.acce_max_x > 0.53
                    if self.acce_kurt_z <= -1.07:
                        if self.acce_rms_z <= 0.86:
                            return [5, 0, 0,]
                        else:  # if self.acce_rms_z > 0.86
                            return [ 0, 25,  0,]
                    else:  # if self.acce_kurt_z > -1.07
                        if self.acce_rms_z <= 1.01:
                            if self.n_samples <= 11.0:
                                return [0, 1, 0,]
                            else:  # if self.n_samples > 11.0
                                return [41,  0,  0,]
                        else:  # if self.acce_rms_z > 1.01
                            if self.gyro_energy_x <= 555.3:
                                return [0, 0, 9,]
                            else:  # if self.gyro_energy_x > 555.3
                                return [1, 1, 0,]
            else:  # if self.acce_min_x > 0.17
                if self.acce_std_z <= 0.21:
                    if self.acce_mean_y <= 1.29:
                        return [5, 0, 0,]
                    else:  # if self.acce_mean_y > 1.29
                        if self.acce_range_x <= 0.39:
                            return [ 0, 14,  0,]
                        else:  # if self.acce_range_x > 0.39
                            return [0, 0, 2,]
                else:  # if self.acce_std_z > 0.21
                    if self.gyro_rms_y <= 3.8:
                        return [0, 4, 0,]
                    else:  # if self.gyro_rms_y > 3.8
                        if self.gyro_min_x <= 4.94:
                            return [155,   0,   0,]
                        else:  # if self.gyro_min_x > 4.94
                            return [0, 1, 0,]
        else:  # if self.acce_max_x > 0.95
            if self.n_samples <= 11.5:
                if self.acce_rms_x <= 3.13:
                    if self.acce_corr_xz <= 0.38:
                        if self.gyro_mean_y <= 8.25:
                            if self.acce_max_x <= 4.0:
                                if self.acce_range_x <= 3.97:
                                    if self.gyro_mean_z <= 2.13:
                                        return [0, 1, 0,]
                                    else:  # if self.gyro_mean_z > 2.13
                                        if self.acce_min_x <= 0.82:
                                            if self.gyro_rms_x <= 1.56:
                                                return [0, 1, 0,]
                                            else:  # if self.gyro_rms_x > 1.56
                                                return [  0,   0, 236,]
                                        else:  # if self.acce_min_x > 0.82
                                            return [0, 1, 0,]
                                else:  # if self.acce_range_x > 3.97
                                    if self.acce_rms_x <= 1.79:
                                        return [0, 5, 0,]
                                    else:  # if self.acce_rms_x > 1.79
                                        return [ 0,  2, 11,]
                            else:  # if self.acce_max_x > 4.0
                                return [2, 0, 0,]
                        else:  # if self.gyro_mean_y > 8.25
                            return [0, 3, 0,]
                    else:  # if self.acce_corr_xz > 0.38
                        if self.gyro_rms_y <= 7.14:
                            if self.gyro_mean_y <= 1.94:
                                return [0, 9, 0,]
                            else:  # if self.gyro_mean_y > 1.94
                                if self.acce_std_z <= 0.75:
                                    return [ 0,  0, 29,]
                                else:  # if self.acce_std_z > 0.75
                                    return [0, 2, 0,]
                        else:  # if self.gyro_rms_y > 7.14
                            return [ 0, 18,  0,]
                else:  # if self.acce_rms_x > 3.13
                    if self.gyro_skew_z <= -1.26:
                        return [0, 1, 4,]
                    else:  # if self.gyro_skew_z > -1.26
                        if self.gyro_std_z <= 4.44:
                            return [ 0, 20,  0,]
                        else:  # if self.gyro_std_z > 4.44
                            return [0, 0, 1,]
            else:  # if self.n_samples > 11.5
                if self.gyro_skew_y <= -0.78:
                    return [ 0, 84,  0,]
                else:  # if self.gyro_skew_y > -0.78
                    if self.gyro_mean_y <= 3.08:
                        if self.acce_max_x <= 2.54:
                            if self.gyro_range_y <= 9.1:
                                return [0, 0, 6,]
                            else:  # if self.gyro_range_y > 9.1
                                return [0, 2, 0,]
                        else:  # if self.acce_max_x > 2.54
                            return [ 2, 45,  0,]
                    else:  # if self.gyro_mean_y > 3.08
                        if self.acce_mean_z <= 1.02:
                            if self.gyro_skew_z <= -1.08:
                                if self.acce_skew_y <= -0.35:
                                    return [0, 0, 2,]
                                else:  # if self.acce_skew_y > -0.35
                                    return [0, 3, 0,]
                            else:  # if self.gyro_skew_z > -1.08
                                if self.acce_min_y <= 2.21:
                                    if self.gyro_kurt_z <= 0.69:
                                        return [79,  0,  0,]
                                    else:  # if self.gyro_kurt_z > 0.69
                                        return [0, 1, 0,]
                                else:  # if self.acce_min_y > 2.21
                                    return [0, 1, 0,]
                        else:  # if self.acce_mean_z > 1.02
                            return [1, 8, 0,]

    def decision_tree_16(self):
        if self.gyro_skew_y <= -1.36:
            if self.n_samples <= 8.5:
                return [0, 0, 2,]
            else:  # if self.n_samples > 8.5
                if self.gyro_variance_z <= 14.39:
                    return [  0, 133,   2,]
                else:  # if self.gyro_variance_z > 14.39
                    if self.gyro_mean_y <= 7.99:
                        return [ 0, 14,  0,]
                    else:  # if self.gyro_mean_y > 7.99
                        if self.acce_min_y <= 0.43:
                            return [0, 0, 6,]
                        else:  # if self.acce_min_y > 0.43
                            return [0, 1, 0,]
        else:  # if self.gyro_skew_y > -1.36
            if self.gyro_std_x <= 4.07:
                if self.gyro_energy_y <= 345.89:
                    if self.acce_energy_z <= 11.76:
                        if self.acce_range_x <= 0.37:
                            if self.gyro_kurt_z <= -1.54:
                                return [2, 0, 0,]
                            else:  # if self.gyro_kurt_z > -1.54
                                return [ 0, 14,  0,]
                        else:  # if self.acce_range_x > 0.37
                            if self.acce_kurt_z <= -1.31:
                                if self.acce_corr_yz <= -0.28:
                                    return [0, 0, 1,]
                                else:  # if self.acce_corr_yz > -0.28
                                    return [0, 4, 0,]
                            else:  # if self.acce_kurt_z > -1.31
                                if self.acce_energy_y <= 45.94:
                                    return [0, 1, 0,]
                                else:  # if self.acce_energy_y > 45.94
                                    return [ 1,  0, 49,]
                    else:  # if self.acce_energy_z > 11.76
                        if self.acce_corr_xz <= -0.12:
                            if self.gyro_rms_y <= 4.88:
                                return [0, 0, 4,]
                            else:  # if self.gyro_rms_y > 4.88
                                return [1, 1, 0,]
                        else:  # if self.acce_corr_xz > -0.12
                            return [ 0, 36,  1,]
                else:  # if self.gyro_energy_y > 345.89
                    if self.gyro_std_z <= 2.65:
                        if self.gyro_mean_z <= 8.68:
                            return [ 0, 15,  0,]
                        else:  # if self.gyro_mean_z > 8.68
                            return [0, 0, 7,]
                    else:  # if self.gyro_std_z > 2.65
                        if self.acce_min_z <= 0.74:
                            if self.gyro_corr_xy <= -0.52:
                                return [0, 1, 1,]
                            else:  # if self.gyro_corr_xy > -0.52
                                if self.acce_min_y <= 3.67:
                                    if self.gyro_std_y <= 3.91:
                                        if self.gyro_variance_x <= 7.08:
                                            return [0, 1, 0,]
                                        else:  # if self.gyro_variance_x > 7.08
                                            return [266,   0,   0,]
                                    else:  # if self.gyro_std_y > 3.91
                                        if self.n_samples <= 16.0:
                                            return [0, 3, 0,]
                                        else:  # if self.n_samples > 16.0
                                            return [1, 0, 0,]
                                else:  # if self.acce_min_y > 3.67
                                    return [0, 1, 0,]
                        else:  # if self.acce_min_z > 0.74
                            if self.gyro_mean_x <= 2.97:
                                if self.acce_energy_y <= 50.18:
                                    return [0, 0, 1,]
                                else:  # if self.acce_energy_y > 50.18
                                    return [0, 5, 0,]
                            else:  # if self.gyro_mean_x > 2.97
                                return [0, 0, 8,]
            else:  # if self.gyro_std_x > 4.07
                if self.acce_energy_x <= 92.75:
                    if self.acce_mean_x <= 0.66:
                        if self.gyro_energy_y <= 874.26:
                            if self.gyro_variance_z <= 10.37:
                                if self.acce_skew_y <= -1.04:
                                    if self.acce_skew_y <= -2.25:
                                        return [0, 2, 0,]
                                    else:  # if self.acce_skew_y > -2.25
                                        return [0, 0, 3,]
                                else:  # if self.acce_skew_y > -1.04
                                    return [ 0, 26,  0,]
                            else:  # if self.gyro_variance_z > 10.37
                                if self.acce_rms_x <= 0.4:
                                    return [0, 0, 8,]
                                else:  # if self.acce_rms_x > 0.4
                                    return [0, 5, 0,]
                        else:  # if self.gyro_energy_y > 874.26
                            return [5, 0, 0,]
                    else:  # if self.acce_mean_x > 0.66
                        if self.gyro_skew_z <= 0.58:
                            if self.gyro_rms_z <= 6.3:
                                if self.gyro_energy_z <= 518.18:
                                    return [0, 0, 7,]
                                else:  # if self.gyro_energy_z > 518.18
                                    return [7, 0, 0,]
                            else:  # if self.gyro_rms_z > 6.3
                                return [  0,   0, 195,]
                        else:  # if self.gyro_skew_z > 0.58
                            if self.gyro_skew_z <= 0.85:
                                return [0, 8, 0,]
                            else:  # if self.gyro_skew_z > 0.85
                                if self.acce_max_z <= 1.44:
                                    return [0, 1, 0,]
                                else:  # if self.acce_max_z > 1.44
                                    return [0, 0, 5,]
                else:  # if self.acce_energy_x > 92.75
                    if self.gyro_mean_x <= 6.09:
                        return [ 0, 43,  0,]
                    else:  # if self.gyro_mean_x > 6.09
                        return [0, 0, 1,]

