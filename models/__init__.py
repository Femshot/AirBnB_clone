#!/usr/bin/python3
"""Contains storage variable that holds instance of FileStorage class"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
