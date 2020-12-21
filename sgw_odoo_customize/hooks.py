# ------------------------------------------------------------------------------
# # (c) 2020 Sugestionweb.com -  javier@sugestionweb.com
# # License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# ------------------------------------------------------------------------------


def pre_init_hook(cr):
    try:
        sql = "UPDATE ir_module_module SET website = '%s' WHERE license like '%s' and website <> ''" % ('https://www.sugestionweb.com', 'OEEL%')
        cr.execute(sql)
    except Exception as e:
        pass


def post_init_hook(cr, registry):
    pass
    # cr.execute("")
