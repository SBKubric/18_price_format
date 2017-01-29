import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser(description='This tiny script transforms given float price value 1234.000000'
                                                 ' to prettier pattern like 1 234.')
    parser.add_argument('price', help='The value of such format 1234.000000')
    return parser.parse_args()


def format_price(price):
    price_pattern = r"\d+([.,])?\d*$"
    if not isinstance(price, str):
        raise TypeError('The price should be type of string.')
    if re.match(price_pattern, price) is None:
        raise ValueError('String has wrong pattern.')
    price.replace(',', '.')
    price_parts = price.split('.')
    int_part_price = int(price_parts[0])
    float_part_price = float(price) - int_part_price
    formatted_int = '{:,}'.format(int_part_price).replace(',', ' ')
    formatted_float = '{:.2f}'.format(float_part_price)[1:]
    if float(price).is_integer():
        return formatted_int
    else:
        return '{}{}'.format(formatted_int, formatted_float)


if __name__ == '__main__':
    args = parse_args()
    print('Formatted price: {}'.format(format_price(args.price)))
