# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class empleados_model(models.Model):
    _name = 'estetica.empleados_model'
    _description = 'Empleados'

    name = fields.Char(string="Nombre", required=True, size=20)
    ape = fields.Char(string="Apellidos", required=True, size=40)
    dni = fields.Char(string="DNI", required=True, size=9)
    telf = fields.Integer(string="Teléfono", required=True, size=15)
    email = fields.Char(string="email", required=True )
    fechanacim = fields.Date(string="Fecha de Nacimiento", required=True, default=fields.Date.context_today)
    foto = fields.Binary(string="Foto")
    tratamientos_ids = fields.One2many("estetica.tratam_model", "emple_id", string="Tratamientos")

    

    @api.constrains("email")
    def _correoValido(self):
        if "@" not in self.email:
            raise ValidationError("El correo electrónico debe tener un formato válido")

    @api.constrains("dni")
    def _comprobarDNI(self):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 caracteres")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")