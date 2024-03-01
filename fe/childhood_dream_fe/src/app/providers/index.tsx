import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { RouterProvider } from "react-router-dom";
import type { Router } from "@remix-run/router/dist/router";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";
import { ThemeProvider, createTheme } from "@mui/material";


type Props = {
  router: Router
  client: QueryClient
}
const defaultTheme = createTheme();

export const Providers = ({ router, client }: Props) => {
  return (
    <QueryClientProvider client={client}>
      <ThemeProvider theme={defaultTheme}>
        <RouterProvider router={router}/>
        <ReactQueryDevtools />
      </ThemeProvider>
    </QueryClientProvider>
  )
}
