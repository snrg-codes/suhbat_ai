# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types
import ast
import re



def generate(vakansiya_matni:str)->dict:
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""{vakansiya_matni}"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""system_instruction = \"\"\"
                                            Sen malakali texnik rekruter yoki HR bo‘limi uchun AI yordamchisan. Men senga ish vakansiyasining matnini yuboraman. Sening vazifang: ushbu matn asosida to‘g‘ri va aniqlashtirilgan quyidagi Python `dict` formatda ma'lumot chiqar:

                                            - \"rol\": vakansiyada aytilgan asosiy lavozim nomi (masalan, \"back end dasturchi\", \"frontend muhandis\", \"DevOps mutaxassisi\" va hokazo).
                                            - \"daraja\": vakansiyada bevosita yoki bilvosita aytilgan tajriba darajasi. Qabul qilinadigan variantlar: \"junior\", \"middle\", \"senior\", \"teamlead\".
                                            - \"stek\": asosiy dasturlash tili va asosiy framework yoki platformalar (masalan: [\"Python\", \"Django\"]).
                                            - \"texnologiyalar\": yordamchi texnologiyalar, kutubxonalar, API, servislar va vositalar (masalan: [\"Git\", \"REST\", \"FastAPI\", \"Redis\", \"Docker\", \"OAuth\", \"Celery\", \"RabbitMQ\", \"PostgreSQL\"]).

                                            **Qoidalarga amal qil:**
                                            - Faqat kerakli maydonlarni chiqar: `rol`, `daraja`, `stek`, `texnologiyalar`
                                            - Natija **faqat** toza Python `dict` formatda bo‘lishi kerak. Hech qanday izoh, qo‘shimcha matn, tavsif bo‘lmasin.
                                            - Agar ma’lumot noaniq bo‘lsa, eng yaqinini tanla.

                                            Natija shunday bo‘lishi kerak:
                                            {
                                                \"rol\": \"back end dasturchi\",
                                                \"daraja\": \"senior\",
                                                \"stek\": [\"Python\", \"Django\"],
                                                \"texnologiyalar\": [\"REST\", \"RabbitMQ\", \"Celery\", \"PostgreSQL\", \"Redis\", \"Docker\", \"Git\", \"S3\", \"OAuth\"]
                                            }
                                            \"\"\"
                                            """),
        ],
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    cleaned = re.sub(r"```python\s*|```", "", response.text).strip()
    data = ast.literal_eval(cleaned)

    return  data


if __name__ == "__main__":
    vakansiya_matni = """
                        Компания Alikson — это интернет-магазин электроники, цифровой и бытовой техники с собственной разработкой backend-системы на Python/Django. Проект представляет собой сложную многомодульную систему с интеграциями различных платежных сервисов, CRM, маркетинговых инструментов и логистических решений.

                        Что мы предлагаем:

                        Уровень дохода обсудим индивидуально (для нас важно найти "своего" человека);
                        Большой потенциал для профессионального роста в компании;
                        Ресурсы и возможность, сделать лучший продукт на рынке.
                        Что нужно будет делать:

                        Поддерживать и дорабатывать сервисы на Python;
                        Интегрировать и поддерживать внутренние и внешние API (Яндекс Маркет, Авито, CDEK, платежные системы Тинькофф, Яндекс Платежи и т.д.);
                        Работать с облачным хранилищем S3 для управления медиа-файлами и данными;
                        Настраивать и обрабатывать очереди RabbitMQ;
                        Писать скрипты для работы фоновых задач и автозагрузки данных;
                        Участвовать в улучшении архитектуры и стабильности системы.
                        Что мы ждём от кандидата:

                        Уверенное знание Python 3, Django и Django REST Framework;

                        Опыт работы с Redis, Celery, RabbitMQ;

                        Навыки работы с PostgreSQL;

                        Знание принципов кэширования (Memcached, django-cachalot);

                        Понимание принципов API-интеграций;

                        Навыки отладки, логирования и профилирования запросов в Django-приложениях;

                        Опыт работы с Docker, GlitchTip/Sentry, Graylog, GitLab будет плюсом.
    """
    a = generate(vakansiya_matni)
    print(a)

