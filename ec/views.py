import datetime
import math
import re
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .forms import JacketsForm, ShirtsForm, PantsForm, ShoesForm, CartListForm, SignUpForm
from .models import Jackets, Shirts, Pants, Shoes, CustomUser, Cart, CartItem, PurchaseHistory

# メイン画面用
class IndexView(TemplateView):
    template_name = 'index.html'

# ユーザー新規登録用
class UserCreateView(CreateView):
    template_name = 'user_entry.html'
    form_class = SignUpForm

    def form_valid(self, form_class):
        entry_user = CustomUser(username=self.request.POST.get('username'))
        entry_password = CustomUser(username=self.request.POST.get('password'))

        # ユーザー名が半角アルファベット、半角数字、@/./+/-/_ で150文字以下の条件に合わない場合
        if int(len(str(entry_user))) > 150 or bool(re.search(r'[a-zA-Z0-9]', str(entry_user))) == False or ('@' not in str(entry_user) and '.' not in str(entry_user) and '+' not in str(entry_user) and '-' not in str(entry_user) and '_' not in str(entry_user)):
            username_error = 'ユーザー名は半角アルファベット、半角数字、@/./+/-/_ で 150文字以下で入力してください。'
            params = {
                'username_error': username_error,
                'form': form_class
            }
            return render(self.request, 'user_entry.html', params)

        # パスワードが8文字以上で数字だけではない条件に合わない場合
        if int(len(str(entry_password))) < 8 or str(entry_password).isdecimal() == True:
            password_error = 'パスワードは 8文字以上で入力してください。' \
                             '数字だけで入力しないでください。'
            params = {
                'password_error': password_error,
                'form': form_class
            }
            return render(self.request, 'user_entry.html', params)

        entry_user.set_password(self.request.POST.get('password'))
        entry_user.save()

        return redirect('ec:index')

    success_url = reverse_lazy('ec:index')

# ログイン用
@login_required
def login_success(request):

    return render(request, 'login_success.html')

# カート機能用 (一覧表示)
class CartListView(ListView):
    model = Cart
    template_name = "cart_list.html"
    context_object_name = 'cart_list'

    def get_context_data(self, **kwargs):
        cart_all = []
        cartItem_list = super(CartListView, self).get_context_data(**kwargs)

        for cart in CartItem.objects.all():
            if cart.cart.cart_id == str(self.request.user):
                cart_all.append(cart)

        if len(cart_all) == 0:
            cart_all = None

        cartItem_list.update({
            'cartItem_list': cart_all
        })

        return cartItem_list

    def get_queryset(self):
        return Cart.objects.all()

# カート機能用 (削除)
def delete_cart(request, id):
    cart_list_info = CartItem.objects.get(id=id)

    cart_list_info.delete()

    return redirect('ec:cart_list')

