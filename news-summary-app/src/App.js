import React, {useState} from "react"
import api from "./api";
import './App.css'


const App = ()  => {

  const [isCopied, setIsCopied] = useState(false);
  const [status, setStatus] = useState(false)
  const [summaryData, setSummaryData] = useState([]);
  const [newsQuery, setNewsQuery] = useState({
    url: "",
    wordcount: 50,
  });

  const fetchSummaryData = async () => {
    try {
      const response = await api.get("/get-summary/", {
        params: {
          url: newsQuery.url,
          summary_len: newsQuery.wordcount,
        },
      });
      setSummaryData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setNewsQuery((prevQuery) => ({
      ...prevQuery,
      [name]: value,
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    fetchSummaryData();
    setIsCopied(false);
    setNewsQuery((prevQuery) => ({
      ...prevQuery,
       // Set the URL input to an empty string
    }))
    
  };

  const handleCopyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(summaryData.Summary);
      setIsCopied(true);
    } catch (error) {
      console.error("Error copying to clipboard:", error);
    }
  };

 
  
  return(
    <div className="App">
      <h1 className="Main-Title">News Summary Application</h1>
        <div className = "Container">
          <form className = "query-form" onSubmit={handleSubmit}>
            <label className = "label" for = "url">News Website : </label><br/>
            <input
                type = "url" 
                placeholder="Enter News Website Url" 
                name = "url"
                id = "url" 
                value={newsQuery.url} 
                onChange={handleInputChange}
                onFocus={() => setNewsQuery((prevQuery) => ({ ...prevQuery, url: "" }))}
            />
            
            <br/><label className = "label" for = "wordcount">Summary Length : </label><br/>
            <input
              type="number"
              name="wordcount"
              id = "wordcount"
              value={newsQuery.wordcount}
              onChange={handleInputChange}
            />
            <br/>
            
            <button onClick = {() => setStatus(true)}>Submit  </button>
          </form>
      </div>
      <div className="Display">
            {
              status ?<label className="News-Title">{summaryData.Title}</label>:null
            }
            {
               status ? <p className="News-Summary">{summaryData.Summary}</p> :null
            }
            {  
              status ? <button onClick={handleCopyToClipboard}>
              {isCopied ? "Copied!" : "Copy to Clipboard"}</button>: null
            } 
            {
             
            /*For Displaying table  */
            }

        </div>
    </div>
            
  );
};

export default App;
