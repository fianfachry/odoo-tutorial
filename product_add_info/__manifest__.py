# product_add_info/__manifest__.py

{
    'name': 'Product Additional Info',
    'version': '14.0.1.0.0',
    'author': 'Your Name',
    'category': 'Product',
    'summary': 'Adds additional information to products',
    'depends': ['base', 'product'],
    'data': [
        'views/product_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
