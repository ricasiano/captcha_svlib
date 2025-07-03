import capsolver
from captcha_svlib.recaptcha_v3 import RecaptchaV3 as IRecaptchaV3


class RecaptchaV3(IRecaptchaV3):
    def solve(self,
              url: str,
              key: str,
              score: float = 0.4,
              action: str = "home_page",
              enterprise: bool = False) -> dict:
        result = {"error": 1, "text": ""}
        try:
            self.logger.info("Solving recaptchaV3 using Capsolver")
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
        except Exception as ex:
            self.logger.error(f"Error while solving recaptchaV3 with Capsolver [{ex}]")
        return result
