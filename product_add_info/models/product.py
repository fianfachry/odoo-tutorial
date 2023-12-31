# product_add_info/models/product.py

from odoo import models, fields

class Product(models.Model):
    _inherit = 'product.product'

    additional_info = fields.Char(string='Additional Info')
