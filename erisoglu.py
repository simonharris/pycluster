import numpy as np

# Erisoglu 2011 "new" algorithm:
# See: A new algorithm for initial cluster centers in k-means algorithm
# https://www.sciencedirect.com/science/article/pii/S0167865511002248

class Erisoglu():

    # Main steps of the algorithm
    # nb. these assume the data to be an ndarray and transposed

    def find_main_axis(self, data):
        '''Step i) Find the feature with greatest variance'''

        allvcs = np.array([self.variation_coefficient(feature) for feature in data])

        return allvcs.argmax()


    def find_secondary_axis(self, data):
        '''Step ii) Find the feature with least correlation to the main axis'''

        main = data[self.find_main_axis(data)]

        min = 1
        min_column = None

        for j in range(0, len(data)):

            ccj = abs(self.correlation_coefficient(main, data[j]))

            if ccj < min:
                min = ccj
                min_column = j

        return min_column


    # Supporting calculations etc ----------------------------------------------

    def variation_coefficient(self, vector):
        '''Absolute value of std dev / mean.'''

        return abs(np.std(vector) / np.mean(vector))


    def correlation_coefficient(self, left, right): # column j, column j'
        '''Correlation coefficient between two vectors'''

        numerator = 0
        denominator_left = 0
        denominator_right = 0

        for i in range(0, len(left)):

            dev_left = (left[i] - np.mean(left))
            dev_right = (right[i] - np.mean(right))

            numerator +=  dev_left * dev_right

            denominator_left += dev_left ** 2
            denominator_right += dev_right ** 2

        # TODO: This is where Erisoglu seems to differ from Pearson
        denominator = denominator_left**0.5 * denominator_right**0.5
        #denominator = denominator_left * denominator_right

        return (numerator / denominator)


    def _prepare_data(self, data):
        '''Since we're working with columns, it's simpler if we transpose first'''

        return np.array(data).T

# ------------------------------------------------------------------------------


if __name__ == '__main__':
    pass
