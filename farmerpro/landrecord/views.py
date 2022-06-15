from dataclasses import fields
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import LandRec
from django.urls import reverse_lazy

# Create your views here.
class ListLand(ListView):
    model = LandRec
    fields = "__all__"
    template_name = 'landrecord/landrec_list.html'
    paginate_by= 2

class CreateLand(CreateView):
    model = LandRec
    fields = "__all__"
    template_name = 'landrecord/landrec_form.html'
    success_url = reverse_lazy('list_url')

class DeleteLand(DeleteView):
    model = LandRec
    fields = "__all__"
    success_url = reverse_lazy('list_url')

class UpdateLand(UpdateView):
    model = LandRec
    fields = "__all__"
    success_url = reverse_lazy('list_url')


from django.http import FileResponse
from reportlab.pdfgen import canvas
import io
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def GenPDF(request):
    buf = io.BytesIO()
    c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont('Helvetica', 14)
    lines =[]
    farm = LandRec.objects.all()

    for f in farm:
        lines.append(f.farmer_name)
        lines.append(f.survey_number)
        lines.append(f.village)
        lines.append(f.farm_area)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='xyz.pdf')


def IndPDF(request,pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont('Helvetica', 14)
    farm = LandRec.objects.get(id=pk)
    nm = farm.farmer_name

    b = f"Name : {farm.farmer_name}, Survey Number : {farm.survey_number}, Village : {farm.village}, Farm Area : {farm.farm_area}"

    textob.textLine(b)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=f'{nm}.pdf')