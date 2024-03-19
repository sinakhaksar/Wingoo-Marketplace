from item.models import Category

def categories_processor(request):
    categories = Category.objects.all()  # Fetch all categories
    return {'categories': categories}
