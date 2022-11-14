
import datetime
from odoo import api, fields, models

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    @api.model
    def default_get(self,fields):
        res= super(CancelAppointmentWizard,self).default_get(fields)
        res["date_cancel"]=  datetime.date.today()
        return res

    appointment_id=fields.Many2one("hospital.appointment",string="appointment")
    reason = fields.Text(string="Reason")
    date_cancel=fields.Date(string="Cancellation Data")
    def action_cancel(self):
        return