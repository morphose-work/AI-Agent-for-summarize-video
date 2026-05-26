from typing import List

from pydantic import BaseModel, Field

class OutputSummarySchema(BaseModel):
    title: str = Field(
        description='Придуманный емкий и вовлекающий заголовок для конспекта на русском языке. Используй максимум в заголовке 5 слов'
    )
    
    brief_summary: str = Field(
        description='Краткое описание видео (5-7 предложения), объясняющее главную суть контента.'
    )
    
    key_points: List[str] = Field(
        description='Список ключевых тезисов, инсайтов и важных мыслей из видео. Минимум 5 пунктов.'
    )
    
    action_items: List[str] = Field(
        description='Практические советы, шаги или выводы: что слушатель может сделать после просмотра этого видео.'
    )