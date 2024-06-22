import random
import string


def generate_captcha(length=5):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha


captcha_code = generate_captcha(5)
print(f"Generated CAPTCHA: {captcha_code}")
