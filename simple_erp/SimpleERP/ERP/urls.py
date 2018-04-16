from django.conf.urls import url,include
from ERP.custom_views.master import company,currency,state,warehouse,unit,itemgroup,customergroup,taxgroup,tax,suppliergroup,supplier,customer,itemsize,itemcolor,itembrand,item
from ERP.custom_views.stock import stockentry
from ERP.custom_views import default
from django.conf import settings
app_name = 'ERP'
urlpatterns = [	
    url(r'^$', default.login_user, name='login'),
    url(r'^home/$', default.index, name='default'),



    url(r'^company/create/', company.company_create,name='company_create'),
    url(r'^company/update/(?P<id>[^/]*)/$', company.company_update),
    url(r'^company/view/(?P<id>[^/]*)/$', company.company_view),
    url(r'^company/list/', company.list_company, name='list_company'),
    url(r'^company/delete/(?P<id>[^/]*)/$', company.delete_company),

    url(r'^currency/create/', currency.currency_create,name='currency_create'),
    url(r'^currency/update/(?P<id>[^/]*)/$', currency.currency_update),
    url(r'^currency/view/(?P<id>[^/]*)/$', currency.currency_view),
    url(r'^currency/list/', currency.list_currency, name='list_currency'),
    url(r'^currency/delete/(?P<id>[^/]*)/$', currency.delete_currency),

    url(r'^state/create/', state.state_create,name='state_create'),
    url(r'^state/update/(?P<id>[^/]*)/$', state.state_update),
    url(r'^state/view/(?P<id>[^/]*)/$', state.state_view),
    url(r'^state/list/', state.list_state, name='list_state'),
    url(r'^state/delete/(?P<id>[^/]*)/$', state.delete_state),

    url(r'^warehouse/create/', warehouse.warehouse_create,name='warehouse_create'),
    url(r'^warehouse/update/(?P<id>[^/]*)/$', warehouse.warehouse_update),
    url(r'^warehouse/view/(?P<id>[^/]*)/$', warehouse.warehouse_view),
    url(r'^warehouse/list/', warehouse.list_warehouse, name='list_warehouse'),
    url(r'^warehouse/delete/(?P<id>[^/]*)/$', warehouse.delete_warehouse),

    url(r'^unit/create/', unit.unit_create,name='unit_create'),
    url(r'^unit/update/(?P<id>[^/]*)/$', unit.unit_update),
    url(r'^unit/view/(?P<id>[^/]*)/$', unit.unit_view),
    url(r'^unit/list/', unit.list_unit, name='list_unit'),
    url(r'^unit/delete/(?P<id>[^/]*)/$', unit.delete_unit),

    url(r'^itemgroup/create/', itemgroup.itemgroup_create,name='itemgroup_create'),
    url(r'^itemgroup/update/(?P<id>[^/]*)/$', itemgroup.itemgroup_update),
    url(r'^itemgroup/view/(?P<id>[^/]*)/$', itemgroup.itemgroup_view),
    url(r'^itemgroup/list/', itemgroup.itemgroup_list, name='itemgroup_list'),
    url(r'^itemgroup/delete/(?P<id>[^/]*)/$', itemgroup.itemgroup_delete),


    url(r'^customergroup/create/', customergroup.customergroup_create,name='customergroup_create'),
    url(r'^customergroup/update/(?P<id>[^/]*)/$', customergroup.customergroup_update),
    url(r'^customergroup/view/(?P<id>[^/]*)/$', customergroup.customergroup_view),
    url(r'^customergroup/list/', customergroup.customergroup_list, name='customergroup_list'),
    url(r'^customergroup/delete/(?P<id>[^/]*)/$', customergroup.customergroup_delete),

    url(r'^taxgroup/create/', taxgroup.taxgroup_create,name='taxgroup_create'),
    url(r'^taxgroup/update/(?P<id>[^/]*)/$', taxgroup.taxgroup_update),
    url(r'^taxgroup/view/(?P<id>[^/]*)/$', taxgroup.taxgroup_view),
    url(r'^taxgroup/list/', taxgroup.taxgroup_list, name='taxgroup_list'),
    url(r'^taxgroup/delete/(?P<id>[^/]*)/$', taxgroup.taxgroup_delete),

    url(r'^tax/create/', tax.tax_create,name='tax_create'),
    url(r'^tax/update/(?P<id>[^/]*)/$', tax.tax_update),
    url(r'^tax/view/(?P<id>[^/]*)/$', tax.tax_view),
    url(r'^tax/list/', tax.tax_list, name='tax_list'),
    url(r'^tax/delete/(?P<id>[^/]*)/$', tax.tax_delete),

    url(r'^suppliergroup/create/', suppliergroup.suppliergroup_create,name='suppliergroup_create'),
    url(r'^suppliergroup/update/(?P<id>[^/]*)/$', suppliergroup.suppliergroup_update),
    url(r'^suppliergroup/view/(?P<id>[^/]*)/$', suppliergroup.suppliergroup_view),
    url(r'^suppliergroup/list/', suppliergroup.suppliergroup_list, name='suppliergroup_list'),
    url(r'^suppliergroup/delete/(?P<id>[^/]*)/$', suppliergroup.suppliergroup_delete),

    url(r'^supplier/create/', supplier.supplier_create,name='supplier_create'),
    url(r'^supplier/update/(?P<id>[^/]*)/$', supplier.supplier_update),
    url(r'^supplier/view/(?P<id>[^/]*)/$', supplier.supplier_view),
    url(r'^supplier/list/', supplier.supplier_list, name='supplier_list'),
    url(r'^supplier/delete/(?P<id>[^/]*)/$', supplier.supplier_delete),

    url(r'^customer/create/', customer.customer_create,name='customer_create'),
    url(r'^customer/update/(?P<id>[^/]*)/$', customer.customer_update),
    url(r'^customer/view/(?P<id>[^/]*)/$', customer.customer_view),
    url(r'^customer/list/', customer.customer_list, name='customer_list'),
    url(r'^customer/delete/(?P<id>[^/]*)/$', customer.customer_delete),

    url(r'^itemcolor/create/', itemcolor.itemcolor_create,name='itemcolor_create'),
    url(r'^itemcolor/update/(?P<id>[^/]*)/$', itemcolor.itemcolor_update),
    url(r'^itemcolor/view/(?P<id>[^/]*)/$', itemcolor.itemcolor_view),
    url(r'^itemcolor/list/', itemcolor.itemcolor_list, name='itemcolor_list'),
    url(r'^itemcolor/delete/(?P<id>[^/]*)/$', itemcolor.itemcolor_delete),


    url(r'^itemsize/create/', itemsize.itemsize_create,name='itemsize_create'),
    url(r'^itemsize/update/(?P<id>[^/]*)/$', itemsize.itemsize_update),
    url(r'^itemsize/view/(?P<id>[^/]*)/$', itemsize.itemsize_view),
    url(r'^itemsize/list/', itemsize.itemsize_list, name='itemsize_list'),
    url(r'^itemsize/delete/(?P<id>[^/]*)/$', itemsize.itemsize_delete),

    url(r'^itembrand/create/', itembrand.itembrand_create,name='itembrand_create'),
    url(r'^itembrand/update/(?P<id>[^/]*)/$', itembrand.itembrand_update),
    url(r'^itembrand/view/(?P<id>[^/]*)/$', itembrand.itembrand_view),
    url(r'^itembrand/list/', itembrand.itembrand_list, name='itembrand_list'),
    url(r'^itembrand/delete/(?P<id>[^/]*)/$', itembrand.itembrand_delete),

    url(r'^item/create/', item.item_create,name='item_create'),
    url(r'^item/update/(?P<id>[^/]*)/$', item.item_update),
    url(r'^item/view/(?P<id>[^/]*)/$', item.item_view),
    url(r'^item/list/', item.item_list, name='item_list'),
    url(r'^item/delete/(?P<id>[^/]*)/$', item.item_delete),
    url(r'^item/delete/(?P<id>[^/]*)/$', item.item_delete),
    url(r'^item/item_list_autocomplete/', item.item_list_autocomplete),
    
    url(r'^stockentry/create/', stockentry.stockentry_create,name='stockentry_create'),
    url(r'^stockentry/stockentry_items/', stockentry.stockentry_items,name='stockentry_items'),
    #url(r'^stockentry/update/(?P<id>[^/]*)/$', stockentry.stockentry_update),
    #url(r'^stockentry/view/(?P<id>[^/]*)/$', stockentry.stockentry_view),
    #url(r'^stockentry/list/', stockentry.stockentry_list, name='stockentry_list'),
    #url(r'^stockentry/delete/(?P<id>[^/]*)/$', stockentry.stockentry_delete),
    

]


