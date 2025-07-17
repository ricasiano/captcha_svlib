from twocaptcha import TwoCaptcha
from captcha_svlib.recaptcha_v2 import RecaptchaV2 as IRecaptchaV2
from captcha_svlib.captcha_exception import CaptchaException


class RecaptchaV2(IRecaptchaV2):
    def solve(self, url: str, key: str, invisible: bool = False) -> dict:
        result = {"error": 1, "text": ""}
        try:
            solver = TwoCaptcha(self.settings.CAPTCHA_2C_KEY)
            solution = solver.recaptcha(
                sitekey=key,
                url=url,
                invisible=1 if invisible else 0
            )
            result["error"] = 0
            result["text"] = solution.get("code")
        except CaptchaException as ex:
            raise CaptchaException("Failed to solve Recaptcha V2 using TwoCaptcha", ex)
        return result
