from urllib.parse import parse_qs, urlparse
from typing import Type

from pydantic import BaseModel

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound

from crewai.tools import BaseTool

from src.schema import UrlInputSchema

class YoutubeSubtitlesTool(BaseTool):
    name: str = 'youtube_subtitles_tool'
    description: str = 'Инструмент для извлечения субтитров с видео'
    args_schema: Type[BaseModel] = UrlInputSchema

    def _get_id_video(self, url: str) -> str:
        parsed = urlparse(url)

        if parsed.hostname in ['www.youtube.com', 'youtube.com']:
            return parse_qs(parsed.query).get('v', None)[0]
        elif parsed.hostname == "youtu.be":
            return parsed.path[1:]
        return None
    
    def _run(self, url: str) -> str:
        try:
            video_id = self._get_id_video(url)

            if not video_id:
                return 'Ошибка: ID видео не найденно!'

            ytt_api = YouTubeTranscriptApi()

            transcript_list = ytt_api.fetch(video_id, languages=['ru','en'])

            full_text = " ".join(item.text for item in transcript_list)

            return full_text
        except NoTranscriptFound:
            return 'Ошибка: Субтитров нет так как их отключил автор!'
        except Exception as e:
            return f'Неизвестная ошибка: {str(e)}'