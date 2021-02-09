# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class tratam_model(models.Model):
    _name = 'estetica.tratam_model'
    _description = 'Tratamiento'

    name = fields.Char(string="Nombre", required=True, size=20)
    duracion = fields.Integer(string="Duracion (min)", required=True)
    precio = fields.Float(string="Precio", required=True)
    emple_id = fields.Many2one("estetica.empleados_model", string="Empleado/a")
    clientes_ids = fields.Many2many("estetica.clientes_model", "tratam_ids", string="Clientes")
    factura_id = fields.Many2many("estetica.facturas_model", "tratam_id" ,string="Facturas")
