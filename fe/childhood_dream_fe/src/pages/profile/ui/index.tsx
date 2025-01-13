import { Box, Typography, CircularProgress } from "@mui/material";
import { useStyles } from "./styles";
import { FC } from "react";
import { useProfile } from "@/entities/profile/api/get_profile";

export const ProfilePage: FC = () => {
  const { data: profile, isLoading } = useProfile();
  const { classes } = useStyles({isFetching: isLoading});

  if (isLoading) {
    return <CircularProgress />;
  }

  return (
    <Box className={classes.root}>
      <Typography variant="h4">{profile?.name} {profile?.surname}</Typography>
      <Typography>Email: {profile?.email}</Typography>
      <Typography>Phone: {profile?.phone}</Typography>
      <Typography>City: {profile?.city}</Typography>
    </Box>
  );
};