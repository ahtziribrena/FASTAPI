export const fetchData = async () => {
    const response = await fetch('http://localhost:8010/api/endpoint');
    if (!response.ok) {
      throw new Error('Error en la petición');
    }
    return await response.json();
  };
  