# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, date


class facturas_model(models.Model):
    _name = 'estetica.facturas_model'
    _description = 'Facturas'
    _sql_constraints = [("name_uniq", "UNIQUE (name)", "No puede haber dos Referencias de Factura iguales")]

    name = fields.Char(string="Referencia", required=True)
    fecha = fields.Date(string="Fecha", required=True, default=date.today())
    base = fields.Float(string="Base", compute="_calc_base", store=True)
    cliente_id = fields.Many2one("estetica.clientes_model", string="Cliente", ondelete='cascade', required=True)
    detallef_ids = fields.One2many("estetica.detfac_model","facturas_id", string="Productos", ondelete='cascade')
    tratam_id = fields.Many2many("estetica.tratam_model", "factura_id", string="Tratamientos", ondelete='cascade')
    total = fields.Float(string="Total", compute="_calc_iva", store=True)
    active = fields.Boolean(readonly=True, default=True)


    @api.depends('tratam_id', 'detallef_ids')
    def _calc_iva(self):
        self.ensure_one()
        total = 0
        for i in self.tratam_id:
            total += i.precio*(int(i.iva)/100+1)
        for i in self.detallef_ids:
            total += i.productos_id.precio*i.cantidad*(int(i.iva)/100+1)
        self.total = total
        

    @api.depends('tratam_id','detallef_ids')
    def _calc_base(self):
        self.ensure_one()
        suma = 0
        for i in self.tratam_id:
            suma += i.precio
        for i in self.detallef_ids:
            suma += i.productos_id.precio*i.cantidad
        self.base = suma

    @api.constrains('detallef_ids')
    def actualizaStock(self):
        self.ensure_one()
        for i in self.detallef_ids:
            if i.productos_id.stock < i.cantidad:
                raise ValidationError("No hay suficiente Stock! Cantidad Disponible: "+str(i.productos_id.stock))
            else:
                i.productos_id.stock -= i.cantidad

    def pagarFactura(self):
        self.ensure_one()
        if not self.active:
            raise ValidationError("La factura ya está pagada")
        else:
            self.active=False

    def borrarPagadas(self):
        self.ensure_one()
        facturasPagadas = self.search([("active","!=","True")])
        for i in facturasPagadas:
            i.unlink()
    

    def recuperarFactura(self):
        self.ensure_one()
        if self.active:
            raise ValidationError("La factura aun no está pagada")
        else:
            self.active=True


