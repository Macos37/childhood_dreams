import { createBrowserRouter } from "react-router-dom";
import { HomePage } from "@/pages/home";
import { LoginPage } from "@/pages/login";
import { SignUpPage } from "@/pages/sign-up";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage/>,
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
