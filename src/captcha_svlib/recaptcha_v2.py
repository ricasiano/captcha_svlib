from abc import ABC, abstractmethod
from captcha_svlib.abstract_captcha import AbstractCaptcha


class RecaptchaV2(ABC, AbstractCaptcha):

    @abstractmethod
    def solve(self, url: str, key: str, invisible: bool = False) -> dict:
        pass
