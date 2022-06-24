from django.shortcuts import render
from products.forms import SearchProduct
from products.models import Product
from products.models import Substitute
from django.views.decorators.http import require_http_methods
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages


def home(request):
    return render(request, "products/home.html")


@require_http_methods(['POST'])
def search_product(request):
    form = SearchProduct(request.POST)
    if form.is_valid():
        product_user = form.cleaned_data
        product_wanted = product_user['product']
        product_db = Product.objects.filter(name__icontains=product_wanted)
        return render(request, "products/products.html", context={"products": product_db})


def food(request, product_id):
    product_detail = Product.objects.get(pk=product_id)
    # substitutes = Product.objects.filter(nutriscore="a")[:5]
    substitutes = Product.objects.annotate(
        common_categories_nb=Count(
            "categories",
            filter=Q(
                categories__in=product_detail.categories.all()
            )
        )
    )
    if product_detail.nutriscore == "a":
        substitutes = substitutes.filter(nutriscore__lte=product_detail.nutriscore)
    else:
        substitutes = substitutes.filter(nutriscore__lt=product_detail.nutriscore)

    substitutes = substitutes.exclude(pk=product_detail.pk).order_by("-common_categories_nb", "nutriscore")[:6]

    return render(request, "products/food.html", context={"product": product_detail, "substitutes": substitutes})

@login_required
def save_substitute(request, product_id, original_product_id):
    product = Product.objects.get(pk=product_id)
    Substitute.objects.create(product=product, user=request.user)
    messages.success(request, "Le produit a bien été ajouté à vos favoris")
    return redirect('products:food', product_id=original_product_id)