# カート機能用 (追加)
@login_required
def add_cart(request, id):
    model = Cart()
    jackets = None
    shirts = None
    pants = None
    shoes = None

    now_date = datetime.datetime.now()
    pre_path = request.get_full_path

    if 'jackets' in str(pre_path):
        # カートへ該当商品を追加
        jackets = get_object_or_404(Jackets, id=id)
        jackets.save()

        # カート内に該当商品が存在しており、かつ、在庫数-購入個数 >= 1 であれば、購入個数を1増やす
        cart_product = CartItem.objects.all()
        for i in range(len(cart_product)):
            if cart_product[i].jackets is not None:
                if cart_product[i].jackets.jacket_id == jackets.jacket_id and int(jackets.jacket_stock) - int(cart_product[i].quantity) >= 1:
                    cart_jacket_duplicate = get_object_or_404(CartItem, jackets=jackets)
                    cart_jacket_duplicate_quantity = int(cart_jacket_duplicate.quantity) + 1
                    cart_jacket_duplicate.quantity = cart_jacket_duplicate_quantity

                    cart_jacket_duplicate.save()

                    return redirect('ec:cart_list')

    elif 'shirts' in str(pre_path):
        shirts = get_object_or_404(Shirts, id=id)
        shirts.save()

        # カート内に該当商品が存在しており、かつ、在庫数-購入個数 >= 1 であれば、購入個数を1増やす
        cart_product = CartItem.objects.all()
        for i in range(len(cart_product)):
            if cart_product[i].shirts is not None:
                if cart_product[i].shirts.shirt_id == shirts.shirt_id and int(shirts.shirt_stock) - int(cart_product[i].quantity) >= 1:
                    cart_shirt_duplicate = get_object_or_404(CartItem, shirts=shirts)
                    cart_shirt_duplicate_quantity = int(cart_shirt_duplicate.quantity) + 1
                    cart_shirt_duplicate.quantity = cart_shirt_duplicate_quantity

                    cart_shirt_duplicate.save()

                    return redirect('ec:cart_list')

    elif 'pants' in str(pre_path):
        pants = get_object_or_404(Pants, id=id)
        pants.save()

        # カート内に該当商品が存在しており、かつ、在庫数-購入個数 >= 1 であれば、購入個数を1増やす
        cart_product = CartItem.objects.all()
        for i in range(len(cart_product)):
            if cart_product[i].pants is not None:
                if cart_product[i].pants.pant_id == pants.pant_id and int(pants.pant_stock) - int(cart_product[i].quantity) >= 1:
                    cart_pant_duplicate = get_object_or_404(CartItem, pants=pants)
                    cart_pant_duplicate_quantity = int(cart_pant_duplicate.quantity) + 1
                    cart_pant_duplicate.quantity = cart_pant_duplicate_quantity

                    cart_pant_duplicate.save()

                    return redirect('ec:cart_list')

    elif 'shoes' in str(pre_path):
        shoes = get_object_or_404(Shoes, id=id)
        shoes.save()

        # カート内に該当商品が存在しており、かつ、在庫数-購入個数 >= 1 であれば、購入個数を1増やす
        cart_product = CartItem.objects.all()
        for i in range(len(cart_product)):
            if cart_product[i].shoes is not None:
                if cart_product[i].shoes.shoe_id == shoes.shoe_id and int(shoes.shoe_stock) - int(cart_product[i].quantity) >= 1:
                    cart_shoe_duplicate = get_object_or_404(CartItem, shoes=shoes)
                    cart_shoe_duplicate_quantity = int(cart_shoe_duplicate.quantity) + 1
                    cart_shoe_duplicate.quantity = cart_shoe_duplicate_quantity

                    cart_shoe_duplicate.save()

                    return redirect('ec:cart_list')

    cart = Cart.objects.create(
        cart_id=request.user,
        date_added=now_date
    )

    CartItem.objects.create(
        jackets=jackets,
        shirts=shirts,
        pants=pants,
        shoes=shoes,
        quantity=1,
        cart=cart
    )

    return redirect('ec:cart_list')

