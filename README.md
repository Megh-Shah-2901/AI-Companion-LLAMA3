# AI Companion With LLAMA3

Welcome to the AI Companion project! This repository hosts a simple yet powerful interactive AI companion built using LLAMA3, Langchain, and Streamlit. The application allows users to ask questions on any topic, and the AI will respond with helpful answers in real-time.

# Overview

This project demonstrates how to integrate Langchain and LLAMA3 to create a conversational AI tool. It uses a Streamlit interface for easy interaction, where users can input their queries and receive intelligent responses from the AI model.

# Features

•	LLAMA3 Integration: Utilizes the LLAMA3 model for generating accurate and context-aware responses.< br / >
•	Langchain Prompting: Leverages Langchain to structure prompts and guide the AI’s output.<br/>
•	Streamlit Interface: Provides a user-friendly web interface to interact with the AI.<br/>
•	Ollama LLM: Uses the Ollama library to access and manage the LLAMA3 model.

# Installation

# 1. Clone the Repository

  git clone https://github.com/Megh-Shah-2901/AI-Companion-LLAMA3.git<br/>
  cd AI-Companion-LLAMA3

# 2. Set Up Virtual Environment

  python -m venv venv<br/>
  source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install Required Packages

  pip install -r requirements.txt

# 4. Setup Environment Variables

  Ensure you have your Langchain API key set up. You can either set it in your environment or create a .env file.

# 5. Run the Application

  Start the Streamlit app with the following command:<br/>
  streamlit run app.py<br/>
  
  The application should now be running locally at http://localhost:8501.

# Usage

1.	Open the Streamlit app in your browser.<br/>
2.	Enter your query or topic in the text area.<br/>
3.	The AI will respond with a helpful answer generated by LLAMA3.

# About Ollama

Ollama is a library that simplifies the interaction with large language models (LLMs) like LLAMA3. It provides a user-friendly interface for managing models, creating prompts, and handling outputs. In this project, Ollama is used to integrate the LLAMA3 model into the Langchain-based prompt structure.

# Project Structure

•	app.py: The main Streamlit application file.<br/>
•	requirements.txt: Lists all the dependencies required to run the project.<br/>
•	README.md: This file, providing an overview and setup instructions.

# Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or create a pull request.

# License

This project is licensed under the MIT License - see the [LICENSE](url) file for details.

Contact

If you have any questions or need further assistance, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/meghshah05) or [GitHub](https://github.com/Megh-Shah-2901).
