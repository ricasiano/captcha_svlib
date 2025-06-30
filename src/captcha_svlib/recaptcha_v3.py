from abc import ABC, abstractmethod
from abstract_captcha import AbstractCaptcha


class RecaptchaV3(ABC, AbstractCaptcha):

    @abstractmethod
    def solve(self,
              url: str,
              key: str,
              score: float = 0.4,
              action: str = "home_page",
              enterprise: bool = False
              ) -> dict:
        pass
