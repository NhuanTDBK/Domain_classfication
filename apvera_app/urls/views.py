from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.http import HttpResponse
from LR import *
def index(request):
    template = loader.get_template('urls/search_box.html')
#    return HttpResponse("Hello, world. You're at the polls index.")
    context = {
    	"label":"File Sharing"
    }
    return HttpResponse(template.render(context, request))
classify = LR();
class AppView(TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'urls/search_box.html'
        template = loader.get_template(template_name)
        label = ""
        # if kwargs.has_key('label'):
        #     label = kwargs['label']
        label = kwargs.get('label','')
        url = kwargs.get('url','')
    #    return HttpResponse("Hello, world. You're at the polls index.")
        context = {
        	"label":label,
            "url":url
        }
        return HttpResponse(template.render(context, request))
        # first_name = request.user.first_name
        # last_name = request.user.last_name
        #
        # for app in apps:
        #     setattr(app, 'config', format_config(
        #         {
        #             'Docker Image': app.docker_image,
        #             'Ports: ': app.ports
        #         }
        #     ))
        #
        # return self.render_to_response({
        #     'fullname': full_name,
        #     'apps': apps
        # })

    def post(self, request, *args, **kwargs):
        """
        Action: create, edit, make network connect to external and delete network
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        url = request.POST.get('url')
        label = classify.predict(url)
        params = {
            'label':label,
            'url':url
        }
        return self.get(request,**params)
