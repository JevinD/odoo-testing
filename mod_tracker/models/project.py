from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"

    module_ids = fields.Many2many(
        "module.tracker.version", string="Project", readonly=True
    )
