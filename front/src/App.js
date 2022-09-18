import React, { Component } from 'react';
import { Routes, Route, Navigate } from "react-router-dom";
import './App.css';
import ResponsiveAppBar from './components/appbar';
import FixedContainer from './components/layout';
import Substances from './pages/substances/substances';
import HomePage from './pages/home/homepage';
import NewsPage from './pages/news/newspage';

class App extends Component {
  render() {
    return (
      <div className="App">
        <ResponsiveAppBar />
        <FixedContainer>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="safetyclass" element={<Substances />} />
            <Route path="news/:newsurl" element={<NewsPage />} />            
            <Route
                path="news/"
                element={<Navigate to="/" replace />}
            />
          </Routes>
        </FixedContainer>
      </div>
    );
  }
}

export default App;
