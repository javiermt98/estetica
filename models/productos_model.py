# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class productos_model(models.Model):
    _name = 'estetica.productos_model'
    _description = 'Productos'

    name = fields.Char(string="Nombre", required=True, size=20)
    descripcion = fields.Char(string="Descripcion", required=True)
    precio = fields.Float(string="Precio", required=True)
    stock = fields.Integer(string="Stock")
    proveedor_id = fields.Many2one("estetica.proveedor_model", string="Proveedor")


