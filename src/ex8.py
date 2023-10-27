#!/usr/bin/env python3

from data import DATA
import huffmancodec.huffmancodec as huffc
import numpy as np


if __name__ == "__main__":
    variable = 'Weight'
    S = DATA.getValues(variable = variable)
    codec = huffc.HuffmanCodec.from_data(S)
    symbols, lengths = codec.get_code_len()

    print('-' * 20)
    print(f'Variable: {variable}')
    print('Codec:', codec, sep = '\n', end = '\n' * 2)
    print('Symbols:', symbols, sep = '\n', end = '\n' * 2)
    print('Lengths:', lengths, sep = '\n', end = '\n' * 2)
    print('-' * 20, end = '\n' * 2)

    avgBits = np.mean(lengths)
    lengthVariance = np.var(lengths)

    print('-' * 20)
    print(f'Variable: {variable}')
    print(f'{f"Average bits per symbol:":<24} {avgBits:.3f}')
    print(f'{"Variance of lengths:":<24} {lengthVariance:.3f}')
    print('-' * 20)
