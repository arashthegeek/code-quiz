# پلتفرم کوییز برنامه‌نویسی

یک پلتفرم وب برای کوییزهای برنامه‌نویسی که کاربران می‌توانند در آن ثبت‌نام کنند، در کوییزها شرکت کنند و بر اساس عملکرد خود رتبه دریافت کنند.

## ویژگی‌ها

- **ثبت‌نام و ورود کاربران**: کاربران می‌توانند حساب کاربری ایجاد کرده و وارد سیستم شوند تا در کوییزها شرکت کنند.
- **کوییزهای برنامه‌نویسی**: کاربران می‌توانند در کوییزهای مختلف مربوط به برنامه‌نویسی شرکت کنند.
- **سیستم رتبه‌بندی**: کاربران بر اساس عملکرد خود در کوییزها امتیاز کسب کرده و در جدول رده‌بندی نمایش داده می‌شوند.
- **پنل مدیریت**: مدیران می‌توانند کوییزها را ایجاد کرده، سوالات را مدیریت کرده و عملکرد کاربران را مشاهده کنند.

## تکنولوژی‌های مورد استفاده

- **بک‌اند**: Django (Python)
- **پایگاه داده**: SQLite (پیش‌فرض برای توسعه)
- **فرانت‌اند**: HTML، CSS، JavaScript
- **احراز هویت**: سیستم احراز هویت داخلی Django

## نصب

برای راه‌اندازی پروژه به صورت محلی، مراحل زیر را دنبال کنید:

### 1. کلون کردن مخزن

```bash
git clone https://github.com/yourusername/quiz-platform.git
cd quiz-platform
