'use client';

import BestReviewSection from "./components/BestReviewSection";
import BrandsSection from "./components/BrandsSection";
import HeroSection from "./components/HeroSection";
import RekomendasiKameraSection from "./components/RekomendasiKameraSection";
import RekomendasiLensaSection from "./components/RekomendasiLensaSection";

export default function Homepage() {
    return (
        <main className="font-sans min-h-screen flex flex-col">
            <HeroSection />
            <BrandsSection />
            <RekomendasiKameraSection />
            <RekomendasiLensaSection />
            <BestReviewSection />
        </main>
    );
}
