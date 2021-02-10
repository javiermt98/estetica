# -*- coding: utf-8 -*-

from odoo import models, fields, api


class detfac_model(models.Model):
    _name = 'estetica.detfac_model'
    _description = 'estetica.detfac_model'

    
    facturas_id = fields.Many2one("estetica.facturas_model", "Factura")
    productos_id = fields.Many2one("estetica.productos_model", "Productos")
    iva = fields.Selection(string="IVA", default='21', selection=[('21','21'),('15', '15'),('7', '7'),('0', '0')], required=True)
    cantidad = fields.Integer(string="Cantidad", default=1, required=True)
    