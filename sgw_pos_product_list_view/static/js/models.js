odoo.define("sgw_pos_product_list_view.models", function(require) {
  "use strict";
  var pos_model = require("point_of_sale.models");
  pos_model.load_fields("product.product", [
    "qty_available",
    "list_price",
    "default_code",
    "virtual_available",
  ]);
});
