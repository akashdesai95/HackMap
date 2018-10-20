import scrapy
from geopy.geocoders import Nominatim
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import gmplot
import os
from bs4 import BeautifulSoup

class HeadphonesSpider(scrapy.Spider):

    name = "headphones"

    def start_requests(self):
        urls = [
        'https://mlh.io/seasons/na-2018/events',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fig = plt.figure(figsize=(8, 8))
        hackathon_name = response.css('h3::text').extract()
        hackathon_city=response.css('span[itemprop="addressLocality"]::text').extract()
        hackathon_state=response.css('span[itemprop="addressRegion"]::text').extract()
        hackathon_link = response.css('a[class="event-link"]::attr(href)').extract()
        longitude=[]
        latitude=[]


        with open('hackmap.txt', 'w') as f:
            for name,city,state,link in zip(hackathon_name,hackathon_city,hackathon_state,hackathon_link):
                geolocator = Nominatim(user_agent="specify_your_app_name_here")

                if city!="Everywhere":
                    location = geolocator.geocode(city + "," + state, timeout=None)
                    longitude.append(location.longitude)
                    latitude.append(location.latitude)
                    f.write(name + "::(" +city+","+state+")::Link--"+link+"::("+str(location.latitude)+","+str(location.longitude)+")\n")

                    # Map (long, lat) to (x, y) for plotting
                    yield {
                        'name': name,
                        'city': city,
                        'state': state,
                        'longitude': location.longitude,
                        'latitude': location.latitude
                    }
                else:
                    longitude.append(0)
                    latitude.append(0)
                    f.write(name + "::(" + city + "," + state + ")::Link--" + link + "::(None)" + "\n")
                    yield {
                        'name': name,
                        'city': city,
                        'state': state,
                        'longitude': 0,
                        'latitude': 0
                    }
                # +location.latitute+","+location.longitude+")"+"\n")
        """
             fig = plt.figure(figsize=(8, 8))
             m = Basemap(projection='lcc', resolution=None,
                        width=8E6, height=8E6,
                        lat_0=45, lon_0=-100, )
            m.etopo(scale=0.5, alpha=0.5)
        
        
        gmaps.configure(api_key="AIzaSyBLqmMW7A7XIlNL04XL64Xz47War4Tu9fc")
        earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
        earthquake_df.head()
        locations = earthquake_df[['latitude', 'longitude']]
        weights = earthquake_df['magnitude']
        fig = gmaps.figure()
        fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
        fig

        
            gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
            gmap.scatter(latitude, longitude, '# FF0000',
                          size=40, marker=False)
            gmap.draw("mymap.html")"""
        """   
           map = Basemap(projection='ortho', resolution=None,
                            width=8E6, height=8E6,
                            lat_0=45, lon_0=-100, )

            map.drawcoastlines()
            map.drawcountries()
            map.fillcontinents(color='coral')

            x, y =map(longitude,latitude)

            map.plot(x, y, 'ok', markersize=5)
            #map.text(x, y, city, fontsize=12)
            plt.show(block=True)
        """
        """ 
            x, y = m(longitude, latitude)
            plt.plot(x, y, 'ok', markersize=5)
            for x,y,label in zip(x,y,hackathon_city):
                plt.text(x, y, label, fontsize=12);
            plt.show(block=True)
        """
        # import gmplot package



        """
        gmap3 = gmplot.GoogleMapPlotter(40.7128, 74.0060,13,api_key=)

        # scatter method of map object
        # scatter points on the google map
        gmap3.scatter(latitude, longitude, '# FF0000',
                      size=40, marker=False)

        # Plot method Draw a line in
        # between given coordinates
        #gmap3.plot(latitude, longitude_list,
         #          'cornflowerblue', edge_width=2.5)

        gmap3.draw("mymap.html")
        os.system("mymap.html")
        """
