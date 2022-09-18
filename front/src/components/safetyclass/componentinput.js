import * as React from 'react';
import TextField from '@mui/material/TextField';
import CloseIcon from '@mui/icons-material/Close';
import { InputAdornment, IconButton } from '@mui/material';


const Adornm = ({id, removeWasteComp}) => {
    return (
        <InputAdornment position="end">
            <IconButton
              children={<CloseIcon/>}
              onClick={() => removeWasteComp(id)}
            />
        </InputAdornment>
    )
}

export default function InputComponent({wastecomp, handleConcentrationChange, setWasteComps, wasteComps}){

    const [ conc, setConc ] = React.useState(0);

    const handleConcChange = (e) => { 

        if (e.target.value >= 0 && e.target.value <= 100 && e.target.value !== ''){
            setConc(e.target.value);
            handleConcentrationChange(e.target.value, wastecomp.id);
        }
    }

    const removeWasteComp = (id) => {
        let noId = wasteComps.filter( el => el.id !== id ); 
        setWasteComps([...noId]);
      }

    return (
        <TextField
            type='number'            
            label="Введте концентрацию в %"
            required
            value={conc}
            onChange={(e) => handleConcChange(e)}
            helperText={wastecomp.name}
            sx={{ my: 1 }}
            InputProps={{
                endAdornment: <Adornm id={wastecomp.id} removeWasteComp={removeWasteComp} />,
                }}                
        /> 
    )
}