Long = {'Bề ngoài' : 'Bình thường', 'Học vấn' : 'Bỏ ngang đại học', 'Tài chính' : 'Éo có gì'}

print(Long.setdefault('Tuổi', 24)) # setdefault(x, y) để xác định key có ở trong dictionary không
                                   # nếu không có thì thêm key vào

print(Long.setdefault('Tuổi', 200)) # tuy nhiên method này không đổi được value đã có trong key, nó chỉ thêm vào thôi

print(Long)



