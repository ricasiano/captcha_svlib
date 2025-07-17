from captcha_svlib.twocaptcha.text_captcha import TextCaptcha as TwoCaptchaTextCaptcha
from captcha_svlib.anticaptcha.text_captcha import TextCaptcha as AnticaptchaTextCaptcha
from captcha_svlib.capsolver.text_captcha import TextCaptcha as CapsolverTextCaptcha
from captcha_svlib.text_captcha import TextCaptcha


class TextCaptchaFactory:

    @staticmethod
    def build(captcha_solver, settings) -> TextCaptcha:
        match captcha_solver:
            case 'twocaptcha':
                return TwoCaptchaTextCaptcha(settings)

            case 'anticaptcha':
                return AnticaptchaTextCaptcha(settings)

            case 'capsolver':
                return CapsolverTextCaptcha(settings)

            case _:
                return TwoCaptchaTextCaptcha(settings)
