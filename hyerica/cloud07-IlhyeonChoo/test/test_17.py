import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_17 import create_products, filter_category

def test():
    data_list = [(1, 'Laptop', 1000, 'Electronics'), (2, 'Python Programming', 2000, 'Books'), (3, 'Chocolate', 3000, 'Food')]
    p_list = create_products(data_list)
    item = filter_category(p_list, 'Books')
    assert item[0].product_id == 2