建议测试过程



/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/lee/PycharmProjects/python_learn/day02_car/car.py
/Users/lee/PycharmProjects/python_learn/day02_car/car.py:89: SyntaxWarning: name 'break_outer_for_flag' is used prior to global declaration
  global break_outer_for_flag
/Users/lee/PycharmProjects/python_learn/day02_car/car.py:290: SyntaxWarning: name 'user_logined' is assigned to before global declaration
  global user_logined
/Users/lee/PycharmProjects/python_learn/day02_car/car.py:291: SyntaxWarning: name 'exit_flag' is assigned to before global declaration
  global exit_flag
username:yangli
password:123456
welcome yangli
cmd(type ? for help):ls
家用电器
pc
cmd(type ? for help):cd pc
cmd is cd
game
inone
normal
cmd(type ? for help):cd game
cmd is cd

                                        ---------------------
                                        name: lennovo
                                        price: 5499
                                        store: 20


                                        ---------------------
                                        name: dall
                                        price: 5999
                                        store: 20


                                        ---------------------
                                        name: mechrevo
                                        price: 6100
                                        store: 30

cmd(type ? for help):addtocar dall
second_args dall
add to my car success
cmd(type ? for help):addtocaat lennovo
try help body
cmd(type ? for help):addtocar lennovo
second_args lennovo
add to my car success
cmd(type ? for help):addtocar bucunzai
second_args bucunzai
this product is not exist
cmd(type ? for help):
cmd(type ? for help):cd dall
cmd is cd
there is no more , you can [cd ..]

                                        ---------------------
                                        name: lennovo
                                        price: 5499
                                        store: 20


                                        ---------------------
                                        name: dall
                                        price: 5999
                                        store: 20


                                        ---------------------
                                        name: mechrevo
                                        price: 6100
                                        store: 30

cmd(type ? for help):
cmd(type ? for help):cd ..
cmd is cd
game
inone
normal
cmd(type ? for help):cd ..
cmd is cd
家用电器
pc
cmd(type ? for help):cd ..
cmd is cd
you can not cd ..
家用电器
pc
cmd(type ? for help):
cmd(type ? for help):shop
money is not enough
total_price_current_time 11498.000000
mymoney 5000.000000
cmd(type ? for help):
cmd(type ? for help):
cmd(type ? for help):earn
how much earn this time:bushishuzi
must be numeric
how much earn this time:99999
cmd(type ? for help):
cmd(type ? for help):shop
shop_car_json: ["pc_game_dall", "pc_game_lennovo"]
shop_car ['pc_game_dall', 'pc_game_lennovo']
shop success
cmd(type ? for help):
cmd(type ? for help):mycenter
----------------------
                                        username:yangli
                                        price:93501.0


cmd(type ? for help):help

        ls  == list
        cd  == change current direction
        pwd == print current direction
        addtocar ==  add product to car
        showcar == show what's in shop car
        mycenter == show user information center
        earn  ==  earn money
        shop  == clear shop car and sub your money
        history  == history shoped


cmd(type ? for help):showcar
[]
cmd(type ? for help):
cmd(type ? for help):exit
0 pc_game_dall
1 pc_game_lennovo

Process finished with exit code 0