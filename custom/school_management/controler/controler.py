from odoo import http
from models.school import School

class StudentController(http.Controller):
    @http.route('/students', auth='public')
    def get_students(self):
        students = School.search([])
        return http.request.render('school_management.student_list', {'students': students})
