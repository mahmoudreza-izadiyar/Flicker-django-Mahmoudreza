# Flicker-Finder
This web site can get your locations and send you back all the pictures of your location in Flickr. 
this website has been build by Django framework (Python language)
To run this web site first you need to install django framework on your machine("pip install django")
Then clone the repo to you local directory. 
change the terminal address to the directory, and enter : py manage.py runserver

now web server will run on your machine locally in (http://127.0.0.1:8000/) . 
This website has Three main tabs in navbar:
Search, Add New Presets and Favourite List. 
in search tab user can search for location pictures by input lan and lon 
in Add Presets tab, user can add presets by insert the lat, lon and name for each preset. then user can use it in search.  


# Fuctions:
    Serch Function:
This function will receive the lat and lon input, will call Flickr API with KEY and SECRET, will send the lat and lon to flickr and receive and object, this object has contain information about all pictures have been taken on that location. Like the number of the pages, number of pictures and information of each photo. 
Then search function will open this object and find the information of photos individually, and build URL for each picture, store it in addresses variable and send it back. 
 
    searchByLatAndLon Function: 
This function will send lan and lon that user insert in search page directly to the search function and receive all addresses. Paginate all addresses to pages, 10 address for each page. Send it to the Django-template (UI)


    searchCities Function : 
This function will call Presets model, to receive all the cities that user stored. 
Will Find the Lat and lon o each location form Backend. 
Will Call search function with lat and lon an receive back all addresses and will send them to template. 


    Add Function: 
This function will receive name, lat and lon form user with a form and it will store it in the model in the backend. 

# Search:
    User can Search in two main ways,
     
     The first way is insert the Lat and Lon of the location directly in the fist form in index page. 
    and user will receive back 250 addresses of picture. These addresses goes to the lmages HTML tag and user can see the actuall pictures in pagination of 10 item in each page. 
     "searchByLatAndLon" fuction has the resposiblity to handle this. 
     this function will recieve the value of Lat and lon, send it to search function, and recevied all the photos addresses, then it will show all of them to user. in django-template, a loop will show all pages one by one.

     The second way is to chose location from presets drop down menu ,
    In this way all information of that location will send back to the server and will take back URLs of pictures, 
    Then these urls will send too template to shoe to the user. 

    
# Add Presets: 
    User can add new location with name, Lat and lon to the server.
    by input the values to the form, those inputs will store in a model in backend.



# views.py:
    in this file you can find all functions, API KEYs and SECRET KEY of api

# urls.py:
    this file has the  responsibility of handling urls of website.
    
# caution:
    Because of lack of time, Favorite List function uncompleted. Model for storing all the addresses has been created, to store the addresses of that user really like and after then, each time user will see the fav page, function call the data base model and will show all the addresses to the user.  
