# -*- coding: utf-8 -*-

from odoo import models, fields, api


class detfac_model(models.Model):
    _name = 'estetica.detfac_model'
    _description = 'estetica.detfac_model'

    
    facturas_id = fields.Many2one("estetica.facturas_model", "Factura")
    productos_id = fields.Many2one("estetica.productos_model", "Productos")
    cantidad = fields.Integer(string="Cantidad", default=1, required=True)