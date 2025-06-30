from captcha_svlib.twocaptcha.text_captcha import TextCaptcha as TwoCaptchaTextCaptcha
from captcha_svlib.anticaptcha.text_captcha import TextCaptcha as AnticaptchaTextCaptcha
from text_captcha import TextCaptcha


class TextCaptchaFactory:

    @staticmethod
    def build(captcha_solver, logger) -> TextCaptcha:
        match captcha_solver:
            case 'twocaptcha':
                return TwoCaptchaTextCaptcha(logger)

            case 'anticaptcha':
                return AnticaptchaTextCaptcha(logger)

            case _:
                raise Exception("Solver not found")
