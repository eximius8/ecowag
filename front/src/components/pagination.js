import * as React from 'react';
import Pagination from '@mui/material/Pagination';
import Stack from '@mui/material/Stack';
import { createSearchParams, useNavigate, useSearchParams } from "react-router-dom";

export default function PaginationControlled({total, numperpage = 20}) {
  const [page, setPage] = React.useState(1);
  const navigate = useNavigate();
  let [searchParams, setSearchParams] = useSearchParams();

  let count = parseInt(total / numperpage) + 1;

  React.useEffect(() => {
    let page = parseInt(searchParams.get("page"));
    if (page){
        setPage(page);
    }
  }, [])

  const handleChange = (event, value) => {
    let searchstr = searchParams.get("search");
    let searchparams = {};
    if (searchstr){
      searchparams = {...searchparams, search: searchstr}
    }    
    if (value){
      searchparams = {...searchparams, page: value}
    }    
    
    setSearchParams(searchparams);
    setPage(value);    

    navigate({      
        search: createSearchParams(searchparams).toString()
    });
  };

  return (
    <Stack spacing={2}>
      <Pagination count={count} page={page} onChange={handleChange} />
    </Stack>
  );
}