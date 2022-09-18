import * as React from 'react';
import Paper from '@mui/material/Paper';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';


export default function SearchSubstance({setSearchParams, searchParams}) {   

  let searchstr = searchParams.get("search");
  searchstr = searchstr ? searchstr : "";
  const [ serchstr, setSearchStr ] = React.useState(searchstr);

  const handleSearch = (event) => {
    event.preventDefault();
    setSearchParams({
      "search": serchstr
    });
  }

  return (
    <Paper
      component="form"
      sx={{ p: '2px 4px', display: 'flex', alignItems: 'center' }}
    >      
      <InputBase
        sx={{ ml: 1, flex: 1 }}
        placeholder="Поиск компонентов"
        inputProps={{ 'aria-label': 'Поиск компонентов' }}
        value={serchstr}
        onChange={(e) => setSearchStr(e.target.value)}
      />
      <IconButton 
        type="submit"
        onClick={handleSearch}
        sx={{ p: '10px' }} 
        aria-label="search"
      >
        <SearchIcon />
      </IconButton>      
    </Paper>
  );
}
