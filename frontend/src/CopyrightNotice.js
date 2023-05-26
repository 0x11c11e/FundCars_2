import React from "react";
import { Box, Typography } from "@mui/material";
import { styled } from "@mui/system";

const Footer = styled(Box)({
  position: 'fixed',
  left: 0,
  bottom: 0,
  width: '100%',
  backgroundColor: 'black',
  color: 'white',
  textAlign: 'center',
  padding: '10px 0',
});

function CopyrightNotice() {
  return (
    <Footer>
      <Typography variant="body2" color="inherit" align="center">
        {'Copyright © '}
        {new Date().getFullYear()}
        {' Dealerclick LLC. All rights reserved.'}
      </Typography>
    </Footer>
  );
}

export default CopyrightNotice;
