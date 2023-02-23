import argparse
from detection import *

#main function to test different functions independently
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    ap.add_argument("-o", "--output", required=True, help="print the output info")
    args = ap.parse_args()

    load_model()
    load_text_model()

    result = detect(args.image, False)
    with open(args.output, mode='w', encoding='utf-8') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
