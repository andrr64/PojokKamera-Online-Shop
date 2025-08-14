import { Metadata } from "next";
import RegisterPage from "./RegisterPage";
export const metadata: Metadata = {
  title: 'Register - Pojok Kamera',
  description: 'Discover the best cameras and lenses at Pojok Kamera. Shop online for top brands and exclusive deals.',
}

export default function Page(){
    return <RegisterPage/>
}