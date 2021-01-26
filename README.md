<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="StoreWarehouseAPI_0"></a>Store-Warehouse-API</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2">An application which reflects two-way synchronization between Store &amp; Warehouse orders added/updated via Admin panel.</p>
<h3 class="code-line" data-line-start=2 data-line-end=3 ><a id="Requirements_2"></a>Requirements:</h3>
<p class="has-line-data" data-line-start="3" data-line-end="9">1.Create two applications. (Store and Warehouse)<br>
2.(Store) One application should provide Orders (should be able to create order from admin page)<br>
3.(Warehouse) Another application should be able to receive these orders via the API and push back the information to the (Store).<br>
4.When an order is created in Store, this should be synced to the Warehouse. If some information(e.g, status) is changed in warehouse, this will update the information in Store.<br>
5.These applications can only communicate via Rest API and don’t share a same database (two separate databases).<br>
6.For more information, please refer <a href="https://www.youtube.com/watch?v=oDIYp41Mohk">this</a> video.</p>
<h3 class="code-line" data-line-start=10 data-line-end=11 ><a id="Approach_10"></a>Approach:</h3>
<p class="has-line-data" data-line-start="11" data-line-end="16">1.Created two separate applications: Store and Warehouse in the same Django project.<br>
2.Created two separate databases for each of the applications to store their orders.<br>
3.While a Store order is added via Admin, prior to saving in the Store database- it makes a POST API request to add a record in Warehouse database.<br>
4.The API request will be a PATCH request if there is an update via the Admin panel, and it will be a DELETE request if there is a delete operation.<br>
5.Similar approach has been followed to synchronize data between the two databases when there is an update in the Warehouse database, i.e, a PATCH request to the Store’s updation API endpoint is called to update Store databse prior to saving the same in the Warehouse database.</p>
<h3 class="code-line" data-line-start=17 data-line-end=18 ><a id="SETUP_Instructions_17"></a>SETUP Instructions:</h3>
<p class="has-line-data" data-line-start="19" data-line-end="22">1.Install <a href="https://www.atlassian.com/git/tutorials/install-git">Git</a><br>
2.Clone the repository using <code>git clone https://github.com/6adityag8/Store-Warehouse-API</code>.<br>
3.Create a .env file with your environment configuration and non-source controlled sensitive information. You can copy the <a href="https://github.com/6adityag8/Store-Warehouse-API/blob/master/store_warehouse_api/.env.example">example file</a> and add the relevent configuration data.</p>
<pre><code class="has-line-data" data-line-start="23" data-line-end="27">cd Store-Warehouse-API/store_warehouse_api/
cp .env.example .env
vim .env
</code></pre>
<p class="has-line-data" data-line-start="27" data-line-end="29">3.Install <a href="https://docs.docker.com/get-docker/">Docker</a><br>
4.Move to the parent directory and build the <a href="https://github.com/6adityag8/Store-Warehouse-API/blob/master/Dockerfile">Dockerfile</a>, using a tag name.</p>
<pre><code class="has-line-data" data-line-start="30" data-line-end="33">cd ..
docker build -t store_warehouse_api -f Dockerfile .
</code></pre>
<p class="has-line-data" data-line-start="33" data-line-end="34">5.Run the created docker image using the same tag name, previously used.</p>
<pre><code class="has-line-data" data-line-start="35" data-line-end="37">docker run -it -p 8888:8888 store_warehouse_api
</code></pre>
<p class="has-line-data" data-line-start="37" data-line-end="38">6.Visit <code>localhost:8888</code> in a web browser and LogIn using the Super User credentials set earlier in .env file.</p>