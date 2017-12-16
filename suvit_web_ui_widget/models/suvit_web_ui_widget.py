# -*- coding: utf-8 -*-
import re

from openerp import api, models, fields, exceptions
from odoo.exceptions import ValidationError

CYRILLIC_PATTERN = re.compile(u"[^а-яА-Я]")


class SuvitWebUiWidgetGroup(models.Model):
    _name = 'odoo.suvit.web.ui.widget.group'
    _description = u"Группа виджетов по назначению"

    name = fields.Char(string=u"Наименование группы", )

    widget_ids = fields.One2many(string=u"Виджеты",
                                 comodel_name='odoo.suvit.web.ui.widget',
                                 inverse_name='group_id', )


class SuvitWebUiWidget(models.Model):
    _name = 'odoo.suvit.web.ui.widget'
    _description = u"Виджет"
    _inherit = 'suvit.ui.widget.base'

    group_id = fields.Many2one(string=u"Группа",
                               comodel_name='odoo.suvit.web.ui.widget.group', )

    features_groups_ids = fields.One2many(string=u"Свойства виджета",
                                          comodel_name='odoo.suvit.web.ui.widget.features.group',
                                          inverse_name='widget_id', )

    descr = fields.Text(string=u"Описание виджета")

    parent_id = fields.Many2one(string=u'Принадлежность',
                                comodel_name=_name)
    child_ids = fields.One2many(string=u'Состав',
                                comodel_name=_name,
                                inverse_name='parent_id')


class SuvitWebUiWidgetFaturesGroup(models.Model):
    _name = 'odoo.suvit.web.ui.widget.features.group'
    _description = u"Группа свойств виджета"

    name = fields.Char(string=u"Группа свойств виджета", )

    widget_id = fields.Many2one(string=u"Виджет",
                                comodel_name='odoo.suvit.web.ui.widget', )

    feature_ids = fields.One2many(string=u"Виджеты в группе свойств",
                                  comodel_name='odoo.suvit.web.ui.widget.feature',
                                  inverse_name='group_id', )


class SuvitWebUiWidgetFature(models.Model):
    _name = 'odoo.suvit.web.ui.widget.feature'
    _description = u"Свойство виджета"

    name = fields.Char(string=u"Свойство виджета", )

    group_id = fields.Many2one(string=u"Группа свойств виджета",
                               comodel_name='odoo.suvit.web.ui.widget.features.group', )
    widget_id = fields.Many2one(related='group_id.widget_id',
                                store=True)

    text = fields.Text(string=u"Описание свойства")

    group_ids = fields.Many2many(string=u"Права доступа",
                                 comodel_name='res.groups')
