#!/usr/bin/env python3
""" Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs"""
    id_obj = mongo_collection.insert_one(kwargs)

    return id_obj.inserted_id
