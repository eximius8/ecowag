import * as React from 'react';
import { Table, TableBody, TableCell, 
  TableContainer, TableHead, TableRow,
  Paper, Card, CardActions, CardContent, Button, Typography, CircularProgress } from '@mui/material';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import FormControl from '@mui/material/FormControl';
import { apiurl } from '../../constants';
import { useFetch } from '../../hooks/usefetch';


const DownloadReportBtn = ({waste, name, fkko}) => {

  const { data, isPending, error, postData } = useFetch(`${apiurl}/report/`, 'POST');   

  React.useEffect(() => {
    let newwaste = {};
    newwaste['name'] = name;
    if (fkko) {
      newwaste['fkko'] = fkko
    }    
    newwaste = {...newwaste, ...waste} 
    console.log(newwaste);
    postData(newwaste);
  }, [waste, name, fkko])

  console.log(data);

  if (isPending){
    return (
        <div style={{display: 'flex', justifyContent: 'center'}}>
            <CircularProgress />
        </div>)
  } //latexonline.cc/compile?data=
  const urltolatex = data ? `https://api.webecolog.ru${data.file}` : null;

  return (    
        <Button 
          size="small"
          disabled={!urltolatex}
          variant="contained"
          onClick={()=> window.open(urltolatex, "_blank")}
        >
          Скачать отчет
        </Button>)
}

export const WasteSummary = ({component, waste}) => {
  
  const [ name, setName ] = React.useState("");
  const [ fkko, setFkko ] = React.useState("");
  const [ dnldreport, setDnldreport ] = React.useState(false);

  React.useEffect(() => {
    setDnldreport(false);
  }, [name, fkko])
  
  const HandleGenRepLink = () => {       
    setDnldreport(true);
  }


  return (
    <Card sx={{ minWidth: 275, mt: 2 }}>
      <CardContent>        
        <Typography variant="h5" component="div">
          Класс опасности отхода: {component.sclass} - 
          {component.sclass === "IV" ? " (Малоопасные)" : 
           component.sclass === "II" ? " (Высоко опасные)" :
           component.sclass === "III" ? " (Умеренно опасные)" :
           component.sclass === "V" ? " (Практически неопасные)" : " (Чрезвычайно опасные)"  
          }
        </Typography>
        <Typography variant="body2">
          Значение получено на основе вычисленной степени опасности 
          отхода для окружающей среды K={component.K.toFixed(1)}
        </Typography>
        <Typography variant="h5">Данные отхода</Typography>
        <FormControl fullWidth sx={{ pb: 1, pt: 2 }}>
          <InputLabel  htmlFor="outlined-adornment-amount">Название отхода</InputLabel>
          <OutlinedInput
            id="outlined-adornment-amount"
            variant="standard"
            required
            value={name}
            onChange={(e) => setName(e.target.value)}            
            label="Amount"
          />
        </FormControl>
        <FormControl fullWidth sx={{ py: 2 }}>
          <InputLabel htmlFor="outlined-adornment-amount">ФККО</InputLabel>
          <OutlinedInput
            id="outlined-adornment-amount"
            value={fkko}
            onChange={(e) => setFkko(e.target.value)}
            label="Amount"
          />
        </FormControl>
      </CardContent>
      <CardActions>
        <Button 
          size="small"
          disabled={!name}
          variant="contained"
          onClick={HandleGenRepLink}
        >
          Сгенерировать отчет
        </Button>
        {dnldreport && <DownloadReportBtn waste={waste} fkko={fkko} name={name} />}
      </CardActions>
    </Card>
  );
}


export function WasteTable({comprows}) {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Компонент</TableCell>
            <TableCell align="right">X</TableCell>
            <TableCell align="right">Z</TableCell>
            <TableCell align="right">W</TableCell>
            <TableCell align="right">C</TableCell>
            <TableCell align="right">K</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {comprows.map((row) => (
            <TableRow
              key={row.id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.x.toFixed(2)}</TableCell>
              <TableCell align="right">{row.z.toFixed(2)}</TableCell>
              <TableCell align="right">{row.w.toFixed(2)}</TableCell>
              <TableCell align="right">{row.conc}</TableCell>
              <TableCell align="right">{row.k.toFixed(2)}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
