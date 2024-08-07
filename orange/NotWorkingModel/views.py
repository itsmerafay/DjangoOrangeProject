import json, os
from django.urls import reverse
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.conf import settings


    

def no_model_found(request):
    if request.method == "POST":
        try:
            data = request.POST
            
            sqm = data.get("sqm")
            errors = []

            if not sqm:
                errors.append("Please fill out all the fields")
                return render(request , "HTML/NoModelFound.html", {"errors":errors})
            
            json_data = {
                "sqm":sqm
            }

            existing_data = {}

            file_path = os.path.join(settings.MEDIA_ROOT, "jsondata.json")

            try:
                with open(file_path, "r") as f:
                    existing_data = json.loads(f.read())

            except FileNotFoundError:
                pass

            except json.JSONDecodeError as e:
                errors.append(f"Error in decoding json : {str(e)}")

            existing_data["no_model_found"] = json_data        

            with open(file_path, "w") as f:
                json.dump(existing_data, f)
            
            return redirect("heating_area")
        
    
        except Exception as e:
            errors.append(f"An error occured. Please try again {str(e)}")
            return render(request, "HTML/NoModelFound.html", {"errors":errors})

    else:
        return render(request, "HTML/NoModelFound.html")
    

    

def heating_area(request):
    if request.method == "POST":
        try:
            data = request.POST
            
            area = data.get("area")
            errors = []

            if not area:
                errors.append("Please fill out all the fields")
                return render(request , "HTML/HeatingArea.html", {"errors":errors})
            
            json_data = {
                "area":area
            }

            existing_data = {}

            file_path = os.path.join(settings.MEDIA_ROOT, "jsondata.json")

            try:
                with open(file_path, "r") as f:
                    existing_data = json.loads(f.read())

            except FileNotFoundError:
                pass

            except json.JSONDecodeError as e:
                errors.append(f"Error in decoding json : {str(e)}")

            existing_data["add_heating_area"] = json_data        

            with open(file_path, "w") as f:
                json.dump(existing_data, f)
            
            return redirect("heating_area")
        
    
        except Exception as e:
            errors.append(f"An error occured. Please try again {str(e)}")
            return render(request, "HTML/HeatingArea.html", {"errors":errors})

    else:
        return render(request, "HTML/HeatingArea.html")
    


