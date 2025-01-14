#--coding: utf8--
from django.shortcuts import render
from templated_docs import fill_template
from templated_docs.http import FileResponse
from invoices.forms import InvoiceForm


def invoice_view(request):
    form = InvoiceForm(request.POST or None)

    if form.is_valid():
        doctype = form.cleaned_data['format']
        filename = fill_template(
            'invoices/invoice.odt', form.cleaned_data,
            output_format=doctype)
        visible_filename = 'invoice.{}'.format(doctype)

        return FileResponse(filename, visible_filename)
    else:
        return render(request, 'invoices/form.html', {'form': form})
