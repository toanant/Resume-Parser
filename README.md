Pre-requisites:
==============

*   It needs [Xpdf](http://www.foolabs.com/xpdf/) to be installed and available at command prompt.
*   It needs MongoDB installed and running on system along with pymongo Driver.
*   It needs certain standard to be followed followed in designing resume :

  * Every titles like name, email, skills must have **' :'** (space + colon) after itself.
    
  * Only titles at Initial level have Colon with spaces in the entire Resume.

Setup:
=====

    $ git clone git@github.com:toanant/Resume-Parser.git
    $ cd Resume-Parser/src
    $ cp <Path/TO/resume.pdf> .
    $ vim db_setup.py (change the database name and collection name accordingly.)
    $ python cvparser.py
    
    
Features:
========

* If Resume is designed as per sample pdf file with only Titles with colon (**:**) it will parse them and store the result in Mongo database collection.

TODO: 
====

* Add logic for more robust data cleaning.
* Add support for other formats also.
