import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser(description='This tiny script transforms given float price value 1234.000000'
                                                 ' to prettier pattern like 1 234.')
    parser.add_argument('price', help='The value of such format 1234.000000')
    return parser.parse_args()


def format_price(price):
    price_pattern = r"\d+([.,])?\d*$"
    price = str(price)
    if re.match(price_pattern, price) is None:
        raise ValueError('Price has wrong pattern.')
    price = price.replace(',', '.')
    int_part_price = int(price.split('.')[0])
    float_part_price = float(price) - int_part_price
    formatted_float = '{:.2f}'.format(float_part_price)
    float_part_rounded = 1 if formatted_float == '1.00' else 0
    formatted_int = '{:,}'.format(int_part_price + float_part_rounded).replace(',', ' ')
    if float(formatted_float).is_integer():
        return formatted_int
    else:
        return '{}{}'.format(formatted_int, formatted_float[1:])


if __name__ == '__main__':
    args = parse_args()
    print('Formatted price: {}'.format(format_price(args.price)))