import React, { useState } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import UserContext from "./UserContext";
import LoginForm from "./LoginForm";
import Dashboard from "./Dashboard";
import DenseAppBar from "./DenseAppBar";
import CopyrightNotice from "./CopyrightNotice";

function App() {
  const [user, setUser] = useState(null);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      <DenseAppBar />
      <Router>
        <Routes>
          <Route
            path="/login"
            element={user ? <Navigate to="/" /> : <LoginForm />}
          />
          <Route
            path="/"
            element={user ? <Dashboard /> : <Navigate to="/login" />}
          />
        </Routes>
      </Router>
      <CopyrightNotice />
    </UserContext.Provider>
  );
}

export default App;
