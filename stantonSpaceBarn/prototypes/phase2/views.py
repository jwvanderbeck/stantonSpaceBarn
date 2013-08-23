from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def show_300i(request):
	template = get_template('prototypes/phase2/sbb_300i.html')
	html = template.render(Context({}))
	return HttpResponse(html)
