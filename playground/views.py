

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q , F, Value,Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Order,Customer
from tags.models import TaggedItem

# Create your views here.
#request -> response

def say_hello(request):
    # query_set = Product.objects.all()
    # query_set.filter().filter().order_by()

    # for product in query_set:
    #     print(product)

    # try: 
    #      product = Product.objects.get(pk=1)
    # except ObjectDoesNotExist:
    #     pass

    # None
    # product = Product.objects.filter(pk=0).first()

    # exists = Product.objects.filter(pk=0).exists()

    #keyword= value
    # product = Product.objects.filter(unit_price_range=20)

    # products = Product.objects.filter(unit_price__range=(20, 30))

    # products = Product.objects.filter(collection__id=1)

    # products = Product.objects.filter(collection__id__gt=1)

    # products = Product.objects.filter(collection__id__range=(1,2,3))

    # products = Product.objects.filter(title__contains='coffee')

    # products = Product.objects.filter(title__icontains='coffee')

    # products = Product.objects.filter(last_update__year= 2021)

    # products = Product.objects.filter(description__isnull= True)

    # products = Product.objects.filter(inventory__lt= 10, unit_price__lt= 20)

    # products = Product.objects.filter(inventory__lt= 10).filter(unit_price__lt= 20)

    # products = Product.objects.filter(Q(inventory__lt= 10)| Q(unit_price__lt= 20))

    # products = Product.objects.filter(Q(inventory__lt= 10)| ~Q(unit_price__lt= 20))


    # products = Product.objects.filter(Q(inventory= F('unit_price')))

    # products = Product.objects.filter(Q(inventory= F('collection__id')))

    # sorting
    # products = Product.objects.order_by('title')

    # products = Product.objects.order_by('-title')

    # products = Product.objects.order_by('unit_price','-title')

    # products = Product.objects.order_by('unit_price','-title').reverse()

    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')


    # products = Product.objects.all()[:5]
    # products = Product.objects.all()[5:10]

    # products = Product.objects.values('id', 'title', 'unit_price')

    # products = Product.objects.values('id', 'title', 'unit_price', 'collection__title')

    # products = Product.objects.values_list('id', 'title', 'unit_price', 'collection__title')

    # products = OrderItem.objects.values('product__id')
    
    # products = Product.objects.filter(id__in= OrderItem.objects.values('product__id').distinct()) 

    # products = Product.objects.filter(id__in= OrderItem.objects.values('product__id').distinct()).order_by('title')

    # products = Product.objects.only('id', 'title')

    # products = Product.objects.differ( 'description')

    # products = Product.objects.all()
    # products = Product.objects.select_related('collection').all()
    # products = Product.objects.select_related('collection__someOtherField').all()
    # products = Product.objects.prefetch_related('promotions').all()
    # products = Product.objects.prefetch_related('promotions').select_related('collection').all()

  


    # orders = Order.objects.select_related('customer').order_by('-placed_at')[:5]
    # orders = Order.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-placed_at')[:5]
    # orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # result = Product.objects.aaggregate(Count('id'))
    # result = Product.objects.aaggregate(count=Count('id'))
    # result = Product.objects.aaggregate(count=Count('id'), min_price= Min('unit_price'))
    # result = Product.objects.filter('collection__id=1').aaggregate(count=Count('id'), min_price= Min('unit_price'))

    # queryset= Customer.objects.annotate(is_new = Value(True))
    # queryset= Customer.objects.annotate(new_id =F( 'id')+1)

    # queryset= Customer.objects.annotate(
    #     full_name= Func(F('first_name'),Value(' ') , F('last_name'), function="CONCAT")
    # )

    # queryset= Customer.objects.annotate(
    #     full_name= Concat('first_name',Value(' '), 'last_name')
    # )

    # queryset= Customer.objects.annotate(
    #     orders_count=Count('order')
    # )

    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset= Product.objects.annotate(
    #     discount_price=discounted_price
    # )

    # content_types = Mapping(
    #     category=Product,
    #     content=ContentType.objects.get_for_model(Product),
    #     object_id=Product.id
    # ) 
    # content_types = ContentType.objects.get_for_models(Product)

    # TaggedItem.objects.filter(
    #     content_type=content_type,
    #     object_id=1
    # )

    # queryset = TaggedItem.objects.select_related('tag').filter(
    #     content_type=content_types,
    #     object_id=1
    # )
    

    return render(request, 'hello.html', {'name': 'mosh'})
