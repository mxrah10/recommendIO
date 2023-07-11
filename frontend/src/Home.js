import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Container } from 'react-bootstrap';

const Home = () => (
  <Container className="center-content text-center">
    <h1 className="mb-4">Welcome to AnimeWorld!</h1>
    <p className="mb-4">Your one-stop platform for all things anime.</p>
    <Button variant="light" as={Link} to="/anime/1" className="mr-2">Go to Test Anime</Button>
    <Button variant="light" as={Link} to="/about">Go to About Page</Button>
  </Container>
);

export default Home;
