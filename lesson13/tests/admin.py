from django.contrib import admin
from .models import Product, Order, OrderItem

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','created_at','is_active')
    search_fields = ('name',)
    list_filter = ('is_active','created_at')
    ordering = ('-created_at',)
    
    
class OrderItemInline(admin.TabularInline):  # yoki admin.StackedInline
    model = OrderItem
    extra = 1  # Yangi order item qo‘shish uchun bitta bo‘sh qatordan boshlaydi
    autocomplete_fields = ['product']  # agar productlar ko‘p bo‘lsa
    fields = ('product', 'quantity')
    show_change_link = True

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'is_active')
    search_fields = ('user__username', 'user__email')
    list_filter = ('created_at','is_active')
    ordering = ('-created_at',)
    inlines = [OrderItemInline] 


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'created_at')
    list_filter = ('created_at', 'product')
    search_fields = ('product__name', 'order__user__username')
    ordering = ('-created_at',)

    


