#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Mini Pokédex - Extração de características e treinamento

    [Módulo]
    Leia README.rst para detalhes da implementação.
'''
import os

import cv2


def get_rgb_hist(image, bins=(8, 8, 8)):
    '''
        retorna o histograma 3D normalizado da imagem
    '''
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()


def load_imgs_from_dir(path):
    '''
        carrega as imagens do diretório path
    '''
    images = []
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path, filename))
        if img is not None:
            images.append(img)
    return images


def get_data(datasetpath):
    '''
        retorna os histogramas e os labels de todas as imagens
    '''
    hists = []
    labels = []
    for idx, directory in enumerate(os.listdir(datasetpath)):
        if not os.path.isfile(os.path.join(datasetpath, directory)):
            imgs = load_imgs_from_dir(os.path.join(datasetpath, directory))
            for image in imgs:
                hists = hists + [get_rgb_hist(image)]
                labels = labels + [idx]
            print idx, directory
    return hists, labels

def train(hists, labels):
    '''
    treinamento kNN, retorna o model
    '''
    model = cv2.ml.KNearest_create()
    model.train(hists, cv2.ml.ROW_SAMPLE, labels)
    return model
