import React, {useState, useEffect} from "react"
import api from "./api";

const App = ()  => {

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

  useEffect(() => {
    fetchSummaryData();
  }, []);

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
  };
  
  return(<div>
    <h1>Fetch Summary Data</h1>
    <form onSubmit={handleSubmit}>
      <label>
        URL:
        <input
          type="text"
          name="url"
          value={newsQuery.url}
          onChange={handleInputChange}
        />
      </label>
      <br />
      <label>
        Summary Length:
        <input
          type="number"
          name="wordcount"
          value={newsQuery.wordcount}
          onChange={handleInputChange}
        />
      </label>
      <br />
      <button type="submit">Fetch Summary</button>
    </form>
    <hr />
    {summaryData && (
      <div>
        <h2>Summary Data</h2>
        <p>Title : {summaryData.Title}</p>
        <p>Original Word Count: {summaryData.OriginalWordCount}</p>
        <p>Summary Word Count: {summaryData.SummaryWordCount}</p>
        <p>Summary: {JSON.stringify(summaryData.Summary)}</p>
        <p>Scores: {JSON.stringify(summaryData.Scores)}</p>
      </div>
    )}
  </div>);
};

export default App;
