# Company Research Tool

A comprehensive Python toolkit for automated company research using Parallel AI and Manus APIs. This tool helps gather detailed information about companies including social media handles, funding stages, and investment history.

## 🚀 Features

- **Social Media Research**: Find Twitter/X handles for companies and founders
- **Funding Analysis**: Determine company funding stages and investment rounds
- **Social Platform Discovery**: Locate LinkedIn, Medium, YouTube, and Substack profiles
- **Nexus Investment Tracking**: Identify first investment rounds by Nexus Venture Partners

## 📁 Project Structure

```
Company Research/
├── README.md                                    # This file
├── example_usage.py                             # Main example script
├── Parallel_client_Twitter_handles.py          # Twitter/X handle research
├── Parallel_client_Other_handles.py             # Other social media research
├── Parallel_client_company_stage.py             # Company funding stage analysis
├── Paralllel_client_Nexus_investment.py         # Nexus investment tracking```

## 🛠️ Installation

### Prerequisites

- Python 3.9+
- pip (Python package installer)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Company Research"
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install parallel-web pydantic requests python-dotenv
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory for your API key with Parallel

## 🚀 Quick Start

### Using Parallel AI (Recommended)

Run the main example script:

```bash
python3 example_usage.py
```

This will research Tesla and display:
- 📱 Founder X Profile
- 🏢 Company X Profile  
- 🔗 LinkedIn, Medium, YouTube, Substack URLs
- 💰 Company Stage
- 💰 First Nexus Investment