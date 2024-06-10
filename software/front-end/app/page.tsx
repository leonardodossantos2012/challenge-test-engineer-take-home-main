'use client';
import React, { useState } from 'react';
import axios from 'axios';
import Image from 'next/image';

const BACKEND_URL = 'http://127.0.0.1:8000';

const handleCaptureImage = async (setModalMessage: React.Dispatch<React.SetStateAction<string>>) => {
  try {
    const response = await axios.post(`${BACKEND_URL}/capture_image`, {
      with_defect: true,
      low_lighting: true,
    }, {
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (response.status === 200) {
      setModalMessage('Captured with success!');
    } else {
      setModalMessage('Failed to capture image.');
    }
    console.log(response.data);
  } catch (error) {
    console.error('Error capturing image:', error);
    setModalMessage('Failed to capture image.');
  }
};

const handleShutdown = async (setModalMessage: React.Dispatch<React.SetStateAction<string>>) => {
  try {
    const response = await axios.post(`${BACKEND_URL}/shutdown`, {}, {
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (response.status === 200) {
      setModalMessage('Server shutting down...');
    } else {
      setModalMessage('Failed to shut down the server.');
    }
    console.log(response.data);
  } catch (error) {
    console.error('Error shutting down the server:', error);
    setModalMessage('Failed to shut down the server.');
  }
};

export default function Home() {
  const [modalMessage, setModalMessage] = useState('');

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="relative z-[-1] flex place-items-center before:absolute before:h-[300px] before:w-full before:translate-x-1/2 before:rounded-full before:bg-gradient-radial before:from-white before:to-transparent before:blur-2xl before:content-[''] after:absolute after:-z-[-1] after:h-[180px] after:w-[240px] after:-translate-x-1/2 after:bg-gradient-conic after:from-sky-200 after:via-blue-200 after:blur-2xl after:content-[''] before:dark:bg-neutral-800/30 after:dark:bg-neutral-800/30 before:dark:from-sky-900 after:dark:from-[#0141ff]/40 before:lg:h-[360px]">
        <Image
          className="relative dark:drop-shadow-[0_0_0.3rem_#ffffff70] dark:invert"
          src="/next.svg"
          alt="Next.js Logo"
          width={180}
          height={37}
          priority
        />
      </div>

      <div className="mb-32 grid text-center">
        <button
          className="group rounded-lg border border-neutral-700 px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-800 hover:dark:bg-neutral-800/30"
          onClick={() => handleCaptureImage(setModalMessage)}
        >
          Capture
        </button>
      </div>

      <div className="mb-32 grid text-center">
        <button
          className="group rounded-lg border border-neutral-700 px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-800 hover:dark:bg-neutral-800/30"
          onClick={() => handleShutdown(setModalMessage)}
        >
          Shutdown
        </button>
      </div>

      {modalMessage && (
        <div className="fixed inset-0 flex items-center justify-center z-50">
          <div className="bg-white p-8 border border-gray-300 rounded shadow-lg">
            <p>{modalMessage}</p>
            <button
              className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
              onClick={() => setModalMessage('')}
            >
              Close
            </button>
          </div>
        </div>
      )}
    </main>
  );
}
