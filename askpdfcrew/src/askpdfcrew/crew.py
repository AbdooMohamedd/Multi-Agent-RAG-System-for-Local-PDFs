from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import PDFSearchTool


@CrewBase
class Askpdfcrew():
    """Askpdfcrew crew for searching PDFs and generating reports"""

    agents: List[BaseAgent]
    tasks: List[Task]
    pdf_path: str

    def __init__(self, pdf_path: str = None):
        """Initialize the crew with a PDF path"""
        super().__init__()
        self.pdf_path = pdf_path
    
    @agent
    def pdf_searcher(self) -> Agent:
        """Creates a PDF search agent that uses PDFSearchTool to find relevant content"""
        pdf_search_tool = PDFSearchTool(pdf=self.pdf_path)
        
        return Agent(
            config=self.agents_config['pdf_searcher'],
            tools=[pdf_search_tool],
            verbose=True
        )

    @agent
    def content_writer(self) -> Agent:
        """Creates a content writer agent that formats answers from PDF search results"""
        return Agent(
            config=self.agents_config['content_writer'],
            verbose=True
        )

    @task
    def pdf_search_task(self) -> Task:
        """Task for searching content in PDFs based on user questions"""
        return Task(
            config=self.tasks_config['pdf_search_task'],
        )

    @task
    def answer_writing_task(self) -> Task:
        """Task for formatting answers from PDF search results into a well-written report"""
        return Task(
            config=self.tasks_config['answer_writing_task'], 
            output_file='pdf_answer.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Askpdfcrew crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
