import Section from "@/components/Section";

// components/HeroSection.tsx
export default function HeroSection() {
    return (
        <Section className="mx-auto flex flex-col md:flex-row items-center md:items-start justify-between gap-10">
            <div className="flex flex-col items-center md:items-start w-full md:max-w-xl text-center md:text-left">
                <p className="text-red-500 text-sm font-medium mb-2">
                    Koleksi Terbaru
                </p>
                <h1 className="font-extrabold text-3xl sm:text-4xl md:text-5xl text-gray-900 leading-tight mb-2">
                    Kamera & Lensa Premium
                </h1>
                <h2 className="font-normal text-lg sm:text-xl md:text-2xl text-gray-700 mb-6">
                    Abadikan Momen Terbaikmu
                </h2>
                <p className="text-gray-500 text-sm sm:text-base md:text-base mb-8 leading-relaxed">
                    Temukan berbagai kamera dan lensa terbaru dengan kualitas terbaik
                    untuk kebutuhan fotografi dan videografi Anda.
                </p>
                <button
                    className="bg-red-500 text-white text-sm sm:text-base md:text-base font-semibold rounded-full px-6 py-2 hover:bg-red-600 transition"
                    type="button"
                >
                    Belanja Sekarang
                </button>
            </div>

            {/* Image Content */}
            <div className="relative flex-shrink-0 w-72 h-72 sm:w-80 sm:h-80 md:w-96 md:h-96">
                <img
                    alt="Kamera profesional dengan lensa premium"
                    className="rounded-full w-full h-full object-cover"
                    src="https://placehold.co/400x400/cccccc/000000/png?text=Kamera+Premium"
                />
                <div className="absolute -top-6 -left-6 w-16 h-16 sm:w-20 sm:h-20 rounded-full bg-yellow-50 flex items-center justify-center overflow-hidden">
                    <img
                        alt="Lensa kamera"
                        className="rounded-full object-cover w-full h-full"
                        src="https://placehold.co/80x80/999999/FFFFFF/png?text=Lensa"
                    />
                </div>
                <div className="absolute bottom-12 left-0 w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-gray-800" />
                <div className="absolute top-6 right-0 w-6 h-6 sm:w-8 sm:h-8 rounded-full bg-red-500" />
            </div>
        </Section>
    );
}
