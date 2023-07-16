import React from "react";
import { Container } from "react-bootstrap";

function SearchBar() {
  return (
    <main>
      <div className="main-head">
        <form className="search-box">
          <input
            type="search"
            placeholder="Search for an anime..."
            required
            className="form-control rounded-pill"
          />
        </form>
      </div>
    </main>
  );
}

const Anime = () => {
  return (
    <Container className="center-content">
      <h1>Test Anime</h1>
      <SearchBar />
      <p>This is a test page for anime.</p>
    </Container>
  );
};

export default Anime;