# カート機能用 (商品個数変更)
def update_cart(request, id):
    cart_list_form = CartListForm(request.POST)
    cart_list_info = CartItem.objects.get(id=id)

    if cart_list_info.jackets is not None:
        if cart_list_form.is_valid():
            jackets_list_info = get_object_or_404(Jackets, jacket_id=cart_list_info.jackets.jacket_id)

            # 変更個数が在庫数を上回ったら何も処理せずカート一覧画面にリダイレクト
            if int(jackets_list_info.jacket_stock) - int(cart_list_form.cleaned_data['purchase_num']) < 0:

                return redirect('ec:cart_list')

            # 変更個数が在庫数以下だったら購入個数を変更
            else:
                #jackets_list_info.jacket_stock = int(jackets_list_info.jacket_stock) + int(cart_list_info.quantity) - int(cart_list_form.cleaned_data['purchase_num'])
                cart_list_info.quantity = cart_list_form.cleaned_data['purchase_num']

                cart_list_info.save()
                #jackets_list_info.save()

                return redirect('ec:cart_list')

    elif cart_list_info.shirts is not None:
        if cart_list_form.is_valid():
            shirts_list_info = get_object_or_404(Shirts, shirt_id=cart_list_info.shirts.shirt_id)

            # 変更個数が在庫数を上回ったら何も処理せずカート一覧画面にリダイレクト
            if int(shirts_list_info.shirt_stock) - int(cart_list_form.cleaned_data['purchase_num']) < 0:

                return redirect('ec:cart_list')

            # 変更個数が在庫数以下だったら購入個数を変更
            else:
                #shirts_list_info.shirt_stock = int(shirts_list_info.shirt_stock) + int(cart_list_info.quantity) - int(cart_list_form.cleaned_data['purchase_num'])
                cart_list_info.quantity = cart_list_form.cleaned_data['purchase_num']

                cart_list_info.save()
                #shirts_list_info.save()

                return redirect('ec:cart_list')

    elif cart_list_info.pants is not None:
        if cart_list_form.is_valid():
            pants_list_info = get_object_or_404(Pants, pant_id=cart_list_info.pants.pant_id)

            # 変更個数が在庫数を上回ったら何も処理せずカート一覧画面にリダイレクト
            if int(pants_list_info.pant_stock) - int(cart_list_form.cleaned_data['purchase_num']) < 0:

                return redirect('ec:cart_list')

            # 変更個数が在庫数以下だったら購入個数を変更
            else:
                #pants_list_info.pant_stock = int(pants_list_info.pant_stock) + int(cart_list_info.quantity) - int(cart_list_form.cleaned_data['purchase_num'])
                cart_list_info.quantity = cart_list_form.cleaned_data['purchase_num']

                cart_list_info.save()
                #pants_list_info.save()

                return redirect('ec:cart_list')

    elif cart_list_info.shoes is not None:
        if cart_list_form.is_valid():
            shoes_list_info = get_object_or_404(Shoes, shoe_id=cart_list_info.shoes.shoe_id)

            # 変更個数が在庫数を上回ったら何も処理せずカート一覧画面にリダイレクト
            if int(shoes_list_info.shoe_stock) - int(cart_list_form.cleaned_data['purchase_num']) < 0:

                return redirect('ec:cart_list')

            # 変更個数が在庫数以下だったら購入個数を変更
            else:
                #shoes_list_info.shoe_stock = int(shoes_list_info.shoe_stock) + int(cart_list_info.quantity) - int(cart_list_form.cleaned_data['purchase_num'])
                cart_list_info.quantity = cart_list_form.cleaned_data['purchase_num']

                cart_list_info.save()
                #shoes_list_info.save()

                return redirect('ec:cart_list')

    params = {
        'cart_list_form': cart_list_form,
    }

    return render(request, 'cart_list.html', params)

# 購入確認機能用
def purchase_confirm(request):
    cart_all = CartItem.objects.all()
    purchase_price_sum = []

    for cart in cart_all:
        if cart.cart.cart_id == str(request.user):
            if cart.jackets is not None:
                # 購入価格合計
                cart_jackets_sum = int(cart.jackets.jacket_price) * int(cart.quantity)
                purchase_price_sum.append(cart_jackets_sum)

            elif cart.shirts is not None:
                # 購入価格合計
                cart_shirts_sum = int(cart.shirts.shirt_price) * int(cart.quantity)
                purchase_price_sum.append(cart_shirts_sum)

            elif cart.pants is not None:
                # 購入価格合計
                cart_pants_sum = int(cart.pants.pant_price) * int(cart.quantity)
                purchase_price_sum.append(cart_pants_sum)

            elif cart.shoes is not None:
                # 購入価格合計
                cart_shoes_sum = int(cart.shoes.shoe_price) * int(cart.quantity)
                purchase_price_sum.append(cart_shoes_sum)

    params = {
        'purchase_price_sum': sum(purchase_price_sum),
        'purchase_price_sum_tax': math.floor(sum(purchase_price_sum) * 0.1),
        'cart_all': zip(cart_all, purchase_price_sum),
    }

    return render(request, 'purchase_confirm.html', params)

