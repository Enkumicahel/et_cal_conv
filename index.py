import os
import cherrypy
from my_ip import get_ip_address

from ethiopian_date import EthiopianDateConverter

INTERFACE = 'wlp2s0'
PORT = 8089
myip = get_ip_address(INTERFACE)

class EthDateConverter(object):

    @cherrypy.expose
    def index(self):
        return """
            <html>
                <body style='text-align: center;'>
                    <div>
                        <h2 style='color: #6ff;'>Ethiopian Date to convertor</h2>
                        <h3 style='color: #6ff;'>API Docs</h3>
                    </div>
                    <div>
                        <p>
                            Required params: 
                        </p>
                        <p>
                            <span>year,</span>
                            <span>month,</span>
                            <span>date,</span>
                        </p>
                        <p>
                            Return value: 
                        </p>
                        <p>
                            Type (JSON) => (e.g) result: [2026, 11, 13]
                        </p>
                        <p>
                            Usage:
                        </p>
                        <p>
                            To convert Gregorian calender to Ethiopian calender
                        </p>
                        <p>
                            <a href='http://{}:{}/to_greg?year=2019&amp;month=03&amp;date=04'> 
                                http://{}:{}/<strong>to_greg?year=2019&amp;month=03&amp;date=04</strong> 
                            </a>
                        </p>
                        <p>
                            To convert Ethiopian calender to Gregorian calender
                        </p>
                        <p>
                            <a href='http://{}:{}/to_et?year=2019&amp;month=03&amp;date=04'> 
                                http://{}:{}/<strong>to_et?year=2019&amp;month=03&amp;date=04</strong> 
                            </a>
                        </p>
                    </div>
                </body>
            </html>
        """.format(myip, PORT, myip, PORT, myip, PORT, myip, PORT)
        # pass

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def to_greg(self, year, month, date):
        edc = EthiopianDateConverter()
        year = int(year)
        month = int(month)
        date= int(date)
        c_date = edc.to_gregorian(year, month, date)
        print(c_date, type(c_date))
        return { 'result': c_date  }
        
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def to_et(self, year, month, date):
        edc = EthiopianDateConverter()
        year = int(year)
        month = int(month)
        date= int(date)
        c_date = edc.to_ethiopian(year, month, date)
        print(c_date, type(c_date))
        return { 'result': c_date  }
		# return c_date



if __name__ == '__main__':

    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
    }

    cherrypy.config.update({
        'server.socket_host': myip,
        'server.socket_port': PORT,
        'server.max_request_body_size': 0,
        'server.socket_timeout': 60,
    })

    webapp = EthDateConverter()

    cherrypy.quickstart(webapp, '/', conf)
