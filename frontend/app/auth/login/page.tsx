import { Metadata } from "next";
import LoginPage from "./LoginPage";

export const metadata: Metadata = {
  title: 'Login - Pojok Kamera',
  description: 'Discover the best cameras and lenses at Pojok Kamera. Shop online for top brands and exclusive deals.',
}

export default function Page(){
    return <LoginPage/>
}