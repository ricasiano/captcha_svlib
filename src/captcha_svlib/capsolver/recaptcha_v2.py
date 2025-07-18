import capsolver
from captcha_svlib.recaptcha_v2 import RecaptchaV2 as IRecaptchaV2
from captcha_svlib.captcha_exception import CaptchaException


class RecaptchaV2(IRecaptchaV2):
    def solve(self, url: str, key: str, invisible: bool = False) -> dict:
        result = {"error": 1, "text": ""}
        try:
            capsolver.api_key = self.settings.CAPTCHA_CS_KEY
            kwargs = {
                "type": "ReCaptchaV2TaskProxyLess",
                "websiteURL": url,
                "websiteKey": key,
                "invisible": 1 if invisible else 0
            }
            solution = capsolver.solve(kwargs)
            result["error"] = 0
            result["text"] = solution.get("gRecaptchaResponse")
        except CaptchaException as ex:
            raise CaptchaException("Failed to solve Recaptcha V2 using Capsolver", ex)
        return result
