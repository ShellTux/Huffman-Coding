import unittest
from data import DATA
# import os

# root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# file_path = os.path.join(root, 'assets', 'CarDataset.xlsx')
# DATA = Data(file_path)

class TestEntropy(unittest.TestCase):

    def test_entropy(self):
        entropyVariables = (
                ('Acceleration', 3.4964235578605165),
                # ('Weight', 6.040364750974289),
                ('MPG', 4.835799622324452),
                )

        for variable, expectedEntropy in entropyVariables:
            entropy = DATA.bitsPerSymbol(variable = variable)
            self.assertEqual(
                    entropy, expectedEntropy,
                    msg = f'Entropy of {variable} doesn\'t match'
                    )

        # For all values
        entropy = DATA.bitsPerSymbol()
        self.assertEqual(entropy, 7.211576568035847)

if __name__ == '__main__':
    unittest.main()
