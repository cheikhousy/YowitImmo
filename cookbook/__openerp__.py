{
 'name': "Cookbook",
    'summary': "Odoo can even make the cook!",
    'description': """
This module permit you to record recipes and to share them
on the internet.
""",
    'author': "S. Namèche",
    'category': 'Knowledge Management',
    'application': True,
    'version': '0.1',
    'licence': 'AGPL',
    'depends': ['base'],
    'data': ['data/cookbook.recipe.category.csv','recipe_view.xml',
    ],
    'demo': ['data/cookbook.recipe_demo.xml',
    ],

}
