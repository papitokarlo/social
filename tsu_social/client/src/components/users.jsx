import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './static/index.css'; // Import your CSS file

function Users() {
  const [data, setData] = useState([]);

  useEffect(() => {
    responseData();
  }, []);

  const responseData = async () => {
    try {
      const response = await axios.get('http://localhost:8006/api/users/');
      const jsonData = response.data;
      setData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className='object-container'>
      <h1 className='object-title'>Users:</h1>
      <ul className='object-list'>
        {data.map((item) => (
          <li key={item.id} className='object-item'>
            {item.first_name} {item.last_name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Users;
