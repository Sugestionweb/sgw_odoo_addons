# -*- coding: utf-8 -*-

def pre_init_hook(cr):
    try:
        sql = "UPDATE ir_module_module SET website = '%s' WHERE license like '%s' and website <> ''" % ('https://www.sugestionweb.com', 'OEEL%')
        cr.execute(sql)
    except Exception as e:
        pass

def post_init_hook(cr, registry):
    pass
    # cr.execute("")
