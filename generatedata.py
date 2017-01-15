#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Mini Pokédex - Geração de dados a serem usados pela ferramenta

    Leia README.rst para instruções de execução e detalhes da implementação.

Uso:
    generatedata.py
'''
import os

import numpy as np
from train import get_data

DATASET_PATH = "images"    # Caminho do diretório do dataset.


def main():
    '''
        main
    '''
    print __doc__.decode("utf-8")
    print u"----------------\n"
    print u"carregando dataset %s (isso pode demorar um pouco)..." % os.path.abspath(DATASET_PATH)
    hists, labels = get_data(DATASET_PATH)
    hists = np.array(hists)
    labels = np.array(labels)
    rand = np.random.RandomState(321)
    shuffle = rand.permutation(len(labels))
    hists, labels = hists[shuffle], labels[shuffle]
    hists = np.array(hists)
    labels = np.array(labels)
    print u"salvando histogramas e labels..."
    data = np.array([None,None])
    data[0] = hists
    data[1] = labels
    np.save("data", data)
    print u"dados salvos em data.npy"


if __name__ == '__main__':
    main()
