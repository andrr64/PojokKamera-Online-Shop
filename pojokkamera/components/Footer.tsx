// components/Footer.tsx
import { FaTwitter, FaLinkedinIn, FaInstagram, FaFacebookF, FaAngleUp } from "react-icons/fa";

export default function Footer() {
  return (
    <footer className="relative overflow-hidden bg-black text-white">
      {/* Decorative background */}
      <div className="absolute inset-0 opacity-10 pointer-events-none select-none">
        <div className="w-full h-full bg-black" style={{ clipPath: "polygon(50% 0%, 100% 100%, 0% 100%)" }} />
      </div>

      <div className="relative max-w-7xl mx-auto px-6 py-12 md:py-16 flex flex-col md:flex-row md:justify-between gap-12 md:gap-0">
        {/* Brand & Social */}
        <div className="md:flex-1 max-w-sm space-y-6">
          <div className="flex items-center space-x-3">
            <div className="w-6 h-6 bg-green-500 flex items-center justify-center text-black font-bold">📷</div>
            <span className="text-white text-lg font-semibold tracking-wide">POJOK KAMERA</span>
          </div>
          <p className="text-sm leading-relaxed max-w-xs">
            Membantu para pecinta fotografi menemukan kamera, lensa, dan aksesoris terbaik dengan mudah.
          </p>
          <div className="flex space-x-6 text-white text-lg">
            <a href="#" className="hover:text-green-500"><FaTwitter /></a>
            <a href="#" className="hover:text-green-500"><FaLinkedinIn /></a>
            <a href="#" className="hover:text-green-500"><FaInstagram /></a>
            <a href="#" className="hover:text-green-500"><FaFacebookF /></a>
          </div>
          {/* <button className="mt-4 inline-flex items-center space-x-2 border border-white px-4 py-2 text-xs tracking-widest uppercase font-semibold hover:bg-white hover:text-black transition">
            <FaAngleUp />
            <span>Back to Top</span>
          </button> */}
        </div>

        {/* Links */}
        <div className="md:flex-1 flex flex-wrap justify-around max-w-lg gap-6">
          <div className="space-y-2 text-sm min-w-[120px]">
            <h3 className="font-semibold text-white mb-2">Site Map</h3>
            <ul className="space-y-1">
              {["Homepage","Cameras","Lenses","Accessories","Reviews","Contact"].map((item,i)=>(
                <li key={i}><a className="hover:text-green-500" href="#">{item}</a></li>
              ))}
            </ul>
          </div>
          <div className="space-y-2 text-sm min-w-[120px]">
            <h3 className="font-semibold text-white mb-2">Legal</h3>
            <ul className="space-y-1">
              {["Privacy Policy","Terms of Services","Disclaimer"].map((item,i)=>(
                <li key={i}><a className="hover:text-green-500" href="#">{item}</a></li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      <div className="text-[10px] text-white text-center py-1">
        Copyright © 2025, A. Software, All Rights Reserved.
      </div>
    </footer>
  );
}
