from captcha_svlib.anticaptcha.recaptcha_v3 import RecaptchaV3 as TwoCaptchaRecaptchaV3
from captcha_svlib.twocaptcha.recaptcha_v3 import RecaptchaV3 as AnticaptchaRecaptchaV3
from captcha_svlib.recaptcha_v3 import RecaptchaV3


class RecaptchaV3Factory:

    @staticmethod
    def build(captcha_solver, logger) -> RecaptchaV3:
        match captcha_solver:
            case 'twocaptcha':
                return TwoCaptchaRecaptchaV3(logger)

            case 'anticaptcha':
                return AnticaptchaRecaptchaV3(logger)

            case _:
                raise Exception("Solver not found")
