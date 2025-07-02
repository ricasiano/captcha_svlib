from captcha_svlib.twocaptcha.text_captcha import TextCaptcha as TwoCaptchaTextCaptcha
from captcha_svlib.anticaptcha.text_captcha import TextCaptcha as AnticaptchaTextCaptcha
from captcha_svlib.capsolver.text_captcha import TextCaptcha as CapsolverTextCaptcha
from captcha_svlib.text_captcha import TextCaptcha


class TextCaptchaFactory:

    @staticmethod
    def build(captcha_solver, logger, settings) -> TextCaptcha:
        match captcha_solver:
            case 'twocaptcha':
                return TwoCaptchaTextCaptcha(logger, settings)

            case 'anticaptcha':
                return AnticaptchaTextCaptcha(logger, settings)

            case 'capsolver':
                return CapsolverTextCaptcha(logger, settings)

            case _:
                raise Exception("Solver not found")
