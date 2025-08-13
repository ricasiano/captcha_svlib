from captcha_svlib.anticaptcha.recaptcha_v3 import RecaptchaV3 as AnticaptchaRecaptchaV3
from captcha_svlib.twocaptcha.recaptcha_v3 import RecaptchaV3 as TwoCaptchaRecaptchaV3
from captcha_svlib.capsolver.recaptcha_v3 import RecaptchaV3 as CapsolverRecaptchaV3
from captcha_svlib.endcaptcha.recaptcha_v3 import RecaptchaV3 as EndcaptchaRecaptchaV3
from captcha_svlib.recaptcha_v3 import RecaptchaV3


class RecaptchaV3Factory:

    @staticmethod
    def build(captcha_solver, logger, settings) -> RecaptchaV3:
        match captcha_solver:
            case 'twocaptcha':
                return TwoCaptchaRecaptchaV3(logger, settings)

            case 'anticaptcha':
                return AnticaptchaRecaptchaV3(logger, settings)

            case 'capsolver':
                return CapsolverRecaptchaV3(logger, settings)

            case 'endcaptcha':
                return EndcaptchaRecaptchaV3(logger, settings)

            case _:
                return TwoCaptchaRecaptchaV3(logger, settings)
