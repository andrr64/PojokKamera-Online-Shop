'use client';

// components/Header.tsx
import { webRoute } from "@/route/web_route";
import Link from "next/link";
import { useState } from "react";
import { FaShoppingBag, FaUser, FaSearch, FaBars, FaTimes } from "react-icons/fa";

export default function Header() {
    const [isMobileMenuOpen, setMobileMenuOpen] = useState(false);
    const [isLoggedIn, setLoggedIn] = useState(false); 
    const userName = "Andreas"; 

    return (
        <header className="w-full bg-white dark:bg-black shadow-sm px-4 sm:px-8 py-4 flex items-center justify-between sticky top-0 z-50 relative">
            {/* Logo */}
            <Link href={webRoute.home} className="flex items-center gap-2">
                <h1 className="text-2xl font-bold text-gray-900 dark:text-white z-10">
                    PojokKamera
                </h1>
            </Link>

            {/* Search Field (centered, desktop only) */}
            <div className="absolute left-1/2 transform -translate-x-1/2 hidden md:flex flex-1 max-w-lg px-4">
                <input
                    type="text"
                    placeholder="Search..."
                    className="w-full px-4 py-1 rounded-full border border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-red-500"
                />
            </div>

            {/* Desktop Right Menu */}
            <div className="hidden md:flex items-center gap-4 md:gap-6 z-10">
                {!isLoggedIn ? (
                    <a
                        href={webRoute.login}
                        className="flex items-center gap-1 text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition"
                    >
                        <FaUser />
                        Login
                    </a>
                ) : (
                    <>
                        <span className="text-gray-700 dark:text-gray-300 font-medium">
                            {userName}
                        </span>
                        <button className="relative flex items-center text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition">
                            <FaShoppingBag />
                            <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full px-1">
                                2
                            </span>
                        </button>
                    </>
                )}
            </div>

            {/* Mobile Menu Toggle */}
            <div className="flex md:hidden items-center gap-4 z-10">
                <button
                    className="text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition"
                    onClick={() => setMobileMenuOpen(!isMobileMenuOpen)}
                >
                    <FaSearch />
                </button>
                <button
                    className="text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition"
                    onClick={() => setMobileMenuOpen(!isMobileMenuOpen)}
                >
                    {isMobileMenuOpen ? <FaTimes /> : <FaBars />}
                </button>
            </div>

            {/* Mobile Menu Content */}
            {isMobileMenuOpen && (
                <div className="absolute top-full left-0 w-full bg-white dark:bg-black flex flex-col items-center py-4 gap-4 shadow-md md:hidden">
                    <a
                        href="#products"
                        className="text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition"
                        onClick={() => setMobileMenuOpen(false)}
                    >
                        Produk
                    </a>
                    <a
                        href="#about"
                        className="text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition"
                        onClick={() => setMobileMenuOpen(false)}
                    >
                        Tentang
                    </a>
                    <a
                        href="#contact"
                        className="text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition"
                        onClick={() => setMobileMenuOpen(false)}
                    >
                        Kontak
                    </a>

                    {!isLoggedIn ? (
                        <button
                            className="flex items-center gap-1 text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition"
                            onClick={() => {
                                setLoggedIn(true);
                                setMobileMenuOpen(false);
                            }}
                        >
                            <FaUser />
                            Login
                        </button>
                    ) : (
                        <>
                            <span className="text-gray-700 dark:text-gray-300 font-medium">
                                {userName}
                            </span>
                            <button className="relative flex items-center text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition">
                                <FaShoppingBag />
                                <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full px-1">
                                    2
                                </span>
                            </button>
                        </>
                    )}
                </div>
            )}
        </header>
    );
}
