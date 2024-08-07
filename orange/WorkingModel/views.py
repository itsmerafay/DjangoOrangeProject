import json, os
from django.urls import reverse
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.conf import settings

def model_page_one(request):
    if request.method == "POST":
        return render(request,"HTML/DeleteModelPage.html")
    else:
        return render(request, "HTML/ModelPageOne.html")
    

def delete_model_page(request):
    if request.method == "POST":
        return render(request, "HTML/DeleteModelPage.html")
    else:
        return render(request, "HTML/DeleteModelPage.html")


def customize_window_planner(request):
    if request.method == "POST":
        return redirect(general_info)
    else:
        return render(request, "HTML/WindowSizePlanner.html")


def general_info(request):
    if request.method == "POST":
        try:
            data = request.POST
            building_type = data.get("building_type")
            year_of_installation = data.get("year_of_installation")
            room_height_feet = data.get("room_height_feet")

            errors = []

            if not all([building_type, year_of_installation, room_height_feet]):
                errors.append("All fields are required")
                return render(request, "HTML/GeneralInfoPage.html",{"errors":errors})
            
            json_data = {
                "building_type":building_type,
                "year_of_installation":year_of_installation,
                "room_height_feet":room_height_feet
            }

            file_path = os.path.join(settings.MEDIA_ROOT, "jsondata.json")
            existing_data = {}
            try:    
                with open(file_path, "r") as f:
                    existing_data = json.load(f)
            except FileNotFoundError:
                pass
            except json.JSONDecodeError as e:
                errors.append(f"Error in decoding json : {str(e)}")


            existing_data["general_info"] = json_data

            with open(file_path, "w") as f:
                json.dump(existing_data, f)
            
            return redirect("expansion_and_cultivation")


        except Exception as e:
            errors.append(f"An error occured . Please try again : {str(e)}")
            return render(request, "HTML/GeneralInfoPage.html", {"errors":errors})
    else:
        return render(request, "HTML/GeneralInfoPage.html")


def expansion_and_cultivation(request):
    if request.method == "POST":
        try:
            data = request.POST
            basement_cellar = data.get("basement_cellar")
            roof = data.get("roof")
            errors = []

            if not all([basement_cellar, roof]):
                errors.append("Please fill out all the fields")
                return render(request , "HTML/Expansion&CultivationPage.html", {"errors":errors})
            
            json_data = {
                "basement_cellar":basement_cellar,
                "roof":roof
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

            existing_data["expansion_and_cultivation"] = json_data        

            with open(file_path, "w") as f:
                json.dump(existing_data, f)
            
            return redirect("thermal_cover")
        
    
        except Exception as e:
            errors.append(f"An error occured. Please try again {str(e)}")
            return render(request, "HTML/Expansion&CultivationPage.html", {"errors":errors})

    else:
        return render(request, "HTML/Expansion&CultivationPage.html")


def thermal_cover(request):
    if request.method == "POST":
        redirect("expansion_and_cultivation")

    else:
        return render(request, "HTML/ThermalCoverPage.html")