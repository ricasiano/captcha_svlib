from twocaptcha import TwoCaptcha
from captcha_svlib.recaptcha_v2 import RecaptchaV2 as IRecaptchaV2


class RecaptchaV2(IRecaptchaV2):
    def solve(self, url: str, key: str, invisible: bool = False) -> dict:
        result = {"error": 1, "text": ""}
        try:
            self.logger.info("Solving recaptchaV2 using 2CaptchaSolver")
            solver = TwoCaptcha(self.settings.CAPTCHA_2C_KEY)
            solution = solver.recaptcha(
                sitekey=key,
                url=url,
                invisible=1 if invisible else 0
            )
            result["error"] = 0
            result["text"] = solution.get("code")
            self.logger.info(f"Successfully solved recaptchaV2 with captchaId: {solution.get('captchaId')}")
        except Exception as ex:
            params = dict(url=url, key=key, invisible=invisible)
            self.logger.error(f"Error while solving recaptchaV2 with 2CaptchaSolver [{ex}]. params={params}")
        return result
