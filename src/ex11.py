from data import DATA
from numpy._typing import NDArray
import numpy as np


sliceLength = 10


def main():
    variables = list(
        filter(lambda variable: variable != "MPG", DATA.getVariables())
    )
    mpg = DATA.getValues(variable="MPG")
    acceleration = DATA.getValues(variable="Acceleration")
    cylinders = DATA.getValues(variable="Cylinders")
    displacement = DATA.getValues(variable="Displacement")
    horsepower = DATA.getValues(variable="Horsepower")
    model = DATA.getValues(variable="ModelYear")
    weight = DATA.getValues(variable="Weight")
    # Define the formula for MPG estimation
    excludedVariables = (None, "Acceleration", "Weight")
    # weight = weight * 0
    # acceleration = acceleration * 0

    for excludedVariable in excludedVariables:
        accelerationFactor = 0 if "Acceleration" == excludedVariable else 1
        cylindersFactor = 0 if "Cylinders" == excludedVariable else 1
        displacementFactor = 0 if "Displacement" == excludedVariable else 1
        horsepowerFactor = 0 if "Horsepower" == excludedVariable else 1
        modelFactor = 0 if "ModelYear" == excludedVariable else 1
        weightFactor = 0 if "Weight" == excludedVariable else 1

        prediction = mpg_estimativa(
            acceleration=acceleration * accelerationFactor,
            cylinders=cylinders * cylindersFactor,
            displacement=displacement * displacementFactor,
            horsepower=horsepower * horsepowerFactor,
            model=model * modelFactor,
            weight=weight * weightFactor,
        )
        MAE = np.mean(np.abs(prediction - mpg))
        if excludedVariable is None:
            print(f"Mean average error with all variables")
        else:
            print(f"Mean average error without {excludedVariable}")
        print(f"MAE = {MAE}")
        print()
    influentialVariableMax = max(
        variables,
        key=lambda variable: DATA.mutualInformation(
            variableX=variable,
            variableY="MPG",
        ),
    )
    print(f"Max influency = {influentialVariableMax}")

    influentialVariableMin = min(
        variables,
        key=lambda variable: DATA.mutualInformation(
            variableX=variable,
            variableY="MPG",
        ),
    )
    print(f"Min influency = {influentialVariableMin}")


def mpg_estimativa(
    *,
    acceleration: NDArray,
    cylinders: NDArray,
    displacement: NDArray,
    horsepower: NDArray,
    model: NDArray,
    weight: NDArray,
):
    return (
        -5.5241
        - 0.146 * acceleration
        - 0.4909 * cylinders
        + 0.0026 * displacement
        - 0.0045 * horsepower
        + 0.6725 * model
        - 0.0059 * weight
    )


if __name__ == "__main__":
    main()
