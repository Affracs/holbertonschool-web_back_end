#!/usr/bin/env python3
"""
Helper function for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing start and end indexes.

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): Number of items per page

    Returns:
        tuple: (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
