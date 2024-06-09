from django.shortcuts import render, redirect
from django.http import JsonResponse
import os
from .models import File
from django.contrib.auth.decorators import login_required
import csv
from django.contrib.auth import logout as auth_logout

#inbuild login reguired ka decorator use kiya gaya hai
@login_required
def index(request):
    if request.method == 'POST': #method post hai ya nahi request ka woh check karega
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file uploaded'})
        #agar bina kisi file k upload kiya gaya toh error msg throw hoga
        file = request.FILES['file']
        # file naam k variable me store kiya jayega uploaded file ko


        #file ko ek temporary location pe save kiya jayega media directory me usi naam se jo naam se upload hui 
        temp_path = os.path.join('media', file.name)

        '''
        temporary file ko open karke usme file save karengey usme chunks me data ko write karengey jis memory 
        me eksath sath load karne ki zarurat nahi padegi
        '''
        with open(temp_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        #
        try:
            #csv file kko open karengey
            with open(temp_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile) #ek reader object banaye hai jo csv file k har row ko dict k taur pe read krega

                #yeh loop har line k liye csv file ka header key hoga or un sabke values ko ek ek karke columns me se nikalaega jaayega
                for row in reader:
                    # id = row.get('id')
                    emp = row.get('emp')
                    name = row.get('name')
                    domain = row.get('domain')
                    year_founded = row.get('year_founded')
                    industry = row.get('industry')
                    size_range = row.get('size_range')
                    locality = row.get('locality')
                    country = row.get('country')
                    linkedin_url = row.get('linkedin_url')
                    current_employee_estimate = row.get('current_employee_estimate')
                    total_employee_estimate = row.get('total_employee_estimate')


            # filhal neechey ka code comment kardiya gaya hai qki sample file bahot saarey blank space they
                    # Validate karega extracted data ko 
                    # if not all([emp, name, domain, year_founded, industry, size_range, locality, country, linkedin_url, current_employee_estimate, total_employee_estimate]):
                    #     return JsonResponse({'Uploaded': 'But Missing fields in File'})

                    # ab company ko file table ka object banaye or usme uper se aaye har data ko file model me save karta jayega
                    company = File(
                        # id=id,
                        emp=emp,
                        name=name,
                        domain=domain,
                        year_founded=year_founded,
                        industry=industry,
                        size_range=size_range,
                        locality=locality,
                        country=country,
                        linkedin_url=linkedin_url,
                        current_employee_estimate=current_employee_estimate,
                        total_employee_estimate=total_employee_estimate
                    )
                    company.save() #model me data save hoga

            return render(request, 'file_upload/index.html') #usi page pe dubara aajayega ek baar process complete hogaya toh or js k madad se usko alert msg dedengey

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return render(request, 'file_upload/index.html')

#logout karne k liye inbuilt logout ka use kiya gaya hai
@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('account_login')