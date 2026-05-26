from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from src.schema import OutputSummarySchema
from src.tools import YoutubeSubtitlesTool
from src.utils import ENV_READER

@CrewBase
class YoutubeSummaryCrew():

    agents: list[BaseAgent]
    tasks: list[Task]

    def __init__(self):
        self.llm = LLM(
            model=ENV_READER().OPENROUTER_MODEL,
            base_url=ENV_READER().OPENROUTER_BASE_URL,
            api_key=ENV_READER().get_api_key()
        )

    @agent
    def summarizator(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizator'],
            tools=[YoutubeSubtitlesTool()],
            llm=self.llm
        )
    
    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],
            llm=self.llm
        )
    
    @task
    def summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarizer_task']
        )
    
    @task
    def editor_task(self) -> Task:
        return Task(
            config=self.tasks_config['editor_task'],
            output_pydantic=OutputSummarySchema
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
