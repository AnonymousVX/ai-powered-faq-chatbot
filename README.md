# AI-Powered FAQ Chatbot

## Project Overview

This is a production-ready AI-powered FAQ Chatbot built using Flask and HuggingFace Transformers.

The chatbot:

- Uses semantic similarity to match user queries with predefined FAQs
- Falls back to a generative Transformer model when confidence is low
- Stores chat history in a SQLite database
- Provides a minimal and clean web interface
- Exposes a REST API endpoint for message handling

This project demonstrates backend architecture design, NLP integration, database management, and scalable modular development.

---

## How It Works

1. User enters a message in the chat interface.
2. The message is sent to the `/api/chat` endpoint.
3. The NLP module:
   - Converts the message into embeddings
   - Compares it with stored FAQ embeddings
   - If similarity ≥ threshold → returns FAQ answer
   - Else → generates response using a Transformer model
4. Chat history is stored in SQLite.
5. The response is returned and displayed in the UI.

---

## Project Structure

```
ai_faq_chatbot/
│
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── database.py         # Database operations
├── nlp.py              # NLP processing logic
├── faq_data.py         # Predefined FAQ dataset
├── requirements.txt    # Project dependencies
│
├── templates/
│   └── index.html      # Frontend UI
│
└── static/
    └── style.css       # Styling
```

---

## Technologies Used

### Backend
- Python 3.10
- Flask

### NLP & AI
- HuggingFace Transformers
- Sentence-Transformers
- DistilGPT2 (Generative fallback)
- Scikit-learn (Cosine similarity)

### Database
- SQLite

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## Features

- Semantic FAQ matching
- Context-aware responses
- Generative fallback model
- RESTful API endpoint
- Persistent chat history storage
- Modular and scalable architecture
- Error handling
- Clean UI

---

## How to Run This Project Locally

### 1. Clone Repository

```bash
git clone https://github.com/AnonymousVX/ai-powered-faq-chatbot.git
cd ai-powered-faq-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## Database Schema

The application automatically creates:

`chat_history.db`

### Table: chat_history

| Column        | Type    |
|---------------|---------|
| id            | INTEGER |
| user_message  | TEXT    |
| bot_response  | TEXT    |
| timestamp     | TEXT    |
