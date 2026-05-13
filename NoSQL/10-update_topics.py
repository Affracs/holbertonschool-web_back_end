#!/usr/bin/env python3
""" Change all topics of a school document """

def update_topics(mongo_collection, name, topics):
    """Updates the topics of all school documents matching name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )