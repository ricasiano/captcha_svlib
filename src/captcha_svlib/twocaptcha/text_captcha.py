from twocaptcha import TwoCaptcha
from captcha_svlib.text_captcha import TextCaptcha as ITextCaptcha


class TextCaptcha(ITextCaptcha):

    def solve(self, image: str) -> dict:
        result = {"error": 1, "text": ""}
        try:
            self.logger.info("Solving text captcha using 2CaptchaSolver")
            solver = TwoCaptcha(self.settings.CAPTCHA_2C_KEY)
            solution = solver.normal(image, caseSensitive=1)
            result["error"] = 0
            result["text"] = solution.get("code")
            self.logger.info(f"Successfully solved text captcha with captchaId: {solution.get('captchaId')}")
        except Exception as ex:
            self.logger.error(f"Error while solving text captcha with 2CaptchaSolver [{ex}]")
        return result
