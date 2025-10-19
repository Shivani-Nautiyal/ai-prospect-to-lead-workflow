# 🤖 AI Prospect-to-Lead Workflow

An intelligent B2B lead generation system that automates prospect discovery, scoring, and personalized outreach using AI agents built with LangGraph principles.

## 📋 Overview

This project demonstrates a complete automated workflow for B2B sales:

1. **Prospect Search** - Discovers potential leads based on industry and criteria
2. **Lead Scoring** - Ranks prospects using intelligent scoring algorithms
3. **Outreach Generation** - Creates personalized email content for top prospects

## 🏗️ Architecture
```
prospect_to_lead_workflow/
│
├── workflow.json                # Workflow configuration
├── langgraph_builder.py         # Main workflow orchestrator
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── README.md                    # This file
│
└── agents/                      # AI Agent modules
    ├── __init__.py
    ├── prospect_search_agent.py     # Finds prospects
    ├── scoring_agent.py             # Scores and ranks leads
    └── outreach_content_agent.py    # Generates emails
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the repository**
```bash
cd prospect_to_lead_workflow
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables (Optional)**
```bash
cp .env.example .env
# Edit .env and add your API keys if you have them
```

4. **Run the workflow**
```bash
python langgraph_builder.py
```

## 🧩 How It Works

### 1. ProspectSearchAgent
- **Purpose**: Discovers B2B prospects matching specified criteria
- **Current Implementation**: Generates sample prospect data
- **Output**: List of companies with contact information

### 2. ScoringAgent
- **Purpose**: Ranks prospects based on multiple factors
- **Scoring Criteria**:
  - Job title (C-level executives score higher)
  - Company location
  - Company size
  - Engagement signals
- **Output**: Sorted list with scores (0-100) and rankings

### 3. OutreachContentAgent
- **Purpose**: Generates personalized outreach emails
- **Features**:
  - OpenAI integration for AI-generated content (optional)
  - Fallback template-based generation
  - Personalized subject lines
  - Value-focused messaging
- **Output**: Complete email drafts ready to send

## 🛠️ Tech Stack

- **Python 3.8+** - Core programming language
- **LangChain** - Agent orchestration framework
- **OpenAI API** - AI content generation (optional)
- **python-dotenv** - Environment management
- **JSON** - Configuration and data storage

## 📊 Sample Output
```
🚀 Starting workflow execution with 3 steps

📍 STEP 1/3: PROSPECT_SEARCH
   Agent: ProspectSearchAgent
   🔍 Searching for 5 prospects in technology industry...
   ✓ Found 5 prospects

📍 STEP 2/3: SCORING
   Agent: ScoringAgent
   📊 Scoring 5 prospects...
   ✓ Scored and ranked 5 prospects
   📈 Top score: 92.45

📍 STEP 3/3: OUTREACH_CONTENT
   Agent: OutreachContentAgent
   ✉️  Generating personalized emails for top 3 prospects...
   ✓ Generated 3 personalized outreach emails

🎉 Workflow completed successfully!
```

## 🔧 Configuration

Edit `workflow.json` to customize:

- Number of prospects to find
- Target industry
- Company size preference
- Number of outreach emails to generate
- Agent execution order

## 🌟 Future Enhancements

- [ ] Real API integration (Apollo.io, Clearbit)
- [ ] Email sending via SendGrid
- [ ] Database storage (SQLite or ChromaDB)
- [ ] Feedback loop with FeedbackTrainerAgent
- [ ] Google Sheets integration
- [ ] Web dashboard for monitoring

## 🐛 Troubleshooting

### Common Issues

**Issue: "No module named 'agents'"**
```bash
# Solution: Ensure agents/__init__.py exists
touch agents/__init__.py
```

**Issue: "Module not found"**
```bash
pip install -r requirements.txt
```

## 📝 Environment Variables

Copy `.env.example` to `.env` and configure:
```bash
OPENAI_API_KEY=sk-...          # For AI-generated content (optional)
APOLLO_API_KEY=...             # For real prospect data (optional)
CLEARBIT_KEY=...               # For company enrichment (optional)
SENDGRID_KEY=...               # For email sending (optional)
```

**Note:** The system works perfectly without any API keys using template-based generation!

## 👥 Author

**Your Name**
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## 📄 License

MIT License - Free to use and modify

## 🙏 Acknowledgments

- Built for Analytos AI technical assessment
- Powered by LangChain and OpenAI
- Inspired by modern AI agent architectures

---

**Built with ❤️ using Python and AI**