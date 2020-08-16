import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './App.scss';

const App = () => {

  const [users, setUsers] = useState([])
  const nameRef = useRef(null);

  const handleAdd = () => {
    if (nameRef.current && nameRef.current.value && nameRef.current.value !== '') {
      axios.post('/api/createUser', {name: nameRef.current.value})
      .then(result => {
        if (result.data.success) setUsers([...users, result.data.data])
      })
    }
  }

  useEffect(() => {
    axios.get('/api/fetchAllUsers')
    .then(result => {
      if (result.data.success) setUsers(result.data.data)
    })
  }, [])

  return (
    <main>

      <section>
        This boilerplate is built with a React.js Frontend,
        and a Flask (Python) backend.
      </section>

      <section>
        The codebase is set up to work seamlessly with Heroku,
        so you can get an app up and running in the shortest time possible (check out the README).
      </section>

      <section>
        <h3>USERS:</h3>
        
        <div>
          <input type="text" ref={nameRef}/>
          <button onClick={handleAdd}>Add</button>
        </div>

        { users.map( (user, index) => {
          return <div key={index}>
            <p>{index}. {user.name}</p>
          </div>
        })

        }
      </section>

    </main>
  )
}

export default App;