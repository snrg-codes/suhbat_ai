# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types

rol = "Sistemniy administrator"
daraja = "junior"
ism = "Pepe"

def generate( rol, daraja, ism, javob= f"salom mening ismim {ism}"):
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
            types.Part.from_text(text=f"""sen {rol} mutaxassisi sifatida 10 yillik tajribaga egasan. Sen {daraja} {rol} lavozimiga {ism} ismli mutaxasisni olish uchun suhbat jarayonidasan. Ketma-ket savollarni ber. savollar soni 10 ta. savollar javobi qoniqtirmasa bu haqida yoz va savol berishni davom ettir. suhbat tugaganidan so'ng statistikani ber va ushbu lavozimga {ism} to'g'ri keladi yoki yo'q 10 ballik tizimda bahola."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

while True:
    user = input("javob: ")
    generate(rol, daraja, ism, user)
