import React, { useState, useContext } from "react";
import axios from "axios";
import UserContext from "./UserContext";
import {
  Box,
  Button,
  Card,
  CardContent,
  Container,
  TextField,
} from "@mui/material";
import { styled } from "@mui/system";
import { Link } from "react-router-dom";

const CenterBox = styled(Box)({
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  justifyContent: "center",
  height: "100vh",
  textAlign: "center",
});

const LoginForm = () => {
  const { setUser } = useContext(UserContext);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://localhost:8000/login/", {
        username: username,
        password: password,
      });

      if (res.data.error) {
        setError(res.data.error);
      } else {
        setUser(username);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <Container maxWidth="xs">
      <CenterBox>
        <Card>
          <CardContent>
            <form onSubmit={handleSubmit}>
              <h2>Login</h2>
              {error && <span>{error}</span>}
              <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                autoFocus
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
              <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <Button
                type="submit"
                fullWidth
                variant="contained"
                color="primary"
                sx={{ mt: 3, mb: 2 }}
              >
                Login
              </Button>
              <Link href="#" variant="body2">
                Forgot your password? Click here.
              </Link>
            </form>
          </CardContent>
        </Card>
      </CenterBox>
    </Container>
  );
};

export default LoginForm;
