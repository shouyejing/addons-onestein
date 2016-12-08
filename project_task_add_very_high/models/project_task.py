# -*- coding: utf-8 -*-
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    priority = fields.Selection(selection_add=[('3', 'Very High')])
