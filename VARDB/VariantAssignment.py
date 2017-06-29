# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:43:43 2017

@author: gburguener
"""

from peewee import ForeignKeyField
from VARDB.Variant import Variant
from VARDB import sqldb, VARDBBase
from VARDB.VariantCollection import VariantCollection
from VARDB.Allele import Allele




class VariantAssignment(VARDBBase):
    variant_collection =  ForeignKeyField(VariantCollection,  related_name='assignments',
                                          db_column="variant_collection_fk") 
    variant =  ForeignKeyField(Variant,  db_column="variant_fk")
    allele =  ForeignKeyField(Allele,  db_column="allele_fk")    
    
    
    class Meta:
        indexes = (
            (('variant_collection', 'variant','allele'), True),

        )
        database = sqldb
      
        
if __name__ == '__main__':
    VariantAssignment.create_table()