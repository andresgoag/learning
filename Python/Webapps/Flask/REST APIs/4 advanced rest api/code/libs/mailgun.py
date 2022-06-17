import os
from typing import List
from requests import Response, post


FAILED_LOAD_DOMAIN = "Failed to load Mailgun domain."
FAILED_LOAD_API_KEY = "Failed to load Mailgun API key."


class MailGunException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Mailgun:

    MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN")
    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")

    FROM_TITLE = "Stores REST API"
    FROM_EMAIL = "postmaster@sandbox12d36d3da76344da82338407987aef46.mailgun.org"

    @classmethod
    def send_email(cls, email: List[str], subject: str, text: str, html:str) -> Response:

        if cls.MAILGUN_DOMAIN is None:
            raise MailGunException(FAILED_LOAD_DOMAIN)

        if cls.MAILGUN_API_KEY is None:
            raise MailGunException(FAILED_LOAD_API_KEY)

        response = post(
            f"https://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages",
            auth = ("api", cls.MAILGUN_API_KEY),
            data = {
                "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                "to": email,
                "subject": subject,
                "text": text,
                "html": html,
            }
        )

        if response.status_code != 200:
            raise MailGunException("Error in sending confirmation email, user registration failed.")

        return response