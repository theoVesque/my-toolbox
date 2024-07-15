// components/sidebar/sidebar.js
"use client";

import React, { useState, useEffect } from "react";
import Logo from "../../assets/images/logo.gif";
import Image from "next/image";
import Link from "next/link";

const Sidebar = () => {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleSidebar = () => {
    setIsExpanded(!isExpanded);
  };

  useEffect(() => {
    const handleScroll = () => {
      const scrollY = window.scrollY;
      const sidebar = document.getElementById("sidebar");
      if (sidebar) {
        sidebar.style.top = `${scrollY}px`;
      }
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div className="lg:flex relative lg:mr-8">
      <button
        className="lg:hidden absolute top-4 right-0 bg-gray-800 text-white p-2 rounded-md shadow-md hover:bg-gray-700"
        onClick={toggleSidebar}
      >
        {isExpanded ? "Réduire" : "Menu"}
      </button>
      <div
        id="sidebar"
        className={`h-[92vh] bg-white text-white w-64 flex-shrink-0 rounded-2xl overflow-y-auto fixed lg:relative z-10 ${
          isExpanded ? "block" : "hidden"
        } lg:block`}
      >
        <div className="p-4 flex flex-col items-center">
          <Image src={Logo} alt="Logo de l'application" className="m-0 w-40" />
          <ul className="mt-0">
            <li className="flex mt-4 hover:bg-light_gray rounded-lg px-4 py-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width={32}
                height={32}
                viewBox="0 0 24 24"
              >
                <path
                  fill="none"
                  stroke="#111421"
                  strokeWidth={2}
                  d="M4 5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1zm10 0a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1zM4 16a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1zm10-3a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1z"
                ></path>
              </svg>
              <Link
                href="/"
                className="block p-2 text-dark_blue font-semibold"
                onClick={toggleSidebar}
              >
                Dashboard
              </Link>
            </li>
            <li className="flex items-center mt-4 hover:bg-light_gray rounded-lg px-4 py-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width={32}
                height={32}
                viewBox="0 0 16 16"
              >
                <path
                  fill="#111421"
                  d="M5.433 2.304A4.49 4.49 0 0 0 3.5 6c0 1.598.832 3.002 2.09 3.802c.518.328.929.923.902 1.64v.008l-.164 3.337a.75.75 0 1 1-1.498-.073l.163-3.33c.002-.085-.05-.216-.207-.316A6 6 0 0 1 2 6a6 6 0 0 1 2.567-4.92a1.48 1.48 0 0 1 1.673-.04c.462.296.76.827.76 1.423v2.82c0 .082.041.16.11.206l.75.51a.25.25 0 0 0 .28 0l.75-.51A.25.25 0 0 0 9 5.282V2.463c0-.596.298-1.127.76-1.423a1.48 1.48 0 0 1 1.673.04A6 6 0 0 1 14 6a6 6 0 0 1-2.786 5.068c-.157.1-.209.23-.207.315l.163 3.33a.752.752 0 0 1-1.094.714a.75.75 0 0 1-.404-.64l-.164-3.345c-.027-.717.384-1.312.902-1.64A4.5 4.5 0 0 0 12.5 6a4.49 4.49 0 0 0-1.933-3.696c-.024.017-.067.067-.067.16v2.818a1.75 1.75 0 0 1-.767 1.448l-.75.51a1.75 1.75 0 0 1-1.966 0l-.75-.51A1.75 1.75 0 0 1 5.5 5.282V2.463c0-.092-.043-.142-.067-.159"
                ></path>
              </svg>
              <Link
                href="/tools"
                className="block p-2 text-dark_blue font-semibold"
                onClick={toggleSidebar}
              >
                Tools
              </Link>
            </li>
            <li className="flex mt-4 hover:bg-light_gray rounded-lg px-4 py-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width={32}
                height={32}
                viewBox="0 0 24 24"
              >
                <path
                  fill="#111421"
                  d="m12 21l-1.45-1.3q-2.525-2.275-4.175-3.925T3.75 12.812T2.388 10.4T2 8.15Q2 5.8 3.575 4.225T7.5 2.65q1.3 0 2.475.55T12 4.75q.85-1 2.025-1.55t2.475-.55q2.35 0 3.925 1.575T22 8.15q0 1.15-.387 2.25t-1.363 2.412t-2.625 2.963T13.45 19.7zm0-2.7q2.4-2.15 3.95-3.687t2.45-2.675t1.25-2.026T20 8.15q0-1.5-1-2.5t-2.5-1q-1.175 0-2.175.662T12.95 7h-1.9q-.375-1.025-1.375-1.687T7.5 4.65q-1.5 0-2.5 1t-1 2.5q0 .875.35 1.763t1.25 2.025t2.45 2.675T12 18.3m0-6.825"
                ></path>
              </svg>
              <Link
                href="#"
                className="block p-2 text-dark_blue font-semibold"
                onClick={toggleSidebar}
              >
                Favorites
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
