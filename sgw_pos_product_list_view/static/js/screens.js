odoo.define('sgw_pos_product_list_view.screens', function (require) {
"use strict";

var module = require('point_of_sale.models');
var screens = require('point_of_sale.screens');
var core = require('web.core');
var QWeb = core.qweb;
var _t = core._t;
var models = module.PosModel.prototype.models;

screens.ProductListWidget.include({
    render_product: function(product){
        var current_pricelist = this._get_active_pricelist();
        var cache_key = this.calculate_cache_key(product, current_pricelist);
        var cached = this.product_cache.get_node(cache_key);
        if(!cached){
            var product_html = QWeb.render('Product',{
                    widget:  this,
                    product: product,
                    pricelist: current_pricelist,
                    image_url: this.get_product_image_url(product),
                });
            var product_node = document.createElement('tbody');
            product_node.innerHTML = product_html;
            product_node = product_node.childNodes[1];
            this.product_cache.cache_node(cache_key,product_node);
            return product_node;
        }
        return cached;
    },
    renderElement: function() {
        var el_str  = QWeb.render(this.template, {widget: this});
        var el_node = document.createElement('div');
            el_node.innerHTML = el_str;
            el_node = el_node.childNodes[1];

        if(this.el && this.el.parentNode){
            this.el.parentNode.replaceChild(el_node,this.el);
        }
        this.el = el_node;
        var list_container = el_node.querySelector('.product-list-contents');
        for(var i = 0, len = this.product_list.length; i < len; i++){
            var product_node = this.render_product(this.product_list[i]);
            product_node.addEventListener('click',this.click_product_handler);
            list_container.appendChild(product_node);
        }
    },
});
});