from products.forms import SearchProduct


def search_form(request):
    return {"search_form":  SearchProduct()}