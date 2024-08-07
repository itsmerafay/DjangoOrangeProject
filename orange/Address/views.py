import json, os
from django.urls import reverse
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.conf import settings
from WorkingModel.views import model_page_one

def address_page(request):
    if request.method == "POST":
        address = request.POST.get("address")
        errors = []
        if address:
            data = {
                "address":address
                    }
            file_path = os.path.join(settings.MEDIA_ROOT, "jsondata.json")
            with open(file_path, "w") as f:
                json.dump(data, f)
        else:
            errors.append("Please fill the field to proceed ")
            return render(request, "HTML/AddressPage.html",{"errors":errors})

        return redirect(model_page_one)
    
    else:
        return render(request, "HTML/AddressPage.html")

