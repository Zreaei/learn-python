/* eslint-disable react/prop-types */
import { useState } from 'react'
import Header from '../components/header';

function App() {
  const students = ['Sandhika','Doddy','Erik'];
  const [likes, setLikes] = useState(0);
  const [number, setNumber] = useState(0);

  function handleClick(){
      setLikes(likes + 1);
  }

  function resetClick(){
      setNumber(0);
  }

  function minusClick(){
      setNumber(number - 1);
  }

  function plusClick(){
      setNumber(number + 1);
  }

  return (
      <div>
          <Header name="Pa Dhika" />
          <ul>
              {
                  students.map((students) => (
                      <li key={students}>{students}</li>
                  ))
              }
          </ul>
          <button onClick={handleClick}>Like ({likes})</button>
          <h2>Latihan React</h2>
          <p>Number : {number}</p>
          <button onClick={minusClick}>-</button>
          <button onClick={resetClick}>Reset</button>
          <button onClick={plusClick}>+</button>
      </div>
      )
}

export default App
