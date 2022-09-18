import * as React from 'react';
import { useState, useEffect } from 'react';
import { apiurl } from '../../constants';
import { useFetch } from '../../hooks/usefetch';
import { Card, CardActionArea, CardContent, CardMedia, Box, 
    Grid, Typography, CircularProgress, Container } from '@mui/material';
import { useNavigate, useSearchParams } from "react-router-dom";
import PaginationControlled from '../../components/pagination';



function NewsCard ({card}) {
    const navigate = useNavigate();

    const publ_date = new Date(card.meta.first_published_at);

    const handleClick = () => {
        navigate(card.meta.html_url.replace(/^.*\/\/[^\/]+/, ''));        
    }

    return (
        <Grid item xs={12} sm={6} md={4}>
            <Card
                sx={{ display: 'flex', flexDirection: 'column' }}
            >
                <CardActionArea
                    onClick={() => handleClick()}
                >
                    <CardMedia
                        component="img"
                        sx={{
                            // 16:9
                            // pt: '56.25%',
                        }}
                        image={card.img_small 
                            ? 
                            `${apiurl}${card.img_small.url}` 
                            : 
                            'localhost'}
                        alt="random"
                    />
                    <CardContent sx={{ flexGrow: 1 }}>
                        <Typography variant="caption">
                            {publ_date.toLocaleDateString("ru-RU")}
                        </Typography>
                        <Typography variant="h5" component="h2">
                            {card.title}
                        </Typography>                        
                    </CardContent>                        
                </CardActionArea>
            </Card>
        </Grid>
    )

} 


export default function NewsBlock () {    
    let [ searchParams, _ ] = useSearchParams();
    
    const initUrl = `${apiurl}/api/v2/pages/?type=blog.BlogPage&fields=img_small&limit=12&order=-first_published_at`;
    let [ burl, setBurl ] = useState(initUrl);
    const { data, isPending, error } = useFetch(burl); 


    useEffect(() => {
        let offset = 12 * parseInt(searchParams.get("page")) - 12;
        let paramstr = '';
        if (offset || offset === 0){
          paramstr = paramstr + `&offset=${offset}`;
        };        
        setBurl(`${initUrl}${paramstr}`);
      }, [searchParams])

    if (isPending){
        return (
            <div style={{display: 'flex', justifyContent: 'center'}}>
                <CircularProgress />
            </div>)
      }
    
    if (error){
        return (
            <Typography>
                Не удалось загрузить новости
            </Typography>)
    }

    return ( 
        <>
            <Typography
              component="h3"
              variant="h4"
              align="center"
              color="text.primary"
              gutterBottom
            >
              Новости
            </Typography>            
            <Grid container spacing={4}>
                {data &&
                    data.items.map((card) => (
                        <NewsCard key={card.id} card={card} />
                    ))
                }
            </Grid>
            {data && data.meta.total_count > 12 && 
                <Box my={8} >
                    <PaginationControlled sx={{ mt: 10 }} total={data.meta.total_count} numperpage={12} />
                </Box>
            }            
        </>)

}