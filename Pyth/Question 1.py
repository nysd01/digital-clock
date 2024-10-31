import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import csv
    
# Load employee data from CSV file
def load_employee_data(filename):
    employees = []
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['birthday'] = datetime.datetime.strptime(row['birthday'], '%Y-%m-%d').date()
            employees.append(row)
    return employees

# Check if today is any employee's birthday
def check_birthdays(employees):
    today = datetime.date.today()
    birthdays_today = [emp for emp in employees if emp['birthday'].month == today.month and emp['birthday'].day == today.day]
    return birthdays_today

# Send a birthday email to the employee
def send_birthday_email(employee, sender_email, sender_password):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = employee['email']
        msg['Subject'] = "Happy Birthday!"
        
        body = f"Dear {employee['name']},\n\nWishing you a wonderful birthday!\n\nBest regards,\nYour Company"
        msg.attach(MIMEText(body, 'plain'))
        
        # Set up SMTP server (example using Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        server.send_message(msg)
        server.quit()
        
        print(f"Birthday email sent to {employee['name']}")
    except Exception as e:
        print(f"Failed to send email to {employee['name']}: {e}")

# Main function to orchestrate the flow of the program
def main():
    # Load employee data from a CSV file
    employees = load_employee_data('employees.csv')

    # Check for birthdays today
    birthdays_today = check_birthdays(employees)
    
    if birthdays_today:
        # Email credentials
        sender_email = 'nysdderek@gmail.com'
        sender_password = 'zjlg ccxl vkzg ppne'
        
        # Send emails to those who have birthdays today
        for employee in birthdays_today:
            send_birthday_email(employee, sender_email, sender_password)
    else:
        print("No birthdays today.")

# Run the main function
if __name__ == "__main__":
    main()
