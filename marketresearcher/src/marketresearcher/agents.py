from crewai import Agent

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools


def market_research_agent():
    return Agent(
        role='Market Research Agent',
        goal="""Gather and analyze data about target markets, including market size, 
              growth potential, key players, customer needs, and trends""",
        backstory=
        """As a Market Research Agent at Broadridge, your mission is to dive deep into the markets of interest to 
      identify opportunities and threats. You employ a combination of qualitative and quantitative research 
      methods, analyzing extensive datasets and public records. Your work is pivotal in mapping out market 
      landscapes, forecasting trends, and highlighting growth potential. By presenting well-rounded reports, 
      you provide Broadridge with actionable insights that inform strategic planning and decision-making processes, 
      ensuring the company remains competitive and informed about emerging market dynamics.""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True)


class TripAgents():

    def market_research_agent(self):
        return Agent(
            role='Market Research Agent',
            goal="""Gather and analyze data about target markets, including market size, 
                  growth potential, key players, customer needs, and trends""",
            backstory=
            """As a Market Research Agent at Broadridge, your mission is to dive deep into the markets of interest to 
          identify opportunities and threats. You employ a combination of qualitative and quantitative research 
          methods, analyzing extensive datasets and public records. Your work is pivotal in mapping out market 
          landscapes, forecasting trends, and highlighting growth potential. By presenting well-rounded reports, 
          you provide Broadridge with actionable insights that inform strategic planning and decision-making processes, 
          ensuring the company remains competitive and informed about emerging market dynamics.""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True)


    def travel_concierge(self):
        return Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
            backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                CalculatorTools.calculate,
            ],
            verbose=True)
