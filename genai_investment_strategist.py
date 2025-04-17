{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.11"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "import os\n",
        "import yfinance as yf\n",
        "import streamlit as st\n",
        "from agno.agent import Agent\n",
        "from agno.models.google import Gemini\n",
        "import plotly.graph_objects as go\n",
        "\n",
        "os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY', '')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def compare_stocks(symbols):\n",
        "    data = {}\n",
        "    for symbol in symbols:\n",
        "        try:\n",
        "            hist = yf.Ticker(symbol).history(period=\"6mo\")\n",
        "            if not hist.empty:\n",
        "                data[symbol] = hist['Close'].pct_change().sum()\n",
        "        except:\n",
        "            continue\n",
        "    return data"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def get_company_info(symbol):\n",
        "    stock = yf.Ticker(symbol)\n",
        "    return {\n",
        "        \"name\": stock.info.get(\"longName\", \"N/A\"),\n",
        "        \"sector\": stock.info.get(\"sector\", \"N/A\"),\n",
        "        \"market_cap\": stock.info.get(\"marketCap\", \"N/A\"),\n",
        "        \"summary\": stock.info.get(\"longBusinessSummary\", \"N/A\")\n",
        "    }"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def get_company_news(symbol):\n",
        "    return yf.Ticker(symbol).news[:5]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "# Agents setup\n",
        "market_analyst = Agent(\n",
        "    model=Gemini(id=\"gemini-2.0-flash-exp\"),\n",
        "    description=\"Analyzes and compares stock performance.\",\n",
        "    instructions=[\n",
        "        \"Retrieve and compare stock performance from Yahoo Finance.\",\n",
        "        \"Calculate percentage change over a 6-month period.\",\n",
        "        \"Rank stocks based on performance.\"\n",
        "    ],\n",
        "    markdown=True\n",
        ")\n",
        "\n",
        "company_researcher = Agent(\n",
        "    model=Gemini(id=\"gemini-2.0-flash-exp\"),\n",
        "    description=\"Fetches company profiles and news.\",\n",
        "    instructions=[\n",
        "        \"Retrieve company info from Yahoo Finance.\",\n",
        "        \"Summarize latest news and key metrics.\"\n",
        "    ],\n",
        "    markdown=True\n",
        ")\n",
        "\n",
        "stock_strategist = Agent(\n",
        "    model=Gemini(id=\"gemini-2.0-flash-exp\"),\n",
        "    description=\"Recommends top stocks for investment.\",\n",
        "    instructions=[\n",
        "        \"Analyze performance and fundamentals.\",\n",
        "        \"Recommend stocks with justification.\"\n",
        "    ],\n",
        "    markdown=True\n",
        ")\n",
        "\n",
        "team_lead = Agent(\n",
        "    model=Gemini(id=\"gemini-2.0-flash-exp\"),\n",
        "    description=\"Combines insights for final report.\",\n",
        "    instructions=[\n",
        "        \"Summarize analysis into investor-ready report.\",\n",
        "        \"Rank stocks based on all inputs.\"\n",
        "    ],\n",
        "    markdown=True\n",
        ")"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
