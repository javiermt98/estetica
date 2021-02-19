# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class empleados_model(models.Model):
    _name = 'estetica.empleados_model'
    _description = 'Empleados'
    _sql_constraints = [("dni_uniq", "UNIQUE (dni)", "No puede haber dos DNI iguales")]

    name = fields.Char(string="Nombre", required=True, size=20)
    ape = fields.Char(string="Apellidos", required=True, size=40)
    dni = fields.Char(string="DNI", required=True, size=9, index=True)
    telf = fields.Integer(string="Teléfono", required=True, size=15)
    email = fields.Char(string="email", required=True )
    fechanacim = fields.Date(string="Fecha de Nacimiento", required=True, default=fields.Date.context_today)
    foto = fields.Binary(string="Foto")

    

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