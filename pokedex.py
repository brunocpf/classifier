#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Mini Pokédex - Identificação de Pokémon

    [Módulo]
    Leia README.rst para detalhes da implementação.
'''
import numpy as np

import cv2
from train import get_rgb_hist, train

POKEDEX_LABELS = {0: 'bulbasaur',
                  1: 'charmander',
                  2: 'eevee',
                  3: 'pikachu',
                  4: 'snorlax',
                  5: 'squirtle'}


def find_pokemon(file_path):
    '''
    encontra o pokémon mais próximo
    '''
    data = np.load("data.npy")
    if data is None:
        return
    image = cv2.imread(file_path)
    if image is None:
        return None
    hists, labels = data[0], data[1]
    model = train(hists, labels)
    hist = get_rgb_hist(image)
    retval, results, neigh_resp, dists = model.findNearest(np.array([hist]), k=6)
    print results[0]
    return POKEDEX_LABELS.get(int(results[0][0]))
