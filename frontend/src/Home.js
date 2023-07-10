import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => (
  <div>
    <h2>Home Page</h2>
    <Link to="/anime/1">Test Anime</Link>
    <br/>
    <Link to="/about">About Page</Link>
  </div>
);

export default Home;
