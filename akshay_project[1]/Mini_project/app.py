from flask import Flask, flash, render_template, request, redirect, url_for, session
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import textwrap
import os

# ---------------- Flask App Setup ---------------- #
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('secretkey', 'devkey')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ---------------- Database Model ---------------- #
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

# ---------------- Load Model ---------------- #
Model_ID = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(Model_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(Model_ID)
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

# ---------------- Helper ---------------- #
def summarize(text: str, max_chunks=5, chunk_tokens=800):
    tokens = tokenizer.encode(text)
    if len(tokens) <= chunk_tokens:
        summaries = summarizer(text, max_length=180, min_length=30, do_sample=False)
        return summaries[0]['summary_text']

    chunks = []
    for i in range(0, len(tokens), chunk_tokens):
        chunk_token_slice = tokens[i:i + chunk_tokens]
        chunk_text = tokenizer.decode(chunk_token_slice)
        chunks.append(chunk_text)
        if len(chunks) == max_chunks:
            break
    partials = [
        summarizer(c, max_length=140, min_length=25, do_sample=False)[0]['summary_text']
        for c in chunks
    ]
    combined = " ".join(partials)
    final = summarizer(combined, max_length=200, min_length=40, do_sample=False)[0]['summary_text']
    return final.strip()

# ---------------- Routes ---------------- #
@app.route('/', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        flash("Please sign up or log in first.")
        return redirect(url_for('signup'))

    if request.method == "POST":
        user_text = request.form.get("article", "").strip()
        if not user_text:
            flash("Please enter valid text.")
            return render_template("home.html")

        try:
            summary = summarize(user_text)
            summary_wrapped = "\n".join(textwrap.wrap(summary, 100))
            return render_template("home.html", article=user_text, summary=summary_wrapped)
        except Exception as e:
            flash(f"An error occurred during summarization: {e}")
            return render_template("home.html")

    return render_template("home.html")

# ---------------- Signup ---------------- #
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password']

        if not username or not email or not password:
            flash("All fields are required.")
            return render_template("signup.html")

        if User.query.filter_by(email=email).first():
            flash("Email already registered.")
            return render_template("signup.html")

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        session['user'] = username
        flash("Signup successful! Welcome to SummarAI.")
        return redirect(url_for('home'))

    return render_template("signup.html")

# ---------------- Logout ---------------- #
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out.")
    return redirect(url_for('signup'))

# ---------------- Init ---------------- #
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
