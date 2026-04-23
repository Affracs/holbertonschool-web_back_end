#!/usr/bin/python3
"""
helper function for pagination
"""

def index_range(page: int, page_size: int) -> tuple:
    """

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): Number of items per page

    Returns:
        tuple: (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
