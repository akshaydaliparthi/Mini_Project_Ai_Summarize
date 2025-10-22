# 🤖 SummarAI - AI-Powered Text Summarization Web App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-yellow)
![License](https://img.shields.io/badge/License-MIT-purple)

SummarAI is a powerful web application that leverages state-of-the-art AI technology to provide quick and accurate text summarization. Built with Flask and powered by the BART-large-CNN model from Facebook, it offers a seamless experience for converting lengthy articles into concise, meaningful summaries.

## ✨ Features

- 🚀 **Powerful AI Summarization**: Uses Facebook's BART-large-CNN model for high-quality summaries
- 👥 **User Authentication**: Secure signup/login system
- 💨 **Fast Processing**: Efficient chunking for handling large texts
- 🎨 **Modern UI**: Clean, responsive interface with real-time character counting
- 📱 **Mobile-Friendly**: Works seamlessly on all devices
- 🔒 **Secure**: Password hashing and session management
- 📊 **Smart Text Processing**: Handles large articles by breaking them into optimal chunks

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite with SQLAlchemy
- **AI Model**: facebook/bart-large-cnn (HuggingFace Transformers)
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Flask-Session, Werkzeug Security

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/akshaydaliparthi/Mini_Project_Ai_Summarize.git
   cd Mini_Project_Ai_Summarize
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy transformers torch werkzeug
   ```

4. **Initialize the database**
   ```bash
   python
   >>> from app import app, db
   >>> with app.app_context():
   >>>     db.create_all()
   >>> exit()
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. Visit `http://localhost:5000` in your browser

## 💡 Usage

1. **Sign Up/Login**: Create an account or log in to access the summarization tool
2. **Input Text**: Paste your article or long text into the text area
3. **Generate Summary**: Click the "Generate Summary" button
4. **View Results**: Get your concise summary with options to copy, download, or share

## 🎯 Key Features Explained

### AI Summarization
- Uses BART-large-CNN model for state-of-the-art summarization
- Handles long texts through smart chunking
- Maintains context and coherence in summaries

### User Management
- Secure password hashing
- Email verification
- Session management
- User-specific history (coming soon)

### Interface Features
- Real-time character counting
- Multiple summary styles
- Copy to clipboard
- Download summaries
- Mobile-responsive design

## 📱 Screenshots

Coming soon...

## 🔧 Configuration

Key configuration options in `app.py`:

```python
# AI Model Configuration
MODEL_ID = "facebook/bart-large-cnn"
MAX_CHUNKS = 5
CHUNK_TOKENS = 800

# Flask Configuration
app.config['SECRET_KEY'] = os.getenv('secretkey', 'devkey')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
```

## 🛣️ Roadmap

- [ ] Add support for URL input
- [ ] Implement summary history
- [ ] Add multiple language support
- [ ] Create API endpoints
- [ ] Add export options (PDF, DOCX)
- [ ] Implement user preferences
- [ ] Add analytics dashboard

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgments

- [HuggingFace Transformers](https://huggingface.co/facebook/bart-large-cnn) for the BART model
- Flask and its ecosystem for the web framework
- The open-source community for various tools and libraries

---
Made with ❤️ by [Akshay Daliparthi](https://github.com/akshaydaliparthi)
