/**
 * Created by lee on 16/10/16.
 */


// 采用自执行函数的方式隔离作用域
(function (jq) {
    jq.extend({
        max:function (a,b) {
            console.log("$.extends({})")
            if(a > b){
                return a;
            }else {
                return b;
            }
        },
        min:function (a,b) {
            if (a < b){
                return a;
            }else {
                return b;
            }
        }
    })
})($)
