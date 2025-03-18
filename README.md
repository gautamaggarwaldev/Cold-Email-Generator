# LLAMA Cold Email Generator ✉️

**A professional Streamlit web application that generates personalized cold emails for job applications by leveraging LLAMA-3.3 to match your skills and experience with job requirements.**

## Features

- **Job Information Extraction**: Automatically extract job details from URLs using LangChain and Groq
- **Manual Job Input**: Option to manually input job details when URL extraction is not available
- **Portfolio Matching**: Automatically selects relevant portfolio links that match the job requirements
- **Personalized Email Generation**: Creates tailored cold emails highlighting your skills and experience
- **User-Friendly Interface**: Clean, intuitive UI with responsive design
- **Save & Export**: Download generated emails or copy them to clipboard

## Tech Stack

- **Streamlit**: Web application framework
- **LangChain**: Framework for LLM application development
- **Groq**: LLM service provider (using Llama 3.3 70B model)
- **ChromaDB**: Vector database for storing and querying portfolio information
- **WebBaseLoader**: For scraping job posting details
- **Pandas**: Data manipulation and CSV handling

## Installation

1. Clone the repository
```bash
git clone https://github.com/gautamaggarwaldev/Cold-Email-Generator.git
cd cold-email-gen
```

2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file in the project root directory and add your API keys:
```
GROQ_API_KEY=your_groq_api_key_here
```

5. Prepare your portfolio data
Create a CSV file named `my_portfolio.csv` with columns for `Techstack` and `Links`.

## Usage

1. Start the application
```bash
streamlit run app.py
```

2. Navigate to the provided local URL (typically http://localhost:8501)

3. Fill in your professional profile details in the sidebar

4. Choose between providing a job URL or manually entering job details

5. Generate your personalized cold email

6. Edit, copy, or download the generated email

## How It Works

1. **Data Input**: User provides their professional profile and job details

2. **Job Processing**: Application extracts job information from URL or accepts manual entry

3. **Portfolio Matching**: ChromaDB vector database finds portfolio items relevant to the job skills

4. **Email Generation**: AI model creates a tailored email highlighting alignment between user skills and job requirements

5. **Result Display**: Generated email is displayed for editing, copying, or downloading

## Project Structure

```
cold-email-generator/
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── my_portfolio.csv      # User portfolio data
├── .env                  # Environment variables (API keys)
└── vector_db_store/      # ChromaDB persistent storage
```

## Requirements

- Python 3.8+
- Streamlit
- LangChain
- Groq API access
- ChromaDB
- Pandas
- dotenv

## Future Improvements

- Add support for more job posting platforms
- Improve job data extraction accuracy
- Add templates for different email styles
- Implement email performance tracking
- Add collaborative features for team review

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or feedback, please reach out to [gautam.aggarwal.tech@gmail.com]