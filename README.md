# Abnormal Loads Permit System (AVP System)

## Overview
The Abnormal Loads Permit System (AVP System) is a Django-based web application designed to streamline the management and processing of abnormal load permits. The system offers various modules for creating, managing, and issuing permits, as well as handling user management, reporting, and payment processing.

## Features
- **Permit Management**: Create, amend, issue, cancel, and print permits for abnormal loads.
- **User Management**: Admin interface for managing users, roles, and permissions.
- **Reports**: Generate monthly, ad-hoc, custom, and traffic escort reports.
- **Payment Processing**: Simulate payments via various methods, including Visa, Mastercard, EFT, mobile wallets, Apple Pay, and Google Pay.
- **Security**: Role-based access control and secure authentication.

## File Structure
```
Abnormal_Loads/
├── avp_system/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   ├── templates/
│   │   ├── user_management/
│   │   ├── ad_hoc_reports.html
│   │   ├── amend_permit.html
│   │   ├── base.html
│   │   ├── cancel_permit.html
│   │   ├── create_permit.html
│   │   ├── custom_reports.html
│   │   ├── data_management.html
│   │   ├── day_end_report.html
│   │   ├── fee_breakdown.html
│   │   ├── help_support.html
│   │   ├── home.html
│   │   ├── index.html
│   │   ├── issue_permit.html
│   │   ├── login.html
│   │   ├── monthly_reports.html
│   │   ├── payment_success.html
│   │   ├── payment.html
│   │   ├── print_permit.html
│   │   ├── security.html
│   │   ├── settings.html
│   │   ├── traffic_escort_report.html
│   │   ├── user_management.html
│   │   └── view_permits.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── docs/
├── db.sqlite3
├── env/
├── .gitignore
├── dockerfile
└── manage.py
```

## Setup Instructions

### Prerequisites
- Python 3.9+
- Django 5.1.5
- Virtual environment (recommended)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/abnormal_loads_project.git
   cd abnormal_loads_project
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the application at `http://127.0.0.1:8000/`.

## Usage
### Payment Simulation
- The payment module supports multiple methods including:
  - **Credit/Debit Card**: Visa, Mastercard (requires card details input).
  - **Bank Transfer**: Simulated via direct transfer.
  - **Mobile Wallet**: Supports Vodapay, MTN, and Airtel wallets.
  - **Apple Pay and Google Pay**: Simulated with one-click payment.

### Generating Reports
- Navigate to the reports section to generate monthly, ad-hoc, or custom reports based on user requirements.

### User Management
- Admin users can manage other users, assign roles, and define access permissions.

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or support, please contact:
- **Hlulani Trevor Nkuna**
- **Email**: [hnkuna@csir.co.za]
- **Company**: Council Ffor Scientific and Industrial Research
