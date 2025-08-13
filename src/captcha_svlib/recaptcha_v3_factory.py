from captcha_svlib.anticaptcha.recaptcha_v3 import RecaptchaV3 as AnticaptchaRecaptchaV3
from captcha_svlib.twocaptcha.recaptcha_v3 import RecaptchaV3 as TwoCaptchaRecaptchaV3
from captcha_svlib.capsolver.recaptcha_v3 import RecaptchaV3 as CapsolverRecaptchaV3
from captcha_svlib.endcaptcha.recaptcha_v3 import RecaptchaV3 as EndcaptchaRecaptchaV3
from captcha_svlib.recaptcha_v3 import RecaptchaV3


class RecaptchaV3Factory:

    @staticmethod
    def build(captcha_solver, settings) -> RecaptchaV3:
        match captcha_solver:
            case 'twocaptcha':
                return TwoCaptchaRecaptchaV3(settings)

            case 'anticaptcha':
                return AnticaptchaRecaptchaV3(settings)

            case 'capsolver':
                return CapsolverRecaptchaV3(settings)

            case 'endcaptcha':
                return EndcaptchaRecaptchaV3(settings)

            case _:
                return TwoCaptchaRecaptchaV3(settings)
