from django.shortcuts import render, request
from models import *

def get_new_role_data(request):
    if request.session['failed_role_creation']:
       request.session.pop['failed_role_creation']
    else:
        request.session.pop['errors']    
    return ("template")

def create_new_role(request):
    response_from_model = RoleManager.create_new_role(request)
    # Successful creation
    if response_from_model['status']:
        request.sessions['status'] = True
        request.sessions['new_role_added'] = response_from_model['new_role']
        if request.session['errors']:
            request.session.pop['errors']
        return ("template")
    else:
        request.session['status'] = False
        request.session['errors'] = response_from_model['error_list']   
        request.session['failed_role_creation'] = True 
        return get_new_role_data(request)