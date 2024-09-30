from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, WebsiteSearchTool   # has FirecrawlSearchTool!
from langchain_community.llms import Ollama
import yaml
import os

product_desc_file = 'product_desc.txt'
base_dir = os.path.dirname(os.path.abspath(__file__))
rag_tool = WebsiteSearchTool(config=dict(
        llm=dict(
            provider="ollama",
            config=dict(
                model="llama3.1",   # experimenting with models here
            ),
        ),
        embedder=dict(
            provider="ollama",
            config=dict(
                model="llama3.1",
            ),
        ),
    ))   # for now; can be limited to a specific site
file_reading_tool = FileReadTool(file_path='product_desc.txt')   # we can also define our own tools


@CrewBase
class RAI_Crew:
    agents_config_file = os.path.join(base_dir, 'config/agents.yaml')
    tasks_config_file = os.path.join(base_dir, 'config/tasks.yaml')

    def __init__(self):
        with open(self.agents_config_file, 'r') as f:
            self.agents_config = yaml.safe_load(f)

        with open(self.tasks_config_file, 'r') as f:
            self.tasks_config = yaml.safe_load(f)

        self.llm = Ollama(model='openhermes') # a small model to experiment with

    @agent
    def researcher(self):
        return Agent(
            config=self.agents_config['researcher'],
            tools=[rag_tool],
            llm=self.llm
        )

    @agent
    def analyst(self):
        return Agent(
            config=self.agents_config['analyst'],
            llm=self.llm
        )

    @agent
    def ceo_assistant(self):
        return Agent(
            config=self.agents_config['ceo_assistant'],
            tools=[file_reading_tool],
            llm=self.llm
        )

    @task
    def research_task(self):
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )

    @task
    def analysis_task(self):
        return Task(
            config=self.tasks_config['analysis_task'],
            agent=self.analyst()
        )

    @task
    def strategy_task(self):
        return Task(
            config=self.tasks_config['strategy_task'],
            agent=self.ceo_assistant()
        )

    @crew
    def crew(self):
        return Crew(
            agents=[self.researcher(), self.analyst(), self.ceo_assistant()],
            tasks=[self.research_task(), self.analysis_task(), self.strategy_task()],
            process=Process.sequential,   # hierarchical proces is available, consensual is in the making
            verbose=False   # True will show prompts
        )
