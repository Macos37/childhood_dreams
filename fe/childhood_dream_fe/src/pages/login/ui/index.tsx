import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { FC, useContext, useState } from 'react';
import { useLogin } from '@/features/login';
import { MuiTelInput } from 'mui-tel-input';
import { Controller, useForm } from 'react-hook-form';
import { Snackbar } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '@/app/providers/auth';

const LoginPage: FC = () => {
  const { mutate: login } = useLogin();
  const { control, handleSubmit } = useForm({
    defaultValues: {
      tel: "",
      password: "",
    },
  });
  const [isError, setIsError] = useState(false);
  const navigate = useNavigate();
  const { setToken } = useContext(AuthContext);

  const onSubmit = (data: {tel: string, password: string}) => {
    login({
      phone: data.tel,
      password: data.password,
    }, {
      onError: () => {
        setIsError(true);
      },
      onSuccess: ({ token }) => {
        setToken(token);
        navigate('/');
      }
    });
  };


  return (
      <Container component="main" maxWidth="xs">
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <Box component="form" onSubmit={handleSubmit(onSubmit)} noValidate sx={{ mt: 1 }}>
            <Controller
              name="tel"
              control={control}
              render={({ field }) => (
                <MuiTelInput
                  {...field}
                  margin="normal"
                  required
                  fullWidth
                  id="phone"
                  label="Phone Number"
                  name="phone"
                  autoComplete="phone"
                  autoFocus
                  onlyCountries={['RU']}
                  defaultCountry='RU'
                  error={isError}
                />
              )}
            />
            <Controller
              name="password"
              control={control}
              render={({ field }) => (
                <TextField
                  {...field}
                  margin="normal"
                  required
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  autoComplete="current-password"
                  error={isError}
                />
              )}
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link href="/sign-up" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Snackbar
          anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
          open={isError}
          message='Oops, something went wrong! Please try again.'
          autoHideDuration={3500}
          onClose={() => setIsError(false)}
          sx={{
            '& .MuiSnackbarContent-root': {
              backgroundColor: '#f44336',
            },
          }}
        />
      </Container>
  );
}

export { LoginPage };