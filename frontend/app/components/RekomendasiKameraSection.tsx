import ProductItem from "@/components/cards/ProductItem";
import Section from "@/components/Section";

export default function RekomendasiKameraSection() {
    const products = [
        {
            image: "https://placehold.co/400x250/cccccc/999999?text=Canon+EOS+R5",
            name: "Canon EOS R5",
            price: "$3899",
            rating: 5,
            sold: 120,
            description: "Mirrorless full-frame, 45MP, 8K video, Dual Pixel AF.",
        },
        {
            image: "https://placehold.co/400x250/cccccc/999999?text=Nikon+Z7II",
            name: "Nikon Z7 II",
            price: "$2999",
            rating: 4,
            sold: 85,
            description: "Mirrorless full-frame, 45.7MP, 4K video, ISO 64-25600.",
        },
        {
            image: "https://placehold.co/400x250/cccccc/999999?text=Sony+A7IV",
            name: "Sony A7 IV",
            price: "$2499",
            rating: 5,
            sold: 200,
            description: "Full-frame mirrorless, 33MP, 4K 60fps video, BIONZ XR.",
        },
    ];

    return (
        <Section className="px-4 sm:px-6 lg:px-8 py-16">
            <div className="max-w-7xl mx-auto">
                <h2 className="text-2xl sm:text-3xl font-bold text-gray-900 mb-8 text-center sm:text-left">
                    Rekomendasi Kamera
                </h2>

                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    {products.map((p, i) => (
                        <ProductItem key={i} {...p} />
                    ))}
                </div>
            </div>
        </Section>
    );
}
