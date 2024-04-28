class RandomForest:

    def __init__(self):
        pass
    
    def score(self, n_samples, gyro_mean_x, gyro_mean_y, gyro_mean_z, acce_mean_x, acce_mean_y, acce_mean_z, gyro_std_x, gyro_std_y, gyro_std_z, acce_std_x, acce_std_y, acce_std_z, gyro_variance_x, gyro_variance_y, gyro_variance_z, acce_variance_x, acce_variance_y, acce_variance_z):
        self.n_samples = n_samples
        self.gyro_mean_x = gyro_mean_x
        self.gyro_mean_y = gyro_mean_y
        self.gyro_mean_z = gyro_mean_z
        self.acce_mean_x = acce_mean_x
        self.acce_mean_y = acce_mean_y
        self.acce_mean_z = acce_mean_z
        self.gyro_std_x = gyro_std_x
        self.gyro_std_y = gyro_std_y
        self.gyro_std_z = gyro_std_z
        self.acce_std_x = acce_std_x
        self.acce_std_y = acce_std_y
        self.acce_std_z = acce_std_z
        self.gyro_variance_x = gyro_variance_x
        self.gyro_variance_y = gyro_variance_y
        self.gyro_variance_z = gyro_variance_z
        self.acce_variance_x = acce_variance_x
        self.acce_variance_y = acce_variance_y
        self.acce_variance_z = acce_variance_z

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

        return trees_values
        # return [sum(col) / len(col) for col in zip(*trees_values)]
        

    def decision_tree_0(self):
        if self.gyro_variance_y <= 15.46:
            if self.gyro_std_x <= 4.16:
                if self.gyro_variance_y <= 10.82:
                    return [  5, 103,  12,]
                else:  # if self.gyro_variance_y > 10.82
                    if self.gyro_variance_x <= 7.5:
                        return [ 1, 17,  4,]
                    else:  # if self.gyro_variance_x > 7.5
                        if self.gyro_mean_y <= 2.89:
                            return [ 0, 10,  4,]
                        else:  # if self.gyro_mean_y > 2.89
                            if self.gyro_mean_y <= 6.37:
                                return [214,   1,   0,]
                            else:  # if self.gyro_mean_y > 6.37
                                return [0, 8, 6,]
            else:  # if self.gyro_std_x > 4.16
                return [ 0, 73, 39,]
        else:  # if self.gyro_variance_y > 15.46
            if self.acce_std_z <= 0.05:
                return [ 0, 14,  3,]
            else:  # if self.acce_std_z > 0.05
                if self.acce_mean_x <= 2.65:
                    if self.acce_mean_x <= 0.56:
                        return [ 0, 11,  3,]
                    else:  # if self.acce_mean_x > 0.56
                        return [  0,   5, 169,]
                else:  # if self.acce_mean_x > 2.65
                    return [ 0, 16,  2,]

    def decision_tree_1(self):
        if self.acce_mean_x <= 0.82:
            if self.gyro_std_z <= 2.77:
                if self.acce_variance_y <= 2.41:
                    return [3, 6, 9,]
                else:  # if self.acce_variance_y > 2.41
                    return [ 0, 48,  1,]
            else:  # if self.gyro_std_z > 2.77
                if self.gyro_mean_z <= 2.86:
                    return [ 2, 24,  1,]
                else:  # if self.gyro_mean_z > 2.86
                    if self.acce_std_z <= 0.19:
                        return [ 0,  4, 14,]
                    else:  # if self.acce_std_z > 0.19
                        return [154,   3,   2,]
        else:  # if self.acce_mean_x > 0.82
            if self.gyro_variance_x <= 10.21:
                return [ 0, 51,  6,]
            else:  # if self.gyro_variance_x > 10.21
                if self.n_samples <= 11.5:
                    return [  0,  21, 221,]
                else:  # if self.n_samples > 11.5
                    if self.gyro_variance_x <= 16.32:
                        if self.gyro_std_z <= 2.54:
                            return [ 0, 15,  0,]
                        else:  # if self.gyro_std_z > 2.54
                            return [63,  7,  2,]
                    else:  # if self.gyro_variance_x > 16.32
                        return [ 5, 55,  3,]

    def decision_tree_2(self):
        if self.gyro_mean_y <= 6.44:
            if self.gyro_mean_z <= 6.37:
                if self.gyro_mean_y <= 3.63:
                    if self.gyro_mean_z <= 4.72:
                        if self.n_samples <= 16.5:
                            return [ 1, 52, 16,]
                        else:  # if self.n_samples > 16.5
                            return [12,  0,  0,]
                    else:  # if self.gyro_mean_z > 4.72
                        return [ 2,  1, 27,]
                else:  # if self.gyro_mean_y > 3.63
                    if self.gyro_std_z <= 3.97:
                        return [204,   3,   1,]
                    else:  # if self.gyro_std_z > 3.97
                        return [ 0,  3, 20,]
            else:  # if self.gyro_mean_z > 6.37
                if self.gyro_variance_z <= 6.46:
                    if self.gyro_std_z <= 0.37:
                        return [ 0,  6, 57,]
                    else:  # if self.gyro_std_z > 0.37
                        return [ 0, 55,  2,]
                else:  # if self.gyro_variance_z > 6.46
                    if self.acce_std_z <= 0.05:
                        return [0, 5, 0,]
                    else:  # if self.acce_std_z > 0.05
                        return [  3,   6, 101,]
        else:  # if self.gyro_mean_y > 6.44
            return [  0, 132,  11,]

    def decision_tree_3(self):
        if self.gyro_std_x <= 4.02:
            if self.gyro_std_z <= 2.57:
                return [ 1, 87, 18,]
            else:  # if self.gyro_std_z > 2.57
                if self.gyro_mean_y <= 6.51:
                    if self.gyro_mean_z <= 6.6:
                        if self.gyro_mean_x <= 2.91:
                            return [ 9, 18,  6,]
                        else:  # if self.gyro_mean_x > 2.91
                            if self.n_samples <= 10.5:
                                return [0, 1, 6,]
                            else:  # if self.n_samples > 10.5
                                return [235,   0,   0,]
                    else:  # if self.gyro_mean_z > 6.6
                        return [ 1,  4, 23,]
                else:  # if self.gyro_mean_y > 6.51
                    return [ 0, 44,  1,]
        else:  # if self.gyro_std_x > 4.02
            if self.acce_mean_x <= 0.65:
                return [ 5, 42, 10,]
            else:  # if self.acce_mean_x > 0.65
                if self.n_samples <= 11.5:
                    if self.gyro_std_y <= 3.37:
                        return [ 0, 14, 12,]
                    else:  # if self.gyro_std_y > 3.37
                        return [  0,   5, 121,]
                else:  # if self.n_samples > 11.5
                    return [ 4, 50,  3,]

    def decision_tree_4(self):
        if self.n_samples <= 14.5:
            if self.gyro_variance_y <= 15.68:
                if self.gyro_variance_z <= 14.8:
                    if self.n_samples <= 9.5:
                        return [ 0,  2, 24,]
                    else:  # if self.n_samples > 9.5
                        if self.acce_variance_z <= 0.12:
                            return [  5, 159,   6,]
                        else:  # if self.acce_variance_z > 0.12
                            if self.gyro_variance_x <= 15.89:
                                return [26,  1,  0,]
                            else:  # if self.gyro_variance_x > 15.89
                                return [ 0, 12,  4,]
                else:  # if self.gyro_variance_z > 14.8
                    if self.n_samples <= 12.5:
                        return [ 0, 12, 39,]
                    else:  # if self.n_samples > 12.5
                        return [ 0, 14,  3,]
            else:  # if self.gyro_variance_y > 15.68
                if self.n_samples <= 11.5:
                    return [  0,  10, 168,]
                else:  # if self.n_samples > 11.5
                    return [ 0, 24,  5,]
        else:  # if self.n_samples > 14.5
            if self.gyro_std_z <= 2.41:
                return [0, 4, 0,]
            else:  # if self.gyro_std_z > 2.41
                return [199,   3,   0,]

    def decision_tree_5(self):
        if self.gyro_std_y <= 3.91:
            if self.gyro_mean_x <= 2.21:
                return [ 0, 61,  2,]
            else:  # if self.gyro_mean_x > 2.21
                if self.gyro_std_z <= 2.72:
                    return [ 2, 79, 14,]
                else:  # if self.gyro_std_z > 2.72
                    if self.gyro_variance_x <= 16.22:
                        if self.gyro_std_z <= 3.96:
                            return [225,   6,   3,]
                        else:  # if self.gyro_std_z > 3.96
                            return [ 1,  1, 11,]
                    else:  # if self.gyro_variance_x > 16.22
                        if self.n_samples <= 17.0:
                            if self.n_samples <= 12.5:
                                return [ 0, 11, 33,]
                            else:  # if self.n_samples > 12.5
                                return [ 0, 27,  2,]
                        else:  # if self.n_samples > 17.0
                            return [14,  0,  0,]
        else:  # if self.gyro_std_y > 3.91
            if self.acce_variance_x <= 0.02:
                return [ 3, 15,  0,]
            else:  # if self.acce_variance_x > 0.02
                if self.n_samples <= 11.5:
                    return [  0,   9, 178,]
                else:  # if self.n_samples > 11.5
                    return [ 2, 18,  3,]

    def decision_tree_6(self):
        if self.acce_mean_z <= 0.96:
            if self.gyro_std_y <= 3.23:
                return [ 2, 38, 11,]
            else:  # if self.gyro_std_y > 3.23
                if self.acce_mean_z <= 0.56:
                    return [ 2,  8, 14,]
                else:  # if self.acce_mean_z > 0.56
                    return [198,  11,   9,]
        else:  # if self.acce_mean_z > 0.96
            if self.acce_std_x <= 1.85:
                if self.gyro_std_y <= 3.89:
                    if self.gyro_mean_y <= 6.61:
                        if self.gyro_mean_y <= 3.15:
                            return [ 0, 40, 17,]
                        else:  # if self.gyro_mean_y > 3.15
                            if self.gyro_mean_x <= 3.42:
                                return [0, 5, 0,]
                            else:  # if self.gyro_mean_x > 3.42
                                return [41,  1,  0,]
                    else:  # if self.gyro_mean_y > 6.61
                        return [ 0, 72, 23,]
                else:  # if self.gyro_std_y > 3.89
                    if self.acce_std_x <= 0.12:
                        return [0, 8, 0,]
                    else:  # if self.acce_std_x > 0.12
                        return [  0,  23, 149,]
            else:  # if self.acce_std_x > 1.85
                return [ 0, 45,  3,]

    def decision_tree_7(self):
        if self.gyro_std_y <= 3.95:
            if self.gyro_std_z <= 2.57:
                return [  1, 103,  18,]
            else:  # if self.gyro_std_z > 2.57
                if self.acce_mean_z <= 0.96:
                    if self.acce_std_z <= 0.1:
                        return [ 0, 10,  0,]
                    else:  # if self.acce_std_z > 0.1
                        if self.n_samples <= 12.5:
                            return [ 6, 19, 14,]
                        else:  # if self.n_samples > 12.5
                            return [177,   2,   0,]
                else:  # if self.acce_mean_z > 0.96
                    if self.acce_variance_x <= 0.02:
                        if self.acce_variance_x <= 0.0:
                            return [0, 9, 0,]
                        else:  # if self.acce_variance_x > 0.0
                            return [25,  1,  1,]
                    else:  # if self.acce_variance_x > 0.02
                        if self.n_samples <= 9.5:
                            return [ 0,  1, 21,]
                        else:  # if self.n_samples > 9.5
                            return [ 7, 68, 15,]
        else:  # if self.gyro_std_y > 3.95
            if self.n_samples <= 11.5:
                return [  2,   8, 175,]
            else:  # if self.n_samples > 11.5
                return [ 2, 27,  8,]

    def decision_tree_8(self):
        if self.gyro_variance_y <= 15.32:
            if self.gyro_variance_z <= 7.03:
                return [  1, 114,  14,]
            else:  # if self.gyro_variance_z > 7.03
                if self.gyro_std_x <= 4.16:
                    if self.gyro_mean_y <= 6.64:
                        if self.gyro_std_z <= 3.95:
                            if self.gyro_mean_x <= 2.49:
                                return [3, 4, 3,]
                            else:  # if self.gyro_mean_x > 2.49
                                if self.gyro_mean_x <= 6.7:
                                    return [231,   0,   1,]
                                else:  # if self.gyro_mean_x > 6.7
                                    return [3, 4, 1,]
                        else:  # if self.gyro_std_z > 3.95
                            return [ 1,  9, 10,]
                    else:  # if self.gyro_mean_y > 6.64
                        return [ 0, 50,  3,]
                else:  # if self.gyro_std_x > 4.16
                    if self.acce_mean_y <= 2.0:
                        return [ 0, 15,  3,]
                    else:  # if self.acce_mean_y > 2.0
                        if self.acce_variance_y <= 1.37:
                            return [0, 5, 0,]
                        else:  # if self.acce_variance_y > 1.37
                            return [ 0, 12, 31,]
        else:  # if self.gyro_variance_y > 15.32
            return [  1,  25, 176,]

    def decision_tree_9(self):
        if self.gyro_std_x <= 4.03:
            if self.acce_std_z <= 0.19:
                if self.gyro_std_x <= 3.65:
                    return [ 5, 79,  2,]
                else:  # if self.gyro_std_x > 3.65
                    if self.n_samples <= 10.5:
                        return [ 0,  1, 20,]
                    else:  # if self.n_samples > 10.5
                        return [ 8, 14,  3,]
            else:  # if self.acce_std_z > 0.19
                if self.gyro_mean_x <= 3.04:
                    return [ 9, 33, 12,]
                else:  # if self.gyro_mean_x > 3.04
                    if self.gyro_std_y <= 3.88:
                        if self.gyro_mean_x <= 6.25:
                            return [210,   0,   0,]
                        else:  # if self.gyro_mean_x > 6.25
                            return [ 4, 14,  7,]
                    else:  # if self.gyro_std_y > 3.88
                        return [ 1,  3, 11,]
        else:  # if self.gyro_std_x > 4.03
            if self.gyro_variance_y <= 11.28:
                if self.n_samples <= 10.5:
                    return [ 0, 14, 16,]
                else:  # if self.n_samples > 10.5
                    return [ 0, 43,  1,]
            else:  # if self.gyro_variance_y > 11.28
                return [  8,  36, 166,]

