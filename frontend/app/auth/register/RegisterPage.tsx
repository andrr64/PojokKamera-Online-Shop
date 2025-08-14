'use client';

import { webRoute } from '@/route/web_route';
import React, { useState } from 'react';
import { FiEye, FiEyeOff } from 'react-icons/fi';

export default function RegisterPage() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [konfirmasiPassword, setKonfirmasiPassword] = useState('');

  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (password !== konfirmasiPassword) {
      alert('Password dan konfirmasi password tidak sama!');
      return;
    }

    console.log('Data pendaftaran:', {
      username,
      email,
      password,
    });

    alert('Pendaftaran berhasil!'); // simulasi
  };

  return (
    <main className="bg-white flex items-center justify-center p-6">
      {/* Card Form */}
      <div className="w-full max-w-md mx-auto bg-white p-8">
        {/* Logo */}
        <div className="flex items-center space-x-2 mb-6">
          <div className="w-4 h-4 rounded-md bg-green-600"></div>
          <span className="font-semibold text-sm text-gray-900">Finnger</span>
        </div>

        {/* Heading */}
        <h1 className="font-bold text-3xl sm:text-4xl text-gray-900 mb-2">
          Buat Akun
        </h1>
        <p className="text-gray-500 text-sm sm:text-base mb-8">
          Bergabunglah dan mulai perjalananmu sekarang.
        </p>

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-5">
          <input
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full border border-gray-300 rounded-md px-4 py-3 text-sm text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent"
            placeholder="Nama pengguna"
            type="text"
            required
          />
          <input
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full border border-gray-300 rounded-md px-4 py-3 text-sm text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent"
            placeholder="Email"
            type="email"
            required
          />

          {/* Password */}
          <div className="relative">
            <input
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full border border-gray-300 rounded-md px-4 py-3 text-sm text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent"
              placeholder="Kata sandi"
              type={showPassword ? 'text' : 'password'}
              required
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              className="absolute inset-y-0 right-3 flex items-center text-gray-400 hover:text-blue-600"
            >
              {showPassword ? <FiEyeOff size={18} /> : <FiEye size={18} />}
            </button>
          </div>

          {/* Konfirmasi Password */}
          <div className="relative">
            <input
              value={konfirmasiPassword}
              onChange={(e) => setKonfirmasiPassword(e.target.value)}
              className="w-full border border-gray-300 rounded-md px-4 py-3 text-sm text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent"
              placeholder="Konfirmasi kata sandi"
              type={showConfirmPassword ? 'text' : 'password'}
              required
            />
            <button
              type="button"
              onClick={() => setShowConfirmPassword(!showConfirmPassword)}
              className="absolute inset-y-0 right-3 flex items-center text-gray-400 hover:text-blue-600"
            >
              {showConfirmPassword ? <FiEyeOff size={18} /> : <FiEye size={18} />}
            </button>
          </div>

          {/* Tombol Daftar */}
          <button
            type="submit"
            className="w-full mt-2 bg-green-600 hover:bg-green-700 text-white font-semibold text-sm rounded-full px-6 py-3 transition-colors duration-200"
          >
            Daftar
          </button>
        </form>

        {/* Link Login */}
        <p className="mt-8 text-sm text-gray-500 text-center">
          Sudah punya akun?{' '}
          <a
            href={webRoute.login}
            className="text-green-600 font-semibold hover:underline"
          >
            Login!
          </a>
        </p>
      </div>
    </main>
  );
}
