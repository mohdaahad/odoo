from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit= "sale.order"
   
    confirmed_usr_id = fields.Many2one("res.users",string="Confirmed User ")

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        self.confirmed_usr_id = self.env.user.id
       