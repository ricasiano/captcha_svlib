from abc import ABC, abstractmethod
from captcha_svlib.abstract_captcha import AbstractCaptcha


class TextCaptcha(ABC, AbstractCaptcha):

    @abstractmethod
    def solve(self, image: str) -> dict:
        pass
