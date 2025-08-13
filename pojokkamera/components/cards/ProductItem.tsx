// components/ProductItem.tsx
import { FaStar, FaShoppingCart, FaHeart } from "react-icons/fa";

interface ProductItemProps {
  image: string;
  name: string;
  price: string;
  rating: number; // misal 0-5
  sold: number;
  description: string;
}

export default function ProductItem({
  image,
  name,
  price,
  rating,
  sold,
  description,
}: ProductItemProps) {
  return (
    <div className="bg-white rounded-lg shadow p-4 sm:p-6 flex flex-col">
      <a href="">
        <img
          src={image}
          alt={name}
          className="w-full h-40 sm:h-48 md:h-56 object-cover rounded mb-3 sm:mb-4"
        />
      </a>

      <h3 className="font-semibold text-gray-900 text-base sm:text-lg mb-1">
        {name}
      </h3>

      <div className="flex items-center text-yellow-400 mb-1 sm:mb-2">
        {Array.from({ length: 5 }).map((_, i) => (
          <FaStar
            key={i}
            className={i < rating ? "" : "text-gray-300"}
            size={14}
          />
        ))}
        <span className="text-gray-500 text-xs sm:text-sm ml-2">
          ({sold} sold)
        </span>
      </div>

      <p className="text-gray-700 text-xs sm:text-sm mb-2 line-clamp-2">
        {description}
      </p>

      <p className="font-bold text-lg sm:text-xl text-gray-900 mb-3 sm:mb-4">
        {price}
      </p>

      <div className="flex flex-col sm:flex-row sm:space-x-3 space-y-2 sm:space-y-0">
        <button className="flex-1 border cursor-pointer border-gray-300 rounded-md py-2 text-gray-900 text-xs sm:text-sm font-normal flex items-center justify-center space-x-1 sm:space-x-2 hover:bg-gray-100 transition">
          <FaHeart size={14} />
          <span>Wishlist</span>
        </button>
        <button className="flex-1 cursor-pointer bg-blue-600 hover:bg-blue-700 text-white rounded-md py-2 text-xs sm:text-sm font-semibold flex items-center justify-center space-x-1 sm:space-x-2 transition">
          <FaShoppingCart size={14} />
          <span>Buy now</span>
        </button>
      </div>
    </div>
  );
}
