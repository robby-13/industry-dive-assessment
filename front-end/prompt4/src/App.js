import './App.css';
import {useEffect, useState} from 'react'

function App() {
  const [archives, setArchives] = useState([]) // store the archives data in a state
  const [search, setSearch] = useState('') // store the input in the search field
  const [filteredArchives, setFilteredArchives] = useState([]) // filtered Archive data results

  const local_host = 'http://127.0.0.1:8000/'
  const api = local_host + 'api/v1/news/'
  // First step in the process: establish a connection the back-end API
  // via useEffect to prevent an infinite amount of data retrieval requests!
  useEffect(() => {
    fetch(api)
      .then(response => response.json())
      .then(data => setArchives(data))
  }, [])
  
  // Based on the search value, filter the archives and display all matching results
  const handleChange = (event) => {
    event.preventDefault()
    setSearch(event.target.value)
    const copy = [...archives]
    if (search !== '') {
      const filteredArchives = copy.filter(match => match.title.toLowerCase().includes(search))
      setFilteredArchives(filteredArchives)
    }
    else {
      setFilteredArchives(archives)
    }
  }

  const handleSubmit = (event) => {
    event.preventDefault()
  }

  // When working with the API data, I noticed that the text in the teasers field still had HTML
  // paragraph tags. They got annoying after a while, so I wrote a function to get rid of them, 
  // and for a couple stragglers that had different HTML tags leading the string.
  const removeParagraphTags = () => {
    const copy = [...archives]
    for(let i = 0; i < copy.length; i++) {
      copy[i].teaser = copy[i].teaser.replaceAll('<p>', '')
      copy[i].teaser = copy[i].teaser.replaceAll('</p>', '')
      if(copy[i].pk === 13) {
        copy[i].teaser = copy[i].teaser.slice(0, 52)
      }
      if(copy[i].pk === 15) {
        copy[i].teaser = copy[i].teaser.slice(12).replace('>', '')
      }

    }
  }
  removeParagraphTags()

 
  const display = filteredArchives.map(i => {
    if(archives[0]) {
      return(
        <div className="archive-post">
          <ul>
            <li key={i.publish_date}>{i.publish_date}</li>
            {i.topics.map((topic, index) => {
              return(
                <div>
                  <li key={index + topic.pk}>{topic.display_name}</li>
                </div>
              )
            })}
          </ul>
          <h2><a href={i.source}>{i.title}</a></h2>
          <p>{i.teaser}</p>
          
        </div>
      )
    }
  })

  return (
    <div className="App">
      <form>
        <input type="text" onChange={(event) => handleChange(event)}></input>
        <button type="search" onClickt={(event) => handleSubmit(event)}>search</button>
      </form>
      
      <ul>
        {display}
      </ul>
    </div>
  );
}

export default App;
