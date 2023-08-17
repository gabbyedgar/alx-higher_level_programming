<h1 class="gap">0x0E. SQL - More queries </h1>


<h4 class="task">
    0. My privileges!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all privileges of the MySQL users <code>user_0d_1</code> and <code>user_0d_2</code> on your server.</p>


<h4 class="task">
    1. Root user
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates the MySQL server user <code>user_0d_1</code>. </p><ul>
<li><code>user_0d_1</code> should have all privileges on your MySQL server</li>
<li>The <code>user_0d_1</code> password should be set to <code>user_0d_1_pwd</code></li>
<li>If the user <code>user_0d_1</code> already exists, your script should not fail</li>
</ul>


<h4 class="task">
    2. Read user
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates the database <code>hbtn_0d_2</code> and the user <code>user_0d_2</code>. </p><ul>
<li><code>user_0d_2</code> should have only SELECT privilege in the database <code>hbtn_0d_2</code></li>
<li>The <code>user_0d_2</code> password should be set to <code>user_0d_2_pwd</code></li>
<li>If the database <code>hbtn_0d_2</code> already exists, your script should not fail</li>
<li>If the user <code>user_0d_2</code> already exists, your script should not fail</li>
</ul>


<h4 class="task">
    3. Always a name
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates the table <code>force_name</code> on your MySQL server.</p><ul>
<li><code>force_name</code> description:

<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256) can’t be null</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>force_name</code> already exists, your script should not fail</li>
</ul>


<h4 class="task">
    4. ID can't be null
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates the table <code>id_not_null</code> on your MySQL server.</p><ul>
<li><code>id_not_null</code> description:

<ul>
<li><code>id</code> INT with the default value <code>1</code> </li>
<li><code>name</code> VARCHAR(256)</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>id_not_null</code> already exists, your script should not fail</li>
</ul>


<h4 class="task">
    5. Unique ID
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates the table <code>unique_id</code> on your MySQL server.</p><ul>
<li><code>unique_id</code> description:

<ul>
<li><code>id</code> INT with the default value <code>1</code> and must be unique</li>
<li><code>name</code> VARCHAR(256)</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>unique_id</code> already exists, your script should not fail</li>
</ul>


<h4 class="task">
    6. States table
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates the database <code>hbtn_0d_usa</code> and the table <code>states</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.</p><ul>
<li><code>states</code> description:

<ul>
<li><code>id</code> INT unique, auto generated, can’t be null and is a primary key</li>
<li><code>name</code> VARCHAR(256) can’t be null</li>
</ul></li>
<li>If the database <code>hbtn_0d_usa</code> already exists, your script should not fail</li>
<li>If the table <code>states</code> already exists, your script should not fail</li>
</ul>


<h4 class="task">
    7. Cities table
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates the database <code>hbtn_0d_usa</code> and the table <code>cities</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.</p><ul>
<li><code>cities</code> description:

<ul>
<li><code>id</code> INT unique, auto generated, can’t be null and is a primary key</li>
<li><code>state_id</code> INT, can’t be null and must be a <code>FOREIGN KEY</code> that references to <code>id</code> of the <code>states</code> table</li>
<li><code>name</code> VARCHAR(256) can’t be null</li>
</ul></li>
<li>If the database <code>hbtn_0d_usa</code> already exists, your script should not fail</li>
<li>If the table <code>cities</code> already exists, your script should not fail</li>
</ul>


<h4 class="task">
    8. Cities of California
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all the cities of California that can be found in the database <code>hbtn_0d_usa</code>.</p><ul>
<li>The <code>states</code> table contains only one record where <code>name</code> = <code>California</code> (but the <code>id</code> can be different, as per the example)</li>
<li>Results must be sorted in ascending order by <code>cities.id</code> </li>
<li>You are not allowed to use the <code>JOIN</code> keyword</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    9. Cities by States
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all cities contained in the database <code>hbtn_0d_usa</code>.</p><ul>
<li>Each record should display: <code>cities.id</code> - <code>cities.name</code> - <code>states.name</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code> </li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    10. Genre ID by show
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a></p><p>Write a script that lists all shows contained in <code>hbtn_0d_tvshows</code> that have at least one genre linked.</p><ul>
<li>Each record should display: <code>tv_shows.title</code> - <code>tv_show_genres.genre_id</code></li>
<li>Results must be sorted in ascending order  by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code></li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    11. Genre ID for all shows
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Import the database dump of <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>10-genre_id_by_show.sql</code>)</p><p>Write a script that lists all shows contained in the database <code>hbtn_0d_tvshows</code>.</p><ul>
<li>Each record should display: <code>tv_shows.title</code> - <code>tv_show_genres.genre_id</code></li>
<li>Results must be sorted in ascending order by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code></li>
<li>If a show doesn’t have a genre, display <code>NULL</code></li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    12. No genre
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>11-genre_id_all_shows.sql</code>)</p><p>Write a script that lists all shows contained in <code>hbtn_0d_tvshows</code> without a genre linked. </p><ul>
<li>Each record should display: <code>tv_shows.title</code> - <code>tv_show_genres.genre_id</code></li>
<li>Results must be sorted in ascending order by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code></li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    13. Number of shows by genre
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>12-no_genre.sql</code>)</p><p>Write a script that lists all genres from <code>hbtn_0d_tvshows</code> and displays the number of shows linked to each.</p><ul>
<li>Each record should display: <code>tv_genres.name</code> - <code>number of shows</code></li>
<li>Don’t display a genre that doesn’t have any shows linked</li>
<li>Results must be sorted in descending order by the number of shows linked</li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    14. My genres
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>13-count_shows_by_genre.sql</code>)</p><p>Write a script that uses the <code>hbtn_0d_tvshows</code> database to lists all genres of the show <code>Dexter</code>.</p><ul>
<li>The <code>tv_shows</code> table contains only one record where <code>title</code> = <code>Dexter</code> (but the <code>id</code> can be different)</li>
<li>Each record should display: <code>tv_genres.name</code></li>
<li>Results must be sorted in ascending order by the genre name</li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    15. Only Comedy
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>14-my_genres.sql</code>)</p><p>Write a script that lists all Comedy shows in the database <code>hbtn_0d_tvshows</code>.</p><ul>
<li>The <code>tv_genres</code> table contains only one record where <code>name</code> = <code>Comedy</code> (but the <code>id</code> can be different)</li>
<li>Each record should display: <code>tv_shows.title</code></li>
<li>Results must be sorted in ascending order by the show title</li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    16. List shows and genres
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>15-comedy_only.sql</code>)</p><p>Write a script that lists all shows, and all genres linked to that show, from the database <code>hbtn_0d_tvshows</code>.</p><ul>
<li>If a show doesn’t have a genre, display <code>NULL</code> in the genre column</li>
<li>Each record should display: <code>tv_shows.title</code> - <code>tv_genres.name</code></li>
<li>Results must be sorted in ascending order by the show title and genre name</li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

