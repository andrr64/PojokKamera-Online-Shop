import { Metadata } from "next";
import Homepage from "./HomePage";

export const metadata: Metadata = {
  title: 'Pojok Kamera',
  description: 'Discover the best cameras and lenses at Pojok Kamera. Shop online for top brands and exclusive deals.',
}
export default function Main() {
  return (
    <Homepage/>
  );
}
