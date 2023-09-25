import json
import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


class EmailUtil(object):
    def __init__(self) -> None:
        logger.info("## EmailUtil ##")
        print(f"Testing mode: {settings.TESTING}")

    def send_generic_email(
        self, subject: str, content: str, to: str, _from: str = None
    ) -> None:
        logger.info("##Sending generic email ##")
        print("sending email")
        img_base_src = settings.STATIC_BASE_URL
        if settings.TESTING:
            print("*** EMAIL TESTING MODE ***")
            print(f"Content: {content}\nSent to: {to}\nFrom:{settings.SITE['_title']}")
        else:
            try:
                print("Email subject:", subject)
                headers = {
                    "Authorization": f"Bearer {settings.SENDGRID_TOKEN}",
                    "Content-Type": "application/json",
                }
                content = content.replace("/static/", img_base_src)
                data = {
                    "personalizations": [{"to": [{"email": to}]}],
                    "from": {"email": f"Efficals.com <{settings.ADMIN_EMAIL}>"},
                    "subject": str(subject),
                    "content": [
                        {"type": "text/plain", "value": str(content)},
                        {"type": "text/html", "value": str(content)},
                    ],
                }

                r = requests.post(
                    url=settings.SENDGRID_URL, headers=headers, data=json.dumps(data)
                )
                logger.info(f"Send generic email response {r} {r.text}")
                # print(f"Send payload {json.dumps(data)}")
                print(f"Send generic email response {r} {r.text}")
            except Exception as e:
                logger.error(e)
                print("Exception:", e)
                print(data)
