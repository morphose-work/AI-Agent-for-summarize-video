# 🎥 AI Agent for YouTube Video Summarization

Интелектуальная многоагентная система с **CrewAI** и **Streamlit** которая извлекает субтитры из *Youtube* и использует ИИ из **OpenRouter**

## 🚀Особенности:
- **Автоматическое извлечение**: Система сама извлекает субтитры из видео.
- **Мультиагентная система**: Каждый агент имеет свою роль.
- **Структрированный ответ**: С помощью *Pydantic-Схемы* ответ будет структурированным
- **Современный интерфейс**: Сделано с помощью **Streamlit** и используется **CSS**

---

## Стек:
- **Framework**: CrewAI
- **UI**: Streamlit + CSS
- **LLM Provider**: OpenRouter
- **Package manager**: uv
- **Validation**: Pydantic

---
## Установка:
1. ``git clone https://github.com/morphose-work/AI-Agent-for-summarize-video``
2. Создайте `.env`
3. Впишите туда `OPENROUTER_MODEL = openai/gpt-oss-20b:free`, `OPENROUTER_BASE_URL = https://openrouter.ai/api/v1`, `OPENROUTER_API_KEY=`
4. Зарегестрируйтесь на OpenRouter: https://openrouter.ai
5. Создайте ключ и вставьте
6. Установите зависимости: `uv add -r requirements.txt` или `python -m pip install -r requirements.txt`
7. Запустите `uv run streamlit run main` или `streamlit run main.py`
