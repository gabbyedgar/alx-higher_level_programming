<h1 class="gap">0x11. Python - Network #1</h1>


<h4 class="task">
    0. What's my status? #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that fetches <code>https://intranet.hbtn.io/status</code></p><ul>
<li>You must use the package <code>urllib</code></li>
<li>You are not allowed to import any packages other than <code>urllib</code></li>
<li>The body of the response must be displayed like the following example (tabulation before <code>-</code>)</li>
<li>You must use a <code>with</code> statement</li>
</ul>


<h4 class="task">
    1. Response header value #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the <code>X-Request-Id</code> variable found in the header of the response.</p><ul>
<li>You must use the packages <code>urllib</code> and <code>sys</code></li>
<li>You are not allow to import packages other than <code>urllib</code> and <code>sys</code></li>
<li>The value of this variable is different for each request</li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
<li>You must use a <code>with</code> statement</li>
</ul>


<h4 class="task">
    2. POST an email #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that takes in a URL and an email, sends a <code>POST</code> request to the passed URL with the email as a parameter, and displays the body of the response (decoded in <code>utf-8</code>)</p><ul>
<li>The email must be sent in the <code>email</code> variable</li>
<li>You must use the packages <code>urllib</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>urllib</code> and <code>sys</code></li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
<li>You must use the <code>with</code> statement</li>
</ul><p>Please test your script in the container provided, using the web server running on port 5000</p>


<h4 class="task">
    3. Error code #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in <code>utf-8</code>).</p><ul>
<li>You have to manage <code>urllib.error.HTTPError</code> exceptions and print: <code>Error code:</code> followed by the HTTP status code</li>
<li>You must use the packages <code>urllib</code> and <code>sys</code></li>
<li>You are not allowed to import other packages than <code>urllib</code> and <code>sys</code></li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
<li>You must use the <code>with</code> statement</li>
</ul><p>Please test your script in the container provided, using the web server running on port 5000</p>


<h4 class="task">
    4. What's my status? #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that fetches <code>https://intranet.hbtn.io/status</code></p><ul>
<li>You must use the package <code>requests</code></li>
<li>You are not allow to import packages other than <code>requests</code></li>
<li>The body of the response must be display like the following example (tabulation before <code>-</code>)</li>
</ul>


<h4 class="task">
    5. Response header value #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable <code>X-Request-Id</code> in the response header</p><ul>
<li>You must use the packages <code>requests</code> and <code>sys</code></li>
<li>You are not allow to import other packages than <code>requests</code> and <code>sys</code></li>
<li>The value of this variable is different for each request</li>
<li>You don’t need to check script arguments (number and type)</li>
</ul>


<h4 class="task">
    6. POST an email #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that takes in a URL and an email address, sends a <code>POST</code> request to the passed URL with the email as a parameter, and finally displays the body of the response.</p><ul>
<li>The email must be sent in the variable <code>email</code></li>
<li>You must use the packages <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code> and <code>sys</code></li>
<li>You don’t need to error check arguments passed to the script (number or type)</li>
</ul><p>Please test your script in the container provided, using the web server running on port 5000</p>


<h4 class="task">
    7. Error code #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.</p><ul>
<li>If the HTTP status code is greater than or equal to 400, print: <code>Error code:</code> followed by the value of the HTTP status code</li>
<li>You must use the packages <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other  than <code>requests</code> and <code>sys</code></li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
</ul><p>Please test your script in the container provided, using the web server running on port 5000</p>


<h4 class="task">
    8. Search API
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that takes in a letter and sends a <code>POST</code> request to <code>http://0.0.0.0:5000/search_user</code> with the letter as a parameter.</p><ul>
<li>The letter must be sent in the variable <code>q</code></li>
<li>If no argument is given, set <code>q=""</code></li>
<li>If the response body is properly JSON formatted and not empty, display the <code>id</code> and <code>name</code> like this: <code>[&lt;id&gt;] &lt;name&gt;</code></li>
<li>Otherwise:

<ul>
<li>Display <code>Not a valid JSON</code> is the JSON is invalid</li>
<li>Display <code>No result</code> is the JSON is empty</li>
</ul></li>
<li>You must use the package <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code> and <code>sys</code></li>
</ul><p>Please test your script in the container provided, using the web server running on port 5000. All JSON generated by this server are random.</p>


<h4 class="task">
    9. Star Wars API #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that takes in a string and sends a search request to the <a href="/rltoken/1-uJUA4XtfDCDgtT17vrTg" target="_blank" title="Star Wars API">Star Wars API</a></p><ul>
