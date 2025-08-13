from .endcaptcha import HttpClient
from captcha_svlib.recaptcha_v3 import RecaptchaV3 as IRecaptchaV3
import json


class RecaptchaV3(IRecaptchaV3):
    def solve(self,
              url: str,
              key: str,
              score: float = 0.4,
              action: str = "home_page",
              enterprise: bool = False) -> dict:

        result = {"error": 1, "text": ""}
        try:
            self.logger.info("Solving Recaptcha V3 using End Captcha Solver.")
            token_dict = {"proxy": "", "proxytype": "", "googlekey": key, "pageurl": url, "action": action, "min_score": score}
            token_params = json.dumps(token_dict)
            solver = HttpClient(self.settings.CAPTCHA_EC_USER, self.settings.CAPTCHA_EC_PASS)
            solution = solver.decode(type=5, token_params=token_params, timeout=90)

            if solution is None or not solution.get("text"):
                return result

            result["error"] = 0
            result["text"] = solution.get("text")

        except Exception as ex:
            params = dict(url=url, key=key, action=action, score=score)
            self.logger.error(f"Error while solving Recaptcha V3 using End Captcha Solver [{ex}]. params={params}")
        return result
