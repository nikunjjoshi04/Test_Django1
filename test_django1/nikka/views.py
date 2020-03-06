from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST, condition
from .models import Entry, Author, Blog
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User


# Create your views here.


@require_http_methods(['GET'])
def first_name(request):
    print('First Name...')
    return redirect('nikka:full_name')


# @login_required(login_url='accounts:login')
# @permission_required('nikka.view_entry', raise_exception=True)
def last_name(request):
    print('Last Name...')
    return redirect('nikka:full_name')


def full_name(request):
    print('Full Name...')
    entrys = get_list_or_404(Entry)
    # entrys = get_object_or_404(Entry)

    print(entrys)
    return render(request, 'nikka/full_name.html', {"entrys": entrys})


# @method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class EntryDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = 'nikka.view_entry'
    login_url = 'accounts:login'
    permission_denied_message = 'Not Allow...!!!'
    model = Entry
    template_name = 'nikka/entry_details.html'


class AuthorDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = 'nikka.view_entry'
    login_url = 'accounts:login'
    permission_denied_message = 'Not Allow...!!!'
    model = Author
    template_name = 'nikka/author_details.html'


class BlogDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = 'nikka.view_entry'
    login_url = 'accounts:login'
    permission_denied_message = 'Not Allow...!!!'
    model = Blog
    template_name = 'nikka/blog_details.html'
