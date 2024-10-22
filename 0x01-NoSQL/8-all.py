#!/usr/bin/env python3
""" Function that lists all documents in a collection """


def list_all(mongo_collection):
    """ Return an empty list if no document in the collection
    """
    cursor = mongo_collection.find()

    return [doc for doc in cursor]
