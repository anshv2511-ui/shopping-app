# Django Shopping Application

A full-featured e-commerce shopping application built with Django and Python.

## Features

- **Product Catalog**: Browse products by category with search functionality
- **Shopping Cart**: Add, update, and remove items from cart
- **User Authentication**: Register, login, and logout functionality
- **Order Management**: Place orders and view order history
- **Admin Panel**: Manage products, categories, orders through Django admin
- **Responsive Design**: Mobile-friendly UI using Bootstrap 5

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Navigate to the project directory**:
   ```bash
   cd "c:\Users\HP\OneDrive\Desktop\Amazon"
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - On Windows (Command Prompt):
     ```cmd
     venv\Scripts\activate.bat
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (admin account):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### For Users

1. **Browse Products**: Visit the home page to see featured products
2. **Search**: Use the search bar to find specific products
3. **Filter by Category**: Click on categories to filter products
4. **Add to Cart**: Click "Add to Cart" button on any product
5. **Checkout**: Review your cart and proceed to checkout (login required)
6. **View Orders**: Access your order history from "My Orders"

### For Administrators

1. **Login to Admin Panel**: Go to http://127.0.0.1:8000/admin/
2. **Add Categories**: Create product categories
3. **Add Products**: Add products with images, prices, and descriptions
4. **Manage Orders**: View and update order statuses
5. **Manage Users**: View registered users

## Project Structure

```
Amazon/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── shopping_project/         # Main project settings
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── shop/                     # Shopping app
│   ├── __init__.py
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   └── context_processors.py # Custom context processors
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   └── shop/                # Shop-specific templates
│       ├── home.html
│       ├── product_list.html
│       ├── product_detail.html
│       ├── cart.html
│       ├── checkout.html
│       ├── order_list.html
│       ├── order_detail.html
│       ├── login.html
│       └── register.html
├── static/                   # Static files (CSS, JS)
│   ├── css/
│   └── js/
└── media/                    # User-uploaded files (product images)
```

## Models

### Category
- Name and description for product categories

### Product
- Name, description, price
- Category association
- Image upload
- Stock tracking
- Availability status

### Cart & CartItem
- User/session-based shopping cart
- Quantity management

### Order & OrderItem
- Order tracking with status
- Customer shipping information
- Order history

## Security Notes

**Important**: Before deploying to production:

1. Change the `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use a production database (PostgreSQL, MySQL)
5. Set up proper static file serving
6. Enable HTTPS
7. Configure secure session and cookie settings

## Technologies Used

- **Backend**: Django 4.2
- **Database**: SQLite (development) - upgrade to PostgreSQL/MySQL for production
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: Font Awesome 6
- **Image Processing**: Pillow

## Contributing

This is a learning project. Feel free to fork and modify as needed.

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please create an issue in the project repository.
