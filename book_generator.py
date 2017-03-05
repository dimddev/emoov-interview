#!/usr/bin/env python3

""" A generator for random books"""
from src.book import BooksGenerator

if __name__ == '__main__':
    BOOKS = BooksGenerator(10000, (550, 670)).process()

