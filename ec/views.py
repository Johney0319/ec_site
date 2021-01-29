from django.db.models import Max, Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic

from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .forms import JacketsForm
from .models import Jackets


# Create your views here.

# メイン画面用
class IndexView(TemplateView):
    template_name = 'index.html'


# 商品登録画面用
def product_entry(request):
    form = JacketsForm(request.POST, request.FILES)

    if form.is_valid():
        model = Jackets()
        jacket_id_max = Jackets.objects.all().aggregate(Max('jacket_id'))

        jacket_id_max_list = []
        for v in jacket_id_max.values():
            jacket_id_max_list.append(v)

        if jacket_id_max_list[0] is None:
            jacket_id_max_list[0] = 0

        model.jacket_name = form.cleaned_data['jacket_name']
        model.jacket_price = form.cleaned_data['jacket_price']
        model.jacket_size = form.cleaned_data['jacket_size']
        model.jacket_sex = form.cleaned_data['jacket_sex']
        model.jacket_bland = form.cleaned_data['jacket_bland']
        model.jacket_image = form.cleaned_data['jacket_image']

        Jackets.objects.create(
            jacket_id=int(jacket_id_max_list[0]) + 1,
            jacket_name=model.jacket_name,
            jacket_price=round(int(model.jacket_price) * 1.10),
            jacket_size=model.jacket_size,
            jacket_sex=model.jacket_sex,
            jacket_bland=model.jacket_bland,
            jacket_image=model.jacket_image,
        )
        return redirect('ec:product_list')

    return render(request, 'product_entry.html', {'form': form})


# 商品一覧画面用
class ProductListView(ListView):
    model = Jackets
    template_name = "product_list.html"
    context_object_name = 'product_list'

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            product_list = Jackets.objects.filter(
                Q(jacket_name__icontains=q_word))
        else:
            product_list = Jackets.objects.all()

            print(product_list)
        return product_list


# 商品削除用
def product_delete(request):

    if request.method == 'POST':
        # Jackets.objects.all().delete()
        jacket_id = request.POST.get('jacket_id')
        Jackets.objects.filter(jacket_id=request.POST.get('jacket_id')).delete()
        # Management.objects.filter(id=request.POST.get('id')).delete()

        return redirect('ec:product_list')

    return render(request, 'product_delete.html')
