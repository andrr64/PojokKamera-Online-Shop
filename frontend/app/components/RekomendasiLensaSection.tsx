import ProductItem from "@/components/cards/ProductItem";

export default function RekomendasiLensaSection() {
  const lenses = [
    {
      image: "https://placehold.co/400x250/cccccc/999999?text=Canon+RF+24-70mm+F2.8",
      name: "Canon RF 24-70mm F2.8",
      price: "$2299",
      rating: 5,
      sold: 75,
      description: "Versatile zoom lens, perfect for portraits and landscapes.",
    },
    {
      image: "https://placehold.co/400x250/cccccc/999999?text=Nikon+Z+24-70mm+F2.8",
      name: "Nikon Z 24-70mm F2.8",
      price: "$2199",
      rating: 4,
      sold: 50,
      description: "High-performance zoom lens for Z-mount mirrorless cameras.",
    },
    {
      image: "https://placehold.co/400x250/cccccc/999999?text=Sony+FE+24-70mm+F2.8",
      name: "Sony FE 24-70mm F2.8",
      price: "$1999",
      rating: 5,
      sold: 120,
      description: "Professional zoom lens for full-frame Sony mirrorless cameras.",
    }
  ];

  return (
    <section className="bg-white px-4 sm:px-6 lg:px-8 py-16">
      <div className="max-w-7xl mx-auto">
        <h2 className="text-2xl sm:text-3xl font-bold text-gray-900 mb-8 text-center sm:text-left">
          Rekomendasi Lensa
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {lenses.map((l, i) => (
            <ProductItem key={i} {...l} />
          ))}
        </div>
      </div>
    </section>
  );
}
