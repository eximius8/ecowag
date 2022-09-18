import * as React from 'react';
import { Table, CircularProgress } from '@mui/material';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { apiurl } from '../../constants';
import { useFetch } from '../../hooks/usefetch';


export default function BasicTable({id}) {
  let burl = `${apiurl}/api/v2/pages/${id}`;
  const { data, isPending, error } = useFetch(burl);


  if (isPending){
    return <CircularProgress />
  }

  if (error){
    return <p>Ошибка</p>
  }

  if (data){
    let allprops = data.soilprops.concat(data.dwprops, data.fwprops,
      data.airprops, data.ecoprops, data.ldprops, data.foodprops, data.props);
    return (
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Свойство</TableCell>
              <TableCell align="right">Значение</TableCell>
              <TableCell align="right">Балл B</TableCell>
              <TableCell align="right">Источник</TableCell>              
            </TableRow>
          </TableHead>
          <TableBody>
            {allprops.map((row) => (
              <TableRow
                key={row.id}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row.value.abbr}
                </TableCell>
                <TableCell align="right">{row.value.value}</TableCell>
                <TableCell align="right">{row.value.B}</TableCell>
                <TableCell align="right">{row.value.source.name}</TableCell>                
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    )
  }

  return <div/>
}
