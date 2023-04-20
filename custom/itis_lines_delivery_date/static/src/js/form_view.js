/** @odoo-module */

import { registry } from '@web/core/registry';
import { formView } from '@web/views/form/form_view';
import { FormController } from '@web/views/form/form_controller';

const { onWillUpdateProps } = owl;

export class myClass extends FormController {
    setup() {
        super.setup();
        onWillUpdateProps((nextProps) => {
            console.log("props");
        });
    }
}

myClass.template = "itis_lines_delivery_date.form_view"
registry.category("views").add("form_view", {
    ...formView,
    Controller: myClass
});