# 購入機能用
@login_required
def purchase(request):
    cart_all = CartItem.objects.all()
    date_now = datetime.datetime.now()
    purchase_price_sum = []

    for cart in cart_all:
        if cart.cart.cart_id == str(request.user):
            if cart.jackets is not None:
                # 購入価格合計
                cart_jackets_sum = int(cart.jackets.jacket_price) * int(cart.quantity)
                purchase_price_sum.append(cart_jackets_sum)

                # 購入対象商品の在庫の再計算
                jackets = get_object_or_404(Jackets, jacket_id=cart.jackets.jacket_id)
                jackets.jacket_stock = int(jackets.jacket_stock) - int(cart.quantity)
                jackets.save()

            elif cart.shirts is not None:
                # 購入価格合計
                cart_shirts_sum = int(cart.shirts.shirt_price) * int(cart.quantity)
                purchase_price_sum.append(cart_shirts_sum)

                # 購入対象商品の在庫の再計算
                shirts = get_object_or_404(Shirts, shirt_id=cart.shirts.shirt_id)
                shirts.shirt_stock = int(shirts.shirt_stock) - int(cart.quantity)
                shirts.save()

            elif cart.pants is not None:
                # 購入価格合計
                cart_pants_sum = int(cart.pants.pant_price) * int(cart.quantity)
                purchase_price_sum.append(cart_pants_sum)

                # 購入対象商品の在庫の再計算
                pants = get_object_or_404(Pants, pant_id=cart.pants.pant_id)
                pants.pant_stock = int(pants.pant_stock) - int(cart.quantity)
                pants.save()

            elif cart.shoes is not None:
                # 購入価格合計
                cart_shoes_sum = int(cart.shoes.shoe_price) * int(cart.quantity)
                purchase_price_sum.append(cart_shoes_sum)

                # 購入対象商品の在庫の再計算
                shoes = get_object_or_404(Shoes, shoe_id=cart.shoes.shoe_id)
                shoes.shoe_stock = int(shoes.shoe_stock) - int(cart.quantity)
                shoes.save()

    for item in cart_all:
        purchase_user = item.cart.cart_id
        quantity = item.quantity

        PurchaseHistory.objects.create(
            purchase_user=purchase_user,
            date_added=date_now,
            quantity=quantity,
            jackets_history=item.jackets,
            shirts_history=item.shirts,
            pants_history=item.pants,
            shoes_history=item.shoes
        )

    Cart.objects.all().delete()
    CartItem.objects.all().delete()

    params = {
        'purchase_price_sum': sum(purchase_price_sum),
        'purchase_price_sum_tax': math.floor(sum(purchase_price_sum) * 0.1),
        'cart_all': zip(cart_all, purchase_price_sum),
    }

    return render(request, 'purchase_success.html', params)

# 購入履歴機能用
@login_required
def purchase_history(request):
    purchase_history_all = PurchaseHistory.objects.all()
    purchase_history_user = []

    for history in purchase_history_all:
        if history.purchase_user == str(request.user):
            purchase_history_user.append(history)

    params = {
        'purchase_history_user': purchase_history_user,
        'purchase_history_user_len': len(purchase_history_user)
    }

    return render(request, 'purchase_history.html', params)

