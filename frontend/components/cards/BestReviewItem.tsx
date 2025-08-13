// components/BestReviewItem.tsx
import { JSX } from "react";
import { FaStar, FaQuoteLeft } from "react-icons/fa";

interface BestReviewItemProps {
  name: string;
  role: string;
  image: string;
  rating: number; // 0-5
  review: string;
  socialBg?: string; // warna background icon social
  socialIcon?: JSX.Element; // misal <FaTwitter />
}

export default function BestReviewItem({
  name,
  role,
  image,
  rating,
  review,
  socialBg = "#1da1f2",
  socialIcon,
}: BestReviewItemProps) {
  return (
    <div className="relative bg-white rounded-md shadow-lg p-8 pt-16 w-full sm:w-80">
      <img
        src={image}
        alt={name}
        className="absolute -top-8 left-8 w-16 h-16 rounded-full object-cover border-4 border-white shadow-md"
      />
      <div className="flex justify-between items-center mb-2">
        <h2 className="font-extrabold text-gray-900 text-lg">{name}</h2>
        {socialIcon && (
          <div
            className="w-7 h-7 rounded-full flex items-center justify-center cursor-pointer"
            style={{ backgroundColor: socialBg }}
          >
            {socialIcon}
          </div>
        )}
      </div>
      <p className="text-green-500 font-semibold text-xs tracking-widest mb-3 uppercase">
        {role}
      </p>
      <div className="flex space-x-1 text-yellow-400 mb-4">
        {Array.from({ length: 5 }).map((_, i) => (
          <FaStar key={i} className={i < rating ? "" : "text-gray-300"} />
        ))}
      </div>
      <div className="flex items-center space-x-2 mb-2">
        <FaQuoteLeft className="text-gray-900 opacity-70" />
        <hr className="border-dotted border-t border-gray-300 flex-grow" />
      </div>
      <p className="italic text-gray-500 text-sm leading-relaxed">{review}</p>
    </div>
  );
}
