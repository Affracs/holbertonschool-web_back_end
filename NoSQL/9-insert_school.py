#!/usr/bin/env python3
""" Insert a new document in a collection """

def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in the collection and returns its _id"""
    return mongo_collection.insert_one(kwargs).inserted_id
