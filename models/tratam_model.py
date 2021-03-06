# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class tratam_model(models.Model):
    _name = 'estetica.tratam_model'
    _description = 'Tratamiento'

    name = fields.Char(string="Nombre", required=True, size=20)
    duracion = fields.Integer(string="Duracion (min)", required=True)
    precio = fields.Float(string="Precio", required=True)
    clientes_ids = fields.Many2many("estetica.clientes_model", "tratam_ids", string="Clientes")
    factura_id = fields.Many2many("estetica.facturas_model", "tratam_id" ,string="Facturas")
    iva = fields.Selection(string="IVA", default='21', selection=[('21','21'),('15', '15'),('7', '7'),('0', '0')], required=True)

