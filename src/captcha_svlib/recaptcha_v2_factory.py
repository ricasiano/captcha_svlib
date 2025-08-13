from captcha_svlib.anticaptcha.recaptcha_v2 import RecaptchaV2 as AnticaptchaRecaptchaV2
from captcha_svlib.twocaptcha.recaptcha_v2 import RecaptchaV2 as TwoCaptchaRecaptchaV2
from captcha_svlib.capsolver.recaptcha_v2 import RecaptchaV2 as CapsolverRecaptchaV2
from captcha_svlib.endcaptcha.recaptcha_v2 import RecaptchaV2 as EndcaptchaRecaptchaV2
from captcha_svlib.recaptcha_v2 import RecaptchaV2


class RecaptchaV2Factory:

    @staticmethod
    def build(captcha_solver: str, settings) -> RecaptchaV2:
        match captcha_solver:
            case 'twocaptcha':
                return TwoCaptchaRecaptchaV2(settings)

            case 'anticaptcha':
                return AnticaptchaRecaptchaV2(settings)

            case 'capsolver':
                return CapsolverRecaptchaV2(settings)

            case 'endcaptcha':
                return EndcaptchaRecaptchaV2(logger, settings)

            case _:
                return TwoCaptchaRecaptchaV2(settings)
