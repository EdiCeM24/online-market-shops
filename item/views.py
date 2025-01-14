from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . models import Item, Category 
from .forms import NewItemForm, EditItemForm
from django.db.models import Q     # for query or search.


@login_required
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category_id', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name=query) | Q(description=query)) # name_icontains is replaced with name.
    
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
        })



def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)    # we passed in the parameters in order to allow users to upload files on request(request.POST, request.FILES).

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
       form = NewItemForm()

    return render(request, 'item/form.html', {
        "form": form,
        "title": 'New item',
    })    


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)    # we passed in the parameters in order to allow users to upload files on request(request.POST, request.FILES).

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
       form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        "form": form,
        "title": 'Edit item',
    })    


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


