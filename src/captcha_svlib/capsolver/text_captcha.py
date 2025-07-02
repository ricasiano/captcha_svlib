import capsolver
from captcha_svlib.text_captcha import TextCaptcha as ITextCaptcha


class TextCaptcha(ITextCaptcha):
    def solve(self, image: str) -> dict:
        result = {"error": 1, "text": ""}
        try:
            self.logger.info("Solving text captcha using Capsolver")
            capsolver.api_key = self.settings.CAPTCHA_CS_KEY
            kwargs = {
                "type": "ImageToTextTask",
                "body": image,
            }
            solution = capsolver.solve(kwargs)
            self.logger.debug(solution)
            result["error"] = 0
            result["text"] = solution.get("text")
        except Exception as ex:
            self.logger.error(f"Error while solving text captcha with Capsolver [{ex}]")
        return result
