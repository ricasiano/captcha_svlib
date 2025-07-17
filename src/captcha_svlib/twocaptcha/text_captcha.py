from twocaptcha import TwoCaptcha
from captcha_svlib.text_captcha import TextCaptcha as ITextCaptcha
from captcha_svlib.captcha_exception import CaptchaException


class TextCaptcha(ITextCaptcha):

    def solve(self, image: str) -> dict:
        result = {"error": 1, "text": ""}
        try:
            solver = TwoCaptcha(self.settings.CAPTCHA_2C_KEY)
            solution = solver.normal(image, caseSensitive=1)
            result["error"] = 0
            result["text"] = solution.get("code")
        except Exception as ex:
            raise CaptchaException("Failed to solve text captcha using TwoCaptcha", ex)
        return result
