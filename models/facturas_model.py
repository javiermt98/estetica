# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, date


class facturas_model(models.Model):
    _name = 'estetica.facturas_model'
    _description = 'Facturas'

    name = fields.Char(string="Referencia", required=True)
    fecha = fields.Date(string="Fecha", required=True, default=date.today())
    base = fields.Float(string="Base", compute="_calc_base", store=True)
    cliente_id = fields.Many2one("estetica.clientes_model", string="Cliente")
    detallef_ids = fields.One2many("estetica.detfac_model","facturas_id", string="Productos")
    tratam_id = fields.Many2many("estetica.tratam_model", "factura_id", string="Tratamientos")
    total = fields.Float(string="Total", compute="_calc_iva", store=True)


    @api.depends('tratam_id', 'base')
    def _calc_iva(self):
        self.ensure_one()
        total = 0
        for i in self.tratam_id:
            total+= (self.base*int(i.iva)/100)+self.base
        self.total = total

    @api.depends('tratam_id')
    def _calc_base(self):
        self.ensure_one()
        suma = 0
        for i in self.tratam_id:
            suma += i.precio
        self.base = suma

    # @api.depends('detallef_ids')
    # def actualizaStock(self):
    #     self.ensure_one()
    #     for i in self.detallef_ids:
    #         i.cantidad -= i.productos_id.cantidad



