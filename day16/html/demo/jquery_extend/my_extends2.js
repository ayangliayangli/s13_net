/**
 *
 * Created by lee on 16/10/17.
 */


(function (jq) {
    jq.fn.extend({
        printthis:function (args) {
            console.log(args);
            console.log(this[0]); //this stand for fn, current element
            console.log(this); //this stand for fn, current element
        }
    });
})($)