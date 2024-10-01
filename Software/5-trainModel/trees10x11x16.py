class RandomForestOptimized:    
    def __init__(self):
            pass
    
    def score(self, n_samples, gyro_std_y, acce_min_z, gyro_std_x, gyro_variance_y, gyro_kurt_z, gyro_kurt_y, gyro_skew_y, gyro_variance_z, gyro_kurt_x, gyro_rms_y, gyro_mean_y, acce_std_z, gyro_mean_z, acce_rms_x, gyro_energy_y):
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
        self.gyro_rms_y = gyro_rms_y
        self.gyro_mean_y = gyro_mean_y
        self.acce_std_z = acce_std_z
        self.gyro_mean_z = gyro_mean_z
        self.acce_rms_x = acce_rms_x
        self.gyro_energy_y = gyro_energy_y
    
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
        if self.gyro_mean_y <= 0.6:
            if self.acce_mean_x <= 9.83:
                if self.gyro_std_z <= -1.7:
                    return [5, 3, 7,]
                else:  # if self.gyro_std_z > -1.7
                    return [ 1, 42,  6,]
            else:  # if self.acce_mean_x > 9.83
                if self.acce_mean_x <= 15.48:
                    if self.gyro_std_x <= 0.93:
                        return [300,  13,   0,]
                    else:  # if self.gyro_std_x > 0.93
                        return [ 0,  7, 14,]
                else:  # if self.acce_mean_x > 15.48
                    return [ 4,  8, 18,]
        else:  # if self.gyro_mean_y > 0.6
            if self.gyro_variance_z <= 574.27:
                if self.acce_std_y <= 3.08:
                    if self.gyro_std_y <= 0.04:
                        return [ 0,  0, 11,]
                    else:  # if self.gyro_std_y > 0.04
                        return [ 2, 63, 20,]
                else:  # if self.acce_std_y > 3.08
                    return [  0,  36, 204,]
            else:  # if self.gyro_variance_z > 574.27
                if self.acce_mean_z <= -1.4:
                    if self.gyro_std_y <= 8.16:
                        return [ 0, 10,  0,]
                    else:  # if self.gyro_std_y > 8.16
                        return [12,  0,  1,]
                else:  # if self.acce_mean_z > -1.4
                    return [  0, 106,   6,]

    def decision_tree_1(self):
        if self.gyro_mean_y <= 0.62:
            if self.n_samples <= 12.5:
                if self.acce_std_y <= 5.73:
                    if self.gyro_variance_y <= 0.89:
                        return [ 8, 16,  5,]
                    else:  # if self.gyro_variance_y > 0.89
                        if self.acce_std_x <= 1.76:
                            return [0, 7, 0,]
                        else:  # if self.acce_std_x > 1.76
                            return [ 2,  5, 45,]
                else:  # if self.acce_std_y > 5.73
                    return [ 2, 35,  2,]
            else:  # if self.n_samples > 12.5
                if self.acce_mean_x <= 10.45:
                    return [ 4, 20,  0,]
                else:  # if self.acce_mean_x > 10.45
                    if self.gyro_variance_x <= 7.05:
                        return [270,   4,   0,]
                    else:  # if self.gyro_variance_x > 7.05
                        return [0, 7, 0,]
        else:  # if self.gyro_mean_y > 0.62
            if self.gyro_variance_z <= 575.83:
                if self.n_samples <= 11.5:
                    return [  3,  26, 231,]
                else:  # if self.n_samples > 11.5
                    return [ 5, 58,  2,]
            else:  # if self.gyro_variance_z > 575.83
                if self.n_samples <= 18.0:
                    return [  0, 126,   8,]
                else:  # if self.n_samples > 18.0
                    return [8, 0, 0,]

    def decision_tree_2(self):
        if self.acce_mean_z <= -1.32:
            if self.gyro_mean_y <= 0.69:
                if self.gyro_mean_x <= 4.03:
                    if self.acce_mean_x <= 4.84:
                        return [ 1, 11,  0,]
                    else:  # if self.acce_mean_x > 4.84
                        return [298,   1,   2,]
                else:  # if self.gyro_mean_x > 4.03
                    return [ 0,  3, 24,]
            else:  # if self.gyro_mean_y > 0.69
                if self.n_samples <= 11.5:
                    if self.acce_mean_y <= -1.96:
                        return [3, 3, 3,]
                    else:  # if self.acce_mean_y > -1.96
                        return [  0,   5, 164,]
                else:  # if self.n_samples > 11.5
                    return [ 4, 24,  2,]
        else:  # if self.acce_mean_z > -1.32
            if self.n_samples <= 9.5:
                return [ 0,  5, 47,]
            else:  # if self.n_samples > 9.5
                if self.gyro_std_x <= -0.9:
                    return [  0, 135,   6,]
                else:  # if self.gyro_std_x > -0.9
                    if self.acce_std_z <= 0.28:
                        return [ 6, 84, 17,]
                    else:  # if self.acce_std_z > 0.28
                        if self.gyro_mean_z <= 4.08:
                            return [4, 8, 5,]
                        else:  # if self.gyro_mean_z > 4.08
                            return [ 0,  3, 31,]

    def decision_tree_3(self):
        if self.gyro_mean_y <= 0.69:
            if self.n_samples <= 14.5:
                if self.gyro_mean_y <= 0.22:
                    if self.acce_std_x <= 5.47:
                        return [ 2,  8, 39,]
                    else:  # if self.acce_std_x > 5.47
                        if self.gyro_variance_y <= 0.8:
                            return [29,  0,  0,]
                        else:  # if self.gyro_variance_y > 0.8
                            return [ 2, 14,  5,]
                else:  # if self.gyro_mean_y > 0.22
                    return [  6, 120,  18,]
            else:  # if self.n_samples > 14.5
                return [222,   5,   0,]
        else:  # if self.gyro_mean_y > 0.69
            if self.gyro_mean_x <= 3.78:
                if self.n_samples <= 10.5:
                    if self.gyro_mean_z <= 3.63:
                        return [ 0, 12,  1,]
                    else:  # if self.gyro_mean_z > 3.63
                        return [ 0,  0, 35,]
                else:  # if self.n_samples > 10.5
                    return [ 1, 99,  8,]
            else:  # if self.gyro_mean_x > 3.78
                if self.gyro_variance_y <= 0.26:
                    return [ 0, 22,  2,]
                else:  # if self.gyro_variance_y > 0.26
                    if self.n_samples <= 11.5:
                        return [  1,   7, 210,]
                    else:  # if self.n_samples > 11.5
                        return [ 0, 26,  5,]

    def decision_tree_4(self):
        if self.gyro_variance_z <= 498.93:
            if self.acce_std_x <= 4.86:
                if self.acce_std_z <= 0.38:
                    return [ 6, 89, 39,]
                else:  # if self.acce_std_z > 0.38
                    return [ 2,  4, 28,]
            else:  # if self.acce_std_x > 4.86
                if self.acce_mean_x <= 13.86:
                    return [49,  0,  2,]
                else:  # if self.acce_mean_x > 13.86
                    if self.gyro_variance_x <= 3.27:
                        return [ 2, 15,  4,]
                    else:  # if self.gyro_variance_x > 3.27
                        return [  0,  14, 210,]
        else:  # if self.gyro_variance_z > 498.93
            if self.acce_std_x <= 6.94:
                if self.gyro_std_y <= 6.65:
                    return [0, 7, 2,]
                else:  # if self.gyro_std_y > 6.65
                    return [215,   0,   0,]
            else:  # if self.acce_std_x > 6.94
                if self.gyro_mean_x <= 3.95:
                    if self.acce_std_y <= 8.93:
                        return [  7, 168,  10,]
                    else:  # if self.acce_std_y > 8.93
                        return [0, 1, 5,]
                else:  # if self.gyro_mean_x > 3.95
                    if self.n_samples <= 11.5:
                        return [ 0,  0, 12,]
                    else:  # if self.n_samples > 11.5
                        return [0, 6, 2,]

    def decision_tree_5(self):
        if self.gyro_mean_y <= 0.7:
            if self.gyro_std_x <= -0.8:
                return [ 1, 78,  4,]
            else:  # if self.gyro_std_x > -0.8
                if self.n_samples <= 12.5:
                    if self.gyro_mean_y <= 0.34:
                        if self.acce_std_y <= 3.76:
                            return [ 0,  1, 31,]
                        else:  # if self.acce_std_y > 3.76
                            return [15,  3, 11,]
                    else:  # if self.gyro_mean_y > 0.34
                        if self.acce_mean_z <= -1.83:
                            return [2, 0, 9,]
                        else:  # if self.acce_mean_z > -1.83
                            return [ 0, 25,  7,]
                else:  # if self.n_samples > 12.5
                    if self.gyro_std_y <= 16.62:
                        if self.gyro_std_y <= 6.55:
                            return [0, 9, 0,]
                        else:  # if self.gyro_std_y > 6.55
                            return [272,   2,   0,]
                    else:  # if self.gyro_std_y > 16.62
                        return [ 0, 13,  0,]
        else:  # if self.gyro_mean_y > 0.7
            if self.n_samples <= 10.5:
                if self.gyro_mean_y <= 0.96:
                    return [  2,   6, 221,]
                else:  # if self.gyro_mean_y > 0.96
                    return [0, 8, 5,]
            else:  # if self.n_samples > 10.5
                return [  5, 148,  21,]

    def decision_tree_6(self):
        if self.n_samples <= 14.5:
            if self.gyro_variance_z <= 578.92:
                if self.acce_mean_x <= 15.67:
                    if self.gyro_variance_y <= 2.6:
                        if self.acce_mean_z <= -1.5:
                            return [30,  1,  0,]
                        else:  # if self.acce_mean_z > -1.5
                            if self.gyro_std_y <= 6.06:
                                return [ 0, 39, 13,]
                            else:  # if self.gyro_std_y > 6.06
                                if self.gyro_std_z <= 7.04:
                                    return [ 2, 19, 68,]
                                else:  # if self.gyro_std_z > 7.04
                                    return [0, 7, 0,]
                    else:  # if self.gyro_variance_y > 2.6
                        return [ 0, 53,  6,]
                else:  # if self.acce_mean_x > 15.67
                    if self.acce_mean_y <= 6.35:
                        return [  0,  28, 187,]
                    else:  # if self.acce_mean_y > 6.35
                        return [0, 8, 0,]
            else:  # if self.gyro_variance_z > 578.92
                return [  4, 141,  14,]
        else:  # if self.n_samples > 14.5
            if self.gyro_mean_y <= 0.69:
                if self.gyro_std_x <= -1.02:
                    return [0, 8, 0,]
                else:  # if self.gyro_std_x > -1.02
                    return [259,   0,   0,]
            else:  # if self.gyro_mean_y > 0.69
                return [ 1, 11,  0,]

    def decision_tree_7(self):
        if self.n_samples <= 14.5:
            if self.gyro_std_x <= -1.36:
                if self.gyro_variance_z <= 513.57:
                    return [0, 0, 7,]
                else:  # if self.gyro_variance_z > 513.57
                    return [  0, 136,   7,]
            else:  # if self.gyro_std_x > -1.36
                if self.n_samples <= 11.5:
                    if self.gyro_variance_y <= 0.74:
                        return [ 3, 23,  9,]
                    else:  # if self.gyro_variance_y > 0.74
                        if self.gyro_variance_y <= 2.87:
                            return [  0,  13, 246,]
                        else:  # if self.gyro_variance_y > 2.87
                            if self.acce_mean_x <= 17.56:
                                return [ 0, 17,  7,]
                            else:  # if self.acce_mean_x > 17.56
                                return [ 0,  0, 14,]
                else:  # if self.n_samples > 11.5
                    if self.acce_std_z <= 0.29:
                        return [ 1, 76,  9,]
                    else:  # if self.acce_std_z > 0.29
                        if self.acce_std_x <= 4.58:
                            return [ 0, 10,  0,]
                        else:  # if self.acce_std_x > 4.58
                            return [32,  5,  0,]
        else:  # if self.n_samples > 14.5
            if self.acce_mean_z <= -0.89:
                return [261,   1,   0,]
            else:  # if self.acce_mean_z > -0.89
                return [ 1, 21,  0,]

    def decision_tree_8(self):
        if self.acce_mean_x <= 15.63:
            if self.n_samples <= 14.5:
                if self.gyro_variance_z <= 629.65:
                    if self.gyro_variance_z <= 336.35:
                        if self.gyro_std_y <= 10.7:
                            return [ 1, 54, 15,]
                        else:  # if self.gyro_std_y > 10.7
                            return [ 0, 20, 49,]
                    else:  # if self.gyro_variance_z > 336.35
                        if self.acce_mean_z <= -1.3:
                            return [53,  3,  0,]
                        else:  # if self.acce_mean_z > -1.3
                            if self.gyro_mean_y <= 0.69:
                                return [ 0, 16,  1,]
                            else:  # if self.gyro_mean_y > 0.69
                                return [ 0,  1, 17,]
                else:  # if self.gyro_variance_z > 629.65
                    return [  1, 138,   7,]
            else:  # if self.n_samples > 14.5
                if self.acce_mean_z <= -0.9:
                    return [241,   0,   0,]
                else:  # if self.acce_mean_z > -0.9
                    return [ 2, 12,  0,]
        else:  # if self.acce_mean_x > 15.63
            if self.gyro_mean_z <= 3.55:
                return [ 0, 22,  6,]
            else:  # if self.gyro_mean_z > 3.55
                if self.n_samples <= 12.5:
                    return [  0,  10, 214,]
                else:  # if self.n_samples > 12.5
                    return [ 2, 13,  1,]

    def decision_tree_9(self):
        if self.acce_mean_z <= -1.31:
            if self.gyro_variance_z <= 499.8:
                if self.gyro_mean_x <= 3.7:
                    return [58,  2,  1,]
                else:  # if self.gyro_mean_x > 3.7
                    if self.gyro_std_z <= 0.5:
                        return [  0,  21, 178,]
                    else:  # if self.gyro_std_z > 0.5
                        return [0, 9, 4,]
            else:  # if self.gyro_variance_z > 499.8
                if self.gyro_std_y <= 3.84:
                    return [0, 4, 1,]
                else:  # if self.gyro_std_y > 3.84
                    if self.n_samples <= 13.5:
                        return [2, 4, 3,]
                    else:  # if self.n_samples > 13.5
                        return [226,   0,   0,]
        else:  # if self.acce_mean_z > -1.31
            if self.gyro_variance_z <= 577.38:
                if self.gyro_variance_y <= 2.61:
                    if self.gyro_mean_x <= 2.55:
                        return [ 0, 25,  3,]
                    else:  # if self.gyro_mean_x > 2.55
                        return [ 5, 35, 82,]
                else:  # if self.gyro_variance_y > 2.61
                    return [ 0, 57,  7,]
            else:  # if self.gyro_variance_z > 577.38
                if self.acce_std_z <= 1.73:
                    return [  7, 156,   5,]
                else:  # if self.acce_std_z > 1.73
                    return [0, 0, 4,]