# 商品登録画面用
@login_required
def product_entry(request):
    jackets_form = JacketsForm(request.POST, request.FILES)
    shirts_form = ShirtsForm(request.POST, request.FILES)
    pants_form = PantsForm(request.POST, request.FILES)
    shoes_form = ShoesForm(request.POST, request.FILES)

    if jackets_form.is_valid():
        model = Jackets()
        jacket_id_max = Jackets.objects.all().aggregate(Max('jacket_id'))

        jacket_id_max_list = []
        for v in jacket_id_max.values():
            jacket_id_max_list.append(v)

        if jacket_id_max_list[0] is None:
            jacket_id_max_list[0] = 100

        model.jacket_name = jackets_form.cleaned_data['jacket_name']
        model.jacket_price = jackets_form.cleaned_data['jacket_price']
        model.jacket_size = jackets_form.cleaned_data['jacket_size']
        model.jacket_sex = jackets_form.cleaned_data['jacket_sex']
        model.jacket_bland = jackets_form.cleaned_data['jacket_bland']
        model.jacket_stock = jackets_form.cleaned_data['jacket_stock']
        #model.jacket_image = jackets_form.cleaned_data['jacket_image']

        model.jacket_image = 'static/images/サンフルシャツ1.jpg'

        Jackets.objects.create(
            jacket_id=int(jacket_id_max_list[0]) + 1,
            jacket_name=model.jacket_name,
            jacket_price=round(int(model.jacket_price) * 1.10),
            jacket_size=model.jacket_size,
            jacket_sex=model.jacket_sex,
            jacket_bland=model.jacket_bland,
            jacket_stock=model.jacket_stock,
            jacket_image=model.jacket_image,
        )
        return redirect('ec:jackets_list')

    elif shirts_form.is_valid():
        model = Shirts()
        shirt_id_max = Shirts.objects.all().aggregate(Max('shirt_id'))

        shirt_id_max_list = []
        for v in shirt_id_max.values():
            shirt_id_max_list.append(v)

        if shirt_id_max_list[0] is None:
            shirt_id_max_list[0] = 200

        model.shirt_name = shirts_form.cleaned_data['shirt_name']
        model.shirt_price = shirts_form.cleaned_data['shirt_price']
        model.shirt_size = shirts_form.cleaned_data['shirt_size']
        model.shirt_sex = shirts_form.cleaned_data['shirt_sex']
        model.shirt_bland = shirts_form.cleaned_data['shirt_bland']
        model.shirt_stock = shirts_form.cleaned_data['shirt_stock']
        model.shirt_image = shirts_form.cleaned_data['shirt_image']

        Shirts.objects.create(
            shirt_id=int(shirt_id_max_list[0]) + 1,
            shirt_name=model.shirt_name,
            shirt_price=round(int(model.shirt_price) * 1.10),
            shirt_size=model.shirt_size,
            shirt_sex=model.shirt_sex,
            shirt_bland=model.shirt_bland,
            shirt_stock=model.shirt_stock,
            shirt_image=model.shirt_image,
        )
        return redirect('ec:shirts_list')

    elif pants_form.is_valid():
        model = Pants()
        pant_id_max = Pants.objects.all().aggregate(Max('pant_id'))

        pant_id_max_list = []
        for v in pant_id_max.values():
            pant_id_max_list.append(v)

        if pant_id_max_list[0] is None:
            pant_id_max_list[0] = 300

        model.pant_name = pants_form.cleaned_data['pant_name']
        model.pant_price = pants_form.cleaned_data['pant_price']
        model.pant_size = pants_form.cleaned_data['pant_size']
        model.pant_sex = pants_form.cleaned_data['pant_sex']
        model.pant_bland = pants_form.cleaned_data['pant_bland']
        model.pant_stock = pants_form.cleaned_data['pant_stock']
        model.pant_image = pants_form.cleaned_data['pant_image']

        Pants.objects.create(
            pant_id=int(pant_id_max_list[0]) + 1,
            pant_name=model.pant_name,
            pant_price=round(int(model.pant_price) * 1.10),
            pant_size=model.pant_size,
            pant_sex=model.pant_sex,
            pant_bland=model.pant_bland,
            pant_stock=model.pant_stock,
            pant_image=model.pant_image,
        )
        return redirect('ec:pants_list')

    elif shoes_form.is_valid():
        model = Shoes()
        shoe_id_max = Shoes.objects.all().aggregate(Max('shoe_id'))

        shoe_id_max_list = []
        for v in shoe_id_max.values():
            shoe_id_max_list.append(v)

        if shoe_id_max_list[0] is None:
            shoe_id_max_list[0] = 400

        model.shoe_name = shoes_form.cleaned_data['shoe_name']
        model.shoe_price = shoes_form.cleaned_data['shoe_price']
        model.shoe_size = shoes_form.cleaned_data['shoe_size']
        model.shoe_sex = shoes_form.cleaned_data['shoe_sex']
        model.shoe_bland = shoes_form.cleaned_data['shoe_bland']
        model.shoe_stock = shoes_form.cleaned_data['shoe_stock']
        model.shoe_image = shoes_form.cleaned_data['shoe_image']

        Shoes.objects.create(
            shoe_id=int(shoe_id_max_list[0]) + 1,
            shoe_name=model.shoe_name,
            shoe_price=round(int(model.shoe_price) * 1.10),
            shoe_size=model.shoe_size,
            shoe_sex=model.shoe_sex,
            shoe_bland=model.shoe_bland,
            shoe_stock=model.shoe_stock,
            shoe_image=model.shoe_image,
        )
        return redirect('ec:shoes_list')

    params = {
        'jackets_form': jackets_form,
        'shirts_form': shirts_form,
        'pants_form': pants_form,
        'shoes_form': shoes_form,
    }
    return render(request, 'product_entry.html', params)

