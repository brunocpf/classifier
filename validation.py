#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Mini Pokédex - Validação

    Leia README.rst para instruções de execução e detalhes da implementação.

Uso:
    validation.py
'''
import os
import sys

import numpy as np

from train import get_data, train

DATASET_PATH = "images"    # caminho do diretório do dataset
N_FOLDS = 5           # número de folds (>1)


def evaluate_model(model, test_hists, test_labels):
    '''
        calcula a matriz de confusão, acurácia e o desvio padrão
    '''
    retval, results, neigh_resp, dists = model.findNearest(test_hists, k=6)
    resp = results.ravel()
    categories = [directory for directory in os.listdir(
        DATASET_PATH) if not os.path.isfile(os.path.join(DATASET_PATH, directory))]
    confusion_matrix = np.zeros((len(categories), len(categories)), np.int32)
    for i, j in zip(test_labels, resp):
        confusion_matrix[int(i), int(j)] += 1.0
    accuracy = (test_labels == resp).mean()
    stdev = (test_labels == resp).std()
    return confusion_matrix, accuracy, stdev


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
    print u"confirmando tamanho do dataset: %d" % len(labels)
    if len(labels) % N_FOLDS != 0:
        sys.exit("erro: dataset indivisível por %d" % N_FOLDS)
    hists_folds = np.split(hists, N_FOLDS)
    labels_folds = np.split(labels, N_FOLDS)
    print u"treinando kNN...\n"
    for fold in range(N_FOLDS):
        print u"..fold %d.." % (fold + 1)
        test_sample_hists = hists_folds[fold]
        test_sample_labels = labels_folds[fold]
        train_sample_hists = np.concatenate(
            tuple(hists_folds[:fold] + hists_folds[fold + 1:]))
        train_sample_labels = np.concatenate(
            tuple(labels_folds[:fold] + labels_folds[fold + 1:]))
        model = train(train_sample_hists, train_sample_labels)
        confusion_matrix, accuracy, stdev = evaluate_model(model,
                                                           test_sample_hists,
                                                           test_sample_labels)
        print u"matriz de confusão:"
        print confusion_matrix
        print u"acurácia média: %.2f %%, desvio padrão: %f\n" % (accuracy * 100, stdev)


if __name__ == '__main__':
    main()
