from .endcaptcha import HttpClient
from captcha_svlib.recaptcha_v2 import RecaptchaV2 as IRecaptchaV2
from captcha_svlib.captcha_exception import CaptchaException
import json


class RecaptchaV2(IRecaptchaV2):
    def solve(self, url: str, key: str, invisible: bool = False) -> dict:
        result = {"error": 1, "text": ""}
        try:
            token_dict = {"proxy": "", "proxytype": "", "googlekey": key, "pageurl": url}
            token_params = json.dumps(token_dict)
            solver = HttpClient(self.settings.CAPTCHA_EC_USER, self.settings.CAPTCHA_EC_PASS)
            solution = solver.decode(type=4, token_params=token_params, timeout=90)

            if solution is None or not solution.get("text"):
                return result

            result["error"] = 0
            result["text"] = solution.get("text")

        except CaptchaException as ex:
            raise CaptchaException("Failed to solve Recaptcha V2 using End Captcha Solver.", ex)
        return result
