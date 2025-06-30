from abc import ABC, abstractmethod
from abstract_captcha import AbstractCaptcha


class RecaptchaV2(ABC, AbstractCaptcha):

    @abstractmethod
    def solve(self, url: str, key: str, invisible: bool = False) -> dict:
        pass
