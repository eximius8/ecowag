import * as React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useNavigate } from 'react-router-dom';
import NewsBlock from './newsblock';

function Copyright() {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
      {'© '}
      <Link color="inherit" href="https://webecolog.ru/">
        webecolog.ru
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}



const theme = createTheme();

export default function HomePage() {
    let navigate = useNavigate();

  return (
    <ThemeProvider theme={theme}>      
      <main>
        {/* Hero unit */}
        <Box
          sx={{
            bgcolor: 'background.paper',
            pt: 8,
            pb: 6,
          }}
        >
          <Container maxWidth="sm">
            <Typography
              component="h1"
              variant="h2"
              align="center"
              color="text.primary"
              gutterBottom
            >
              Вэб Эколог
            </Typography>
            <Typography variant="h5" align="center" color="text.secondary" paragraph>
              Рассчитайте класс опасности отходов и подготовьте протокол расчета онлайн.
            </Typography>
            <Stack
              sx={{ pt: 4 }}
              direction="row"
              spacing={2}
              justifyContent="center"
            >
                <Button 
                    variant="contained"
                    onClick={() => navigate('safetyclass')}
                >
                  Начать расчеты
                </Button>
              {/* <Button variant="outlined">Смотреть инструкции</Button> */}
            </Stack>            
          </Container>
        </Box>        
        <NewsBlock />          
      </main>
      {/* Footer */}
      <Box sx={{ bgcolor: 'background.paper', p: 6, mt: 10 }} component="footer">
        <Typography variant="h6" align="center" gutterBottom>
          Программа, проводящая расчет зарегистрирована в РосПатент
        </Typography>
        <Typography
          variant="subtitle1"
          align="center"
          color="text.secondary"
          component="p"
        >
          Связаться с нами info@webecolog.ru
        </Typography>
        <Copyright />
      </Box>
      {/* End footer */}
    </ThemeProvider>
  );
}