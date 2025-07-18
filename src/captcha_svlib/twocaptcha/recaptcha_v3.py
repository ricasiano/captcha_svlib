from twocaptcha import TwoCaptcha
from captcha_svlib.recaptcha_v3 import RecaptchaV3 as IRecaptchaV3
from captcha_svlib.captcha_exception import CaptchaException


class RecaptchaV3(IRecaptchaV3):
    enterprise: bool = False

    def solve(self,
              url: str,
              key: str,
              score: float = 0.4,
              action: str = "verify",
              enterprise: bool = False) -> dict:
        result = {"error": 1, "text": ""}
        try:
            solver = TwoCaptcha(self.settings.CAPTCHA_2C_KEY)
            solution = solver.recaptcha(
                sitekey=key,
                url=url,
                version='v3',
                enterprise=1 if enterprise else 0,
                action=action,
                score=score
            )
            result["error"] = 0
            result["text"] = solution.get("code")
        except Exception as ex:
            raise CaptchaException("Failed to solve Recaptcha V3 using TwoCaptcha", ex)
        return result
