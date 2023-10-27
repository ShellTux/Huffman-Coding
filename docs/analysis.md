# Análise

## Exercício 2

![Ex2](../assets/Ex2.png)

> d. Comente a relação de MPG com as restantes variáveis.

`MPG` tem uma relação inversa com `Displacement`, `Horsepower`, `Weight`

Não existe uma relação significativa entre `MPG` e `Acceleration`

Houve um incremento no `MPG` ao longo dos anos.

Veículos com menos que 4 cilindros utilizam menos combustível por milhas

## Exercício 7

```sh
❯ ./src/ex7.py
Acceleration = 3.50 bits/symbol
Cylinders    = 1.59 bits/symbol
Displacement = 5.73 bits/symbol
Horsepower   = 5.84 bits/symbol
ModelYear    = 3.69 bits/symbol
Weight       = 8.39 bits/symbol
MPG          = 4.84 bits/symbol

bps(values) = 7.21 bits/symbol
```

> c. Comentar os resultados.


`Cylinders` é a variável com <font color="red">menor</font> __*entropia*__ e
`Weight` é a variável com <font color="red">maior</font> __*entropia*__.

Quanto maior a entropia, menor a incerteza.

Significando que, quando temos maior entropia então podemos identificar padrões repetitivos
na nossa fonte de dados e poder comprimi-los.
