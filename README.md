# Chat with Multiple PDFs - AI Document Assistant

 

A powerful AI-powered document assistant that lets you chat with multiple PDF files using cutting-edge AI technologies. Built with Streamlit and powered by Google's Gemini AI.

## 🚀 Features

- **Multi-PDF Analysis**: Upload and process multiple PDF documents simultaneously
- **Natural Language Q&A**: Ask questions in plain English about your documents
- **Conversational Memory**: Maintains context between questions for natural dialogue
- **AI-Powered Insights**: Powered by Google Gemini 1.5 Flash model for intelligent responses
- **Efficient Processing**: Uses Hugging Face embeddings and FAISS vectorization
- **Secure**: API key management through environment variables

## ⚙️ Technologies Used

- **Google Gemini AI** - Core LLM for intelligent responses
- **LangChain** - Conversational AI pipeline and memory management
- **Hugging Face** - Sentence Transformers for text embeddings
- **FAISS** - Efficient vector similarity search
- **Streamlit** - Web interface and UI components
- **PyPDF2** - PDF text extraction

Install dependencies:
 pip install -r requirements.txt

 Set up environment variables:
 # .env file
GOOGLE_API_KEY=your_api_key_here

Start the Streamlit server:
streamlit run app.py
