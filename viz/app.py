import httplib2
import webapp2
from google.appengine.ext.webapp import template
from apiclient.discovery import build
from oauth2client.appengine import AppAssertionCredentials
import json

url = 'https://www.googleapis.com/auth/bigquery'
PROJECT_NUMBER = 'your_gcp_project_id'

credentials = AppAssertionCredentials(scope=url)
httpss = credentials.authorize(httplib2.Http())
bigquery_service = build('bigquery','v2',http=httpss)

class ShowChartPage(webapp2.RequestHandler):
    def get(self):
	temp_data = {}
	temp_path = 'Templates/chart.html'
	queryData = {'query':'SELECT word FROM [publicdata:samples.shakespeare] LIMIT 1000'}
	tableData = bigquery_service.jobs()
	response = tableData.query(projectId=PROJECT_NUMBER,body=queryData).execute()
	self.response.out.write(response)
	#self.response.out.write(template.render(temp_path,temp_data))
	
class ShowHome(webapp2.RequestHandler):
    def get(self):
        template_data = {}
        template_path = 'Templates/index.html'
        self.response.out.write(template.render(template_path,template_data))


class GetChartData(webapp2.RequestHandler):
  def get(self):
    inputData = self.request.get("inputData")
    queryData = {'query':'SELECT SUM(word_count) as WCount,corpus_date,group_concat(corpus) as Work FROM '
'[publicdata:samples.shakespeare] WHERE word="'+inputData+'" and corpus_date>0 GROUP BY corpus_date ORDER BY WCount'}
    tableData = bigquery_service.jobs()
    dataList = tableData.query(projectId=PROJECT_NUMBER,body=queryData).execute()
    
    resp = []
    if 'rows' in dataList:
      for row in dataList['rows']:
        for key,dict_list in row.iteritems():
          count = dict_list[0]
          year = dict_list[1]
          corpus = dict_list[2]
          resp.append({'count': count['v'],'year':year['v'],'corpus':corpus['v']})
    else:
      resp.append({'count':'0','year':'0','corpus':'0'})
    
 	
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(resp))

class GetSupplyDataActual(webapp2.RequestHandler):
  def get(self):
    inputData = self.request.get("inputData")
    queryData = {'query':'SELECT User, Date, Building, SUM(Seats) as Seats FROM [interface.source_supply] '
    'GROUP BY User, Date, Building ORDER BY User, Date, Building'}
    tableData = bigquery_service.jobs()
    dataList = tableData.query(projectId=PROJECT_NUMBER,body=queryData).execute()
    
    resp = []
    if 'rows' in dataList:
      for row in dataList['rows']:
        for key,dict_list in row.iteritems():
          User = dict_list[0]
          Date = dict_list[1]
          Building = dict_list[2]
          Seats = dict_list[3]
          resp.append({'User': User['v'], 'Date':Date['v'], 'Building':Building['v'], 'Seats':Seats['v']})
    else:
      resp.append({'User':'0','Date':'0','Building':'0','Seats':'0'})
    
 	
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(resp))

class GetSupplyDataForecast(webapp2.RequestHandler):
  def get(self):
    inputData = self.request.get("inputData")
    queryData = {'query':'SELECT User, Date, Building, SUM(Seats) as Seats FROM [interface.supply_forecast] '
    'GROUP BY User, Date, Building ORDER BY User, Date, Building'}
    tableData = bigquery_service.jobs()
    dataList = tableData.query(projectId=PROJECT_NUMBER,body=queryData).execute()
    
    resp = []
    if 'rows' in dataList:
      for row in dataList['rows']:
        for key,dict_list in row.iteritems():
          User = dict_list[0]
          Date = dict_list[1]
          Building = dict_list[2]
          Seats = dict_list[3]
          resp.append({'User': User['v'], 'Date':Date['v'], 'Building':Building['v'], 'Seats':Seats['v']})
    else:
      resp.append({'User':'0','Date':'0','Building':'0','Seats':'0'})
    
 	
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(resp))

class GetChartData2(webapp2.RequestHandler):
  def get(self):
    inputData = self.request.get("inputData")
    queryData = {'query':'SELECT Date, SUM(Seats) as Seats FROM [interface.supply_forecast] '
    ' GROUP BY Date ORDER BY Date'}
    tableData = bigquery_service.jobs()
    dataList = tableData.query(projectId=PROJECT_NUMBER,body=queryData).execute()
    
    resp = []
    if 'rows' in dataList:
      for row in dataList['rows']:
        for key,dict_list in row.iteritems():
          Date = dict_list[0]
          Seats = dict_list[1]
          resp.append({'Date': Date['v'], 'Seats':Seats['v']})
    else:
      resp.append({'Date':'0','Seats':'0'})
      #resp = {"jsonarray":[{'Date':'0','Seats':'0'}]}
    resp_full = {"jsonarray":resp}
    
 	
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(resp_full))

class GetChartData3(webapp2.RequestHandler):
  def get(self):
    inputData = self.request.get("inputData")
    queryData = {'query':'SELECT Date, SUM(Seats) as Seats FROM [interface.supply_forecast] '
    'WHERE User = "'+inputData+'" GROUP BY Date ORDER BY Date'}
    tableData = bigquery_service.jobs()
    dataList = tableData.query(projectId=PROJECT_NUMBER,body=queryData).execute()
    
    resp = []
    if 'rows' in dataList:
      for row in dataList['rows']:
        for key,dict_list in row.iteritems():
          Date = dict_list[0]
          Seats = dict_list[1]
          resp.append({'Date': Date['v'], 'Seats':Seats['v']})
    else:
      resp.append({'Date':'0','Seats':'0'})
      #resp = {"jsonarray":[{'Date':'0','Seats':'0'}]}
    resp_full = {"jsonarray":resp}
    
 	
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(resp_full))

class DisplayChart(webapp2.RequestHandler):
  def get(self):
    template_data = {}
    template_path = 'Templates/displayChart.html'
    self.response.out.write(template.render(template_path,template_data))

class DisplayChart3(webapp2.RequestHandler):
  def get(self):
    template_data = {}
    template_path = 'Templates/displayChart_3.html'
    self.response.out.write(template.render(template_path,template_data))
    

class DisplayChart4(webapp2.RequestHandler):
  def get(self):
    template_data = {}
    template_path = 'Templates/displayChart_4.html'
    self.response.out.write(template.render(template_path,template_data))
     
 
application = webapp2.WSGIApplication([
    #('/chart',ShowChartPage),
    #('/displayChart',DisplayChart),
    #('/displayChart3',DisplayChart3),
    #('/displayChart4',DisplayChart4),
    ('/getChartData',GetChartData),
    ('/getSupplyDataActual',GetSupplyDataActual),
    ('/getSupplyDataForecast',GetSupplyDataForecast),
    ('/getChartData3',GetChartData3),
    ('/', ShowHome),
], debug=True)
