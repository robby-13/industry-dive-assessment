import './App.css';

function App() {
  const local_host = 'http://127.0.0.1:8000/'
  const api = local_host + 'api/v1/news/'

  fetch(api)
  .then(response => response.json())
  .then(data => console.log(data))

  return (
    <div className="App">
      
    </div>
  );
}

export default App;
