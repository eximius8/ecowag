import * as React from 'react';
import Box from '@mui/material/Box';
import { Button, Typography, CircularProgress } from '@mui/material';
import { useFetch } from '../../hooks/usefetch';
import { apiurl } from '../../constants';
import { WasteTable, WasteSummary } from './wastetable';
import InputComponent from './componentinput';

const WasteClsCalculate = ({waste}) => {

  const { data, isPending, error, postData } = useFetch(`${apiurl}/calcsclass/`, 'POST'); 

  React.useEffect(() => {
    postData(waste);
  }, [waste])

  if (isPending){
    return <CircularProgress />
  }

  if (error){
    <p>Ошибка</p>
  }

  if (data){    
    return (
      <>
        <WasteTable comprows={data.components} />        
        <WasteSummary component={data} waste={waste} />
      </>
    )
  }
  return <div />
}


export default function WasteComponents({wasteComps, setWasteComps}) {
  
  const [ totalConc, setTotalConc ] = React.useState(0);
  const [ showCalcClsres, setShowCalcClsres ] = React.useState(false);
  const [ waste, setWaste ] = React.useState({});  

  React.useEffect(() => {
    setShowCalcClsres(false);
    setWaste({});
    calcTotalConc();

  }, [JSON.stringify(wasteComps)])

  const calcTotalConc = () => {
    let conc = 0;
    wasteComps.map((comp) => {
      conc = conc + parseFloat(comp.concentration);
    })
    setTotalConc(conc);
  }


  const handleConcentrationChange = (value, id) => { 
      
    let newComps;    
    newComps = wasteComps.map((compon) => {
      let newcompon;
      if (compon.id === id){
        newcompon = {
          ...compon,
          'concentration': value};
      }else{
        newcompon = compon;        
      }
      return newcompon;
    });
    setWasteComps(newComps);
    calcTotalConc();
  }

  const handleCalcButtonclick = () => {    
    
    setWaste({"components": wasteComps});
    setShowCalcClsres(true);    
  }


  return (
    <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { width: '100%' },
      }}
      noValidate
      autoComplete="off"
    > 
        {wasteComps.map((wastecomp) => 
            <InputComponent 
              key={wastecomp.id}
              wastecomp={wastecomp} 
              handleConcentrationChange={handleConcentrationChange} 
              setWasteComps={setWasteComps}
              wasteComps={wasteComps}
            />
        )}
        <Button
          variant="contained"
          onClick={handleCalcButtonclick}
          disabled={totalConc < 99.999 || totalConc > 100.0001}
        >
          Расчет класса опасности
        </Button> 
        <Typography>
          Общая концентрация: {totalConc}%
        </Typography>
        {showCalcClsres && waste && <WasteClsCalculate waste={waste} />}
    </Box>
  );
}
