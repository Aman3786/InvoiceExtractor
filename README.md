:page_facing_up: Invoice Extraction API
:pushpin: Project Overview
This is a Django-based project that allows users to upload PDF invoices and extract key details such as:
Invoice Vendor
Invoice Number
Amount
Due Date
The project uses LangChain to extract text from PDF files and LLMs (GPT-4 or OpenAI models) to analyze and extract structured invoice data.
---
:rocket: Features
User Authentication (Signup, Signin, Logout)
PDF Upload Functionality (Only PDFs allowed)
Invoice Processing using LangChain & LLM
Database Storage for Uploaded Invoices
Frontend UI for Uploading & Viewing Invoices
Uses Django Messages Framework for Alerts
---
:hammer_and_wrench: Installation & Setup
:one: Clone the Repository
git clone https://github.com/yourusername/invoice-extraction.git
cd invoice-extraction
:two: Create a Virtual Environment & Activate It
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
:three: Install Dependencies
pip install -r requirements.txt
:four: Set Up Environment Variables
Add Groq API Key in settings.py file:
GROQ_API_KEY=your_groq_api_key_here
:five: Apply Database Migrations
python manage.py makemigrations
python manage.py migrate
:six: Create Superuser
python manage.py createsuperuser
:seven: Run the Development Server
python manage.py runserver
:eight: Access the App in Your Browser
http://127.0.0.1:8000/
---
:open_file_folder: API Endpoints
---
:scroll: How It Works
:one: User logs in and uploads a PDF invoice. :two: File is saved in the database (media/invoices/). :three: LangChain extracts text from the PDF. :four: LLAMA 3.3 model extracts invoice details. :five: Extracted data is displayed to the user.
---
:hammer_and_wrench: Technologies Used
Django (Python Web Framework)
LangChain (PDF Processing)
GROQ LLM API (LLM for Invoice Data Extraction)
SQLite (Database)
Bootstrap 5 (Frontend Styling)
Django Messages Framework (Alerts & Notifications)

---
:envelope_with_arrow: Contact
For questions or suggestions, reach out at: :e-mail: Email: amaanshk3786@gmail.com GitHub: Aman3786