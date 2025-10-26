"""

On day 66, we create an API that serves data on cafes with wifi and good coffee. Today, you're going to use the data from that project to build a fully-fledged website to display the information. 

Using this database and what you learnt about REST APIs and web development, create a website that uses this data. It should display the cafes, but it could also allow people to add new cafes or delete cafes.




Database Structure
Database Type: SQLite 3.x
Table: cafe
Columns:

id: INTEGER (Primary Key) - Unique identifier for each cafe
name: VARCHAR(250) NOT NULL - Name of the cafe
map_url: VARCHAR(500) NOT NULL - Google Maps URL link
img_url: VARCHAR(500) NOT NULL - URL to cafe image
location: VARCHAR(250) NOT NULL - Area/neighborhood location
has_sockets: BOOLEAN NOT NULL - Whether the cafe has power outlets
has_toilet: BOOLEAN NOT NULL - Whether the cafe has restrooms
has_wifi: BOOLEAN NOT NULL - Whether the cafe offers WiFi
can_take_calls: BOOLEAN NOT NULL - Whether it's suitable for phone calls
seats: VARCHAR(250) NULL - Number/range of available seats
coffee_price: VARCHAR(250) NULL - Price of coffee

Data Summary:

Total records: 21 cafes
All cafes appear to be in London (based on the sample data showing London Bridge, Peckham areas)
The database tracks amenities useful for remote workers/students (WiFi, sockets, call-friendliness)

The database is designed to help people find cafes suitable for working or studying, with key information about facilities and pricing.
"""