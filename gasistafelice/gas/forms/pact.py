from django.utils.translation import ugettext as _, ugettext_lazy as _lazy
from django import forms
from django.forms import ValidationError

from gasistafelice.gas.models.proxy import GASSupplierSolidalPact
from gasistafelice.base.models import Person
from gasistafelice.supplier.models import Supplier

from gasistafelice.auth import GAS_REFERRER_SUPPLIER
from gasistafelice.auth.models import ParamRole, PrincipalParamRoleRelation


class Base_PactForm(forms.ModelForm):
        pass

class GAS_PactForm(Base_PactForm):
    """Form for pact management by a GAS resource"""
    supplier_referrer = forms.ModelChoiceField(queryset=Person.objects.none())

    def __init__(self, request, *args, **kw):
        super(GAS_PactForm, self).__init__(*args, **kw)
        self.__gas = request.resource.gas
        self.fields['supplier_referrer'].queryset = self.__gas.persons
        des = self.__gas.des
        self.fields['supplier'].queryset = des.suppliers.exclude(pk__in=[obj.pk for obj in self.__gas.suppliers])

    def clean(self):
        cleaned_data = super(GAS_PactForm, self).clean()

        try:
            GASSupplierSolidalPact.objects.get(gas=self.__gas, supplier=cleaned_data['supplier'])
        except GASSupplierSolidalPact.DoesNotExist:
            #ok
            pass
        else:
            raise ValidationError(_("Pact between this GAS and this Supplier already exists"))

        return cleaned_data

    def save(self):
        self.instance.gas = self.__gas
        super(GAS_PactForm, self).save()
        
        pr = ParamRole.get_role(GAS_REFERRER_SUPPLIER, pact=self.instance)
        PrincipalParamRoleRelation.objects.create(role=pr, user=self.cleaned_data['supplier_referrer'].user)

    class Meta:

        model = GASSupplierSolidalPact
        fields = ('supplier', 'date_signed', 
            'order_minimum_amount', 'order_delivery_cost', 'order_deliver_interval'
        )

        gf_fieldsets = [(None, { 
            'fields' : (
                'supplier', 'date_signed', 
                ('order_minimum_amount', 'order_delivery_cost'),
                'order_deliver_interval',        
                'supplier_referrer',
        )})]


class Supplier_PactForm(Base_PactForm):
    """Form for pact management by a Supplier resource"""

    def __init__(self, request, *args, **kw):

        super(Supplier_PactForm, self).__init__(*args, **kw)
        self.__supplier = request.resource.supplier
        if not request.user.is_superuser:
            self.fields['gas'].queryset = request.user.person.gas_list

    def clean(self):
        cleaned_data = super(Supplier_PactForm, self).clean()
        try:
            GASSupplierSolidalPact.objects.get(gas=cleaned_data['gas'], supplier=self.__supplier)
        except GASSupplierSolidalPact.DoesNotExist:
            #ok
            pass
        else:
            raise ValidationError(_("Pact between this GAS and this Supplier already exists"))

        return cleaned_data

    def save(self):
        self.instance.supplier = self.__supplier
        return super(Supplier_PactForm, self).save()

    class Meta:

        model = GASSupplierSolidalPact
        fields = ('gas', 'date_signed', 'order_minimum_amount', 'order_delivery_cost', 'order_deliver_interval')

        gf_fieldsets = [(None, { 
            'fields' : (
                'gas', 'date_signed', 
                ('order_minimum_amount', 'order_delivery_cost'),
                'order_deliver_interval',        
        )})]
    

