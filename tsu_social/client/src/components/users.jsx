import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Users() {
  const [data, setData] = useState([]);

  useEffect(() => {
    responseData();
  }, []);

  const responseData = async () => {
    try {
      const response = await axios.get('http://localhost:8005/users/');
      const jsonData = response.data;
      setData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h1>Users:</h1>
      <ul className='list-group'>
        {data.map((item) => (
          <li key={item.id} className='list-group-item'>
            {item.first_name} {item.last_name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Users;
