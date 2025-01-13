import { Box, Link, Typography } from "@mui/material";
import { useStyles } from "./styles";
import { FC } from "react";
import { router } from "@/app/router";

export const HomePage: FC = () => {
  const { classes } = useStyles({isFetching: false});

  return (
    <Box className={classes.root}>
      <Typography variant="h1">Home page</Typography>
      <Link component="button" onClick={() => router.navigate('/profile')}>
      Go to profile
      </Link>
    </Box>
  )
}
