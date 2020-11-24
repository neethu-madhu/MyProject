odoo.define('pos_discount_tag.pos_discount_tag', function(require){
    'use strict';

    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var gui = require('point_of_sale.gui');
    var core    = require('web.core');
    var _t = core._t;

    models.load_fields('product.product', ['discount_tag']);
    console.log('js loaded', models)
    screens.OrderWidget.include({
        set_value: function(val) {
            var order = this.pos.get_order();
            if (order.get_selected_orderline()) {
                var orderline = order.get_selected_orderline().product.discount_tag;
                console.log('selected-order-line', orderline)
                order.get_selected_orderline().set_discount(orderline);
                var mode = this.numpad_state.get('mode');
                if( mode === 'quantity'){
                    var product = order.get_orderlines();
                    console.log('order', product)
                    order.get_selected_orderline().set_quantity(val);
//                    order.get_selected_orderline().set_discount(orderline);
                }else if( mode === 'discount'){
                    console.log('discount mode', val)
                    order.get_selected_orderline().set_discount(val);
                }else if( mode === 'price'){
                    var selected_orderline = order.get_selected_orderline();
                    selected_orderline.price_manually_set = true;
                    selected_orderline.set_unit_price(val);
                }
                if (this.pos.config.iface_customer_facing_display) {
                    this.pos.send_current_order_to_customer_facing_display();
                }
            }
        },
    });
});