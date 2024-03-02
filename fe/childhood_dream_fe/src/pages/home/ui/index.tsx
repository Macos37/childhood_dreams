import { Box, Typography } from "@mui/material";
import { useStyles } from "./styles";
import { FC } from "react";



export const HomePage: FC = () => {
  const { classes } = useStyles({isFetching: false});

  return (
    <Box className={classes.root}>
      <Typography variant="h1">Home page</Typography>
    </Box>
  )
}
