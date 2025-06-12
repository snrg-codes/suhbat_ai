# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate(data, javob):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""{javob}"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=f"""Siz 10 yillik tajribaga ega tajribali {data['rol']} mutaxassissiz. Sizning vazifangiz — yangi ishga kirayotgan junior darajadagi Python dasturchisi bilan texnik suhbat o‘tkazish. Suhbatga oid vakansiya quyidagi kabi:
                                            
                                            \"rol\": [\"{data['rol']}\"],
                                            \"stek\": [\"{data['stek']}\"],
                                            \"texnologiyalar\": [{data['texnologiyalar']}],
                                            \"daraja\": [{data['daraja']}]
                                            
                                            Talablar:
                                            Kandidatga yuqoridagi talabalar bo‘yicha 10 ta texnik savol bering.
                                            Har bir savoldan so‘ng javobini eshiting (foydalanuvchi kiritadi).
                                            Javobni tajribali dasturchi sifatida tahlil qiling: to‘g‘rimi, noto‘g‘rimi, tushunchasi qanday.
                                            Suhbat ohirida quyidagi statistika va tahlilni bering:
                                            Nechta savolga to‘g‘ri javob berdi.
                                            Har bir texnologiya bo‘yicha qisqacha bilim darajasini baholang (masalan: Python — yaxshi, Docker — zaif).
                                            Umumiy baho: 10 ballik tizimda bu lavozimga qanchalik mos keladi.
                                            Kandidatga nimani o‘rganishni tavsiya etasiz (texnologiyalar yoki mavzular bo‘yicha).
                                            Javobni faqat professionallar darajasida, aniq, muloyim va tahliliy tilda yozing.
                                            Savollar ketma-ketligini saqla va 10 ta savol ber. kandidat yaxshi javob bermasa tushuntirishini ayt, agar yana notog'ri javob bersa davom et
                                            """),
                                                    ],
                                                )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    import gen_json

    vakansiya = """
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
    data = gen_json.generate(vakansiya)
    print(data)
    generate(data, "salom")
