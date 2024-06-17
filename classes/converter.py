from abc import ABC, abstractmethod

class Converter (ABC):
    def __init__(self, img_type):
        self.img_type=img_type