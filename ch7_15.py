msg1 = '人機對話專欄，告訴我心事吧，我會重覆你告訴我的心事!'
msg2 = '輸入q可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' +'= '
input_msg = ''
while input_msg != 'q':
    input_msg = input(msg)
    if input_msg != 'q':
        print(input_msg)