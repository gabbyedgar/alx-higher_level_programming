<h1 class="gap">0x14. Javascript - Web scraping</h1>


<h4 class="task">
    0. Readme
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that reads and prints the content of a file.</p><ul>
<li>The first argument is the file path</li>
<li>The content of the file must be read in <code>utf-8</code></li>
<li>If an error occurred during the reading, print the error object</li>
</ul>


<h4 class="task">
    1. Write me
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that writes a string to a file.</p><ul>
<li>The first argument is the file path</li>
<li>The second argument is the string to write</li>
<li>The content of the file must be written in <code>utf-8</code></li>
<li>If an error occurred during while writing, print the error object</li>
</ul>


<h4 class="task">
    2. Status code
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that display the status code of a <code>GET</code> request.</p><ul>
<li>The first argument is the URL to request (<code>GET</code>)</li>
<li>The status code must be printed like this: <code>code: &lt;status code&gt;</code></li>
<li>You must use the module <code>request</code></li>
</ul>


<h4 class="task">
    3. Star wars movie title
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.</p><ul>
<li>The first argument is the episode number</li>
<li>You must use the <a href="/rltoken/lA22rFkBzdXeF0NNuBDeNA" target="_blank" title="Star wars API">Star wars API</a> with the endpoint <code>http://swapi.co/api/films/:episode_id</code></li>
<li>You must use the module <code>request</code></li>
</ul>


<h4 class="task">
    4. Star wars Wedge Antilles
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints the number of movies where the character “Wedge Antilles” is present.</p><ul>
<li>The first argument is the API URL of the <a href="/rltoken/lA22rFkBzdXeF0NNuBDeNA" target="_blank" title="Star wars API">Star wars API</a>: <code>http://swapi.co/api/films/</code></li>
<li>Wedge Antilles is character ID <code>18</code></li>
<li>You must use the module <code>request</code></li>
</ul>


<h4 class="task">
    5. Loripsum
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that gets the contents of a webpage and stores it in a file.</p><ul>
<li>The first argument is the URL to request</li>
<li>The second argument the file path to store the body response</li>
<li>The file must be UTF-8 encoded</li>
<li>You must use the module <code>request</code></li>
</ul>


<h4 class="task">
    6. How many completed?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that computes the number of tasks completed by user id.</p><ul>
<li>The first argument is the API URL: <code>https://jsonplaceholder.typicode.com/todos</code></li>
<li>You must use the module <code>request</code></li>
</ul>


<h4 class="task">
    7. Who was playing in this movie?
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that prints all characters of a Star Wars movie:</p><ul>
<li>The first argument is the Movie ID - example: <code>3</code> = “Return of the Jedi” </li>
<li>Display one character name by line</li>
<li>You must use the <a href="/rltoken/lA22rFkBzdXeF0NNuBDeNA" target="_blank" title="Star wars API">Star wars API</a></li>
<li>You must use the module <code>request</code></li>
</ul>


<h4 class="task">
    8. Right order
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that prints all characters of a Star Wars movie:</p><ul>
<li>The first argument is the Movie ID - example: <code>3</code> = “Return of the Jedi” </li>
<li>Display one character name by line <strong>in the same order of the list “characters” in the <code>/films/</code> response</strong></li>
<li>You must use the <a href="/rltoken/lA22rFkBzdXeF0NNuBDeNA" target="_blank" title="Star wars API">Star wars API</a></li>
<li>You must use the module <code>request</code></li>
</ul>


<h4 class="task">
    9. Twitter Auth
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a Javascript script that takes in 3 strings and sends a search request to the <a href="/rltoken/fyEHtzbUagmJMVacV7n3Ww" target="_blank" title="Twitter API">Twitter API</a></p><ul>
<li>Use the <a href="/rltoken/fyEHtzbUagmJMVacV7n3Ww" target="_blank" title="Twitter API search endpoint">Twitter API search endpoint</a></li>
<li>Use the <a href="/rltoken/NIh-aYdkjEv7iZ8L-I_CsQ" target="_blank" title="Application-only authentication">Application-only authentication</a> flow to do a search request </li>
<li>Create an Twitter application <a href="/rltoken/GwW2n0UD_q9RYXAguDrtLA" target="_blank" title="here">here</a></li>
<li>The first argument must be the Consumer Key (API Key)</li>
<li>The second argument must be the Consumer Secret (API Secret)</li>
<li>The third argument must be the search string</li>
<li>Display only 5 results in the following format: <code>[&lt;Tweet ID&gt;] &lt;Tweet text&gt; by &lt;Tweet owner name&gt;</code> (see example below)</li>
<li>Only these modules are allowed: <code>request</code>, <code>base-64</code> and <code>utf8</code></li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
</ul>

