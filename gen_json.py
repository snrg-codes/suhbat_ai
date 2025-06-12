# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types
import re
import ast

def generate(vakansiya_matni):
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
            types.Part.from_text(text="""Siz 10 yillik tajribaga ega professional HR/rekrutersiz. Sizga ish vakansiyasi matni yuboriladi. Sizning vazifangiz — ushbu matndan quyidagi asosiy ma’lumotlarni aniqlab, faqat quyidagi tuzilma bo‘yicha JSON formatida aniq va qisqa javob qaytarish:
                                        {
                                        \"rol\": [qaysi lavozim],
                                        \"stek\": [asosiy ishlatiladigan texnologiya],
                                        \"texnologiyalar\": [talab etiladigan qo'shimcha texnologiyalar],
                                        \"daraja\": [qaysi daraja uchun - junior, middle, senior]
                                        }
                                        Eslatma:
                                        \"rol\" — bu lavozim nomi (masalan: Python Developer, Frontend Engineer).
                                        \"stek\" — vakansiyada asosiy ishlatiladigan texnologiya (masalan: Python, React, Java).
                                        \"texnologiyalar\" — qo‘shimcha texnologiyalar, kutubxonalar, frameworklar yoki vositalar (masalan: Docker, REST API, PostgreSQL).
                                        \"daraja\" — vakansiya kim uchun mo‘ljallangani (junior, middle, senior).
                                        Agar matnda ba'zi ma'lumotlar aniq ko'rsatilmagan bo‘lsa, ularni bo‘sh qoldiring (\"\" yoki []).
                                        """),
                                                ],
                                            )

    data = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    ).text

    tozalash = re.sub(r"```json\s*|```", "", data).strip()
    info = ast.literal_eval(tozalash)

    return info

if __name__ == "__main__":
    vakansiya_matni = """
        Обязанности:
        Разработка и поддержка серверной части веб-приложений
        Проектирование и реализация REST API
        Интеграция с внешними сервисами
        Оптимизация производительности и обеспечение безопасности приложений
        Требования:
        Уверенные знания одного из языков программирования (например, Python, Go, Java, PHP и т.д.)
        Опыт работы с реляционными и/или NoSQL базами данных
        Опыт разработки RESTful API
        Понимание принципов OOP, SOLID
        Умение работать в команде, ответственность, внимательность
        Опыт работы с Docker, Git
        Знание архитектурных паттернов
        Опыт работы с облачными сервисами (AWS, GCP, Azure)
    """
    generate(vakansiya_matni)