### 商品一覧画面用 ###
# ジャケット
class JacketsListView(ListView):
    model = Jackets
    template_name = "jackets_list.html"
    context_object_name = 'jackets_list'

    def get_queryset(self):
        q_jacket_bland = self.request.GET.get('jacket_bland_icon')
        q_min_price = self.request.GET.get('min_price')
        q_max_price = self.request.GET.get('max_price')

        # ブランド名(完全一致)と価格範囲検索
        if q_jacket_bland and q_min_price and q_max_price:
            jackets_list = Jackets.objects.filter(
                Q(jacket_bland__icontains=q_jacket_bland, jacket_price__range=[q_min_price, q_max_price])
            )

        # ブランド名検索(完全一致)
        elif q_jacket_bland:
            jackets_list = Jackets.objects.filter(
                Q(jacket_bland__icontains=q_jacket_bland))

        # 価格範囲検索
        elif q_min_price and q_max_price:
            jackets_list = Jackets.objects.filter(
                Q(jacket_price__range=[q_min_price, q_max_price])
            )

        else:
            jackets_list = Jackets.objects.all()

        return jackets_list

# シャツ
class ShirtsListView(ListView):
    model = Shirts
    template_name = "shirts_list.html"
    context_object_name = 'shirts_list'

    def get_queryset(self):
        q_shirt_bland = self.request.GET.get('shirt_bland_icon')
        q_min_price = self.request.GET.get('min_price')
        q_max_price = self.request.GET.get('max_price')

        # ブランド名(完全一致)と価格範囲検索
        if q_shirt_bland and q_min_price and q_max_price:
            shirts_list = Shirts.objects.filter(
                Q(shirt_bland__icontains=q_shirt_bland, shirt_price__range=[q_min_price, q_max_price])
            )

        # ブランド名検索(完全一致)
        elif q_shirt_bland:
            shirts_list = Shirts.objects.filter(
                Q(shirt_bland__icontains=q_shirt_bland))

        # 価格範囲検索
        elif q_min_price and q_max_price:
            shirts_list = Shirts.objects.filter(
                Q(shirt_price__range=[q_min_price, q_max_price])
            )

        else:
            shirts_list = Shirts.objects.all()

        return shirts_list

