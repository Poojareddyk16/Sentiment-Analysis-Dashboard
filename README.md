# Twitter Sentiment Analysis for Market Intelligence

A Python pipeline for collecting tweets about major tech companies, analyzing sentiment (using **VADER** for polarity and **TextBlob** for subjectivity), and exporting structured data for visualization in Tableau. Designed for market intelligence and competitive analysis roles.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Data Schema](#data-schema)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Compliance](#compliance)
- [License](#license)

## Project Overview
This tool helps market intelligence professionals:
- Track public sentiment about tech companies via Twitter (X)
- Analyze polarity (positive/negative/neutral) using **NLTK's VADER**
- Calculate subjectivity scores using **TextBlob**
- Export structured data for dashboarding in Tableau/Power BI

Aligned with requirements for roles requiring:
- Market/competitive analysis 📈
- Technical data synthesis 🔍
- Cross-functional reporting 🗂️

## Features
- **Hybrid Sentiment Analysis**  
  `VADER` for social media-optimized polarity + `TextBlob` for subjectivity
- **Targeted Data Collection**  
  Fetches tweets mentioning official company handles (e.g., `@Apple`)
- **Time-Series Ready**  
  Includes `created_date` for trend analysis
- **Enterprise-Grade**  
  Handles API rate limits automatically

## Prerequisites
- Python 3.8+
- Twitter Developer Account with **Bearer Token** ([Guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api))
- Tableau/Power BI (for visualization)

## Installation
**Clone repository**
- `git clone https://github.com/Poojareddyk16/Sentiment-Analysis-Dashboard.git`
- `cd Sentiment-Analysis-Dashboard` <br><br>
**Install dependencies**
- `pip install tweepy pandas nltk textblob`
### Download NLTK lexicon (first-time setup)
- `python -c "import nltk; nltk.download('vader_lexicon')"`


## Configuration
1. **API Setup**  
   Replace `YOUR_BEARER_TOKEN` in the script with your Twitter API v2 credentials.

2. **Target Companies**  
   Modify the `tech_handles` list in `sentiment_analysis.py`:
   tech_handles = ["@Apple", "@Samsung", "@NVIDIA", "@Google", "@Microsoft"]

## Usage
python sentiment_analysis.py

**Output**  
- Generates `tech_sentiment_data.csv` with:
  - Raw tweet text
  - VADER polarity scores (-1 to 1)
  - TextBlob subjectivity scores (0-1)
  - Sentiment classification (Positive/Neutral/Negative)
  - Timestamps

**Expected Runtime**  
~2-5 minutes for 50 tweets/company (varies by API rate limits).

## Data Schema
| Column | Description | Source |
|--------|-------------|--------|
| `tweet_id` | Unique tweet identifier | Twitter API |
| `created_at` | UTC timestamp of tweet | Twitter API |
| `text` | Full tweet text | Twitter API |
| `company` | Target handle being monitored | Config |
| `polarity` | Sentiment strength (-1 to 1) | VADER |
| `subjectivity` | Opinion vs fact (0-1) | TextBlob |
| `sentiment` | Classification label | VADER thresholds |
| `analysis_date` | When data was processed | Script |
| `created_date` | Date-only (for time-series) | Derived |

## Customization
**1. Adjust Companies**  
Edit the `tech_handles` list to track different accounts.

**2. Modify Tweet Volume**  
Change `max_results=50` to control tweets per company.

**3. Sentiment Thresholds**  
Update VADER classification logic:

Current thresholds
- if polarity >= 0.05: sentiment = "Positive"
- if polarity <= -0.05: sentiment = "Negative"


## Troubleshooting
**API Errors**  
- Ensure bearer token has `tweet.read` permission
- Verify X API tier allows sufficient request volume

**No Tweets Fetched**  
- Check query syntax (e.g., `-is:retweet lang:en`)
- Test with fewer companies/higher `max_results`

**NLTK Download Issues**  
Run manually in Python shell: 
- `import nltk` 
- `nltk.download('vader_lexicon')`


## Compliance
- Adheres to [X Developer Policy](https://developer.x.com/en)
- Stores only tweet IDs/text (no user PII)
- Delete raw data after analysis per Twitter (X) guidelines

## License
MIT License. See [LICENSE](LICENSE) for details.

