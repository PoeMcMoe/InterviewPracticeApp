# Interview Practice App 🎯

An AI-powered interview preparation application built with Streamlit and OpenAI's GPT models. Practice technical interviews, behavioral questions, and analyze job descriptions to prepare for your dream job.

## Features

- Technical Interview Practice
- Behavioral Interview Questions
- Job Description Analysis
- AI-powered feedback and suggestions

## Setup Instructions

1. Clone the repository
```bash
git clone <repository-url>
cd InterviewPracticeApp
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
- Copy `.env.example` to `.env`
- Add your OpenAI API key to the `.env` file

5. Run the application
```bash
streamlit run app.py
```

## Project Structure

```
InterviewPracticeApp/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (create from .env.example)
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── components/            # Streamlit components
│   ├── technical_interview.py
│   ├── behavioral_interview.py
│   └── job_analysis.py
└── utils/                 # Utility functions
    └── openai_helper.py   # OpenAI API integration
```

## Contributing

Feel free to submit issues and enhancement requests! 