from abc import ABC, abstractmethod
from abstract_captcha import AbstractCaptcha


class TextCaptcha(ABC, AbstractCaptcha):

    @abstractmethod
    def solve(self, image: str) -> dict:
        pass
