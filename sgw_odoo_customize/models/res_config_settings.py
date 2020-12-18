# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sgw_system_name = fields.Char('System Name',
                                  help=u"Setup System Name,which replace Odoo")
    sgw_show_lang = fields.Boolean('Show Quick Language Switcher',
                                   help=u"If this option is enabled,User can quick switch language in user menu")
    sgw_show_debug = fields.Boolean('Show Quick Debug',
                                    help=u"When enable,everyone login can see the debug menu")
    sgw_show_documentation = fields.Boolean('Show Documentation',
                                            help=u"When enable,User can visit user manual")
    sgw_show_documentation_dev = fields.Boolean('Show Developer Documentation',
                                                help=u"When enable,User can visit development documentation")
    sgw_show_support = fields.Boolean('Show Support', 
                                      help=u"When enable,User can visit your support site")
    sgw_show_account = fields.Boolean('Show My Account', 
                                      help=u"When enable,User can login to your website")
    sgw_show_enterprise = fields.Boolean('Show Enterprise Tag', 
                                         help=u"Uncheck to hide the Enterprise tag")
    sgw_show_share = fields.Boolean('Show Share Dashboard', 
                                    help=u"Uncheck to hide the Odoo Share Dashboard")
    sgw_show_poweredby = fields.Boolean('Show Powered by Odoo', 
                                        help=u"Uncheck to hide the Powered by text")
    sgw_stop_subscribe = fields.Boolean('Stop Odoo Subscribe(Performance Improve)', 
                                        help=u"Check to stop Odoo Subscribe function")
    group_show_author_in_apps = fields.Boolean(string="Show Author in Apps Dashboard", 
                                               implied_group='sgw_odoo_customize.group_show_author_in_apps',
                                               help=u"Uncheck to Hide Author and Website in Apps Dashboard")
    sgw_documentation_url = fields.Char('Documentation Url')
    sgw_documentation_dev_url = fields.Char('Developer Documentation Url')
    sgw_support_url = fields.Char('Support Url')
    sgw_account_title = fields.Char('My Odoo.com Account Title')
    sgw_account_url = fields.Char('My Odoo.com Account Url')
    sgw_enterprise_url = fields.Char('Customize Module Url(eg. Enterprise)')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ir_config = self.env['ir.config_parameter'].sudo()
        sgw_system_name = ir_config.get_param('sgw_system_name',
                                              default='odooApp')

        sgw_show_lang = True if ir_config.get_param('sgw_show_lang') == "True" else False
        sgw_show_debug = True if ir_config.get_param('sgw_show_debug') == "True" else False
        sgw_show_documentation = True if ir_config.get_param('sgw_show_documentation') == "True" else False
        sgw_show_documentation_dev = True if ir_config.get_param('sgw_show_documentation_dev') == "True" else False
        sgw_show_support = True if ir_config.get_param('sgw_show_support') == "True" else False
        sgw_show_account = True if ir_config.get_param('sgw_show_account') == "True" else False
        sgw_show_enterprise = True if ir_config.get_param('sgw_show_enterprise') == "True" else False
        sgw_show_share = True if ir_config.get_param('sgw_show_share') == "True" else False
        sgw_show_poweredby = True if ir_config.get_param('sgw_show_poweredby') == "True" else False
        sgw_stop_subscribe = True if ir_config.get_param('sgw_stop_subscribe') == "True" else False

        sgw_documentation_url = ir_config.get_param('sgw_documentation_url',
                                                    default='https://www.sugestionweb.com/documentation/user/12.0/en/index.html')
        sgw_documentation_dev_url = ir_config.get_param('sgw_documentation_dev_url',
                                                        default='https://www.sugestionweb.com/documentation/12.0/index.html')
        sgw_support_url = ir_config.get_param('sgw_support_url', default='https://www.sugestionweb.com/trial/')
        sgw_account_title = ir_config.get_param('sgw_account_title', default='My Online Account')
        sgw_account_url = ir_config.get_param('sgw_account_url', default='https://www.sugestionweb.com/my-account/')
        sgw_enterprise_url = ir_config.get_param('sgw_enterprise_url', default='https://www.sugestionweb.com')
        res.update(
            sgw_system_name=sgw_system_name,
            sgw_show_lang=sgw_show_lang,
            sgw_show_debug=sgw_show_debug,
            sgw_show_documentation=sgw_show_documentation,
            sgw_show_documentation_dev=sgw_show_documentation_dev,
            sgw_show_support=sgw_show_support,
            sgw_show_account=sgw_show_account,
            sgw_show_enterprise=sgw_show_enterprise,
            sgw_show_share=sgw_show_share,
            sgw_show_poweredby=sgw_show_poweredby,
            sgw_stop_subscribe=sgw_stop_subscribe,

            sgw_documentation_url=sgw_documentation_url,
            sgw_documentation_dev_url=sgw_documentation_dev_url,
            sgw_support_url=sgw_support_url,
            sgw_account_title=sgw_account_title,
            sgw_account_url=sgw_account_url,
            sgw_enterprise_url=sgw_enterprise_url
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ir_config = self.env['ir.config_parameter'].sudo()
        ir_config.set_param("sgw_system_name", self.sgw_system_name or "")
        ir_config.set_param("sgw_show_lang", self.sgw_show_lang or "False")
        ir_config.set_param("sgw_show_debug", self.sgw_show_debug or "False")
        ir_config.set_param("sgw_show_documentation", self.sgw_show_documentation or "False")
        ir_config.set_param("sgw_show_documentation_dev", self.sgw_show_documentation_dev or "False")
        ir_config.set_param("sgw_show_support", self.sgw_show_support or "False")
        ir_config.set_param("sgw_show_account", self.sgw_show_account or "False")
        ir_config.set_param("sgw_show_enterprise", self.sgw_show_enterprise or "False")
        ir_config.set_param("sgw_show_share", self.sgw_show_share or "False")
        ir_config.set_param("sgw_show_poweredby", self.sgw_show_poweredby or "False")
        ir_config.set_param("sgw_stop_subscribe", self.sgw_stop_subscribe or "False")

        ir_config.set_param("sgw_documentation_url",
                            self.sgw_documentation_url or "https://www.sugestionweb.com/documentation/user/12.0/en/index.html")
        ir_config.set_param("sgw_documentation_dev_url",
                            self.sgw_documentation_dev_url or "https://www.sugestionweb.com/documentation/12.0/index.html")
        ir_config.set_param("sgw_support_url", self.sgw_support_url or "https://www.sugestionweb.com/trial/")
        ir_config.set_param("sgw_account_title", self.sgw_account_title or "My Online Account")
        ir_config.set_param("sgw_account_url", self.sgw_account_url or "https://www.sugestionweb.com/my-account/")
        ir_config.set_param("sgw_enterprise_url", self.sgw_enterprise_url or "https://www.sugestionweb.com")

    def set_module_url(self):
        sql = "UPDATE ir_module_module SET website = '%s' WHERE license like '%s' and website <> ''" % (self.sgw_enterprise_url, 'OEEL%')
        try:
            self._cr.execute(sql)
        except Exception as e:
            pass

    def remove_sales(self):
        to_removes = [
            ['sale.order.line', ],
            ['sale.order', ],
            ['sale.commission.line', ],
            # ['sale.order.template.option', ],
            # ['sale.order.template.line', ],
            # ['sale.order.template', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            seqs = self.env['ir.sequence'].search([
                '|', ('code', '=', 'sale.order'),
                ('code', '=', 'sale.commission.line')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            raise Warning(e)
        return True

    def remove_product(self):
        to_removes = [
            ['product.product', ],
            ['product.template', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            seqs = self.env['ir.sequence'].search([('code', '=', 'product.product')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_product_attribute(self):
        to_removes = [
            ['product.attribute.value', ],
            ['product.attribute', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_pos(self):
        to_removes = [
            ['pos.order.line', ],
            ['pos.order', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            seqs = self.env['ir.sequence'].search([('code', '=', 'pos.order')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_purchase(self):
        to_removes = [
            ['purchase.order.line', ],
            ['purchase.order', ],
            ['purchase.requisition.line', ],
            ['purchase.requisition', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            seqs = self.env['ir.sequence'].search([
                '|', ('code', '=', 'purchase.order'),
                '|', ('code', '=', 'purchase.requisition.purchase.tender'),
                ('code', '=', 'purchase.requisition.blanket.order')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_expense(self):
        to_removes = [
            ['hr.expense.sheet', ],
            ['hr.expense', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            seqs = self.env['ir.sequence'].search([
                ('code', '=', 'hr.expense.invoice')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_mrp(self):
        to_removes = [
            ['mrp.workcenter.productivity', ],
            ['mrp.workorder', ],
            ['mrp.production.workcenter.line', ],
            ['change.production.qty', ],
            ['mrp.production', ],
            ['mrp.production.product.line', ],
            ['mrp.unbuild', ],
            ['change.production.qty', ],
            ['sale.forecast.indirect', ],
            ['sale.forecast', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            seqs = self.env['ir.sequence'].search([
                '|', ('code', '=', 'mrp.production'),
                ('code', '=', 'mrp.unbuild'),
            ])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_mrp_bom(self):
        to_removes = [
            ['mrp.bom.line', ],
            ['mrp.bom', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_inventory(self):
        to_removes = [
            ['stock.quant', ],
            ['stock.move.line', ],
            ['stock.package.level', ],
            ['stock.quantity.history', ],
            ['stock.quant.package', ],
            ['stock.move', ],
            ['stock.pack.operation', ],
            ['stock.picking', ],
            ['stock.scrap', ],
            ['stock.picking.batch', ],
            ['stock.inventory.line', ],
            ['stock.inventory', ],
            ['stock.production.lot', ],
            ['stock.fixed.putaway.strat', ],
            ['procurement.group', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            seqs = self.env['ir.sequence'].search([
                '|', ('code', '=', 'stock.lot.serial'),
                '|', ('code', '=', 'stock.lot.tracking'),
                '|', ('code', '=', 'stock.orderpoint'),
                '|', ('code', '=', 'stock.picking'),
                '|', ('code', '=', 'picking.batch'),
                '|', ('code', '=', 'stock.quant.package'),
                '|', ('code', '=', 'stock.scrap'),
                '|', ('code', '=', 'stock.picking'),
                '|', ('prefix', '=', 'WH/IN/'),
                '|', ('prefix', '=', 'WH/INT/'),
                '|', ('prefix', '=', 'WH/OUT/'),
                '|', ('prefix', '=', 'WH/PACK/'),
                ('prefix', '=', 'WH/PICK/')
            ])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_account(self):
        to_removes = [
            ['account.voucher.line', ],
            ['account.voucher', ],
            ['account.bank.statement.line', ],
            ['account.bank.statement', ],
            ['account.payment', ],
            ['account.analytic.line', ],
            ['account.analytic.account', ],
            ['account.invoice.line', ],
            ['account.invoice.refund', ],
            ['account.invoice', ],
            ['account.partial.reconcile', ],
            ['account.move.line', ],
            ['hr.expense.sheet', ],
            ['account.move', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)

                    seqs = self.env['ir.sequence'].search([
                        '|', ('code', '=', 'account.reconcile'),
                        '|', ('code', '=', 'account.payment.customer.invoice'),
                        '|', ('code', '=', 'account.payment.customer.refund'),
                        '|', ('code', '=', 'account.payment.supplier.invoice'),
                        '|', ('code', '=', 'account.payment.supplier.refund'),
                        '|', ('code', '=', 'account.payment.transfer'),
                        '|', ('prefix', 'like', 'BNK1/'),
                        '|', ('prefix', 'like', 'CSH1/'),
                        '|', ('prefix', 'like', 'INV/'),
                        '|', ('prefix', 'like', 'EXCH/'),
                        '|', ('prefix', 'like', 'MISC/'),
                        '|', ('prefix', 'like', '账单/'),
                        ('prefix', 'like', '杂项/')
                    ])
                    for seq in seqs:
                        seq.write({
                            'number_next': 1,
                        })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_account_chart(self):
        to_removes = [
            ['account.tax.account.tag', ],
            ['account.tax', ],
            ['account.account.account.tag', ],
            ['wizard_multi_charts_accounts'],
            ['account.account', ],
            ['account.journal', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)

            # reset default tax，
            field1 = self.env['ir.model.fields']._get('product.template',
                                                      "taxes_id").id
            field2 = self.env['ir.model.fields']._get('product.template',
                                                      "supplier_taxes_id").id

            sql = ("delete from ir_default where field_id = %s or field_id = %s") % (field1, field2)
            self._cr.execute(sql)

            sql = "update res_company set chart_template_id=null ;"
            self._cr.execute(sql)
        except Exception as e:
            pass
        return True

    @api.multi
    def remove_project(self):
        to_removes = [
            ['account.analytic.line', ],
            ['project.task', ],
            ['project.forecast', ],
            ['project.project', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_website(self):
        to_removes = [
            ['blog.tag.category', ],
            ['blog.tag', ],
            ['blog.post', ],
            ['blog.blog', ],
            ['website.published.multi.mixin', ],
            ['website.published.mixin', ],
            ['website.multi.mixin', ],
            ['website.redirect', ],
            ['website.seo.metadata', ],
            ['website.page', ],
            ['website.menu', ],
            ['website', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_message(self):
        to_removes = [
            ['mail.message', ],
            ['mail.followers', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_workflow(self):
        to_removes = [
            ['wkf.workitem', ],
            ['wkf.instance', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)

        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_all_biz(self):
        try:
            self.remove_account()
            self.remove_inventory()
            self.remove_mrp()
            self.remove_purchase()
            self.remove_sales()
            self.remove_project()
            self.remove_message()
        except Exception as e:
            pass  # raise Warning(e)
        return True
