from captcha_svlib.anticaptcha.recaptcha_v2 import RecaptchaV2 as AnticaptchaRecaptchaV2
from captcha_svlib.twocaptcha.recaptcha_v2 import RecaptchaV2 as TwoCaptchaRecaptchaV2
from captcha_svlib.capsolver.recaptcha_v2 import RecaptchaV2 as CapsolverRecaptchaV2
from captcha_svlib.recaptcha_v2 import RecaptchaV2


class RecaptchaV2Factory:

    @staticmethod
    def build(captcha_solver: str, logger, settings) -> RecaptchaV2:
        match captcha_solver:
            case 'twocaptcha':
                return TwoCaptchaRecaptchaV2(logger, settings)

            case 'anticaptcha':
                return AnticaptchaRecaptchaV2(logger, settings)

            case 'capsolver':
                return CapsolverRecaptchaV2(logger, settings)

            case _:
                raise Exception("Solver not found")
