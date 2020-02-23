import  qrcode
from PIL import  Image
import  os, sys
def gen_qrcode(string,path,logo="logo.png"):
    qr=qrcode.QRCode(
       version=1,
       error_correction=qrcode.constants.ERROR_CORRECT_H,
       box_size=8,
       border=1
    )
    qr.add_data(string)
    qr.make(fit=True)
    img=qr.make_image()
    img=img.convert("RGBA")
    if logo and os.path.exists(logo):
        try:
            icon=Image.open(logo)
            img_w,img_h=img.size
        except Exception as e:
            print(e)
            sys.exit(1)
        factor=4
        size_w=int(img_w/factor)
        size_h=int(img_h/factor)
        icon_w,icon_h=icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)
        w=int((img_w-icon_w)/2)
        h=int((img_h-icon_h)/2)
        icon=icon.convert("RGBA")
        # icon=icon.conver("RGBA")
        img.paste(icon,(w,h),icon)
        img.save(path)
if __name__=="__main__":
    info="ww维维王二维多去问问w"
    pic_path="qrcode.png"
    logo_path="logo.png"
    gen_qrcode(info,pic_path,logo_path)
