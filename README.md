# DZ_Django2
### A new application has been created with the following models:
- Store
- Book
- Author
- Publisher

### Their connections:

![](my_project_subsystem.png)


#### To fill the database with data, I recommend using the command "createss", the maximum amount of data for one command is 20.
#### To create connections between tables, I recommend executing the command several times "connections".

## Update dated 11/16/2022.

#### A new "mail" application in which "Celery" is implemented

## Update dated 11/20/2022.

#### A new "pars" application in which "Celery beat".


## Update dated 11/23/2022.

#### Updates in the annotate_aggregate application. Changed views from functions to class based views


## Update dated 11/29/2022.

#### Caching has been added to some views where it is "most necessary". 
#### Views with caching:
- store_in
- authors
- authors_in
- PublisherList
- PublisherDetail
- BookList
- BookDetail
#### Also added fixtures for models of the annotate_aggregate application for a quick start