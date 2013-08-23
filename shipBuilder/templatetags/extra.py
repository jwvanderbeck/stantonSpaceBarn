from django import template
register = template.Library()

@register.filter
def filter_by_category(value, arg):
	arg = arg.replace('_', ' ')
	newList = []
	if value:
		for item in value:
			if item.item_category.description == arg:
				newList.append(item)
	# assert False
	return newList
