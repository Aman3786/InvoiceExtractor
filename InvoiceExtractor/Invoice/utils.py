import json
from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from django.conf import settings


GROQ_API_KEY = settings.GROQ_API_KEY
GROQ_CHAT_MODEL = settings.GROQ_CHAT_MODEL

# Extract text from a PDF file using LangChain.
def extract_text_from_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    return "\n".join(page.page_content for page in pages)


# Call an LLM to extract invoice fields.
def extract_invoice_details(text):
    prompt = PromptTemplate(
        input_variables=["text"],
        template=(
            """
            Extract the following fields from the Invoice text below:\n"
            Invoice date, Invoice Number, Amount, Due Date.\n
            All Dates should be in YYYY-MM-DD format\n
            If any of the field is missing then put Not Found for that specific field\n
            Return the result as JSON with keys 'invoice_date', 'invoice_number', 'amount', 'due_date'\n
            Exclude ```json``` from output\n\n
            Invoice Text:\n{text}
            
            No Preamble 
            """
        )
    )
    model = ChatGroq(api_key=GROQ_API_KEY, model=GROQ_CHAT_MODEL)
    chain = prompt | model
    response = chain.invoke({'text':text})
    try:
        return json.loads(response.content)
    except json.JSONDecodeError as e:
        return {}