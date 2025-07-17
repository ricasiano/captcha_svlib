import capsolver
from captcha_svlib.text_captcha import TextCaptcha as ITextCaptcha
from captcha_svlib.captcha_exception import CaptchaException


class TextCaptcha(ITextCaptcha):
    def solve(self, image: str) -> dict:
        result = {"error": 1, "text": ""}
        try:
            capsolver.api_key = self.settings.CAPTCHA_CS_KEY
            kwargs = {
                "type": "ImageToTextTask",
                "body": image,
            }
            solution = capsolver.solve(kwargs)
            result["error"] = 0
            result["text"] = solution.get("text")
        except CaptchaException as ex:
            raise CaptchaException("Failed to solve text captcha using Capsolver", ex)
        return result
