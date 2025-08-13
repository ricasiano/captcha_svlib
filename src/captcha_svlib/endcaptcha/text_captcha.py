from endcaptcha import HttpClient
from captcha_svlib.text_captcha import TextCaptcha as ITextCaptcha
from captcha_svlib.captcha_exception import CaptchaException
import base64
import io


class TextCaptcha(ITextCaptcha):
    def solve(self, image: str) -> dict:
        result = {"error": 1, "text": ""}
        try:
            self.logger.info("Solving text captcha using End Captcha Solver.")
            image = io.BytesIO(base64.b64decode(image))

            solver = HttpClient(self.settings.CAPTCHA_EC_USER, self.settings.CAPTCHA_EC_PASS)
            solution = solver.decode(image)

            if solution is None or not solution.get("text"):
                return result

            result["error"] = 0
            result["text"] = solution.get("text")

        except Exception as ex:
            raise CaptchaException("Failed to solve text captcha using End Captcha Solver.", ex)
        return result
