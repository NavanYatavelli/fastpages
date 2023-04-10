
<h1>Breaking News!!</h1>
<br/>

<table  style="width:100%" id = "table">
  <thead>
  <tr>
    <th>Item</th>
    <th>City</th>
    <th>Network</th>
    <th>News</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>

<script>

// Builds the request headers
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

/* List array to store the breaking news headers */
let news_header = ["Item", "City","Network","News"];
/* List array to store the breaking news values */
let news_rows = new Array();
/* Total news items*/
let news_item_count = 0;
/* News column headers to be displayed */
const  news_headers_count = 4;

fetch("https://fnvs.duckdns.org/api/breakingnews", requestOptions)
  .then(response => response.json())
  .then(r => {
    r.forEach(ev => {
      let news_column_count = 0;
      news_rows[news_item_count] = new Array();
      const row = document.createElement("tr")
      const itemData = document.createElement("td")
      itemData.innerHTML = `${ev.id}`
      row.appendChild(itemData)
      /* Add the news data to the List row */
      news_rows[news_item_count][news_column_count] = itemData;
      news_column_count++;

      const cityData = document.createElement("td")
      cityData.innerHTML = `${ev.city}`
      row.appendChild(cityData)
      /* Add the news data to the List row */
      news_rows[news_item_count][news_column_count] = cityData;
      news_column_count++;

      const networkData = document.createElement("td")
      networkData.innerHTML = `${ev.network}`
      row.appendChild(networkData)
      /* Add the news data to the List row */
      news_rows[news_item_count][news_column_count] = networkData;
      news_column_count++;

      const titleData = document.createElement("td")
      titleData.innerHTML = `<a href=${ev.link}> ${ev.title} </a>`
      row.appendChild(titleData)
      /* Add the news data to the List row */
      news_rows[news_item_count][news_column_count] = titleData;
      news_column_count++;
      news_item_count++;

      document.getElementById("table").appendChild(row)
    })
  })
  .catch(error => console.log('error', error))

function reset() {
  window.location.reload();
}
</script>

<script>
const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
//const url = "http://127.0.0.1:8086/api/breakingnews"
const url = "https://fnvs.duckdns.org/api/breakingnews"
const create_fetch = url + '/create';
const read_fetch = url + '/';
read_breaking_news();

/**
 * Display breaking news
 */
function read_breaking_news() {
    // prepare fetch options
    const read_options = {
      method: 'GET', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'omit', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
      },
    };     // fetch the data from API
    fetch(read_fetch, read_options)
      // response is a RESTful "promise" on any successful fetch
      .then(response => {
        // check for response errors
        if (response.status !== 200) {
            const errorMsg = 'Database read error: ' + response.status;
            //console.log(errorMsg);
            const tr = document.createElement("tr");
            const td = document.createElement("td");
            td.innerHTML = errorMsg;
            tr.appendChild(td);
            return;
        }
        // valid response will have json data
        response.json().then(data => {
            console.log(data);
            for (let row in data) {
              console.log(data[row]);
              //add_row(data[row]);
            }
        })
    }) 
      // catch fetch errors (ie ACCESS to server blocked)
    .catch(err => {
      //console.error(err);
      const tr = document.createElement("tr");
      const td = document.createElement("td");
      td.innerHTML = err;
      tr.appendChild(td);
      resultContainer.appendChild(tr);
    });
  }
</script>

		
<br/>
<h2>Add Breaking News!!</h2>

<form action="javascript:create_breaking_news()">
    <p><label>
        News:
        <input type="text" name="addnews" id="addnews" required>
    </label></p>
    <p><label>
        Network:
        <input type="text" name="addnetwork" id="addnetwork" value="CNN" required>
    </label></p>
    <p><label>
        City:
        <input type="text" name="addcity" id="addcity" value="San Diego" required>
    </label></p>

    <p>
        <button>Input Breaking News</button>
    </p>
</form>

<script>
  /**
   * Adds a new breaking news.
   */
 function create_breaking_news(){
    const body = {
        title: document.getElementById("addnews").value,
        network: document.getElementById("addnetwork").value,
        city: document.getElementById("addcity").value        
    };

    const requestOptions = {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            "content-type": "application/json",
            'Authorization': 'Bearer my-token',
        },
    };

//fetch("http://127.0.0.1:8086/api/breakingnews/create", requestOptions)
  fetch("https://fnvs.duckdns.org/api/breakingnews/create", requestOptions)
    .then(response  => {
       if (response.status == 200) {
          const errorMsg = 'POST SUCCESS: ' + response.status;
          console.log(errorMsg);
          reset(); 
          return;
        }
    })
    .catch(error => console.log('error', error))
 }

</script>


<script>
 
/** 
 * This function checks if the breaking news item exists in the List. 
 * @param news_item check if this news item is valid or not
 * @return boolean  true if valid news item else false
 */
 function boolean is_valid_breaking_news_item(int news_item) {
    if (news_item < 0 || news_item > news_rows.length) {
      return false;
    }

    for (int i = 0; i < news_rows.length; i++) {
      for (int j = 0; j < news_headers_count; j++) {
        if (news_rows[i][j] == news_item) {
          /* breaking news item found */
          return true;
        }
      }
    }

    // not a valid breaking news item 
    return false;
 }

</script>

<br/>
<h2>Delete Breaking News!!</h2>

<form action="javascript:delete_news()">
    <p><label>
        News Item:
        <input type="text" name="deletenews" id="deletenews" required>
    </label></p>

    <p>
        <button>Delete Breaking News</button>
    </p>
</form>

<script>
/** 
 * This function deleted the breaking news item from the List and 
 * updated the UI to notify the breaking news changes.
 */
 function boolean delete_breaking_news(int news_item) {
    if (!is_valid_breaking_news_item(news_item)) {
      return false;
    }

 
    /* Delete the news item from the breaking news List */ 
    news_rows.splice(news_item, 1);

    return true;
 }
 
/**
 * Notifies status message to the user 
 */ 
 function notify_bottom_status(msg) {
  if (msg != null || msg == "") {
    document.getElementById("message").innerHTML = msg;
  }
 }
 
 function delete_news(){
    /* Check if its a valid breaking news to be deleted before sending the request to server */
     if (!delete_breaking_news(document.getElementById("deletenews").value) {
        notify_bottom_status("Invalid Delete");
     }
    
    /* Build and send delete request to server */
    const body = {
        id: document.getElementById("deletenews").value,
    };

    const requestOptions = {
        method: 'DELETE',
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'omit', // include, *same-origin, omit	
        body: JSON.stringify(body),
        headers: {
            "content-type": "application/json",
            'Authorization': 'Bearer my-token',
        },
    };

//fetch("http://127.0.0.1:8086/api/breakingnews/delete", requestOptions)
 fetch("https://fnvs.duckdns.org/api/breakingnews/delete", requestOptions)
    .then(response  => {
       if (response.status == 200) {
          const errorMsg = 'DELETE SUCCESS: ' + response.status;
          console.log(errorMsg);
          reset(); 
          return;
        }
    })
    .catch(error => console.log('error', error))
 }

</script>

<p id="message"></p>
