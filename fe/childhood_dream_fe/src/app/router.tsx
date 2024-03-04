import { createBrowserRouter } from "react-router-dom";
import { HomePage } from "@/pages/home";
import { LoginPage } from "@/pages/login";
import { SignUpPage } from "@/pages/sign-up";
import { AuthRoute } from "./providers/auth";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <AuthRoute><HomePage/></AuthRoute>,
  },
  {
    path: "/login",
    element: <LoginPage/>,
  },
  {
    path: "/sign-up",
    element: <SignUpPage/>,
  },
  {
    path: "*",
    element: <div>Not Found</div>,
  },
]);
