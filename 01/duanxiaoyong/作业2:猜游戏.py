# /usr/bin/env python
# -*- coding: utf-8 -*-
# auth: duanxiaoyong

import random
num_random = random.randint(0,100)
count = 1
while True:
    input_num = int(input('游戏限制输入5次结束，请慎重输入>>'))
    if input_num ==num_random:
        print('高手！猜对了')
        break
    elif input_num > num_random:
        print('猜大了！！小伙伴')
    else:
        print('猜小了！！小伙伴')
    count =count+1
    if count > 5:
        print('太笨了，下次再来，正确的数字是',int(num_random))
        break