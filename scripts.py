from rango.models import Category
for cat in Category.objects.all():
	cat.slug = cat.name
	cat.save()