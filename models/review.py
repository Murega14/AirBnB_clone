#!/usr/bin/python3
"""the class review inherits from BaseModel"""
from base_models import BaseModel

class Review(BaseModel):
    """initializes the review xlass"""
    place_id = ""
    user_id = ""
    text = ""