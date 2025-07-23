from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def gen_resume(request):
    if request.method == 'POST':
        # Static fields
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        post_applied = request.POST.get('post_applied', '')
        sex = request.POST.get('sex', '')
        dob = request.POST.get('dob', '')
        birth_place = request.POST.get('birth_place', '')
        marital_status = request.POST.get('marital_status', '')
        nationality = request.POST.get('nationality', '')
        state_origin = request.POST.get('state_origin', '')
        lga = request.POST.get('lga', '')
        phones = request.POST.get('phones', '')
        perm_address = request.POST.get('perm_address', '')
        next_kin_name = request.POST.get('next_kin_name', '')
        next_kin_phone = request.POST.get('next_kin_phone', '')
        next_kin_address = request.POST.get('next_kin_address', '')

        # Dynamic education
        institutions = request.POST.getlist('institution[]')
        dates = request.POST.getlist('date[]')
        qualifications = request.POST.getlist('qualification[]')
        education_list = zip(institutions, dates, qualifications)

        # Dynamic work experience
        orgs = request.POST.getlist('org[]')
        work_dates = request.POST.getlist('work_date[]')
        duties = request.POST.getlist('duty[]')
        work_experience = zip(orgs, work_dates, duties)

        # Dynamic certificates
        cert_names = request.POST.getlist('cert_name[]')
        cert_dates = request.POST.getlist('cert_date[]')
        certificate_list = zip(cert_names, cert_dates)

        # Dynamic research and extracurricular (can be multiple)
        research = request.POST.getlist('research[]')
        extracurricular = request.POST.getlist('extracurricular[]')

        # Referees
        referees = request.POST.getlist('referee[]')

        return render(request, 'resume.html', {
            # Personal
            'name': name,
            'email': email,
            'post_applied': post_applied,
            'sex': sex,
            'dob': dob,
            'birth_place': birth_place,
            'marital_status': marital_status,
            'nationality': nationality,
            'state_origin': state_origin,
            'lga': lga,
            'phones': phones,
            'perm_address': perm_address,
            'next_kin_name': next_kin_name,
            'next_kin_phone': next_kin_phone,
            'next_kin_address': next_kin_address,

            # Lists
            'education_list': education_list,
            'work_experience': work_experience,
            'certificate_list': certificate_list,
            'research': research,
            'extracurricular': extracurricular,
            'referees': referees,
        })

    return render(request, 'index.html')
