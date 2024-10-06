class Statistics:

    def __init__(self):
        pass

    # Calculate the mean
    def mean(self, data):
        return sum(data) / len(data)

    # Calculate the standard deviation
    def std(self, data):
        mean_value = self.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return variance ** 0.5

    # Calculate the variance
    def variance(self, data):
        mean_value = self.mean(data)
        return sum((x - mean_value) ** 2 for x in data) / len(data)

    # Calculate the skewness
    def skew(self, data):
        mean_value = self.mean(data)
        std_dev = self.std(data)
        if std_dev == 0:
            return 0  # Return 0 when standard deviation is zero
        n = len(data)
        skewness = sum((x - mean_value) ** 3 for x in data) / n
        skewness /= std_dev ** 3
        return skewness

    # Calculate the kurtosis
    def kurt(self, data):
        mean_value = self.mean(data)
        std_dev = self.std(data)
        if std_dev == 0:
            return 0  # Return 0 when standard deviation is zero
        n = len(data)
        kurtosis = sum((x - mean_value) ** 4 for x in data) / n
        kurtosis /= std_dev ** 4
        return kurtosis

    # Calculate the maximum
    def max(self, data):
        return max(data)

    # Calculate the minimum
    def min(self, data):
        return min(data)

    # Calculate the range
    def range(self, data):
        return self.max(data) - self.min(data)

    # Calculate the root mean square (RMS)
    def rms(self, data):
        n = len(data)
        return (sum(x ** 2 for x in data) / n) ** 0.5

    # Calculate the energy
    def energy(self, data):
        return sum(x ** 2 for x in data)

    # Calculate the correlation between two data sets
    def corr(self, data1, data2):
        if len(data1) != len(data2):
            raise ValueError("Data sets must have the same number of elements")

        mean1 = self.mean(data1)
        mean2 = self.mean(data2)
        std1 = self.std(data1)
        std2 = self.std(data2)
        if std1 == 0 or std2 == 0:
            return 0  # Return 0 when either standard deviation is zero

        covariance = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2)) / len(data1)
        correlation_coefficient = covariance / (std1 * std2)
        return correlation_coefficient