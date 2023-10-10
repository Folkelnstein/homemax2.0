from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','created_at','created_date','update_at','update_date','auction']
    list_filter = ['auction','created_at','price']
    actions = ['make_auction_false','make_auction_true']
    fieldsets = (
        ('Общее', {
            'fields':('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price','auction'),
            'classes' : ['collapse']
        })
    )

    @admin.action(description = "Убрать торг")
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить торг")
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)




admin.site.register(Advertisement, AdvertisementAdmin)
