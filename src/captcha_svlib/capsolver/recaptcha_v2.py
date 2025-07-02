import capsolver
from captcha_svlib.recaptcha_v2 import RecaptchaV2 as IRecaptchaV2


class RecaptchaV2(IRecaptchaV2):
    def solve(self, url: str, key: str, invisible: bool = False) -> dict:
        result = {"error": 1, "text": ""}
        try:
            self.logger.debug("Solving text captcha using Capsolver")
            capsolver.api_key = self.settings.CAPTCHA_CS_KEY
            kwargs = {
                "type": "ReCaptchaV2TaskProxyLess",
                "websiteURL": url,
                "websiteKey": key,
                "invisible": 1 if invisible else 0
            }
            solution = capsolver.solve(kwargs)
            self.logger.info(solution)
            result["error"] = 0
            result["text"] = solution.get("gRecaptchaResponse")
        except Exception as ex:
            self.logger.error(f"Error while solving recaptchaV2 with Capsolver [{ex}]")
        return result
