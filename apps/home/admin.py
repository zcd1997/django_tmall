from django.contrib import admin

import xadmin

from apps.home.models import *
# 全局配置
from xadmin import views
# 开启主题修改
class BaseStyleSettings:
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseStyleSettings)

class GlobalSettings:
    site_title = '天猫后台管理系统'
    site_footer = 'XX互联科技有限公司'
    menu_style = 'accordion'  # 后台菜单样式修改
xadmin.site.register(views.CommAdminView, GlobalSettings)

#添加自定义的模型对象
class BannerAdmin:
    #后台要显示的字段:
    list_display = ['banner_id','title','image','detail_url','order','create_time']
    search_fields =['banner_id','title','image','detail_url','order','create_time']
xadmin.site.register(Banner,BannerAdmin)


class CategoryAdmin:
    list_display = ['cate_id','name']
    search_fields = ['cate_id','name']
xadmin.site.register(Category,CategoryAdmin)

class NavigationAdmin:
    list_display = ['nav_id','nav_name']
    search_fields = ['nav_id','nav_name']
xadmin.site.register(Navigation,NavigationAdmin)


class OrderAdmin:
    list_display = ['oid','order_code','address','post','receiver'
            ,'mobile','user_message','create_date','pay_date','delivery_date',
                    'confirm_date','status','uid']
    search_fields =['oid','order_code','address','post','receiver'
            ,'mobile','user_message','create_date','pay_date','delivery_date',
                    'confirm_date','status']
xadmin.site.register(Order,OrderAdmin)


class PropertyAdmin:
    list_display = ['property_id','cate','name']
    search_fields = ['property_id','name']
xadmin.site.register(Property,PropertyAdmin)


class PropertyValueAdmin:
    list_display = ['pro_value_id','property_id','shop_id','value']
    search_fields = ['pro_value_id','property_id','shop_id','value']
xadmin.site.register(PropertyValue,PropertyValueAdmin)


class ReviewAdmin:
    list_display = ['review_id','content','create_date','shop','uid']
    search_fields = ['review_id','content','create_date']
xadmin.site.register(Review,ReviewAdmin)

class ShopAdmin:
    list_display = ['shop_id','name','sub_title','original_price','promote_price',
                    'stock','cate','create_date']
    search_fields = ['shop_id','name','sub_title','original_price','promote_price',
                    'stock','create_date']
xadmin.site.register(Shop,ShopAdmin)


class ShopCarAdmin:
    list_display = ['car_id','number','shop','uid','oid','status']
    search_fields = ['car_id','number','oid','status']
xadmin.site.register(ShopCar,ShopCarAdmin)

class ShopImageAdmin:
    list_display = ['shop_img_id','shop','type']
    search_fields =['shop_img_id','type']
xadmin.site.register(ShopImage,ShopImageAdmin)


class SubMenuAdmin:
    list_display = ['sub_menu_id','name','cate']
    search_fields = ['sub_menu_id','name']
xadmin.site.register(SubMenu,SubMenuAdmin)

class SubMenu2Admin:
    list_display = ['sub_menu2_id','name','sub_menu']
    search_fields = ['sub_menu2_id','name']
xadmin.site.register(SubMenu2,SubMenu2Admin)


class UserProfileAdmin:
    list_display = ['uid','icon','phone','desc','user']
    search_fields = ['uid','icon','phone','desc']
xadmin.site.register(UserProfile,UserProfileAdmin)
