import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './static/index.css';

function Groups() {
  const [data, setData] = useState([]);
  const [groupName, setGroupName] = useState('');
  const [groupDescription, setGroupDescription] = useState('');
  const [expandedGroups, setExpandedGroups] = useState([]); // Changed to an array
  const [creatingGroup, setCreatingGroup] = useState(false);

  useEffect(() => {
    responseData();
  }, []);

  const responseData = async () => {
    try {
      const response = await axios.get('http://localhost:8006/api/groups/');
      const jsonData = response.data;
      setData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleCreateGroup = async () => {
    try {
      setCreatingGroup(true);
      await axios.post('http://localhost:8006/api/groups/', {
        name: groupName,
        description: groupDescription,
      });
      responseData(); // Refresh the list after creating a group
      setGroupName('');
      setGroupDescription('');
      setCreatingGroup(false);
    } catch (error) {
      console.error('Error creating group:', error);
      setCreatingGroup(false);
    }
  };

  const toggleGroupDetails = (groupId) => {
    if (expandedGroups.includes(groupId)) {
      setExpandedGroups(expandedGroups.filter(id => id !== groupId));
    } else {
      setExpandedGroups([...expandedGroups, groupId]);
    }
  };

  return (
    <div className='object-container'>
      <h1 className='object-title'>Groups</h1>
      <div className='create'>
        <input
          type='text'
          placeholder='Enter group name'
          value={groupName}
          onChange={(e) => setGroupName(e.target.value)}
          disabled={creatingGroup}
        />
        <input
          type='text'
          placeholder='Enter group description'
          value={groupDescription}
          onChange={(e) => setGroupDescription(e.target.value)}
          disabled={creatingGroup}
        />
      </div>
      <button className='create-btn' onClick={handleCreateGroup} disabled={creatingGroup}>
        {creatingGroup ? 'Creating...' : 'Create Group'}
      </button>
      <ul className='object-list'>
        {data.map((item) => (
          <li key={item.id} className='object-item'>
          <button className='group-name-btn' onClick={() => toggleGroupDetails(item.id)}>
            {item.name}
          </button>
          {expandedGroups.includes(item.id) && (
            <div className='group-details'>
              <p>Creator: {item.creator}</p>
              <p>Description: {item.description}</p>
              <p>Members Count: {item.members_count}</p>
            </div>
          )}
        </li>
        ))}
      </ul>
    </div>
  );
}

export default Groups;
