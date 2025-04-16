## AI Investment Strategist

An interactive Streamlit web app that uses **Google's Gemini LLM**, **financial data from Yahoo Finance**, and **custom agent reasoning** to analyze stock performance, summarize company profiles, and recommend top investment opportunities.

---

### Features

- **Compare Stock Performance**  
  Uses real-time data from Yahoo Finance to evaluate percentage change over the last 6 months.

- **LLM-Driven Market Analysis**  
  Custom agents powered by Google's Gemini API analyze market trends and stock fundamentals.

- **Company Research**  
  Automatically summarizes sector, market cap, business overviews, and latest news headlines.

- **Investment Recommendations**  
  Aggregates all insights to generate a ranked list of the best stocks to consider.

- **Interactive Charts**  
  Visualize historical stock performance using Plotly.

---

### Tech Stack

- [Streamlit](https://streamlit.io/) – Web UI  
- [Google Gemini (via Agno SDK)](https://developers.google.com/) – LLM-based decision logic  
- [Yahoo Finance](https://pypi.org/project/yfinance/) – Financial data  
- [Plotly](https://plotly.com/python/) – Data visualization  
- [pyngrok](https://pyngrok.readthedocs.io/en/latest/) – Public tunnel for Colab usage  

---

### How to Run (Locally or on Google Colab)

#### On Google Colab:

1. Upload `investment_app.py` or use the notebook version.
2. Install dependencies:
   ```bash
   !pip install streamlit yfinance plotly pyngrok agno
   ```
3. Set your ngrok authtoken:
   ```bash
   !ngrok config add-authtoken YOUR_NGROK_TOKEN
   ```
4. Launch the app:
   ```bash
   !nohup streamlit run investment_app.py --server.port 8501 &
   from pyngrok import ngrok
   public_url = ngrok.connect(8501)
   print(public_url)
   ```

#### Locally:

```bash
pip install streamlit yfinance plotly agno
streamlit run investment_app.py
```

---

### Input

- Comma-separated stock symbols (e.g., `AAPL, TSLA, GOOG`)
- Google Gemini API key (from [Google AI Studio](https://makersuite.google.com/))

---

### Output

- Textual investment report with:
  - Market analysis
  - Company profiles
  - LLM-based investment recommendations
- Interactive 6-month stock performance chart

---

### Sample Screenshot

[App Screenshot](assets/app_screenshot.png) <!-- Optional, if you plan to add images -->

---

### Contributing

Feel free to fork this repo and submit PRs for new features like:
-  Sentiment analysis from news headlines
-  Integration with financial APIs (e.g., Alpha Vantage)
-  International stock support

---

### License

MIT License

---
