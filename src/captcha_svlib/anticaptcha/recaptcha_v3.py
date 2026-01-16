from anticaptchaofficial import recaptchav3proxyless
from anticaptchaofficial import recaptchav3enterpriseproxyless
from captcha_svlib.recaptcha_v3 import RecaptchaV3 as IRecaptchaV3
from captcha_svlib.captcha_exception import CaptchaException



class RecaptchaV3(IRecaptchaV3):
    def solve(self,
              url: str,
              key: str,
              score: float = 0.4,
              action: str = "home_page",
              enterprise: bool = False) -> dict:
        try:
            if enterprise:
                solver_class = recaptchav3enterpriseproxyless.recaptchaV3EnterpriseProxyless
            else:
                solver_class = recaptchav3proxyless.recaptchaV3Proxyless

            solver = solver_class()
            solver.set_verbose(0)
            solver.set_soft_id(0)
            solver.set_key(self.settings.CAPTCHA_AC_KEY)
            solver.set_website_key(key)
            solver.set_website_url(url)
            solver.set_cookies("")
            solver.set_page_action(action)
            solver.set_min_score(score)
            solution = solver.solve_and_return_solution()

            if solution != 0:
                return {"error": 0, "text": solution}
            return {"error": 1, "text": "", "message": "Captcha solving failed"}
        except CaptchaException as ex:
            raise CaptchaException("Failed to solve Recaptcha V3 using Anticaptcha", ex)
