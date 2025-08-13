// components/BestReviewSection.tsx
import BestReviewItem from "@/components/cards/BestReviewItem";
import { FaInstagram, FaFacebookF, FaTwitter } from "react-icons/fa";

export default function BestReviewSection() {
  const reviews = [
    {
      name: "Frank Klin",
      role: "Designer",
      image: "https://placehold.co/64x64/4caf50/ffffff?text=Frank",
      rating: 5,
      review: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed.",
      socialBg: "#f0008c",
      socialIcon: <FaInstagram className="text-white text-sm" />,
    },
    {
      name: "Linda Anand",
      role: "Doctor",
      image: "https://placehold.co/64x64/000000/ffffff?text=Linda",
      rating: 5,
      review: "Abore et dolore magna aliqua. Ut enim ad minim veniam.",
      socialBg: "#1877f2",
      socialIcon: <FaFacebookF className="text-white text-sm" />,
    },
    {
      name: "David Gueta",
      role: "Artist",
      image: "https://placehold.co/64x64/3a5a2a/ffffff?text=David",
      rating: 5,
      review: "Exercitation ullamco laboris nisi ut aliquip ex ea commodo quat.",
      socialBg: "#1da1f2",
      socialIcon: <FaTwitter className="text-white text-sm" />,
    },
    {
      name: "Alice Smith",
      role: "Photographer",
      image: "https://placehold.co/64x64/ff9900/ffffff?text=Alice",
      rating: 4,
      review: "Great service and excellent camera quality!",
      socialBg: "#e4405f",
      socialIcon: <FaInstagram className="text-white text-sm" />,
    },
  ];

  return (
    <section className="py-16 px-4 bg-gray-50">
      <header className="max-w-4xl text-center mb-12 mx-auto px-4">
        <h1 className="text-2xl sm:text-3xl font-extrabold text-gray-900">
          Apa Yang <span className="text-green-500">Pelanggan Kami Katakan</span>
        </h1>
        <p className="mt-2 text-gray-400 text-sm sm:text-base max-w-xl mx-auto">
          Testimoni dari pelanggan kami yang puas dengan kamera dan lensa kami.
        </p>
      </header>

      <div className="max-w-7xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        {reviews.map((r, i) => (
          <BestReviewItem key={i} {...r} />
        ))}
      </div>
    </section>
  );
}
