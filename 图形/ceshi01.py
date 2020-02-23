import qrcode
img = qrcode.make('说的就是你！ 不要整天扫啊扫啊，会中毒的！')
img.save('test.png')


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('hello, qrcode')
qr.make(fit=True)
img = qr.make_image()
img.save('123.png')