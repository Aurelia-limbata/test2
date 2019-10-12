from PIL import Image

src1 = Image.open('./kadai2.jpg')

print(src1.format)
print(src1.mode)
print(src1.size)
print(src1.getpixel((0,0)))

mx,my = src1.size

src2 = Image.new('RGB',(mx,my))

for i in range(2,mx-1):
    for j in range(2,my-1):
            rl,gl,bl = src1.getpixel((i,j-1))
            ru,gu,bu = src1.getpixel((i-1,j))
            r,g,b = src1.getpixel((i,j))
            rmax = 0
            if r> 0 and g > 0 and b > 0: #データの有無で条件分岐させる
                if r > g and r > b:
                    color = (r+100,int(g+100*g/r),int(b+100*b/r))
                    src2.putpixel((i,j),color)
                elif g > r and  g > b:
                    color = (int(r+100*r/g),g+100,int(b+100*b/g))
                    src2.putpixel((i,j),color)
                elif b > r and b > g:
                    color = (int(r+100*r/b),int(g+100*g/b),b+100)
                    src2.putpixel((i,j),color)#ここまでが色がすべて異なる場合
                elif r > g and g == b:
                    color = (r+100,int(g+100*g/r),int(b+100*b/r))
                    src2.putpixel((i,j),color)
                elif g > r and r == b:
                    color = (int(r+100*r/g),g+100,int(b+100*b/g))
                    src2.putpixel((i,j),color)
                elif b > r and r == g:
                    color = (int(r+100*r/b),int(g+100*g/b),b+100)
                    src2.putpixel((i,j),color)
                elif r < g and g == b:
                    color = (int(r+100*r/g),g+100,b+100)
                    src2.putpixel((i,j),color)
                elif g < r and r == b:
                    color = (r+100,int(g+100*g/r),b+100)
                    src2.putpixel((i,j),color)
                elif b < r and r == g:
                    color = (r+100,g+100,int(b+100*b/r))
                    src2.putpixel((i,j),color)#ここまでが色が１種類異なる場合
                else:
                    color = (r*(r+10),g*(g+10),b*(b+10))
                    src2.putpixel((i,j),color)#色がすべて同じである場合
                    
            else:
                color = (r,g,b)
                src2.putpixel((i,j),color)
                
src2.save('color2.2.png')
