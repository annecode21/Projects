import os

def main():
    value = 1
    path = "/home/marianne/Pictures/"
    for filename in os.listdir(path):
        my_dest = f'wallpaper {value}.jpg'
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        value += 1
if __name__ == '__main__':
    main()
