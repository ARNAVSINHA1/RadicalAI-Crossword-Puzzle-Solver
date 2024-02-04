import React from 'react';
import Game from './game.py';
import Solver from './solver.py';

function App() {
  return (
    <div>
      <h1>AI Crossword Game</h1>
      <Game />
      <Solver />
    </div>
  );
}

export default App;
