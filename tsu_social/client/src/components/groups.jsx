import React, { useEffect, useState } from 'react';

function Groups() {
  const [data, setData] = useState([]);

  useEffect(() => {
    responseData();
  }, []);

  const responseData = async () => {
    try {
      const response = await fetch('http://localhost:8005/groups/');
      const jsonData = await response.json();
      setData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h1>Groups:</h1>
      <ol className='list-group'>
        {data.map((item) => (
          <li key={item.id} className='list-group-item'>
            {item.name}
          </li>
        ))}
      </ol>
    </div>
  );
}

export default Groups;
