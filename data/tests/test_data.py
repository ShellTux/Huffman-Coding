from data import DATA
from src.ex11 import mpg_estimativa
import numpy as np
import unittest


class TestEntropy(unittest.TestCase):
    def test_entropy(self):
        entropyVariables = (
            ("Acceleration", 3.4964235578605165),
            ("MPG", 4.835799622324452),
            (None, 7.211576568035847),
        )

        for variable, expectedEntropy in entropyVariables:
            entropy = DATA.bitsPerSymbol(variable=variable)

            if variable is None:
                variable = "All"

            self.assertEqual(
                entropy,
                expectedEntropy,
                msg=f"Entropy of {variable} doesn't match",
            )

    def test_average_bits_per_symbol_huffman(self):
        expectedResults = (
            ("Acceleration", 3.535626535626536),
            ("MPG", 4.8697788697788695),
            (None, 7.247104247104245),
        )

        for variable, expectedABPS in expectedResults:
            avgBits = DATA.averageBitsPerSymbol(variable=variable)

            if variable is None:
                variable = "All"

            self.assertEqual(
                avgBits,
                expectedABPS,
                msg=f"Average bps of {variable} doesn't match",
            )

    def test_length_variance(self):
        expectedResults = (
            ("Acceleration", 0.8138413150698163),
            ("Weight", 0.8074663897759721),
            ("MPG", 0.8847623589638332),
            (None, 4.929462481586032),
        )

        for variable, expectedLengthVariance in expectedResults:
            lengthVariance = DATA.lengthVariance(variable=variable)

            if variable is None:
                variable = "All"

            self.assertEqual(
                lengthVariance,
                expectedLengthVariance,
                msg=f"Variance length of {variable} doesn't match",
            )

    def test_correlation(self):
        expectedResults = (
            (("Acceleration", "MPG"), 0.41358533807577513),
            (("Weight", "MPG"), -0.8312488949454783),
        )

        for (variableX, variableY), expectedCorrelation in expectedResults:
            correlation = DATA.pearsonCoeficient(
                variableX=variableX, variableY=variableY
            )

            if variableX is None:
                variableX = "All"

            if variableY is None:
                variableY = "All"

            self.assertEqual(
                correlation,
                expectedCorrelation,
                msg=f'Not expected correlation between "{variableX}" and'
                + f'"{variableY}"',
            )

    def test_mutual_information(self):
        expectedResults = (
            (("Acceleration", "MPG"), 0.8720358363934793),
            (("Weight", "MPG"), 2.614683626627084),
        )

        for (
            variableX,
            variableY,
        ), expectedMutualInformation in expectedResults:
            mutualInformation = DATA.mutualInformation(
                variableX=variableX,
                variableY=variableY,
            )

            self.assertEqual(
                mutualInformation,
                expectedMutualInformation,
                msg=f"Not expected mutual information between "
                + f'"{variableX}" and"{variableY}"',
            )

    def test_mpg_prediction_without_variable(self):
        expectedResults = (
            (
                (None,),
                np.array(
                    [
                        15.4061,
                        14.2505,
                        16.0505,
                        15.8629,
                        15.8474,
                        10.8706,
                        10.9826,
                        11.1516,
                        10.2444,
                        13.7537,
                    ]
                ),
            ),
            (
                ("Acceleration",),
                np.array(
                    [
                        17.1581,
                        16.0025,
                        17.6565,
                        17.6149,
                        17.4534,
                        12.3306,
                        12.2966,
                        12.4656,
                        11.7044,
                        15.0677,
                    ]
                ),
            ),
            (
                ("Weight",),
                np.array(
                    [
                        36.0797,
                        36.0392,
                        36.1695,
                        35.9819,
                        36.1729,
                        36.3881,
                        36.5001,
                        36.4862,
                        36.3342,
                        36.4687,
                    ]
                ),
            ),
        )

        acceleration = DATA.getValues(variable="Acceleration")
        cylinders = DATA.getValues(variable="Cylinders")
        displacement = DATA.getValues(variable="Displacement")
        horsepower = DATA.getValues(variable="Horsepower")
        model = DATA.getValues(variable="ModelYear")
        weight = DATA.getValues(variable="Weight")

        for excludedVariables, expectedPrediction in expectedResults:
            accelerationFactor = 0 if "Acceleration" in excludedVariables else 1
            cylindersFactor = 0 if "Cylinders" in excludedVariables else 1
            displacementFactor = 0 if "Displacement" in excludedVariables else 1
            horsepowerFactor = 0 if "Horsepower" in excludedVariables else 1
            modelFactor = 0 if "ModelYear" in excludedVariables else 1
            weightFactor = 0 if "Weight" in excludedVariables else 1

            prediction = mpg_estimativa(
                acceleration=acceleration * accelerationFactor,
                cylinders=cylinders * cylindersFactor,
                displacement=displacement * displacementFactor,
                horsepower=horsepower * horsepowerFactor,
                model=model * modelFactor,
                weight=weight * weightFactor,
            )
            prediction = prediction[: expectedPrediction.size]

            self.assertTrue(
                all(prediction == expectedPrediction),
                msg=f"Not expected results for variables {excludedVariables}\n"
                + f"{prediction} != {expectedPrediction}",
            )


if __name__ == "__main__":
    unittest.main()
