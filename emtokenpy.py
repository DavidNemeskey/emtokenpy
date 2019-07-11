#!/usr/bin/python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

"""Python wrapper for quntoken.
"""

from io import StringIO
import os.path as op
import sys

## Load the interface class from the downloaded quntoken directory
from .quntoken.quntoken import QunToken


class EmTokenPy:
    pass_header = True

    def __init__(self, source_fields=None, target_fields=None):

        # Field names for e-magyar TSV
        if source_fields is None:
            source_fields = set()

        if target_fields is None:
            target_fields = []

        self.source_fields = source_fields
        self.target_fields = target_fields
        self.qt = QunToken('vert', 'token', False)

    def process_sentence(self, sentences, _=None):
        for sen in sentences:
            for token in StringIO(self.qt.tokenize(sen)):
                yield token

    @staticmethod
    def prepare_fields(field_names):
        return field_names
