// app/not-found.tsx
'use client';

import Link from 'next/link';

export default function NotFoundPage() {
    return (
        <main className="min-h-screen flex items-center justify-center bg-white px-4">
            <div className="max-w-3xl w-full flex flex-col md:flex-row items-center md:items-start justify-between gap-8">
                {/* Teks */}
                <div className="md:w-1/2 text-center md:text-left">
                    <h1 className="text-black text-4xl sm:text-5xl font-normal mb-4 leading-tight">
                        Whoops.<br />
                        This page is<br />
                        not available
                    </h1>
                    <p className="text-black text-sm sm:text-base mb-8 max-w-xs">
                        The link you clicked may be broken or the page may have been removed.
                    </p>
                    <Link href="/">
                        <button className="bg-blue-600 text-white text-base sm:text-lg font-medium rounded-lg py-3 px-8 hover:bg-blue-700 transition">
                            Back to Home
                        </button>
                    </Link>
                </div>

                {/* Gambar */}
                <div className="md:w-1/2 flex justify-center md:justify-end">
                    <img
                        className="max-w-full h-auto"
                        src="https://placehold.co/400x300/png?text=Construction+Barrier+and+Cones+Illustration"
                        alt="Construction illustration"
                    />
                </div>
            </div>
        </main>
    );
}
