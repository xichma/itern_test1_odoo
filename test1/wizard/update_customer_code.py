from odoo import fields, models, api


class UpdateCustomerCode(models.TransientModel):
    _name = 'code.update'
    _description = 'Mass Update Customer Code'

    customer_discount_code = fields.Text(string="Customer Code")

    def update_code(self):
        partners = self.env['res.partner'].browse(self._context['active_ids'])
        for rec in partners:
            rec.customer_discount_code = self.customer_discount_code
