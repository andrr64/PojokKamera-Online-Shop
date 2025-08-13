'use client';

import Loading from '@/components/LoadingPage';
import { useSearchParams, useRouter } from 'next/navigation';
import { useEffect } from 'react';
import HeroSection from '../components/HeroSection';
import RekomendasiKameraSection from '../components/RekomendasiKameraSection';

export default function MerekPage() {
    const searchParams = useSearchParams();
    const router = useRouter();
    const merekId = searchParams.get('id');

    useEffect(() => {
        if (!merekId) {
            // Redirect ke halaman notfound
            router.push('/notfound');
        }
    }, [merekId, router]);

    if (!merekId) {
        return <Loading />
    } // sementara tunggu redirect

    return (
        <div className="font-sans min-h-screen flex flex-col">
            <RekomendasiKameraSection/>
        </div>
    );
}
