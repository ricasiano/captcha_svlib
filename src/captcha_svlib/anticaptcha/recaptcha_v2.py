from anticaptchaofficial import recaptchav2proxyless
from captcha_svlib.recaptcha_v2 import RecaptchaV2 as IRecaptchaV2
from captcha_svlib.captcha_exception import CaptchaException

class RecaptchaV2(IRecaptchaV2):
    def solve(self, url: str, key: str, invisible: bool = False) -> dict:
        try:
            solver = recaptchav2proxyless.recaptchaV2Proxyless()
            solver.set_verbose(0)
            solver.set_soft_id(0)
            solver.set_key(self.settings.CAPTCHA_AC_KEY)
            solver.set_website_key(key)
            solver.set_website_url(url)
            solver.set_cookies("")
            solver.set_is_invisible(invisible)
            solution = solver.solve_and_return_solution()

            if solution != 0:
                return {"error": 0, "text": solution}
            return {"error": 1, "text": "", "message": "Captcha solving failed"}
        except CaptchaException as ex:
            raise CaptchaException("Failed to solve Recaptcha v2 using Anticaptcha", ex)
