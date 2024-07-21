import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Components/Home/Home';
import Display from './Components/Display/Display';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="display" element={<Display />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
