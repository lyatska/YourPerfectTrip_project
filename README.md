# YourPerfectTrip_project
```Description```

This project is created to help people in choosing the most suitable variants of hotels and restaurants. You have an opportunity to choose the function that depends on your need. The first function is done for searching the cheapest hotel of desirable city, and the second one is for searching the most rated restaurants. The program is based on Goibibo API and Zomato API.

```Incoming and outgoing data```

To get necessary data needed for processing information program uses Goibibo API and Zomato API. After each user's request, the data returns in json format. The outgoing data displays on user's screen as a map with appropriate mark.

```Program structure```

The program consists of some modules. The arrays.py module has DynamicArray ADT that is used as helper in searching the most suitable variant of hotels. Module hotels.py has methods that help to get necessary data using Goibobo API and find needed information such as price, coordinates and title in json files that were created. The restaurants.py module is created for searching the most rated restaurants. As hotels.py it also helps to get information about hotels using Zomato API and search the best variants. The main.py module is the most important because it contains functions responsible for output of the program. This module hepls to create maps with appropriate marks of hotel or restaurants. The flaskgo.py module is needed for running program on Flask microframework and creating the program interface. It also worth adding that while implementation of the program some json files such as rating_restaurants.json, data.json and hotels.json are creating. (You can see examples on the main page of project). In the folder templates there are some html files such as site.html, proposition_res.html, proposition_hot.html, bestrestaurants.html and besthotels.html for program representation.

```Program usage```

You can use the program on PythonAnywhere: http://anastasiyka.pythonanywhere.com/ or just clonning the project and running it on your own computer using flaskgo.py module.

```Instructions of program using.```

 Step 1.
 
 The user have to choose the option he needs. It can be hotel search or restaurants search.
 
 ![](https://github.com/lyatska/YourPerfectTrip_project/blob/master/images/example1.jpg)
 
 Step 2 (hotel search)
 
 If user chooses restaurant function, he will get the page with entering field where he should put down the name of the needed city.
 
 ![](https://github.com/lyatska/YourPerfectTrip_project/blob/master/images/example2.jpg)
 ![](https://github.com/lyatska/YourPerfectTrip_project/blob/master/images/example3.jpg)
 
 Step 2 (restaurants search)
 
 If user chooses hotels function, he will get the page with entering field where he should put down the name of the needed city.
 
 ![](https://github.com/lyatska/YourPerfectTrip_project/blob/master/images/example4.jpg)
 ![](https://github.com/lyatska/YourPerfectTrip_project/blob/master/images/example5.jpg)
 
 
 Step 3 (hotel search)
 
 The user gets the map with mark of the cheapest hotel.
 
 ![](https://github.com/lyatska/YourPerfectTrip_project/blob/master/images/example6.jpg)
 
 Step 3 (restaurants search)
 
 The user gets the map with marks of the most rated restaurants.
 
 ![](https://github.com/lyatska/YourPerfectTrip_project/blob/master/images/example7.jpg)
 
 ```Documentation```
 
 Documentation is located in docs folder.
 https://github.com/lyatska/YourPerfectTrip_project/tree/master/docs/build/html/rst
 
```Developer```

Anastasiya Lyatska
