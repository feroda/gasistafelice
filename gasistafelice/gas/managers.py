from django.db import models

from gasistafelice.auth.models import ParamRole

from datetime import date

class GASMembersManager(models.Manager):
    """
    A custom manager class for the `GASMember` model.
    """

    def gas_referrers(self, gas=None):
        """
        Return a QuerySet containing all GAS members who have been assigned the 'GAS Referrer'
        role for the GAS they belong to.
        
        If a `gas` argument is provided, the result set is filtered accordingly.      
        """
        # TODO: UNITTEST needed !
        p_roles = ParamRole.objects.gas_referrers(gas)
        # initialize the return QuesrySet to an EmptyQuerySet
        qs = self.model.objects.none()
        # costruct the result set by joining partial QuerySets
        # (one for each parametric role of interest)
        for pr in p_roles:
            # filter out spurious GAS members arising when a Person belongs to multiple GAS
            qs = qs | self.model.objects.filter(person__user__in=pr.get_users(), gas=pr.gas)

        return qs


    def tech_referrers(self, gas=None):
        """
        Return a QuerySet containing all GAS members who have been assigned the 'Tech Referrer'
        role for the GAS they belong to.    
        
        If a `gas` argument is provided, the result set is filtered accordingly.
        """
        # TODO: UNITTEST needed !
        p_roles = ParamRole.objects.gas_tech_referrers(gas)
        # initialize the return QuesrySet to an EmptyQuerySet
        qs = self.model.objects.none()
        # costruct the result set by joining partial QuerySets
        # (one for each parametric role of interest)
        for pr in p_roles:
            # filter out spurious GAS members arising when a Person belongs to multiple GAS
            qs = qs | self.model.objects.filter(person__user__in= pr.get_users(), gas=pr.gas)

        return qs
        

    def cash_referrers(self, gas=None):
        """
        Return a QuerySet containing all GAS members who have been assigned the 'Cash Referrer'
        role for the GAS they belong to.    
        
        If a `gas` argument is provided, the result set is filtered accordingly.
        """
        # TODO: UNITTEST needed !
        p_roles = ParamRole.objects.gas_cash_referrers(gas)
        # initialize the return QuesrySet to an EmptyQuerySet
        qs = self.model.objects.none()
        # costruct the result set by joining partial QuerySets
        # (one for each parametric role of interest)
        for pr in p_roles:
            # filter out spurious GAS members arising when a Person belongs to multiple GAS
            qs = qs | self.model.objects.filter(person__user__in= pr.get_users(), gas=pr.gas)

        return qs

    def supplier_referrers(self, gas=None, supplier=None):
        """
        Return a QuerySet containing all GAS members who have been assigned the 'Supplier Referrer'
        role for the GAS they belong to.    
        
        If a `gas` and/or a 'supplier' arguments are provided, the result set is filtered accordingly.
        """
        # TODO: UNITTEST needed !
        p_roles = ParamRole.objects.gas_supplier_referrers(gas, supplier)
        # initialize the return QuesrySet to an EmptyQuerySet
        qs = self.model.objects.none()
        # costruct the result set by joining partial QuerySets
        # (one for each parametric role of interest)
        for pr in p_roles:
            # filter out spurious GAS members arising when a Person belongs to multiple GAS
            qs = qs | self.model.objects.filter(person__user__in= pr.get_users(), gas=pr.gas)

        return qs


    def order_referrers(self, order=None):
        """
        Return a QuerySet containing all GAS members who have been assigned the 'Order Referrer'
        role for the GAS they belong to.    
        
        If a `order` argument is provided, the result set is filtered accordingly.
        """
        # TODO: UNITTEST needed !
        p_roles = ParamRole.objects.gas_order_referrers(order)
        # initialize the return QuesrySet to an EmptyQuerySet
        qs = self.model.objects.none()
        # costruct the result set by joining partial QuerySets
        # (one for each parametric role of interest)
        for pr in p_roles:
            # filter out spurious GAS members arising when a Person belongs to multiple GAS
            qs = qs | self.model.objects.filter(person__user__in= pr.get_users(), gas=pr.order.pact.gas)

        return qs

    def delivery_referrers(self, delivery=None):
        """
        Return a QuerySet containing all GAS members who have been assigned the 'Delivery Referrer'
        role for the GAS they belong to.    
        
        If a `delivery` argument is provided, the result set is filtered accordingly.
        """
        # TODO: UNITTEST needed !
        p_roles = ParamRole.objects.gas_order_referrers(delivery)
        # initialize the return QuesrySet to an EmptyQuerySet
        qs = self.model.objects.none()
        # costruct the result set by joining partial QuerySets
        # (one for each parametric role of interest)
        for pr in p_roles:
            # filter out spurious GAS members arising when a Person belongs to multiple GAS
            qs = qs | self.model.objects.filter(person__user__in= pr.get_users(), gas__in=pr.delivery.gas_set)

        return qs

    def withdrawal_referrers(self, withdrawal=None):
        """
        Return a QuerySet containing all GAS members who have been assigned the 'Withdrawal Referrer'
        role for the GAS they belong to.
        
        If a `withdrawal` argument is provided, the result set is filtered accordingly.    
        """
        # TODO: UNITTEST needed !
        p_roles = ParamRole.objects.gas_order_referrers(withdrawal)
        # initialize the return QuesrySet to an EmptyQuerySet
        qs = self.model.objects.none()
        # costruct the result set by joining partial QuerySets
        # (one for each parametric role of interest)
        for pr in p_roles:
            # filter out spurious GAS members arising when a Person belongs to multiple GAS
            qs = qs | self.model.objects.filter(person__user__in= pr.get_users(), gas__in=pr.withdrawal.gas_set)

        return qs

class ActiveAppointmentManager(models.Manager):
    # TODO UNITTEST
    """
    A custom manager class for the `Appointment` model, 
    meant to retrieve only active appointments.
    """
    
    def get_query_set(self):
        """
        Return a QuerySet containing all appointments scheduled for a future date.
        """
        return super(ActiveAppointmentManager, self).get_query_set().filter(date__gt=date.today())

class ArchivedAppointmentManager(models.Manager):
    # TODO UNITTEST
    """
    A custom manager class for the `Appointment` model, 
    meant to retrieve only archived (past) appointments.
    """
    
    def get_query_set(self):
        """
        Return a QuerySet containing all past appointments.
        """
        return super(ArchivedAppointmentManager, self).get_query_set().filter(date__lt=date.today())

