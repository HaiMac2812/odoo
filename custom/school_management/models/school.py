from odoo import models, fields
class School(models.Model):
    _name = "school.student"
    _description = 'School management system'
    
    
    
    
    
    name = fields.Many2one('res.partner',string = 'student')
    class_id = fields.Integer(string = 'Class')
    division = fields.Char(string = 'Division') 
