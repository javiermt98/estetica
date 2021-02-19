# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class proveedor_model(models.Model):
    _name = 'estetica.proveedor_model'
    _description = 'Proveedor'

    name = fields.Char(string="Nombre", required=True, size=20, index=True)
    telf = fields.Integer(string="Teléfono", required=True, size=15)
    email = fields.Char(string="email", required=True )
    prod_ids = fields.One2many("estetica.productos_model", "proveedor_id", string="Productos")

    @api.constrains("email")
    def _correoValido(self):
        if "@" not in self.email:
            raise ValidationError("El correo electrónico debe tener un formato válido")