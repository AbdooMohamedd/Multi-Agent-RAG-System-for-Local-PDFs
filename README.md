# 🤖 Multi-Agent RAG System for Local PDFs

![Multi-Agent RAG System Banner](https://github.com/user/Multi-Agent-RAG-System-for-Local-PDFs/raw/main/doc/system-flowchart.png)

## 📋 Overview

This system uses CrewAI's multi-agent architecture to enable intelligent searching and querying of local PDF documents. Perfect for researchers, students, and professionals who need to quickly extract accurate information from PDF files without the need for internet connectivity.

## 🚀 What This System Does

The Multi-Agent RAG System for Local PDFs automates the entire process of:

1. Taking user questions about PDF document content
2. Searching through PDF files using semantic search technology
3. Extracting the most relevant information related to the query
4. Generating well-formatted, comprehensive answers
5. Creating markdown documents with the results

All with just one command and a question about your PDFs!

## 🔄 Workflow

```
User Question → PDF Search → Content Extraction → Answer Generation → Markdown Document
```

1. **Input**: User provides a question about their PDF content
2. **Search**: System uses semantic search to find relevant sections
3. **Extraction**: The most pertinent information is extracted from the PDF
4. **Answer Generation**: AI generates a comprehensive, structured answer
5. **Output**: Results are saved as markdown documents

## 👥 Agent System Design

This project uses a specialized team of AI agents, each with a dedicated role:

### 1. PDF Search Specialist

- **Role**: PDF Content Search Specialist
- **Task**: Find the most relevant content from PDF documents based on user questions
- **Input**: User question and PDF path
- **Output**: Extracted relevant content with page references
- **Tools**: PDFSearchTool from crewai_tools

### 2. Content Writer

- **Role**: Technical Content Writer and Information Synthesizer
- **Task**: Create well-structured, readable answers from the extracted PDF content
- **Input**: User question and extracted PDF content
- **Output**: Well-formatted markdown answer document
- **Features**: Generates clear explanations, properly formatted content, and direct answers

## 💻 How to Run the System

### Installation

1. Clone the repository:

   ```powershell
   git clone https://github.com/username/Multi-Agent-RAG-System-for-Local-PDFs.git
   cd Multi-Agent-RAG-System-for-Local-PDFs
   ```

2. Install dependencies:

   ```powershell
   pip install -e .
   ```

   This will install all required dependencies.

3. Set up your API key:
   - Create a `.env` file in the root directory
   - Add your API key: `OPENAI_API_KEY=your_api_key_here`

### Usage

Run the system with a specific question:

```powershell
python -m askpdfcrew.src.askpdfcrew.main --pdf "path/to/your/document.pdf" --question "What is the main topic of this document?"
```

Or run in interactive mode to ask multiple questions:

```powershell
python -m askpdfcrew.src.askpdfcrew.main --pdf "path/to/your/document.pdf" --interactive
```

If no PDF path is provided, the system will prompt you to enter one.

## ✅ Project Outputs

For each question, the system produces:

- `pdf_answer.md` - A well-formatted markdown document containing the answer to your question

## 🔧 Technical Details

- **Python Version**: 3.10+
- **Key Dependencies**:
  - CrewAI for the multi-agent architecture
  - crewai_tools for PDF searching capabilities
  - Python-dotenv for environment variable management
  - Argparse for command-line argument parsing

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- CrewAI for the multi-agent framework
- OpenAI for the language processing capabilities
- CrewAI Tools for PDF search functionality

## 📬 Contact

For questions or feedback, please open an issue on the GitHub repository or contact the project maintainer.
