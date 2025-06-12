import re
import ast

data = """
    ```json
{
  "rol": [
    "Разработчик серверной части веб-приложений"
  ],
  "stek": [
    "Python",
    "Go",
    "Java",
    "PHP"
  ],
  "texnologiyalar": [
    "REST API",
    "Docker",
    "Git",
    "AWS",
    "GCP",
    "Azure"
  ],
  "daraja": []
}
```
"""
tozalash = re.sub(r"```json\s*|```", "", data).strip()
info = ast.literal_eval(tozalash)
print(info)