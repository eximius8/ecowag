import * as React from 'react';
import Box from '@mui/material/Box';

import { Paper, Typography } from '@mui/material';
import WasteComponents from './componentinlist';

export default function InputWaste({ wasteComps, setWasteComps }) {
  
  

  return (
    <Box sx={{ display: 'block' }}>
      <Paper sx={{ p: 2, mb: 2, backgroundColor: '#eceff1' }} >
        
        <Typography variant="h5">Компоненты:</Typography>
        <WasteComponents wasteComps={wasteComps} setWasteComps={setWasteComps} />
      </Paper>      
    </Box>
  );
}
