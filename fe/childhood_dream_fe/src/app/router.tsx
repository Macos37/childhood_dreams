import { createBrowserRouter } from "react-router-dom";
import { HomePage } from "@/pages/home";
import { LoginPage } from "@/pages/login";
import { SignUpPage } from "@/pages/sign-up";
import { ProfilePage } from "@/pages/profile";
import { ProtectedRoute } from "./providers/auth";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <ProtectedRoute><HomePage/></ProtectedRoute>,
  },
  {
    path: "/profile",
    element: <ProtectedRoute><ProfilePage/></ProtectedRoute>,
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
