import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Container } from 'react-bootstrap';
import './App.css';

function Home() {
  return (
    <Container className="center-content text-center">
      <h1 className="mb-4">Welcome to RecommendIO!</h1>
      <p className="mb-4">Your one-stop platform for all things anime, movies and games.</p>
      <Button variant="dark" as={Link} to="/anime/1" className="mr-3 my-2 equal-width-buttons">Go to Test Anime</Button>
      <Button variant="dark" as={Link} to="/movies/1" className="mr-3 my-2 equal-width-buttons">Go to Test Movies</Button>
      <Button variant="dark" as={Link} to="/games/1" className="mr-3 my-2 equal-width-buttons">Go to Test Games</Button>
      <Button variant="dark" as={Link} to="/about" className="mr-3 my-2 equal-width-buttons">Go to About Page</Button>
    </Container>
  );
}

export default Home;
