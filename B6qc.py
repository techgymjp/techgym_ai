import tensorflow as tf
import os

path_dataset = './dataset/'
dir_list = os.listdir(path_dataset)

def check_image(path):
    files = []
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            files.append(filename)
    
    for fn in files:
        print(fn)
        filepath = os.path.join(path, fn)
        try:
            with tf.Graph().as_default():
                image_contents = tf.read_file(filepath)
                image = tf.image.decode_jpeg(image_contents, channels=3)
                init_op = tf.initialize_all_tables()
                with tf.Session() as sess:
                    sess.run(init_op)
                    tmp = sess.run(image)
                    print('---OK!---')
        except:
            os.remove(filepath)
            print('---error file removed---')

for dirname in dir_list:
    print(dirname, '---check this folder image---')
    path = os.path.join(path_dataset ,dirname)
    check_image(path)