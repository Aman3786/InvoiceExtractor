## :page_facing_up: Invoice-Extractor

### :pushpin: Project Overview

#### This is a Django-based project that allows users to upload PDF invoices and extract key details such as:
- Invoice Date
- Invoice Number
- Amount
- Due Date

#### The project uses LangChain to extract text from PDF files and Langchain+Groq LLama-3.3-70B Model to analyze and extract structured invoice data.
---

### :rocket: Features
- User Authentication (Signup, Signin, Logout)
- PDF Upload Functionality (Only PDFs allowed)
- Invoice Processing using LangChain & Groq LLama-3.3-70B Model
- Database Storage for Uploaded Invoices 
- Frontend UI for Uploading & Viewing Invoices using Bootstrap5
- Uses Django Messages Framework for Alerts
---

### :hammer_and_wrench: Installation & Setup
:one: Clone the Repository
```bash
git clone https://github.com/Aman3786/InvoiceExtractor.git
cd InvoiceExtractor
```
:two: Create a Virtual Environment & Activate It (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
:three: Install Dependencies
```bash
pip install -r requirements.txt
```
:four: Set Up Environment Variables
#### Add Djnago Secret Key and Groq API Key in settings.py file:
```bash
SECRET_KEY='Your Secret Key'
GROQ_API_KEY="Your GROQ API key"
```
:five: Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
:six: Create Superuser
```bash
python manage.py createsuperuser
```
:seven: Run the Development Server
```bash
python manage.py runserver
```
:eight: Access the App in Your Browser
```bash
http://127.0.0.1:8000/
```
---

### :scroll: How It Works

:one: User signup/Signin and uploads a PDF invoice.

:two: File is saved inside the database.

:three: LangChain's Document Loader(Pypdfloader) extracts text from the PDF.

:four: Groq's LLAMA-3.3-70B model extracts invoice details.

:five: Extracted data is saved inside the database and displayed to the user.

---
### :hammer_and_wrench: Technologies Used
- Python (Core programming language)
- Django (Python Web Framework)
- LangChain (PDF Processing & Groq LLM wrapper)
- GROQ (LLama-3.3-70B model for Invoice Data Extraction)-
- SQLite (Database)-
- Bootstrap 5 (Frontend)
- Django Messages Framework (Alerts & Notifications)

---
### :envelope_with_arrow: Contact

For questions or suggestions, reach out at:

:mailbox_with_mail: Email: amaanshk3786@gmail.com

Github: [Aman3786](https://github.com/Aman3786)
