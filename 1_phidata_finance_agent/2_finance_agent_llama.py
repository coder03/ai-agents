"""Run `pip install yfinance` to install dependencies."""

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()


def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    instructions=[
        "Use tables to display data.",
        "If you need to find the symbol for a company, use the get_company_symbol tool.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for TSLA and Phidata. Show in tables.", stream=True
)

# agent.print_response(
#     "what is the interinsic value of AMD, TSMC, ARM, Qualcomm, broadcom, direxon daily semiconductor bull 3X ETF, Toyota motor corporation, TSLA, SMC, alphabet, Nvdia, Intel, Apple, Unitedhealth group, Eli lilly and company, microsoft, kratos defense, Adobe, crowdstike, Palantir, nutanix, kraneshare hang seng, nova nordisk, li auto, paccar inc, honda motor co, global x robotics, hewlett packard, and cisco. Show in tables.", stream=True
# )