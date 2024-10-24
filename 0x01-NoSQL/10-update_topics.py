#!/usr/bin/env python3
""" Use of module for using PyMongo """


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school
    document based on name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
