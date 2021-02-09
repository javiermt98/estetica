# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class clientes_model(models.Model):
    _name = 'estetica.clientes_model'
    _description = 'Clientes'

    name = fields.Char(string="Nombre", required=True, size=20)
    ape = fields.Char(string="Apellidos", required=True, size=40)
    telf = fields.Integer(string="Teléfono", required=True, size=15)
    email = fields.Char(string="email", required=True )
    tratam_ids = fields.Many2many("estetica.tratam_model", "clientes_ids", string="Tratamientos")
    facturas_ids = fields.One2many("estetica.facturas_model", "cliente_id", string="Facturas")
    

    @api.constrains("email")
    def _correoValido(self):
        if "@" not in self.email:
            raise ValidationError("El correo electrónico debe tener un formato válido")