"""module returning the different views of the products application"""

from django.db.models import Count, Q
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from products.forms import SearchProduct
from products.models import Product
from products.models import Substitute


def home(request):

    """class returning the home page"""

    return render(request, "products/home.html")


@require_http_methods(['POST'])
def search_product(request):

    """method to search the product requested by the user and returns the corresponding information
    return a list of object product or nothing"""

    form = SearchProduct(request.POST)
    if form.is_valid():
        product_user = form.cleaned_data
        product_wanted = product_user['product']
        product_db = Product.objects.filter(name__icontains=product_wanted)
        return render(request, "products/products.html", context={"products": product_db})


def food(request, product_id):

    """method to find the substitute of a product selected by the user
    return a list of substitute or nothing"""

    product_detail = Product.objects.get(pk=product_id)
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

    """method to save the substitute of user in database
        return the same template"""

    product = Product.objects.get(pk=product_id)
    try:
        Substitute.objects.create(product=product, user=request.user)
        messages.success(request, "Le produit a bien été ajouté à vos favoris")
    except IntegrityError:
        messages.error(request, "Le produit est déjà dans vos favoris")
    return redirect('products:food', product_id=original_product_id)


def user_food(request):

    """method to see the user food favorite product
    return a template containing the user's substitute"""

    return render(request, "products/userfood.html")


def mentions_legales(request):

    """method to see the mention legal used for this project"""

    return render(request, "products/mentionlegale.html")

