import React from 'react';
import { Link } from 'react-router-dom';
import './static/index.css'; // Import your CSS file

function Header() {
  return (
    <header className="header">
      <nav className="nav">
        <ul className="nav-list">
          <li className="nav-item">
            <Link className="nav-link" to="/">Home</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/api/groups/">Groups</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/api/users/">Users</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
