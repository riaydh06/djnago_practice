
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from  . import models
from django.db.models.aggregates import Count
from django.urls import reverse



class InventoryFilter(admin.SimpleListFilter):
    title= 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10','Low',)
        ]
    
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
          return  queryset.filter(inventory__lt=10)

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    autocomplete_fields= ['featured_product']
    list_display=["title",'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            +'?'
            +urlencode({
            'collection__id': str(collection.id)
        }))
        return format_html('<a href="{}">{}</a>',url, collection.products_count)
        
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('products'))



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields=['collection']
    prepopulated_fields={
        'slug': ['title']
    }
    # fields=['title', 'slug']
    # exclude=['promotions']
    # readonly_fields=[]
    actions =['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page= 10
    list_select_related= ['collection']
    list_filter = ['collection','last_update',  InventoryFilter ]
    search_fields=['title']

    def collection_title(self, product ):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10: 
            return 'Low'
        return 'Ok'
    @admin.action(description= 'Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count= queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} product were successfully updated.',
            messages.SUCCESS
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'memberShip']
    list_editable = ['memberShip']
    list_per_page= 10
    ordering =  ['first_name', 'last_name']
    search_fields= ['first_name__istartswith', 'last_name__istartswith','first_name']
    
class OrderItemInline(admin.StackedInline):
    autocomplete_fields = ['product']
    model = models.OrderItem
    min_num= 1
    max_num=10
    extra=0
  

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display= ['id', 'placed_at', 'customer']
    autocomplete_fields= ['customer']
    inlines = [OrderItemInline]


