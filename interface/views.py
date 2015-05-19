from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    return render(request, 'interface/home.html', {})


def sign_in(request):
    if request.method == 'POST':
        return redirect('home')
    context = {}
    return render(request, 'interface/sign_in.html', context)


def sign_out(request):
    return redirect('/sign-in')


def providers(request):
    context = {
        'providers': ServiceProvider.objects.all()
    }
    return render(request, 'interface/providers.html', context)


def update_provider(request, provider_model):
    provider_model.name = request.POST['name']
    provider_model.website = request.POST['website']
    provider_model.phone_number = request.POST['phone_number']
    provider_model.address = request.POST['address']
    provider_model.hours_of_operation = request.POST['hours_of_operation']


def new_provider(request):
    if request.method == 'POST' and request.POST['name']:
        provider_model = ServiceProvider()
        update_provider(request, provider_model)
        provider_model.save()
        return redirect('providers')
    context = {'provider': request.POST}
    return render(request, 'interface/new_provider.html', context)


def provider(request, provider_id):
    provider_model = ServiceProvider.objects.get(pk=provider_id)
    if not provider_model:
        # temporary, should 404
        redirect('providers')
    context = {provider: provider_model}
    return render(request, 'interface/provider.html', context)


def edit_provider(request, provider_id):
    provider_model = ServiceProvider.objects.get(pk=provider_id)
    if not provider_model:
        # temporary, should 404
        redirect('providers')
    if request.method == 'POST':
        update_provider(request, provider_model)
        if provider_model.name:
            provider_model.save()
            return redirect('providers')
    context = {"provider": provider_model}
    return render(request, 'interface/edit_provider.html', context)


def delete_provider(request, provider_id):
    context = {}
    return render(request, 'interface/delete_provider.html', context)


def categories(request):
    context = {"categories": ServiceCategory.objects.all()}
    return render(request, 'interface/categories.html', context)


def update_category(request, category_model):
    category_model.name = request.POST['name']


def new_category(request):
    if request.method == 'POST' and request.POST['name']:
        category_model = ServiceCategory()
        update_category(request, category_model)
        category_model.save()
        return redirect('categories')
    context = {'category': request.POST}
    return render(request, 'interface/new_category.html', context)


def category(request, category_id):
    category_model = ServiceProvider.objects.get(pk=category_id)
    if not category_model:
        # temporary, should 404
        redirect('providers')
    context={"category": category_model}
    return render(request, 'interface/category.html', context)


def edit_category(request, category_id):
    category_model = ServiceCategory.objects.get(pk=category_id)
    if not category_model:
        # temporary, should 404
        redirect('providers')
    if request.method == 'POST':
        update_category(request, category_model)
        if category_model.name:
            category_model.save()
            return redirect('categories')
    context = {"category": category_model}
    return render(request, 'interface/edit_category.html', context)


def delete_category(request, category_id):
    context = {}
    return render(request, 'interface/delete_category.html', context)


def items(request):
    context = {"items": Item.objects.all()}
    return render(request, 'interface/items.html', context)


def item(request, item_id):
    context = {}
    return render(request, 'interface/item.html', context)


def update_item(request, item_model):
    item_model.name = request.POST['name']


def new_item(request):
    if request.method == 'POST' and request.POST['name']:
        item_model = Item()
        update_item(request, item_model)
        item_model.save()
        return redirect('items')
    context = {'item': request.POST}
    return render(request, 'interface/new_item.html', context)


def edit_item(request, item_id):
    item_model = Item.objects.get(pk=item_id)
    if not item_model:
        # temporary, should 404
        redirect('providers')
    if request.method == 'POST':
        update_category(request, item_model)
        if item_model.name:
            item_model.save()
            return redirect('items')
    context = {"item": item_model}
    return render(request, 'interface/edit_item.html', context)


def delete_item(request, item_id):
    context = {}
    return render(request, 'interface/delete_item.html', context)


def links(request):
    context = {}
    return render(request, 'interface/links.html', context)


def link(request, link_id):
    context = {}
    return render(request, 'interface/link.html', context)


def edit_link(request, link_id):
    context = {}
    return render(request, 'interface/edit_link.html', context)
