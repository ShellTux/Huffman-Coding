from data import DATA
from numpy._typing import NDArray

sliceLength = 10

def main():
    mpg = DATA.getValues(variable='MPG')
    acceleration = DATA.getValues(variable='Acceleration')
    cylinders = DATA.getValues(variable='Cylinders')
    displacement = DATA.getValues(variable='Displacement')
    horsepower = DATA.getValues(variable='Horsepower')
    model = DATA.getValues(variable='ModelYear')
    weight = DATA.getValues(variable='Weight')
    # Define the formula for MPG estimation
    estimativa = mpg_estimativa(
        acceleration=acceleration,
        cylinders=cylinders,
        displacement=displacement,
        horsepower=horsepower,
        model=model,
        weight=weight
    )
    print('Com todas as variaveis')
    print(mpg[:sliceLength])
    print(estimativa[:sliceLength])
    print()

    estimativa = mpg_estimativa(
        acceleration=acceleration * 0,
        cylinders=cylinders,
        displacement=displacement,
        horsepower=horsepower,
        model=model,
        weight=weight
    )
    print('Sem a variavel Acceleration')
    print(mpg[:sliceLength])
    print(estimativa[:sliceLength])
    print()

    estimativa = mpg_estimativa(
        acceleration=acceleration,
        cylinders=cylinders,
        displacement=displacement,
        horsepower=horsepower,
        model=model,
        weight=weight * 0
    )
    print('Sem a variavel Weight')
    print(mpg[:sliceLength])
    print(estimativa[:sliceLength])
    print()

    variables = list(filter(
        lambda variable: variable != 'MPG',
        DATA.getVariables()
        ))

    influentialVariableMax = max(
            variables,
            key = lambda variable: DATA.mutualInformation(
                variableX = variable,
                variableY = 'MPG',
                )
            )
    print(f'Max influency = {influentialVariableMax}')

    influentialVariableMin = min(
            variables,
            key = lambda variable: DATA.mutualInformation(
                variableX = variable,
                variableY = 'MPG',
                )
            )
    print(f'Min influency = {influentialVariableMin}')


def mpg_estimativa(
        *,
        acceleration: NDArray,
        cylinders: NDArray,
        displacement: NDArray,
        horsepower: NDArray,
        model: NDArray,
        weight: NDArray,
        ):
    return -5.5241 - 0.146 * acceleration - 0.4909 * cylinders + 0.0026 * displacement - 0.0045 * horsepower + 0.6725 * model - 0.0059 * weight


if __name__ == '__main__':
    main()
