'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import pygal
import lxml


x = 0
newdata = {}
datedata = []
highdata = []
lowdata = []

#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

if (chart_type == '1')
	bar_chart = pygal.Bar(x_label_rotation = 80)
	bar_chart.title = ("Stock Data Range from " + start_date + " to " + end_date)
	datedata.reverse()
	bar_chart.x_labels = datedata
	highdata.reverse()
	bar_chart.add('High', convert(highdata))
	lowdata.reverse()
	bar_chart.add('Low', convert(lowdata))
	bar_chart.render_in_browser()
	pass
if (chart_type == '2')
	line_chart = pygal.Line(x_label_rotation = 80)
	line_chart.title = ("Stock Data Range from " + start_date + " to " + end_date)
	datedata.reverse()
	line_chart.x_labels = datedata
	highdata.reverse()
	line_chart.add('High', convert(highdata))
	lowdata.reverse()
	line_chart.add('Low', convert(lowdata))
	line_chart.render_in_browser()
	pass