class RandomForestOptimized:    
    def __init__(self):
            pass
    
    def score(self, n_samples, gyro_std_y, acce_min_z, gyro_std_x, gyro_variance_y, gyro_kurt_z, gyro_kurt_y, gyro_skew_y, gyro_energy_y, gyro_kurt_x):
        self.n_samples = n_samples
        self.gyro_std_y = gyro_std_y
        self.acce_min_z = acce_min_z
        self.gyro_std_x = gyro_std_x
        self.gyro_variance_y = gyro_variance_y
        self.gyro_kurt_z = gyro_kurt_z
        self.gyro_kurt_y = gyro_kurt_y
        self.gyro_skew_y = gyro_skew_y
        self.gyro_energy_y = gyro_energy_y
        self.gyro_kurt_x = gyro_kurt_x
    
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
    
        trees_values = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]
    
        return [sum(col) / len(col) for col in zip(*trees_values)]

    def decision_tree_0(self):
        if self.gyro_std_y <= 3.94:
            if self.gyro_kurt_y <= -1.36:
                return [307,  10,   1,]
            else:  # if self.gyro_kurt_y > -1.36
                if self.n_samples <= 9.5:
                    return [ 0,  9, 42,]
                else:  # if self.n_samples > 9.5
                    if self.n_samples <= 18.0:
                        if self.gyro_energy_y <= 167.85:
                            if self.acce_min_z <= 0.12:
                                return [ 0,  2, 20,]
                            else:  # if self.acce_min_z > 0.12
                                if self.gyro_std_x <= 4.29:
                                    return [ 0, 37,  1,]
                                else:  # if self.gyro_std_x > 4.29
                                    return [0, 2, 8,]
                        else:  # if self.gyro_energy_y > 167.85
                            return [  6, 181,  11,]
                    else:  # if self.n_samples > 18.0
                        return [7, 0, 0,]
        else:  # if self.gyro_std_y > 3.94
            if self.gyro_kurt_z <= 6.26:
                if self.gyro_energy_y <= 569.8:
                    if self.n_samples <= 11.5:
                        if self.gyro_std_x <= 2.54:
                            return [0, 6, 0,]
                        else:  # if self.gyro_std_x > 2.54
                            return [  0,   6, 201,]
                    else:  # if self.n_samples > 11.5
                        return [ 0, 13,  2,]
                else:  # if self.gyro_energy_y > 569.8
                    return [ 4, 12,  1,]
            else:  # if self.gyro_kurt_z > 6.26
                return [ 0, 10,  0,]

    def decision_tree_1(self):
        if self.gyro_kurt_y <= -1.1:
            if self.gyro_variance_y <= 15.5:
                if self.gyro_kurt_z <= -0.35:
                    if self.gyro_std_x <= 4.17:
                        return [295,   5,   2,]
                    else:  # if self.gyro_std_x > 4.17
                        return [0, 8, 0,]
                else:  # if self.gyro_kurt_z > -0.35
                    return [ 1, 12,  2,]
            else:  # if self.gyro_variance_y > 15.5
                if self.gyro_std_x <= 3.41:
                    if self.gyro_energy_y <= 324.29:
                        return [3, 0, 2,]
                    else:  # if self.gyro_energy_y > 324.29
                        return [ 0, 19,  1,]
                else:  # if self.gyro_std_x > 3.41
                    if self.n_samples <= 11.5:
                        return [  0,   7, 195,]
                    else:  # if self.n_samples > 11.5
                        return [ 0, 13,  3,]
        else:  # if self.gyro_kurt_y > -1.1
            if self.gyro_std_x <= 3.65:
                return [  1, 119,   4,]
            else:  # if self.gyro_std_x > 3.65
                if self.acce_min_z <= 0.19:
                    if self.n_samples <= 12.5:
                        return [ 0,  0, 28,]
                    else:  # if self.n_samples > 12.5
                        return [0, 4, 0,]
                else:  # if self.acce_min_z > 0.19
                    if self.n_samples <= 10.5:
                        return [ 0,  8, 46,]
                    else:  # if self.n_samples > 10.5
                        return [  2, 109,  10,]

    def decision_tree_2(self):
        if self.acce_min_z <= 0.69:
            if self.gyro_std_y <= 3.23:
                if self.gyro_energy_y <= 587.57:
                    if self.acce_min_z <= 0.13:
                        return [ 1,  3, 12,]
                    else:  # if self.acce_min_z > 0.13
                        return [ 7, 26,  1,]
                else:  # if self.gyro_energy_y > 587.57
                    return [ 0, 50,  0,]
            else:  # if self.gyro_std_y > 3.23
                if self.gyro_kurt_y <= -1.24:
                    if self.n_samples <= 11.5:
                        if self.gyro_variance_y <= 12.94:
                            return [4, 0, 0,]
                        else:  # if self.gyro_variance_y > 12.94
                            return [ 0,  2, 26,]
                    else:  # if self.n_samples > 11.5
                        return [293,   2,   0,]
                else:  # if self.gyro_kurt_y > -1.24
                    if self.gyro_std_x <= 4.25:
                        return [ 3, 28,  9,]
                    else:  # if self.gyro_std_x > 4.25
                        if self.gyro_energy_y <= 251.4:
                            return [ 0,  1, 20,]
                        else:  # if self.gyro_energy_y > 251.4
                            return [0, 6, 0,]
        else:  # if self.acce_min_z > 0.69
            if self.n_samples <= 10.5:
                if self.gyro_std_x <= 2.68:
                    return [ 3, 11,  0,]
                else:  # if self.gyro_std_x > 2.68
                    return [  0,   8, 207,]
            else:  # if self.n_samples > 10.5
                return [  5, 145,  26,]

    def decision_tree_3(self):
        if self.n_samples <= 14.5:
            if self.gyro_std_x <= 3.65:
                if self.gyro_kurt_x <= -1.51:
                    return [26,  0,  0,]
                else:  # if self.gyro_kurt_x > -1.51
                    return [  0, 131,  23,]
            else:  # if self.gyro_std_x > 3.65
                if self.gyro_energy_y <= 578.92:
                    if self.n_samples <= 11.5:
                        if self.acce_min_z <= 0.69:
                            if self.gyro_energy_y <= 507.81:
                                return [ 0, 12, 44,]
                            else:  # if self.gyro_energy_y > 507.81
                                return [ 0, 13,  1,]
                        else:  # if self.acce_min_z > 0.69
                            return [  0,   6, 232,]
                    else:  # if self.n_samples > 11.5
                        if self.gyro_std_x <= 3.94:
                            return [12,  7,  5,]
                        else:  # if self.gyro_std_x > 3.94
                            return [ 0, 49,  6,]
                else:  # if self.gyro_energy_y > 578.92
                    if self.gyro_variance_y <= 0.09:
                        return [0, 0, 5,]
                    else:  # if self.gyro_variance_y > 0.09
                        return [ 2, 73,  7,]
        else:  # if self.n_samples > 14.5
            if self.acce_min_z <= 0.71:
                if self.gyro_kurt_z <= -0.25:
                    return [222,   0,   0,]
                else:  # if self.gyro_kurt_z > -0.25
                    return [1, 5, 0,]
            else:  # if self.acce_min_z > 0.71
                return [ 0, 17,  0,]

    def decision_tree_4(self):
        if self.gyro_std_y <= 3.96:
            if self.acce_min_z <= 0.6:
                if self.gyro_variance_y <= 11.31:
                    if self.acce_min_z <= 0.35:
                        if self.gyro_skew_y <= 2.18:
                            return [15, 15,  2,]
                        else:  # if self.gyro_skew_y > 2.18
                            return [ 0,  3, 16,]
                    else:  # if self.acce_min_z > 0.35
                        if self.gyro_kurt_y <= -1.62:
                            return [7, 0, 0,]
                        else:  # if self.gyro_kurt_y > -1.62
                            return [ 1, 53,  2,]
                else:  # if self.gyro_variance_y > 11.31
                    if self.gyro_kurt_y <= -1.07:
                        return [237,   2,   1,]
                    else:  # if self.gyro_kurt_y > -1.07
                        if self.gyro_skew_y <= 1.01:
                            return [ 0, 10,  1,]
                        else:  # if self.gyro_skew_y > 1.01
                            return [ 0,  3, 22,]
            else:  # if self.acce_min_z > 0.6
                if self.n_samples <= 9.5:
                    return [ 0,  5, 33,]
                else:  # if self.n_samples > 9.5
                    if self.n_samples <= 17.5:
                        return [  0, 176,  18,]
                    else:  # if self.n_samples > 17.5
                        return [19,  0,  0,]
        else:  # if self.gyro_std_y > 3.96
            if self.gyro_std_x <= 3.4:
                return [ 2, 14,  9,]
            else:  # if self.gyro_std_x > 3.4
                return [  0,  23, 210,]

    def decision_tree_5(self):
        if self.n_samples <= 14.5:
            if self.gyro_std_y <= 3.81:
                if self.gyro_kurt_y <= -1.35:
                    if self.gyro_std_y <= 1.77:
                        return [2, 5, 5,]
                    else:  # if self.gyro_std_y > 1.77
                        return [48,  0,  0,]
                else:  # if self.gyro_kurt_y > -1.35
                    if self.n_samples <= 9.5:
                        return [ 0,  5, 36,]
                    else:  # if self.n_samples > 9.5
                        if self.gyro_energy_y <= 171.46:
                            if self.acce_min_z <= 0.33:
                                return [ 0,  6, 16,]
                            else:  # if self.acce_min_z > 0.33
                                return [ 0, 36,  8,]
                        else:  # if self.gyro_energy_y > 171.46
                            return [  1, 161,   4,]
            else:  # if self.gyro_std_y > 3.81
                if self.gyro_std_x <= 3.55:
                    if self.gyro_energy_y <= 325.88:
                        return [2, 1, 5,]
                    else:  # if self.gyro_energy_y > 325.88
                        return [ 0, 25,  0,]
                else:  # if self.gyro_std_x > 3.55
                    if self.acce_min_z <= 0.96:
                        return [  0,  24, 231,]
                    else:  # if self.acce_min_z > 0.96
                        return [ 0, 10,  4,]
        else:  # if self.n_samples > 14.5
            if self.gyro_kurt_y <= -0.9:
                return [244,   1,   0,]
            else:  # if self.gyro_kurt_y > -0.9
                return [ 0, 19,  0,]

    def decision_tree_6(self):
        if self.acce_min_z <= 0.63:
            if self.n_samples <= 14.5:
                if self.gyro_kurt_y <= -1.24:
                    if self.gyro_kurt_x <= -0.22:
                        if self.gyro_std_y <= 3.68:
                            return [36,  2,  1,]
                        else:  # if self.gyro_std_y > 3.68
                            return [ 0,  2, 13,]
                    else:  # if self.gyro_kurt_x > -0.22
                        return [0, 9, 1,]
                else:  # if self.gyro_kurt_y > -1.24
                    return [ 0, 93, 38,]
            else:  # if self.n_samples > 14.5
                return [249,   4,   0,]
        else:  # if self.acce_min_z > 0.63
            if self.gyro_energy_y <= 573.51:
                if self.gyro_skew_y <= 0.71:
                    return [  5,  30, 187,]
                else:  # if self.gyro_skew_y > 0.71
                    if self.acce_min_z <= 0.87:
                        return [ 0, 49, 10,]
                    else:  # if self.acce_min_z > 0.87
                        if self.gyro_std_x <= 3.92:
                            return [ 0, 13,  2,]
                        else:  # if self.gyro_std_x > 3.92
                            if self.n_samples <= 11.5:
                                return [ 0,  0, 21,]
                            else:  # if self.n_samples > 11.5
                                return [0, 5, 0,]
            else:  # if self.gyro_energy_y > 573.51
                if self.gyro_std_x <= 4.4:
                    return [  6, 108,   9,]
                else:  # if self.gyro_std_x > 4.4
                    return [0, 0, 6,]

    def decision_tree_7(self):
        if self.n_samples <= 14.5:
            if self.gyro_variance_y <= 15.6:
                if self.gyro_kurt_y <= -1.63:
                    if self.gyro_variance_y <= 14.46:
                        return [27,  0,  0,]
                    else:  # if self.gyro_variance_y > 14.46
                        return [0, 4, 0,]
                else:  # if self.gyro_kurt_y > -1.63
                    if self.n_samples <= 9.5:
                        if self.gyro_skew_y <= -2.34:
                            return [0, 5, 0,]
                        else:  # if self.gyro_skew_y > -2.34
                            return [ 0,  3, 67,]
                    else:  # if self.n_samples > 9.5
                        if self.gyro_skew_y <= 1.45:
                            if self.acce_min_z <= 0.37:
                                return [ 9, 20,  4,]
                            else:  # if self.acce_min_z > 0.37
                                return [  0, 174,  11,]
                        else:  # if self.gyro_skew_y > 1.45
                            if self.gyro_variance_y <= 10.66:
                                if self.gyro_energy_y <= 85.66:
                                    return [ 0,  4, 11,]
                                else:  # if self.gyro_energy_y > 85.66
                                    return [ 0, 31,  2,]
                            else:  # if self.gyro_variance_y > 10.66
                                return [ 0,  2, 20,]
            else:  # if self.gyro_variance_y > 15.6
                return [  0,  37, 184,]
        else:  # if self.n_samples > 14.5
            if self.gyro_kurt_z <= -0.65:
                return [260,   7,   0,]
            else:  # if self.gyro_kurt_z > -0.65
                return [ 2, 15,  0,]

    def decision_tree_8(self):
        if self.gyro_std_y <= 3.95:
            if self.n_samples <= 14.5:
                if self.gyro_kurt_x <= -1.51:
                    if self.gyro_energy_y <= 669.4:
                        if self.gyro_std_x <= 4.02:
                            return [52,  1,  0,]
                        else:  # if self.gyro_std_x > 4.02
                            return [ 0, 30, 52,]
                    else:  # if self.gyro_energy_y > 669.4
                        return [ 0, 35,  7,]
                else:  # if self.gyro_kurt_x > -1.51
                    if self.gyro_energy_y <= 165.93:
                        if self.gyro_std_y <= 2.56:
                            return [ 0, 18,  3,]
                        else:  # if self.gyro_std_y > 2.56
                            return [ 0,  6, 24,]
                    else:  # if self.gyro_energy_y > 165.93
                        return [  3, 142,   3,]
            else:  # if self.n_samples > 14.5
                if self.gyro_std_x <= 4.16:
                    if self.gyro_skew_y <= 0.98:
                        return [243,   1,   0,]
                    else:  # if self.gyro_skew_y > 0.98
                        return [0, 4, 0,]
                else:  # if self.gyro_std_x > 4.16
                    return [0, 7, 0,]
        else:  # if self.gyro_std_y > 3.95
            if self.gyro_std_x <= 3.55:
                return [ 0, 22,  6,]
            else:  # if self.gyro_std_x > 3.55
                if self.gyro_energy_y <= 575.57:
                    return [  0,  18, 213,]
                else:  # if self.gyro_energy_y > 575.57
                    return [2, 5, 2,]

    def decision_tree_9(self):
        if self.gyro_kurt_y <= -1.31:
            if self.gyro_std_y <= 3.95:
                if self.gyro_variance_y <= 4.84:
                    return [0, 6, 1,]
                else:  # if self.gyro_variance_y > 4.84
                    return [286,   1,   1,]
            else:  # if self.gyro_std_y > 3.95
                if self.gyro_kurt_x <= 0.5:
                    if self.gyro_energy_y <= 490.14:
                        return [  0,  13, 169,]
                    else:  # if self.gyro_energy_y > 490.14
                        return [ 0, 10, 12,]
                else:  # if self.gyro_kurt_x > 0.5
                    return [ 0, 10,  4,]
        else:  # if self.gyro_kurt_y > -1.31
            if self.n_samples <= 10.5:
                if self.gyro_variance_y <= 6.62:
                    return [ 0, 16,  0,]
                else:  # if self.gyro_variance_y > 6.62
                    if self.gyro_kurt_x <= 3.4:
                        if self.gyro_std_x <= 3.62:
                            return [0, 8, 3,]
                        else:  # if self.gyro_std_x > 3.62
                            return [ 0, 12, 73,]
                    else:  # if self.gyro_kurt_x > 3.4
                        return [0, 5, 0,]
            else:  # if self.n_samples > 10.5
                if self.acce_min_z <= 0.06:
                    if self.n_samples <= 11.5:
                        return [ 0,  0, 11,]
                    else:  # if self.n_samples > 11.5
                        return [4, 8, 3,]
                else:  # if self.acce_min_z > 0.06
                    return [  8, 224,  11,]

    def decision_tree_10(self):
        if self.n_samples <= 14.5:
            if self.n_samples <= 10.5:
                if self.gyro_std_y <= 3.6:
                    if self.gyro_std_x <= 3.66:
                        return [ 5, 21,  3,]
                    else:  # if self.gyro_std_x > 3.66
                        return [ 0, 15, 27,]
                else:  # if self.gyro_std_y > 3.6
                    return [  0,  14, 209,]
            else:  # if self.n_samples > 10.5
                if self.n_samples <= 11.5:
                    if self.gyro_variance_y <= 14.6:
                        if self.gyro_kurt_x <= -1.64:
                            return [ 5, 16, 16,]
                        else:  # if self.gyro_kurt_x > -1.64
                            return [ 0, 39,  2,]
                    else:  # if self.gyro_variance_y > 14.6
                        return [ 0,  5, 29,]
                else:  # if self.n_samples > 11.5
                    if self.gyro_kurt_y <= -1.37:
                        if self.acce_min_z <= 0.39:
                            return [32,  2,  0,]
                        else:  # if self.acce_min_z > 0.39
                            return [ 0, 32,  0,]
                    else:  # if self.gyro_kurt_y > -1.37
                        return [  3, 148,   6,]
        else:  # if self.n_samples > 14.5
            if self.acce_min_z <= 0.69:
                if self.gyro_std_x <= 4.22:
                    return [255,   1,   0,]
                else:  # if self.gyro_std_x > 4.22
                    return [0, 4, 0,]
            else:  # if self.acce_min_z > 0.69
                return [2, 8, 0,]

