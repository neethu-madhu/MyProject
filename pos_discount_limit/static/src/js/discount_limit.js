odoo.define('pos_discount_limit.pos_discount_limit', function (require) {
"use strict";
    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var core = require('web.core');
    var _t = core._t;

    models.load_fields('pos.category', 'limited_discount');
    console.log('loaded')
    screens.OrderWidget.include({
        set_value: function(val) {
            var order = this.pos.get_order();
            console.log('cat', order)
//            pos product category
            var pos_prod_id = order.selected_orderline.product.pos_categ_id[0]
            console.log('cat', pos_prod_id)
//            check if discount limit is enabled
            if(this.pos.config.discount_limit){
                if (order.get_selected_orderline()) {
                    var mode = this.numpad_state.get('mode');
                    if( mode === 'quantity'){
                        order.get_selected_orderline().set_quantity(val);
                    }else if( mode === 'discount'){
                        console.log('discount-mode')
                        var rounded = Math.round(val);
                        if(Number.isInteger(pos_prod_id)){
                            if(this.pos.db.category_by_id[pos_prod_id].limited_discount){
                                if(rounded > this.pos.db.category_by_id[pos_prod_id].limited_discount){
                                    this.gui.show_popup('error', {
                                        title : _t("Discount not applicable"),
                                        body  : _t("The discount applied must be with in the discount limit."),
                                    });
                                    order.get_selected_orderline().set_discount(0);
                                        this.numpad_state.reset();
                                    return;
                                }
                                else
                                {
                                    order.get_selected_orderline().set_discount(val);
                                }
                            }
                            else{
                                order.get_selected_orderline().set_discount(val);
                            }
                        }
                        else{
                            order.get_selected_orderline().set_discount(val);
                        }
                    }else if( mode === 'price'){
                        var selected_orderline = order.get_selected_orderline();
                        selected_orderline.price_manually_set = true;
                        selected_orderline.set_unit_price(val);
                    }
//                    if (this.pos.config.iface_customer_facing_display) {
//                        this.pos.send_current_order_to_customer_facing_display();
//                    }
                }
            }
            else{
                if (order.get_selected_orderline()) {
                    var mode = this.numpad_state.get('mode');
                    if( mode === 'quantity'){
                        order.get_selected_orderline().set_quantity(val);
                    }else if( mode === 'discount'){
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
            }

        },
    });
});