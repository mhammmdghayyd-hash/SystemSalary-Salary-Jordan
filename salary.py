# نظام حساب الرواتب - الأردن
basic_salary = float(input("أدخل الراتب الأساسي: "))
overtime_hours = float(input("أدخل عدد ساعات الإضافي: "))

# الحسابات (سعر ساعة الإضافي 5 دنانير وخصم الضمان 7.5%)
overtime_pay = overtime_hours * 5.0
social_security = basic_salary * 0.075
net_salary = (basic_salary + overtime_pay) - social_security

print(f"الراتب الصافي النهائي هو: {net_salary} دينار")
