
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Book


# Create your views here.
def home(request):
	# collect every info from Book db
	book_list = Book.objects.order_by('-pub_date')

	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'book_list': book_list,
		})


	# call index.html
	return HttpResponse(template.render(context))