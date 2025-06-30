from twocaptcha import TwoCaptcha
from ..recaptcha_v3 import RecaptchaV3 as IRecaptchaV3


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
            self.logger.info("Solving recaptchaV3 using 2CaptchaSolver")
            solver = TwoCaptcha(self.settings.CAPTCHA_2C_KEY)
            solution = solver.recaptcha(
                sitekey=key,
                url=url,
                version='v3',
                enterprise=1 if enterprise else 0,
                action=action,
                score=score
            )
            self.logger.debug(solution)
            result["error"] = 0
            result["text"] = solution.get("code")
            self.logger.info(f"Successfully solved recaptchaV3 with captchaId: {solution.get('captchaId')}")
        except Exception as ex:
            params = dict(url=url, key=key, enterprise=enterprise, action=action, score=score)
            self.logger.error(f"Error while solving recaptchaV3 with 2CaptchaSolver [{ex}]. params={params}")
        return result
