from datetime import date, timedelta

def display_current_datetime():
	current_date = datetime.datetime.now()
	formatted_date =  current_date.strftime("%Y-%m-%d %H:%M:%S")
	print(formated_date)


def calculate_future_date(days):
	current_date = datetime.date.today()
	future_date = current_date + datetime.timedelta(days=days)
	print("The future date is:", future_date.strftime("%Y-%m-%d %H:%M:%S"))

days_input = int(input("Enter the number of days:"))
calculate_future_date(days_input)
