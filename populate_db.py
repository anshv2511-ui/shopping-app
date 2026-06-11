import os
import django
import random
from decimal import Decimal

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_project.settings')
django.setup()

from shop.models import Category, Product

def populate():
    # Define categories
    category_data = [
        {'name': 'Electronics', 'description': 'Gadgets, smartphones, and computers.'},
        {'name': 'Clothing', 'description': 'Men and Women apparel and accessories.'},
        {'name': 'Home & Kitchen', 'description': 'Furniture, decor, and appliances.'},
        {'name': 'Books', 'description': 'Educational, fiction, and non-fiction books.'},
    ]

    # Create Categories
    categories = {}
    for cat_info in category_data:
        cat, created = Category.objects.get_or_create(
            name=cat_info['name'],
            defaults={'description': cat_info['description']}
        )
        categories[cat.name] = cat
        if created:
            print(f"Created category: {cat.name}")

    # Define products
    product_data = [
        # Electronics
        {
            'name': 'Wireless Noise-Cancelling Headphones',
            'description': 'Premium over-ear headphones with active noise cancellation and 30-hour battery life.',
            'price': '299.99',
            'category': categories['Electronics'],
            'stock': 45
        },
        {
            'name': 'Smartwatch Series 8',
            'description': 'Advanced health tracking, water resistant, and bright Always-On display.',
            'price': '399.00',
            'category': categories['Electronics'],
            'stock': 20
        },
        {
            'name': '4K Ultra HD Smart TV',
            'description': '55-inch smart TV with vivid colors and built-in streaming apps.',
            'price': '450.50',
            'category': categories['Electronics'],
            'stock': 12
        },
        # Clothing
        {
            'name': 'Classic Denim Jacket',
            'description': 'Vintage style blue denim jacket for everyday casual wear. 100% cotton.',
            'price': '59.99',
            'category': categories['Clothing'],
            'stock': 80
        },
        {
            'name': 'Performance Running Shoes',
            'description': 'Lightweight and breathable running shoes designed for maximum comfort on the track.',
            'price': '119.95',
            'category': categories['Clothing'],
            'stock': 35
        },
        # Home & Kitchen
        {
            'name': 'Programmable Coffee Maker',
            'description': '12-cup stainless steel coffee maker with auto-brew functionality.',
            'price': '89.00',
            'category': categories['Home & Kitchen'],
            'stock': 60
        },
        {
            'name': 'Ergonomic Office Chair',
            'description': 'Adjustable mesh office chair providing excellent lumbar support.',
            'price': '210.00',
            'category': categories['Home & Kitchen'],
            'stock': 15
        },
        # Books
        {
            'name': 'The Python Crash Course',
            'description': 'A hands-on, project-based introduction to programming using Python.',
            'price': '35.50',
            'category': categories['Books'],
            'stock': 100
        },
        {
            'name': 'Clean Code: A Handbook',
            'description': 'Principles, patterns, and practices of writing clean software.',
            'price': '42.99',
            'category': categories['Books'],
            'stock': 25
        }
    ]

    # Create Products
    for p_info in product_data:
        prod, created = Product.objects.get_or_create(
            name=p_info['name'],
            defaults={
                'description': p_info['description'],
                'price': Decimal(p_info['price']),
                'category': p_info['category'],
                'stock': p_info['stock'],
                'available': True
            }
        )
        if created:
            print(f"Created product: {prod.name}")

    print("Success! Database populated with sample categories and products.")

if __name__ == '__main__':
    print("Starting database population script...")
    populate()
