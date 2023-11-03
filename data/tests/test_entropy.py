import unittest
from data import DATA

class TestEntropy(unittest.TestCase):

    def test_entropy(self):
        entropyVariables = (
                ('Acceleration', 3.4964235578605165),
                ('Weight',       6.040364750974289),
                ('MPG',          4.835799622324452),
                (None,           7.211576568035847),
                )

        for variable, expectedEntropy in entropyVariables:
            entropy = DATA.bitsPerSymbol(variable = variable)

            if variable is None:
                variable = 'All'

            self.assertEqual(
                    entropy, expectedEntropy,
                    msg = f'Entropy of {variable} doesn\'t match'
                    )

    def test_average_bits_per_symbol_huffman(self):
        expectedResults = (
                ('Acceleration', 3.535626535626536),
                ('Weight',       6.076167076167077),
                ('MPG',          4.8697788697788695),
                (None,           7.247104247104245),
                )

        for variable, expectedABPS in expectedResults:
            avgBits = DATA.averageBitsPerSymbol(variable = variable)

            if variable is None:
                variable = 'All'

            self.assertEqual(
                    avgBits, expectedABPS,
                    msg = f'Average bps of {variable} doesn\'t match'
                    )

    def test_length_variance(self):
        expectedResults = (
                ('Acceleration', 0.8138413150698163),
                ('Weight',       0.8074663897759721),
                ('MPG',          0.8847623589638332),
                (None,           4.929462481586032),
                )

        for variable, expectedLengthVariance in expectedResults:
            lengthVariance = DATA.lengthVariance(variable = variable)

            if variable is None:
                variable = 'All'

            self.assertEqual(
                    lengthVariance, expectedLengthVariance,
                    msg = f'Variance length of {variable} doesn\'t match'
                    )

    def test_correlation(self):
        expectedResults = (
                ('Acceleration', 0.41358533807577513),
                ('Weight',       -0.8312488949454783),
                )

        for variable, expectedCorrelation in expectedResults:
            pass

        # TODO: Implement unit test for correlation

    def test_mutual_information(self):
        expectedResults = (
                ('Acceleration', 0.8720358363934793),
                ('Weight',       2.614683626627084),
                )

        for variable, expectedMutualInformation in expectedResults:
            pass

if __name__ == '__main__':
    unittest.main()
