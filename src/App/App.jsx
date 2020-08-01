import React from 'react';
import './App.scss';

const App = () => {

  return (
    <main>

      <section>
        This boilerplate is built with a React.js Frontend,
        and a Flask (Python) backend.
      </section>

      <section>
        To make requests to the backend, use <a href="https://www.npmjs.com/package/axios">axios (npm)</a>
        and use the url prefix "/api" ( ex: "axios.get(`/api/users`)" )
      </section>

      <section>
        The codebase is set up to work seamlessly with Heroku,
        so you can get an app up and running in the shortest time possible (check out the README).
      </section>

    </main>
  )
}

export default App;