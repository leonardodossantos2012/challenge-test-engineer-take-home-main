'use client';
import React, { useState } from 'react';
import axios from 'axios';
import Image from 'next/image';

const BACKEND_URL = 'http://127.0.0.1:8000';

interface ModalProps {
  id: string;
  text: string;
  isOpen: boolean;
  onClose: () => void;
}

const Modal: React.FC<ModalProps> = ({ id, text, isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50">
      <div className="bg-white p-4 rounded shadow-lg">
        <h2  id="text1" className="text-lg font-bold">{text}</h2>
        <button onClick={onClose} className="mt-4 px-4 py-2 bg-blue-500 text-white rounded">Close</button>
      </div>
    </div>
  );
};

const Home: React.FC = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalText, setModalText] = useState('');

  const handleCaptureImage = async () => {
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
        setModalText('Captured with success!');
        setIsModalOpen(true);
      }
      console.log(response.data);
    } catch (error) {
      console.error('Error capturing image:', error);
      alert('Failed to capture image.');
    }
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="relative z-10 flex place-items-center before:absolute before:h-[300px] before:w-[480px] before:-translate-x-1/2 before:rounded-full before:bg-gradient-radial before:from-white before:to-transparent before:blur-2xl before:content-[''] after:absolute after:h-[180px] after:w-[240px] after:translate-x-1/3 after:bg-gradient-conic after:from-sky-200 after:via-blue-200 after:blur-2xl after:content-['']">
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
          id="button1"
          className="group rounded-lg border border-neutral-700 px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800"
          onClick={handleCaptureImage}
        >
          Capture
        </button>
        <button
          className="group rounded-lg border border-neutral-700 px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800"
          onClick={async () => {
            const response = await axios.post(`${BACKEND_URL}/shutdown`);
            console.log(response.data);
          }}
        >
          Shutdown
        </button>
      </div>
      <Modal id="capture-success-modal" text={modalText} isOpen={isModalOpen} onClose={handleCloseModal} />
    </main>
  );
};

export default Home;
