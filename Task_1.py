import re
def email_parse(email_address):
    RE_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w)', re.IGNORECASE)
    if not RE_email.match(email_address):
        raise ValueError(f'wrong email: {email_address}')
    print(RE_email.match(email_address).groupdict())

for i in ['someone@geekbrains.ru', 'som&one@geekbrainsru', 'someone@geekbrainsru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)