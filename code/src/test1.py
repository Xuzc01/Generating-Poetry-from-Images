import nn_process
import time
import os
import sys

DEFAULT_PATH = '../images/test.jpg'

def get_poem(image_file):
    """Generate a poem from the image whose filename is `image_file`

    Parameters
    ----------
    image_file : str
        Path to the input image

    Returns
    -------
    str
        Generated Poem
    """
    # Check whether the file exists
    assert os.path.exists(image_file), FileNotFoundError(
            'File `{}` not found.'.format(image_file))
    assert not os.path.isdir(image_file), FileNotFoundError(
            'The path should be a filename instead of `{}`.'.format(image_file))
    img_feature = extract_feature(image_file)
    return generate_poem(img_feature)

if __name__ == '__main__':
    # 多进程的部分需要放在这里
    print('Loading Extracting Feature Module...')
    extract_feature = nn_process.create('extract_feature')
    
    print('Loading Generating Poem Module...')
    generate_poem = nn_process.create('generate_poem')
    
    while True:
        try:
            s = input(f"Please input the path to an image [default='{DEFAULT_PATH}']: ")
            if not s:
                s = DEFAULT_PATH
            tic = time.time()
            poem = get_poem(s)
            print('\n' + poem[0].replace('\n', '\n') + '\n')
            print(f"Cost Time: {time.time() - tic}")
        except Exception as e:
            print(e)
