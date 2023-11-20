<h1 class="gap">0x0F. Python - Object-relational mapping</h1>


<h4 class="task">
    0. Get all states
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all <code>states</code> from the database <code>hbtn_0e_0_usa</code>: </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    1. Filter states
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all <code>states</code> with a <code>name</code> starting with <code>N</code> (upper N) from the database <code>hbtn_0e_0_usa</code>: </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    2. Filter states by user input
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that takes in an argument and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument.</p><ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use <code>format</code> to create the SQL query with the user input</li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    3. SQL Injection...
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Wait, do you remember the previous task? Did you test <code>"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"</code> as an input?</p>


<h4 class="task">
    4. Cities by states
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all <code>cities</code> from the database <code>hbtn_0e_4_usa</code> </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    5. All cities by state
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that takes in the name of a state as an argument and lists all <code>cities</code> of that state, using the database <code>hbtn_0e_4_usa</code> </p><ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name</code> (SQL injection free!)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    6. First state model
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p><img alt="ORM" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/283/63890860.jpg"/></p><p>Write a python file that contains the class definition of a <code>State</code> and an instance <code>Base = declarative_base()</code>:</p><ul>
<li><code>State</code> class:

<ul>
<li>inherits from <code>Base</code> <a href="/rltoken/YU9M_E7Fw1bZDIIE-t1xkg" target="_blank" title="Tips">Tips</a></li>
<li>links to the MySQL table <code>states</code></li>
<li>class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can’t be null and is a primary key</li>
<li>class attribute <code>name</code> that represents a column of a string with maximum 128 characters and can’t be null</li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li><strong>WARNING:</strong> all classes who inherit from <code>Base</code> <strong>must</strong> be imported before calling <code>Base.metadata.create_all(engine)</code></li>
</ul>


<h4 class="task">
    7. All states via SQLAlchemy
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all <code>State</code> objects from the database <code>hbtn_0e_6_usa</code> </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    8. First state
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints the first <code>State</code> object from the database <code>hbtn_0e_6_usa</code> </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>The state you display must be the first in <code>states.id</code></li>
<li>You are not allowed to fetch all states from the database before displaying the result</li>
<li>The results must be displayed as they are in the example below</li>
<li>If the table <code>states</code> is empty, print <code>Nothing</code> followed by a new line</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    9. Contains `a`
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all <code>State</code> objects that contain the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code> </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    10. Get a state
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints the <code>State</code> object with the <code>name</code> passed as argument from the database <code>hbtn_0e_6_usa</code> </p><ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name to search</code> (SQL injection free)</li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You can assume you have one record with the state name to search</li>
<li>Results must display the <code>states.id</code></li>
<li>If no state has the name you searched for, display <code>Not found</code></li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    11. Add a new state
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that adds the <code>State</code> object “Louisiana” to the database <code>hbtn_0e_6_usa</code> </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Print the new <code>states.id</code> after creation</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    12. Update a state
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that changes the name of a <code>State</code> object from the database <code>hbtn_0e_6_usa</code> </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Change the name of the <code>State</code> where <code>id = 2</code> to <code>New Mexico</code></li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    13. Delete states
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that deletes all <code>State</code> objects with a name containing the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code> </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    14. Cities in state
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python file similar to <code>model_state.py</code> named <code>model_city.py</code> that contains the class definition of a <code>City</code>.</p><ul>
<li><code>City</code> class:

<ul>
<li>inherits from <code>Base</code> (imported from <code>model_state</code>)</li>
<li>links to the MySQL table <code>cities</code></li>
<li>class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can’t be null and is a primary key</li>
<li>class attribute <code>name</code> that represents a column of a string of 128 characters and can’t be null</li>
<li>class attribute <code>state_id</code> that represents a column of an integer, can’t be null and is a foreign key to <code>states.id</code></li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
</ul><p>Next, write a script <code>14-model_city_fetch_by_state.py</code> that prints all <code>City</code> objects from the database <code>hbtn_0e_14_usa</code>: </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>Results must be display as they are in the example below (<code>&lt;state name&gt;: (&lt;city id&gt;) &lt;city name&gt;</code>)</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    15. Roman to Integer
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a function <code>def roman_to_int(roman_string):</code> that converts a <a href="/rltoken/EO2D_IdU21c-SZ2CP8XXJg" target="_blank" title="Roman number">Roman number</a> to an integer.</p><ul>
<li>You can assume the number will be between 1 to 3999.</li>
<li><code>def roman_to_int(roman_string)</code> must return an integer</li>
<li>If the <code>roman_string</code> is not a string or <code>None</code>, return 0</li>
</ul>


<h4 class="task">
    16. City relationship
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Improve the files <code>model_city.py</code> and <code>model_state.py</code>, and save them as <code>relationship_city.py</code> and <code>relationship_state.py</code>:</p><ul>
<li><code>City</code> class:

<ul>
<li>No change</li>
</ul></li>
<li><code>State</code> class:

<ul>
<li>In addition to previous requirements, the class attribute <code>cities</code> must represent a relationship with the class <code>City</code>. If the <code>State</code> object is deleted, all linked <code>City</code> objects must be automatically deleted. Also, the reference  from a <code>City</code> object to his <code>State</code> should be named <code>state</code></li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
</ul><p>Write a script that creates the <code>State</code> “California” with the <code>City</code> “San Francisco” from the database <code>hbtn_0e_100_usa</code>: (<code>100-relationship_states_cities.py</code>)</p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use the <code>cities</code> relationship for all <code>State</code> objects</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    17. List relationship
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that lists all <code>State</code> objects, and corresponding <code>City</code> objects, contained in the database <code>hbtn_0e_101_usa</code> </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>The connection to your MySQL server must be to <code>localhost</code> on port <code>3306</code></li>
<li>You must only use one query to the database</li>
<li>You must use the <code>cities</code> relationship for all <code>State</code> objects</li>
<li>Results must be sorted in ascending order by <code>states.id</code> and <code>cities.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    18. From city
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that lists all <code>City</code> objects from the database <code>hbtn_0e_101_usa</code> </p><ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use only one query to the database</li>
<li>You must use the <code>state</code> relationship to access to the <code>State</code> object linked to the <code>City</code> object</li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

