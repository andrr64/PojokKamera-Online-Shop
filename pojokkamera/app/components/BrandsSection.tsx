import Section from "@/components/Section";

// components/BrandsSection.tsx
export default function BrandsSection() {
    const brands = [
        "https://placehold.co/320x50?text=Canon",
        "https://placehold.co/320x50?text=Nikon",
        "https://placehold.co/320x50?text=Sony",
        "https://placehold.co/320x50?text=Fujifilm",
        "https://placehold.co/320x50?text=Panasonic",
        "https://placehold.co/320x50?text=Olympus",
    ];

    return (
        <Section className="py-12 bg-white">
            <h2 className="text-2xl sm:text-3xl font-bold text-gray-900 mb-8 text-center sm:text-center">
                Merek 
            </h2>
            <div className="flex flex-wrap justify-center items-center gap-8 px-4">
                {brands.map((brand, i) => (
                    <img
                        key={i}
                        src={brand}
                        alt={`Brand ${i}`}
                        className="h-12 object-contain transition-transform duration-300 hover:scale-110"
                    />
                ))}
            </div>
        </Section>
    );
}