<li>Use the <a href="/rltoken/n5zDuNtdbipdsG0VSWKYoQ" target="_blank" title="Star Wars API search people endpoint">Star Wars API search people endpoint</a> </li>
<li>Use the string argument as the <code>search</code> value of the request</li>
<li>The body response must be JSON and converted to a Python dictionary.</li>
<li>Display: <code>Number of results: &lt;count&gt;</code> </li>
<li>Display the <code>name</code> of each result (see example below)</li>
<li>You must use the packages <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code> and <code>sys</code></li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
<li>You don’t need to manage the pagination</li>
</ul>


<h4 class="task">
    10. My Github!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Python script that takes your Github credentials (username and password) and uses the <a href="/rltoken/RBCqKJiUKUYdiOKvFqFJaw" target="_blank" title="Github API">Github API</a> to display your <code>id</code></p><ul>
<li>You must use <a href="/rltoken/S4DQNs9gIqNeieyUhfV1Pw" target="_blank" title="Basic Authentication">Basic Authentication</a> to access to your information</li>
<li>The first argument will be your <code>username</code></li>
<li>The second argument will be your <code>password</code></li>
<li>You must use the package <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code> and <code>sys</code></li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
</ul>


<h4 class="task">
    11. Time for an interview!
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:</p>


<h4 class="task">
    12. Star Wars API #1
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Based on <code>9-starwars.py</code>:</p><p>Write a Python script that takes in a string and sends a search request to the <a href="/rltoken/1-uJUA4XtfDCDgtT17vrTg" target="_blank" title="Star Wars API">Star Wars API</a></p><ul>
<li>Use the <a href="/rltoken/n5zDuNtdbipdsG0VSWKYoQ" target="_blank" title="Star Wars API search people endpoint">Star Wars API search people endpoint</a> </li>
<li>Use the string argument as <code>search</code> value of the request</li>
<li>The body response must be a JSON and converted to a Python dictionary.</li>
<li>Display: <code>Number of results: &lt;count&gt;</code> </li>
<li>Display the <code>name</code> of each result (see example below)</li>
<li>You must manage the pagination to display all results</li>
<li>You must use the package <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code> and <code>sys</code></li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
</ul>


<h4 class="task">
    13. Star Wars API #2
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Based on <code>101-starwars.py</code>:</p><p>Write a Python script that takes in a string and sends a search request to the <a href="/rltoken/1-uJUA4XtfDCDgtT17vrTg" target="_blank" title="Star Wars API">Star Wars API</a></p><ul>
<li>Use the <a href="/rltoken/n5zDuNtdbipdsG0VSWKYoQ" target="_blank" title="Star Wars API search people endpoint">Star Wars API search people endpoint</a> </li>
<li>Use the string argument as the <code>search</code> value of the request</li>
<li>The body response must be JSON and converted to a Python dictionary.</li>
<li>Display: <code>Number of results: &lt;count&gt;</code> </li>
<li>Display the <code>name</code> of each result </li>
<li>For each character (people), display a list of movie (film) names: <code>&lt;tabulation&gt;&lt;film name&gt;</code> (see example below)</li>
<li>You must manage the pagination to display all results</li>
<li>You must use the package <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code> and <code>sys</code></li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
</ul>


<h4 class="task">
    14. Twitter Auth
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a Python script that takes in 3 strings and sends a search request to the <a href="/rltoken/klWEPDgGezaDBNkOYvxz9g" target="_blank" title="Twitter API">Twitter API</a></p><ul>
<li>Use the <a href="/rltoken/klWEPDgGezaDBNkOYvxz9g" target="_blank" title="Twitter API search endpoint">Twitter API search endpoint</a></li>
<li>Use the <a href="/rltoken/m8lDJBgvnNXNqsu3octBZg" target="_blank" title="Application-only authentication">Application-only authentication</a> flow to do a search request </li>
<li>Create an Twitter application <a href="/rltoken/G2vwEvbZJiqF1NIboxBMZg" target="_blank" title="here">here</a></li>
<li>The first argument must be the Consumer Key (API Key)</li>
<li>The second argument must be the Consumer Secret (API Secret)</li>
<li>The third argument must be the search string</li>
<li>Display only 5 results in the following format: <code>[&lt;Tweet ID&gt;] &lt;Tweet text&gt; by &lt;Tweet owner name&gt;</code> (see example below)</li>
<li>You must use the packages <code>requests</code>, <code>base64</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code>, <code>base64</code> and <code>sys</code></li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
</ul>

