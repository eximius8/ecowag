import * as React from 'react';
import Box from '@mui/material/Box';
import { CircularProgress } from '@mui/material';
import Grid from '@mui/material/Grid';
import SubstanceCard from './substancecard';
import PaginationControlled from '../../components/pagination';
import { useFetch } from '../../hooks/usefetch';
import { useSearchParams } from "react-router-dom";
import { apiurl } from '../../constants';
import SearchSubstance from './searchinput';
import InputWaste from '../../components/safetyclass/layout';

export default function Substances() {
  let [ searchParams, setSearchParams ] = useSearchParams();
  const initUrl = `${apiurl}/api/v2/pages/?type=substance.Substance&fields=b_inf`;
  let [ burl, setBurl ] = React.useState(initUrl);
  const { data, isPending, error } = useFetch(burl);
  const [ wasteComps, setWasteComps ] = React.useState([]);

  const addWasteComp = (newwaste) => {
    if (!wasteComps.some(el => el.id === newwaste.id)) {      
      setWasteComps([...wasteComps, {...newwaste, "concentration": 0}])
    } 
  }  

  React.useEffect(() => {
    let offset = 10 * parseInt(searchParams.get("page")) - 10;
    let searchstr = searchParams.get("search");
    let paramstr = '';
    if (offset || offset === 0){
      paramstr = paramstr + `&offset=${offset}`;
    };
    if (searchstr){
      paramstr = paramstr + `&search=${searchstr}`;
    }
    setBurl(`${initUrl}${paramstr}`);
  }, [searchParams])
 

  if (error){
    return <p>Ошибка</p>
  }

  return (
    <Box sx={{ flexGrow: 1 }}>      
      <Grid container spacing={2}>          
          <Grid item xs={12} sx={{ pb: 3 }}>
            {wasteComps.length>0 && 
              <InputWaste wasteComps={wasteComps} setWasteComps={setWasteComps} />
            }
            <SearchSubstance setSearchParams={setSearchParams} searchParams={searchParams} />
          </Grid>
          {isPending && <Grid item xs={12} align="center"><CircularProgress /></Grid>}
          {data && 
            <>
              {data.items.map((substance) => 
                <Grid key={substance.id} item xs={12}>
                    <SubstanceCard substance={substance} addWasteComp={addWasteComp} />
                </Grid>)}
            </>
          }  
      </Grid>
      {data && 
        <Box my={4} >
          {data.meta.total_count > 20 && <PaginationControlled total={data.meta.total_count} />}
        </Box>
      }
    </Box>
  );
}