from anticaptchaofficial import imagecaptcha
from captcha_svlib.text_captcha import TextCaptcha as ITextCaptcha
import base64
import tempfile


class TextCaptcha(ITextCaptcha):
    def solve(self, image: str) -> dict:
        self.logger.info("Solving text captcha using Anticaptcha")
        solver = imagecaptcha.imagecaptcha()
        solver.set_verbose(0)
        solver.set_key(self.settings.CAPTCHA_AC_KEY)
        solver.set_soft_id(0)
        try:
            # Decode base64 and write to a real temporary file
            decoded_image = base64.b64decode(image)
            with tempfile.NamedTemporaryFile(suffix=".png", delete=True) as tmp_file:
                tmp_file.write(decoded_image)
                tmp_file.flush()

                solution = solver.solve_and_return_solution(tmp_file.name)
                if solution != 0:
                    return {"error": False, "text": solution}
                else:
                    return {"error": True, "text": "", "message": solver.error_code}
        except Exception as ex:
            return {"error": True, "text": "", "message": str(ex)}
