#!/usr/bin/env python
import sys
import warnings
import os
import argparse
import shlex

from crew import Askpdfcrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()   

def get_user_input(prompt="Enter your question about the PDF: "):
    """Get user input with a prompt."""
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit(0)
    except Exception as e:
        print(f"Error getting input: {e}")
        sys.exit(1)

def run():
    """
    Run the PDF search and answer generation crew.
    """
    parser = argparse.ArgumentParser(description="Search PDF content and generate answers")
    parser.add_argument("--pdf", type=str, help="Path to the PDF file to search")
    parser.add_argument("--question", type=str, nargs="+", help="Question to search in the PDF (put multi-word questions in quotes)")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")
    
    args = parser.parse_args()
    
    # Set default PDF path if not provided
    pdf_path = args.pdf
    if not pdf_path:
        pdf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), r"Multi-Agent-RAG-System-for-Local-PDFs\company_profile.pdf")
        if not os.path.exists(pdf_path):
            print(f"Default PDF file not found at {pdf_path}.")
            pdf_path = get_user_input("Enter the path to your PDF file: ")
    
    # Validate PDF path
    if not os.path.exists(pdf_path):
        print(f"PDF file not found at {pdf_path}.")
        sys.exit(1)
        
    print(f"Using PDF at: {pdf_path}")
    question = " ".join(args.question) if args.question else None
    
    # Initialize the crew with PDF path
    crew_instance = Askpdfcrew(pdf_path)
    
    if args.interactive:
        print("Interactive mode: Press Ctrl+C to exit.")
        while True:
            question = get_user_input()
            try:
                result = crew_instance.crew().kickoff(inputs={"question": question})
                print("\n------------- Answer -------------\n")
                print(result)
                print("\n----------------------------------\n")
            except Exception as e:
                print(f"An error occurred: {e}")
    else:
        if not question:
            question = get_user_input()
            
        try:
            result = crew_instance.crew().kickoff(inputs={"question": question})
            print("\n------------- Answer -------------\n")
            print(result)
            print("\n----------------------------------\n")
        except Exception as e:
            raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()