Long = {'Bề ngoài' : 'Bình thường', 'Học vấn' : 'Bỏ ngang đại học', 'Tài chính' : 'Éo có gì'}

# get(x, y) kiểm tra xem trong dictionary có lưu key này không

print(Long.get('Bề ngoài', 'Xấu')) # nếu có thì trả về x
print(Long.get('Tuổi', 24)) # không có thì trả về y

print('-----------------\n')

print('Long là một người có vẻ bên ngoài ' + Long.get('Bề ngoài', 0) + ' như vậy đó.')