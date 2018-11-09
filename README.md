# ScriptTPM
1. Install crontab https://www.raspberrypi.org/documentation/linux/usage/cron.md
2. Install required packages under Ubuntu
These are the things we are going to need:

FreeTDS is is a set of libraries that allows programs to natively talk to Microsoft SQL Server databases. It’s what we usually call a driver.
UnixODBC acts as a driver manager and is the implementation of the ODBC API.
pyodbc is a Python 2.x and 3.x module that allows you to use ODBC to connect to almost any database.
From a terminal, run:
```
sudo apt-get install unixodbc unixodbc-dev freetds-dev tdsodbc
```
From the Virtualenv of our Python application (if you are not using one, you should!) run pip install pyodbc.

3. Setup server in FreeTDS’s settings
Edit the file */etc/freetds/freetds.conf* and replace placeholders appropriately. Note that we are calling our server sqlserver.
```
[sqlserver]
  host = ip address of the computer running SQL Server or name
  port = 1433  
  tds version = 7.0
```
After this you can test the connection with this command:
```
tsql -S sqlserver -U <username> -P <password>
```
Then run some SQL Server command to make sure everything works fine. For example you may run a DB query like this:
```
select * from <database name>.dbo.<table name>
go
```
If it worked, it will print the results of the query. Quit with Ctrl+D.

4. Setup unixODBC to use FreeTSD & add a data source
First, run *odbcinst -j* to know where our configuration files are located. We will need to edit two files: the “drivers” and “system data source”. I assume they are */etc/odbcinst.ini* and */etc/odbc.ini* respectively, but the output of the command will tell you this.

Edit */etc/odbcinst.ini* like this:
```
[FreeTDS]
Description = TDS driver (Sybase/MS SQL)
Some installations may differ in the paths
#Driver = /usr/lib/odbc/libtdsodbc.so
#Setup = /usr/lib/odbc/libtdsS.so
Driver = /usr/lib/arm-linux-gnueabihf/odbc/libtdsodbc.so
Setup = /usr/lib/arm-linux-gnueabihf/odbc/libtdsS.so
CPTimeout =
CPReuse =
FileUsage = 1
```
If the paths for Driver and Setup do not work in your installation, you can find where these files are located by running find / -name “libtds*“.

Edit */etc/odbc.ini* like this, to add a data source named sqlserverdatasource:
```
[sqlserverdatasource]
Driver = FreeTDS
Description = ODBC connection via FreeTDS
Trace = No
Server = sqlserver
Database = <name of your database>
```
Now you may test the connection to out data source works by running 
```
isql -v sqlserverdatasource
```