# パンツ
class PantsListView(ListView):
    model = Pants
    template_name = "pants_list.html"
    context_object_name = 'pants_list'

    def get_queryset(self):
        q_pant_bland = self.request.GET.get('pant_bland_icon')
        q_min_price = self.request.GET.get('min_price')
        q_max_price = self.request.GET.get('max_price')

        # ブランド名(完全一致)と価格範囲検索
        if q_pant_bland and q_min_price and q_max_price:
            pants_list = Pants.objects.filter(
                Q(pant_bland__icontains=q_pant_bland, pant_price__range=[q_min_price, q_max_price])
            )

        # ブランド名検索(完全一致)
        elif q_pant_bland:
            pants_list = Pants.objects.filter(
                Q(shoe_bland__icontains=q_pant_bland))

        # 価格範囲検索
        elif q_min_price and q_max_price:
            pants_list = Pants.objects.filter(
                Q(pant_price__range=[q_min_price, q_max_price])
            )
        else:
            pants_list = Pants.objects.all()

        return pants_list

# 靴
class ShoesListView(ListView):
    model = Shoes
    template_name = "shoes_list.html"
    context_object_name = 'shoes_list'

    def get_queryset(self):
        q_shoe_bland = self.request.GET.get('shoe_bland_icon')
        q_min_price = self.request.GET.get('min_price')
        q_max_price = self.request.GET.get('max_price')

        # ブランド名(完全一致)と価格範囲検索
        if q_shoe_bland and q_min_price and q_max_price:
            shoes_list = Shoes.objects.filter(
                Q(shoe_bland__icontains=q_shoe_bland, shoe_price__range=[q_min_price, q_max_price])
            )

        # ブランド名検索(完全一致)
        elif q_shoe_bland:
            shoes_list = Shoes.objects.filter(
                Q(shoe_bland__icontains=q_shoe_bland))

        # 価格範囲検索
        elif q_min_price and q_max_price:
            shoes_list = Shoes.objects.filter(
                Q(shoe_price__range=[q_min_price, q_max_price])
            )

        else:
            shoes_list = Shoes.objects.all()

        return shoes_list

# 商品一覧画面用(ブランド別)
class BlandListView(ListView):
    model = Jackets
    template_name = "bland_list.html"
    context_object_name = 'bland_list'

    def get_context_data(self, **kwargs):
        bland_list = super(BlandListView, self).get_context_data(**kwargs)

        pre_path = self.request.get_full_path
        bland_name = None

        if 'bland_a' in str(pre_path):
            bland_name = 'ブランドA'

        elif 'bland_b' in str(pre_path):
            bland_name = 'ブランドB'

        elif 'bland_c' in str(pre_path):
            bland_name = 'ブランドC'

        elif 'bland_d' in str(pre_path):
            bland_name = 'ブランドD'

        bland_jackets = Jackets.objects.filter(jacket_bland=bland_name)
        bland_shirts = Shirts.objects.filter(shirt_bland=bland_name)
        bland_pants = Pants.objects.filter(pant_bland=bland_name)
        bland_shoes = Shoes.objects.filter(shoe_bland=bland_name)

        bland_list.update({
            'bland_list_jackets': bland_jackets,
            'bland_list_shirts': bland_shirts,
            'bland_list_pants': bland_pants,
            'bland_list_shoes': bland_shoes,
            'bland_name': bland_name
        })

        return bland_list

    def get_queryset(self):
        return Jackets.objects.all()

### 商品詳細画面用 ###
# ジャケット
class JacketsDetailView(DetailView):
    model = Jackets
    template_name = "jackets_detail.html"

# シャツ
class ShirtsDetailView(DetailView):
    model = Shirts
    template_name = "shirts_detail.html"

# パンツ
class PantsDetailView(DetailView):
    model = Pants
    template_name = "pants_detail.html"

# 靴
class ShoesDetailView(DetailView):
    model = Shoes
    template_name = "shoes_detail.html"

# 商品削除用
@login_required
def product_delete(request):

    if request.method == 'POST':
        Jackets.objects.all().delete()
        Shirts.objects.all().delete()
        Pants.objects.all().delete()
        Shoes.objects.all().delete()
        Cart.objects.all().delete()
        CartItem.objects.all().delete()
        PurchaseHistory.objects.all().delete()

        return redirect('ec:index')

    return render(request, 'product_delete.html')
