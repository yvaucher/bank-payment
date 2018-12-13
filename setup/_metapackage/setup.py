import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-bank-payment",
    description="Meta package for oca-bank-payment Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_banking_mandate',
        'odoo12-addon-account_banking_pain_base',
        'odoo12-addon-account_payment_mode',
        'odoo12-addon-account_payment_order',
        'odoo12-addon-account_payment_partner',
        'odoo12-addon-account_payment_sale',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)