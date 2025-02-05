import React, { useState, useEffect } from 'react';
import './App.css';
import { fetchData } from './services/api';  // Servicio para la API de FastAPI

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Hacer una petición al backend de FastAPI cuando el componente se monta
    fetchData()
      .then(response => setData(response))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Mi aplicación React con FastAPI</h1>
        {data ? (
          <pre>{JSON.stringify(data, null, 2)}</pre>
        ) : (
          <p>Cargando...</p>
        )}
      </header>
    </div>
  );
}

export default App;
