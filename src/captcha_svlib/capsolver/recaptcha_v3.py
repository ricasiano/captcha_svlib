import capsolver
from captcha_svlib.recaptcha_v3 import RecaptchaV3 as IRecaptchaV3
from captcha_svlib.captcha_exception import CaptchaException


class RecaptchaV3(IRecaptchaV3):
    def solve(self,
              url: str,
              key: str,
              score: float = 0.4,
              action: str = "home_page",
              enterprise: bool = False) -> dict:
        result = {"error": 1, "text": ""}
        try:
            capsolver.api_key = self.settings.CAPTCHA_CS_KEY
            kwargs = {
                "type": "ReCaptchaV3TaskProxyLess" if enterprise else "ReCaptchaV3EnterpriseTaskProxyLess",
                "websiteURL": url,
                "websiteKey": key,
            }
            if action:
                kwargs["action"] = action
            solution = capsolver.solve(kwargs)
            result["error"] = 0
            result["text"] = solution.get("gRecaptchaResponse")
        except CaptchaException as ex:
            raise CaptchaException("Failed to solve Recaptcha V3 using Capsolver", ex)
        return result
