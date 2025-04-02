from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Invoice
from .utils import extract_text_from_pdf, extract_invoice_details


def invoice(request):
    if request.method == 'POST' and request.user and request.user.is_authenticated:
        if 'invoice_file' not in request.FILES:
            messages.error(request, 'No file uploaded.')
            return redirect('invoice_upload')
        
        invoice_file = request.FILES['invoice_file']
        
        # Restrict to PDF files only
        if not invoice_file.name.lower().endswith('.pdf'):
            messages.error(request, 'Only PDF files are allowed.')
            return redirect('invoice_upload')
        
        # Save file to the database
        invoice_instance = Invoice.objects.create(user=request.user, file=invoice_file)
        pdf_path = invoice_instance.file.path
        
        try:
            # Extract text using LangChain
            text = extract_text_from_pdf(pdf_path)
        except Exception as e:
            messages.error(request, f'Error processing PDF: {e}')
            return redirect('invoice_upload')
        
        # Call LLM to extract invoice details
        extracted_data = extract_invoice_details(text)
        
        invoice_instance.invoice_date = extracted_data.get('invoice_date')
        invoice_instance.invoice_number = extracted_data.get('invoice_number')
        invoice_instance.amount = extracted_data.get('amount')
        invoice_instance.due_date = extracted_data.get('due_date')
        invoice_instance.save()
        
        messages.success(request, 'Invoice uploaded and processed successfully.')
        return render(request, 'home.html', {'invoice_result': invoice_instance})
    
    return render(request, 'home.html')