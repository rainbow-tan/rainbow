from django.contrib import admin

from Model.models import PartTable


@admin.register(PartTable)
class PartAcceptanceTableAdmin(admin.ModelAdmin):
    list_display = (
        'sn', 'pn', 'part_name', 'car_type', 'producer', 'receive_date', 'batch', 'send_people',
        'contact',
        'save_count', 'deal_count', 'receive_people', 'deal_mode', 'deal_remark', 'deal_date',
        )

    list_filter = ['pn', 'part_name', 'car_type']  # 过滤
    search_fields = ['pn', 'part_name', 'car_type']
