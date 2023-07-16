import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';
import Home from './Home';
import About from './About';
import Anime from './Anime';
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  return (
    <Router>
      <Navbar bg="dark" variant="dark" className="justify-content-between fixed-navbar" style={{ paddingTop: '20px', paddingBottom: '20px' }}>
        <Navbar.Brand as={Link} to="/" style={{ paddingLeft: '15px', fontSize: '25px' }}>RecommendIO</Navbar.Brand>
        <Nav className="mr-auto" style={{paddingRight:'50px'}}>
          <Nav.Link as={Link} to="/">Home</Nav.Link>
          <Nav.Link as={Link} to="/about">About</Nav.Link>
          <Nav.Link as={Link} to="/anime">Anime</Nav.Link>
          <Nav.Link as={Link} to="/movies">Movies</Nav.Link>
          <Nav.Link as={Link} to="/games">Games</Nav.Link>
        </Nav>
        <Nav>
          <Nav.Link as={Link} to="/user" style={{paddingRight: '100px'}}>
            <img src="https://imageio.forbes.com/blogs-images/olliebarder/files/2016/06/goku_black_new-1200x675.jpg?height=399&width=711&fit=bounds" alt="user" style={{ width: "50px", height: "50px", objectFit: "cover" , borderRadius: "50%" }} />
          </Nav.Link>
        </Nav>
      </Navbar>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/anime" element={<Anime />} />
      </Routes>
    </Router>
  );
}

export default App;
