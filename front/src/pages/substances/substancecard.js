import * as React from 'react';
import { Card, Grid, Box, CardHeader, IconButton, Collapse } from '@mui/material';
import { styled } from '@mui/material/styles';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';

import AddIcon from '@mui/icons-material/Add';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import BasicTable from './substanceprops';

const ExpandMore = styled((props) => {
    const { expand, ...other } = props;
    return <IconButton {...other} />;
  })(({ theme, expand }) => ({
    transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
    marginLeft: 'auto',
    transition: theme.transitions.create('transform', {
      duration: theme.transitions.duration.shortest,
    }),
  }));

export default function SubstanceCard({substance, addWasteComp}) {
  const [expanded, setExpanded] = React.useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    <Box >
      <Card>
        <Grid container>
            <Grid item xl={10} lg={8} md={6} xs={12}>
                <CardHeader title={substance.title} />
            </Grid>            
            <Grid item xl={1} lg={2} md={3} xs={6}>
                <CardContent>
                    B = {substance.b_inf}
                </CardContent>
            </Grid>
            <Grid item xl={1} lg={2} md={3} xs={6}>
                <CardActions disableSpacing>
                    <IconButton 
                        children={<AddIcon/>}
                        onClick={() => addWasteComp({id: substance.id, name: substance.title})}
                    />                    
                    <ExpandMore
                        expand={expanded}
                        onClick={handleExpandClick}
                        aria-expanded={expanded}
                        aria-label="show more"
                    >
                        <ExpandMoreIcon />
                    </ExpandMore>
                </CardActions>
            </Grid>
        </Grid>
        <Collapse in={expanded} timeout="auto" unmountOnExit>
            <CardContent>
              <BasicTable id={substance.id} />
            </CardContent>
        </Collapse>

      </Card>
    </Box>
  );
}
