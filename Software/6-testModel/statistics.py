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
