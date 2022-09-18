import * as React from 'react';
import { useState, useEffect } from 'react';
import { apiurl } from '../../constants';
import { useFetch } from '../../hooks/usefetch';
import { useParams } from "react-router-dom";
import { Typography, CircularProgress, Container, Paper } from '@mui/material';


function NewsParagraph ({value}){

    return (
        <Paper
            sx={{ px: '10px', py: '8px', my: '4px' }}
            component="div"
            dangerouslySetInnerHTML={{__html: value}}
        />
    )
}


export default function NewsPage () {
    let params = useParams();
    const initUrl = `${apiurl}/api/v2/pages/find/?html_path=/news/${params.newsurl}`;
    let [ burl, setBurl ] = useState(initUrl);
    const { data, isPending, error } = useFetch(burl);

    if (data){
        var publ_date = new Date(data.meta.first_published_at);
    }

    if (isPending){
        return (
            <div style={{display: 'flex', justifyContent: 'center'}}>
                <CircularProgress />
            </div>)
      }
    
    if (error){
        return (
            <Typography>
                Не удалось загрузить новость
            </Typography>)
    }
    if (data){
        return (
            <Container sx={{ py: 3 }} maxWidth="md">
                <Typography>
                    {publ_date && publ_date.toLocaleDateString("ru-RU")}
                </Typography>
                <Typography 
                    sx={{ my: '5px' }}
                    variant='h4'
                    component='h3'
                >
                    {data.title}
                </Typography>
                {data.body.map((newsbody) => 
                    <NewsParagraph key={newsbody.id} value={newsbody.value} />
                )}
                
            </Container>);
    }
    
    return <div/>

}