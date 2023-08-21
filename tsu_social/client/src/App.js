import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/header';
import Home from './components/index';
import Groups from './components/groups';
import Users from './components/users';

function App() {
  return (
    <Router>
      <div>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/api/groups" element={<Groups />} />
          <Route path="/api/users" element={<Users />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
