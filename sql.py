## create tables and insert data
## this file can be optimzed in the future

table_annualticketsales = ('''
  create table if not exists petl1.annualticketsales(
  sales_year int,
  ticket_sold varchar,
  total_box_office money,
  total_inflation_adjusted_box_office money,
  average_ticket_price money
  )
  ;
''')
table_highestgrossers = ('''
  create table if not exists petl1.highestgrossers(
  year int,
  movie varchar (60),
  genre varchar (20),
  MPAA_rating varchar (10),
  distributor varchar (50),
  total_for_year money,
  total_in_2019_dollars money,
  tickets_sold money
  )
  ;
''')
table_popularcreativetypes = ('''
  create table if not exists petl1.popularcreativetypes(
  rank int,
  creative_types varchar (50),
  movies varchar (20),
  total_cross money,
  average_cross money,
  market_share varchar (10)
  )
  ;
''')
table_topdistributors = ('''
  create table if not exists petl1.topdistributors(
  rank int,
  distributors varchar (50),
  movies int ,
  total_cross money,
  average_cross money,
  market_share varchar (10)
  )
  ;
''')
table_topgenres = ('''
  create table if not exists petl1.topgenres(
  rank int,
  genres varchar (50),
  movies varchar (20),
  total_cross money,
  average_cross money,
  market_share varchar (10)
  )
  ;
''')
table_topgrossingratings = ('''
  create table if not exists petl1.topgrossingratings(
  rank int,
  genres varchar (50),
  movies varchar (20),
  total_cross money,
  average_cross money,
  market_share varchar (10)
  )
  ;
''')
table_topgrossingsources = ('''
  create table if not exists petl1.topgrossingsources(
  rank int,
  sources varchar (50),
  movies varchar (20),
  total_cross money,
  average_cross money,
  market_share varchar (10)
  )
  ;
''')
table_topproductionmethods = ('''
  create table if not exists petl1.topproductionmethods(
  rank int,
  production_methods varchar (50),
  movies varchar (20),
  total_cross money,
  average_cross money,
  market_share varchar (10)
  )
  ;
''')
table_widereleasescount = ('''
  create table if not exists petl1.widereleasescount(
  year int,
  warner_bros int,
  walt_disney int,
  _28th_century_fox int,
  paramount_pictures int,
  sony_pictures int,
  universal int,
  total_major_6 int,
  total_other_studios int
  )
  ;
''')

insert_annualticketsales = ('''
  INSERT INTO petl1.annualticketsales
  VALUES(%s,%s,%s,%s,%s);
''')

insert_highestgrossers = ('''
  INSERT INTO petl1.highestgrossers
  VALUES(%s,%s,%s,%s,%s,%s,%s,%s);
''')

insert_popularcreativetypes = ('''
  INSERT INTO petl1.popularcreativetypes
  VALUES(%s,%s,%s,%s,%s,%s);
''')

insert_topdistributors = ('''
  INSERT INTO petl1.topdistributors
  VALUES(%s,%s,%s,%s,%s,%s);
''')

insert_topgenres = ('''
  INSERT INTO petl1.topgenres
  VALUES(%s,%s,%s,%s,%s,%s);
''')

insert_topgrossingratings = ('''
  INSERT INTO petl1.topgrossingratings
  VALUES(%s,%s,%s,%s,%s,%s);
''')

insert_topgrossingsources = ('''
  INSERT INTO petl1.topgrossingsources
  VALUES(%s,%s,%s,%s,%s,%s);
''')

insert_topproductionmethods = ('''
  INSERT INTO petl1.topproductionmethods
  VALUES(%s,%s,%s,%s,%s,%s);
''')

insert_widereleasescount = ('''
  INSERT INTO petl1.widereleasescount
  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);
''')
