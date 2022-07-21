import NoblePrize from './NoblePrize';
// import './App.css';
import { useState } from 'react';
import axios from "axios"
import Prediction from './Prediction'
function App() {

  console.log("NODE_ENV=", process.env.NODE_ENV)
  const [year, setYear] = useState(null);
  const [algorithm, setAlgorithm] = useState("lr");
  const [prediction, setPrediction] = useState("-");
  const server_address = process.env.REACT_APP_SERVER
  console.log(server_address)
  axios.get(`${server_address}/prediction/${algorithm}`)
  .then(res => setPrediction(res.data));

  return (
    <div id="container">
      <h1> Machine Learning Prediction: Interpretation</h1>
      <h2> {algorithm} </h2>
      <select value={algorithm} onChange={(e) => { setAlgorithm(e.target.value)}}>
        <option value="lr">Linear Regression</option>
        <option value="rf">Random Forest</option>
      </select>

      <Prediction algorithm={algorithm} prediction={prediction} />

      <hr />
      <header className="App-header">
        <h1> Noble Prize App </h1>
      </header>

      <p>Year:</p>
      <input 
      type="text" 
      value={year} 
      onChange={event => setYear(event.target.value)}
      />
      <p> Here are the list of winners:</p>
      <NoblePrize year={year} />
    </div>
  );
}

export default App;
