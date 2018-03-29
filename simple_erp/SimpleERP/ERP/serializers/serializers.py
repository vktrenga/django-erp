from rest_framework import serializers
from ERP.models.masters import *


class ProfileSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""
    class Meta:
        """docstring for  Meta"""
        model = Profile
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
    """docstring for CurrencySerializer"""
    class Meta:
        """docstring for  Meta"""
        model = Currency
        fields = "__all__"

class StateSerializer(serializers.ModelSerializer):
    """docstring for CompanySerializer"""
    class Meta:
        """docstring for  Meta"""
        model = StateMaster
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    """docstring for CompanySerializer"""
    class Meta:
        """docstring for  Meta"""
        model = Company
        fields = "__all__"


class WareHouseSerializer(serializers.ModelSerializer):
    """docstring for WareHouse"""
    class Meta(object):
        """docstring for Meta"""
        model = WareHouse
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    """docstring for Field"""
    class Meta(object):
        """docstring for Meta"""
        model = Unit
       
        fields = "__all__"
        


class ItemGroupSerializer(serializers.ModelSerializer):
    """docstring for ItemGroup"""
    class Meta(object):
        """docstring for Meta"""
        model = ItemGroup
        fields = "__all__"


class CustomerGroupSerializer(serializers.ModelSerializer):
    """docstring for CustomerGroup"""
    class Meta(object):
        """docstring for Meta"""
        model = CustomerGroup
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    """docstring for Customer"""
    class Meta(object):
        """docstring for Meta"""
        model = Customer
        fields = "__all__"


class TaxGroupSerializer(serializers.ModelSerializer):
    """docstring for TaxGroup"""
    class Meta(object):
        """docstring for Meta"""
        model = TaxGroup
        fields = "__all__"


class TaxSerializer(serializers.ModelSerializer):
    """docstring for Tax"""
    class Meta(object):
        """docstring for Meta"""
        model = Tax
        fields = "__all__"

class SupplierGroupSerializer(serializers.ModelSerializer):
    """docstring for CustomerGroup"""
    class Meta(object):
        """docstring for Meta"""
        model = SupplierGroup
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    """docstring for Supplier"""
    class Meta(object):
        """docstring for Meta"""
        model = Supplier
        fields = "__all__"

class ItemSizeSerializer(serializers.ModelSerializer):
    """docstring for Tax"""
    class Meta(object):
        """docstring for Meta"""
        model = ItemSize
        fields = "__all__"

class ItemColorSerializer(serializers.ModelSerializer):
    """docstring for Tax"""
    class Meta(object):
        """docstring for Meta"""
        model = ItemColor
        fields = "__all__"

class ItemBrandSerializer(serializers.ModelSerializer):
    """docstring for Tax"""
    class Meta(object):
        """docstring for Meta"""
        model = ItemBrand
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    """docstring for Tax"""
    class Meta(object):
        """docstring for Meta"""
        model = Item
        fields = "__all__"

class ItemTaxSerializer(serializers.ModelSerializer):
    """docstring for Tax"""
    class Meta(object):
        """docstring for Meta"""
        model = ItemTax
        fields = "__all__"