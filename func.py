# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate(data:dict):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=f"""Sen 10 yillik tajribaga ega {data.['rol']} mutaxassisan . Sen hozirda \"rol\", \"daraja\", \"stek\" va \"texnologiyalar\" bo‘yicha malakali mutaxassisni suhbatdan o‘tkazmoqdasan.

                                        Vakansiya quyidagicha:
                                        - Rol: {data['rol']}
                                        - Daraja: {data['daraja']}
                                        - Stek: {data['stek']}
                                        - Texnologiyalar: {data['texnologiyalar']}

                                        Sening vazifang:
                                        - Ketma-ket texnik savollar berish (jami 10 ta)
                                        - Savollarni turlicha darajada ber: oson, o‘rtacha va murakkab
                                        - Har bir javobdan so‘ng qisqacha baho ber: (masalan, \"to‘liq javob\", \"yuzaki javob\", \"noto‘g‘ri\", \"qo‘shimcha so‘rash kerak\")
                                        - Agar javob etarli bo‘lmasa, aniqlashtiruvchi savol ber yoki boshqa misol so‘ra
                                        - Suhbat so‘ngida natijani chiqar:
                                        - 10 ballik baho tizimi asosida umumiy texnik darajasini bahola
                                        - Qisqacha izoh yoz: kuchli tomonlar, zaif joylar, tavsiyalar
                                        - Ushbu lavozimga mos yoki mos emasligini yoz

                                        Faqat texnik savollar va professional suhbatga e’tibor qarat.

                                        ---

                                        Endi foydalanuvchi quyidagi savolga javob yozadi va sen unga asoslanib intervyuni boshlaysan:
                                        """),
        ],
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )
    return response.text


if __name__ == "__main__":
    generate()
